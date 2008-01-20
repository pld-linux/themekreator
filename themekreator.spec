Summary:	SonyEricsson display theme creator
Name:		themekreator
Version:	0.3
Release:	0.1
License:	GPL
Group:		X11/Applications
URL:		http://www.matthiaswetzka.de/themekreator.en.php
Source0:	%{_tmppath}/%{name}-%{PACKAGE_VERSION}.tar.gz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ThemeKreator is a program to create themes for SonyEricsson mobile
phones.

%prep
%setup -q
CFLAGS="$RPM_OPT_FLAGS" CXXFLAGS="$RPM_OPT_FLAGS" \
./configure --prefix=%{_prefix} --disable-debug --enable-debug=no

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig
%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog NEWS README TODO
/
