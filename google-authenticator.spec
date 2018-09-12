Name:           google-authenticator
Version:        1.05
Release:        0.1%{?dist}
Summary:        One-time passcode support using open standards

License:        ASL 2.0
URL:            https://github.com/google/google-authenticator-libpam/archive/
Source0:        1.05.tar.gz
BuildRequires:  pam-devel

%description
The Google Authenticator package contains a pluggable authentication
module (PAM) which allows login using one-time passcodes conforming to
the open standards developed by the Initiative for Open Authentication
(OATH) (which is unrelated to OAuth).

Passcode generators are available (separately) for several mobile
platforms.

These implementations support the HMAC-Based One-time Password (HOTP)
algorithm specified in RFC 4226 and the Time-based One-time Password
(TOTP) algorithm currently in draft.

%prep
%setup -q -n google-authenticator-libpam-%{version}

%build
./bootstrap.sh
./configure
make CFLAGS="${CFLAGS:-%optflags}" LDFLAGS=-ldl %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_lib}/security
install -m0755 .libs/pam_google_authenticator.so $RPM_BUILD_ROOT/%{_lib}/security/pam_google_authenticator.so
install -m0755 .libs/pam_google_authenticator.lai $RPM_BUILD_ROOT/%{_lib}/security/pam_google_authenticator.lai
install -m0755 pam_google_authenticator.la $RPM_BUILD_ROOT/%{_lib}/security/pam_google_authenticator.la
mkdir -p $RPM_BUILD_ROOT/%{_bindir}
install -m0755 google-authenticator $RPM_BUILD_ROOT/%{_bindir}/google-authenticator
mkdir -p $RPM_BUILD_ROOT/%{_mandir}/man1
mkdir -p $RPM_BUILD_ROOT/%{_mandir}/man8
install -m0644 man/google-authenticator.1 $RPM_BUILD_ROOT/%{_mandir}/man1/google-authenticator.1
install -m0644 man/pam_google_authenticator.8 $RPM_BUILD_ROOT/%{_mandir}/man8/pam_google_authenticator.8

%files
/%{_lib}/security/*
%{_bindir}/google-authenticator
%doc FILEFORMAT README.md totp.html
%{_mandir}/man1/google-authenticator.1*
%{_mandir}/man8/pam_google_authenticator.8*


%changelog
* Wed Sep 12 2018 Vamegh Hedayati <vhedayati@ev9.io> - 1.05
- Packaged up the latest version of google-authenticator-libpam, for use on RHEL6

* Mon Oct 03 2011 David Woodhouse <David.Woodhouse@intel.com> - 0-0.3.20110830.hgd525a9bab875
- Remove qrencode-devel from BR; it doesn't exist on RHEL6

* Mon Sep 12 2011 David Woodhouse <David.Woodhouse@intel.com> - 0-0.2.20110830.hgd525a9bab875
- Add support for expanding PAM environment variables in secret key file name:
  http://code.google.com/p/google-authenticator/issues/detail?id=108

* Mon Sep 12 2011 David Woodhouse <David.Woodhouse@intel.com> - 0-0.1.20110830.hgd525a9bab875
- Initial import

