#
# Conditional build:
#
Summary:	libmodbus is a free software library to send/receive data according to the Modbus protocol
Summary(pl.UTF-8):	libmodbus to darmowa biblioteka do wysyłania/odbierania danych zgodnie z protokołem Modbus
Name:		libmodbus
Version:	3.0.2
Release:	1
License:	LGPL v2.1+
Group:		Libraries
Source0:	http://github.com/downloads/stephane/libmodbus/%{name}-%{version}.tar.gz
# Source0-md5:	1aaacce9d9779d3a84f7d1a75774c943
URL:		http://www.libmodbus.org/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libmodbus is a free software library to send/receive data according to
the Modbus protocol. This library is written in C and supports RTU
(serial) and TCP (Ethernet) communications.

%description -l pl.UTF-8
libmodman to darmowa biblioteka do wysyłania/odbierania danych zgodnie
z protokołem Modbus. Jest napisana w C i wspiera komunikacje RTU
(porty szeregowe) i TCP (sieć ethernet)

%package devel
Summary:	Header files for libmodbus library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libmodbus
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libstdc++-devel

%description devel
Header files for libmodbus library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libmodbus.

%prep
%setup -q

%build

%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__autoconf}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS COPYING MIGRATION README.rst
%attr(755,root,root) %{_libdir}/libmodbus.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libmodbus.so.5
%{_mandir}/man3/modbus_*
%{_mandir}/man7/libmodbus.7*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libmodbus.so
%{_libdir}/libmodbus.la
%dir %{_includedir}/modbus
%{_includedir}/modbus/modbus*.h
%{_pkgconfigdir}/libmodbus.pc
