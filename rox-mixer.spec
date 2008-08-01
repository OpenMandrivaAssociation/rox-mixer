Name:		rox-mixer
Version:	0.1
Release:	%mkrel 9
Summary:	OSS sound volume ROX-applet
Group:		Graphical desktop/Other
License:	GPL
URL:		ftp://ftp.atmsk.ru/pub/rox/
Source0:	rox-mixer-0.1.tar.bz2
Patch: rox-mixer-0.1-build.patch
BuildRoot:	%_tmppath/%name-%version
BuildRequires:  libgtk+2-devel
Requires:	rox

%description
OSS sound volume ROX-applet

%define _appsdir %{_libdir}/apps

%prep
%setup -q -n %{name}
%patch -p1
chmod 644 .DirIcon
perl -pi -e "s!usr/lib!usr/%_lib!g" src/Makefile

%build
export CFLAGS="$RPM_OPT_FLAGS"
./AppRun --compile

%install
rm -rf %buildroot
mkdir -p $RPM_BUILD_ROOT%{_appsdir}
cp -a ./ $RPM_BUILD_ROOT%{_appsdir}/%{name}
rm -rf %buildroot%_appsdir/%name/src

%clean 
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc %{_appsdir}/%name/Help
%dir %{_appsdir}/%name
%{_appsdir}/%name/.DirIcon
%{_appsdir}/%name/App*
%{_appsdir}/%name/Linux-*


