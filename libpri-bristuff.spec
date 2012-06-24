Summary:	ISDN PRI channel interface library.
Name:		libpri
Version:	0.1
%define snap 20040407
Release:	0.%{snap}.1
License:	?
Group:	Development/Libraries
Source0:	%{name}-%{snap}.tar.gz
# Source0-md5:	a0ce6ab4cf516386a8201cdfa1e2a680
Patch0:	%{name}-Makefile.patch
URL:		http://www.asteriskpbx.com/
BuildRequires: zaptel-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ISDN PRI channel interface library.

%package devel
Summary:	Header files and development documentation for libpri
Summary(pl):	Pliki nag��wkowe i dokumentacja do libpri
Group:	Development/Libraries
Requires:	%{name} = %{version}

%description devel
Header files and development documentation for libpri.

%description devel -l pl
Pliki nag��wkowe i dokumentacja do libpri.

%package static
Summary:	libpri static library
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
bpri static library

%prep
%setup -q -n %{name}
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
