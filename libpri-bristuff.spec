Summary:	ISDN PRI channel interface library
Summary(pl):	Biblioteka interfejsu do kana³ów PRI ISDN
Name:		libpri
Version:	1.0.0
Release:	1
License:	GPL
Group:		Libraries
Source0:	ftp://ftp.digium.com/pub/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	814ebe7c24ccbe48f29814965d7f8f36
Patch0:		%{name}-Makefile.patch
URL:		http://www.asterisk.org/
BuildRequires:	zaptel-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ISDN PRI channel interface library.

%description -l pl
Biblioteka interfejsu do kana³ów PRI ISDN.

%package devel
Summary:	Header files and development documentation for libpri
Summary(pl):	Pliki nag³ówkowe i dokumentacja do libpri
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files and development documentation for libpri.

%description devel -l pl
Pliki nag³ówkowe i dokumentacja do libpri.

%package static
Summary:	libpri static library
Summary(pl):	Statyczna biblioteka libpri
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
libpri static library.

%description static -l pl
Statyczna biblioteka libpri.

%prep
%setup -q -n %{name}-%{version}
%patch0 -p1

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man{1,3},%{_includedir},%{_libdir}}

%{__make} install \
	INSTALL_PREFIX=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ChangeLog README TODO
%attr(755,root,root) %{_libdir}/libpri.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libpri.so
%{_includedir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/libpri.a
