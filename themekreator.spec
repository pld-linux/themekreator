Summary:	SonyEricsson display theme creator
Summary(pl.UTF-8):	Kreator motywów dla wyświetlaczy SonyEricsson
Name:		themekreator
Version:	0.3
Release:	0.4
License:	GPL v2
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/themekreator/%{name}-%{version}.tar.gz
# Source0-md5:	323c95e65ccd9a94eba29039fd7b2e48
Patch0:		%{name}-fix_build.patch
URL:		http://www.matthiaswetzka.de/themekreator.en.php
BuildRequires:	kdelibs-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdir	%{_datadir}/apps/themekreator

%description
ThemeKreator is a program to create themes for SonyEricsson mobile
phones.

%description -l pl.UTF-8
ThemeKreator to program do tworzenia motywów dla telefonów komórkowych
SonyEricsson.

%prep
%setup -q
%patch0 -p1

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_desktopdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

mv $RPM_BUILD_ROOT%{_datadir}/applnk/Utilities/themekreator.desktop \
	$RPM_BUILD_ROOT%{_desktopdir}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/%{name}
%attr(755,root,root) %dir %{_appdir}
%{_appdir}/*.dtd
%{_appdir}/*.rc
%{_appdir}/*.xml
%{_appdir}/K600i
%{_appdir}/K700i
%{_appdir}/K750i
%{_appdir}/T610
%{_appdir}/T630
%{_appdir}/W800i
%{_datadir}/config.kcfg/%{name}.kcfg
%{_datadir}/mimelnk/application/vnd.eri.thm.desktop
%{_iconsdir}/*/*/apps/%{name}.*
%{_desktopdir}/%{name}.desktop
#%{_pixmapsdir}/%{name}.png
