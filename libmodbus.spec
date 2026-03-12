#
# Conditional build:
%bcond_without	tests		# testing
%bcond_without	static_libs	# static library
#
Summary:	libmodbus - free software library to send/receive data according to the Modbus protocol
Summary(pl.UTF-8):	libmodbus - darmowa biblioteka do wysyłania/odbierania danych zgodnie z protokołem Modbus
Name:		libmodbus
# 3.0.x is stable, 3.1.x devel
# This development version is very stable and will be marked as stable very soon
# according to https://www.libmodbus.org/download
Version:	3.1.12
Release:	1
License:	LGPL v2.1+
Group:		Libraries
#Source0Download: https://github.com/stephane/libmodbus/releases
Source0:	https://github.com/stephane/libmodbus/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	24482d341203e048d4a7b7c15a417f53
Patch0:		optflags.patch
Patch1:		test.patch
URL:		https://libmodbus.org/
BuildRequires:	autoconf >= 2.63
BuildRequires:	automake >= 1:1.11
BuildRequires:	libtool >= 2:2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libmodbus is a free software library to send/receive data according to
the Modbus protocol. This library is written in C and supports RTU
(serial) and TCP (Ethernet) communications.

%description -l pl.UTF-8
libmodman to darmowa biblioteka do wysyłania/odbierania danych zgodnie
z protokołem Modbus. Jest napisana w C i obsługuje komunikację RTU
(porty szeregowe) i TCP (sieć Ethernet).

%package devel
Summary:	Header files for libmodbus library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libmodbus
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for libmodbus library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libmodbus.

%package static
Summary:	Static libmodbus library
Summary(pl.UTF-8):	Statyczna biblioteka libmodbus
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libmodbus library.

%description static -l pl.UTF-8
Statyczna biblioteka libmodbus.

%prep
%setup -q

%patch -P0 -p1
%patch -P1 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules \
	%{?with_static_libs:--enable-static}

%{__make}

%if %{with tests}
%{__make} check
%endif

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libmodbus.la

%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS.md README.md
%attr(755,root,root) %{_libdir}/libmodbus.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libmodbus.so.5

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libmodbus.so
%{_includedir}/modbus
%{_pkgconfigdir}/libmodbus.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libmodbus.a
%endif
