%define	major 2
%define libname	%mklibname bhpos_commonlibs %{major}

Summary:	BananaPOS bhpos common libraries
Name:		bhpos_commonlibs
Version:	2.0.0
Release:	%mkrel 0.beta3.4
License:	GPL
Group:		System/Libraries
URL:		http://www.bananahead.com
Source0:	ftp://bananahead.com/pub/bhpos2/stable/%{name}-%{version}.tar.bz2
BuildRequires:	bhpos_base >= 2.0.0
BuildRequires:	bhpos_base-devel >= 2.0.0
BuildRequires:	gtkmm2.4
BuildRequires:	gtkmm2.4-devel
BuildRequires:	intltool
BuildRequires:	libtool >= 1.5
BuildRequires:	libxml2 >= 2.5.8
BuildRequires:	libusb-devel >= 0.1.8
BuildRequires:	libxml++-devel >= 2.6
BuildRequires:	pkgconfig
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
BananaPOS common bibraries, as the name suggests are needed by
the server, client, and utilities.

%package -n	%{libname}
Summary:	BananaPOS bhpos common libraries
Group:          System/Libraries
Requires:	bhpos_base >= 2.0.0

%description -n	%{libname}
BananaPOS common bibraries, as the name suggests are needed by
the server, client, and utilities.

%package -n	%{libname}-devel
Summary:	Development files for the %{libname} library
Group:		Development/C
Requires:	libtool >= 1.5
Requires:	bhpos_base-devel >= 2.0.0
Provides:	%{name}-devel = %{version}
Provides:	lib%{name}-devel = %{version}
Requires:	%{libname} = %{version}-%{release}

%description -n	%{libname}-devel
Development files for the %{libname} library

%prep

%setup -q -n %{name}-%{version}

%build
sh ./autogen.sh

%configure2_5x

%make

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%makeinstall_std

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files -n %{libname}
%defattr(-,root,root)
%doc ChangeLog NEWS README
%{_libdir}/bhpos2.0/lib*.so.*

%files -n %{libname}-devel
%defattr(-, root, root)  
%{_libdir}/bhpos2.0/*.a
%{_libdir}/bhpos2.0/*.la
%{_libdir}/bhpos2.0/*.so
%{_libdir}/pkgconfig/bhcommlib-2.0.pc
%{_includedir}/bhpos2.0/*.h


