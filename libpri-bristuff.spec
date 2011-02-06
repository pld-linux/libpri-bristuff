Summary:	ISDN PRI and BRI channel interface library
Summary(pl.UTF-8):	Biblioteka interfejsu do kanałów PRI/BRI ISDN
Name:		libpri-bristuff
Version:	1.4.3
Release:	2
License:	GPL
Group:		Libraries
Source0:	http://downloads.digium.com/pub/libpri/libpri-%{version}.tar.gz
# Source0-md5:	c5be91fc98f1638ba0365bf87f696cd1
# http://svn.debian.org/wsvn/pkg-voip/libpri/trunk/debian/patches
Patch0:		%{name}-libname.patch
# http://svn.debian.org/wsvn/pkg-voip/libpri/trunk/debian/patches
Patch1:		%{name}-bristuff.patch
URL:		http://www.asterisk.org/
BuildRequires:	zaptel-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ISDN PRI/BRI channel interface library.

%description -l pl.UTF-8
Biblioteka interfejsu do kanałów PRI/BRI ISDN.

%package devel
Summary:	Header files and development documentation for libpri-bristuff
Summary(pl.UTF-8):	Pliki nagłówkowe i dokumentacja do libpri-bristuff
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files and development documentation for libpri-bristuff.

%description devel -l pl.UTF-8
Pliki nagłówkowe i dokumentacja do libpri-bristuff.

%package static
Summary:	libpri-bristuff static library
Summary(pl.UTF-8):	Statyczna biblioteka libpri-bristuff
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
libpri-bristuff static library.

%description static -l pl.UTF-8
Statyczna biblioteka libpri-bristuff.

%prep
%setup -q -n libpri-%{version}
%patch0 -p1
%patch1 -p1
%{__sed} -i 's,/lib,/%{_lib},g' Makefile

%build
%{__make} \
	LIB_SUF="bristuff" \
	CC="%{__cc}" \
	OPTFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man{1,3},%{_includedir},%{_libdir}}

%{__make} install \
	LIB_SUF="bristuff" \
	INSTALL_PREFIX=$RPM_BUILD_ROOT \
	LIBDIR=%{_lib}

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ChangeLog README TODO
%attr(755,root,root) %{_libdir}/libpri-*.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libpri-*.so
%{_includedir}/bristuff

%files static
%defattr(644,root,root,755)
%{_libdir}/libpri-*.a
