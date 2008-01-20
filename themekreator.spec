Summary:	SonyEricsson display theme creator
Name:		themekreator
Version:	0.3
Release:	0.1
License:	GPL v2
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/themekreator/%{name}-%{version}.tar.gz
# Source0-md5:	323c95e65ccd9a94eba29039fd7b2e48
URL:		http://www.matthiaswetzka.de/themekreator.en.php
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ThemeKreator is a program to create themes for SonyEricsson mobile
phones.

%prep
%setup -q
%configure

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
