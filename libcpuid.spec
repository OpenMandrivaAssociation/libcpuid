%define major 17
%define libname %mklibname cpuid
%define oldlibname %mklibname cpuid 16
%define devname %mklibname cpuid -d

Summary:	Small C library for x86 CPU detection and feature extraction 
Name:		libcpuid
Version:	0.7.1
Release:	1
License:	BSD
Group:		System/Libraries
Url:		https://libcpuid.sourceforge.net
Source0:	https://github.com/anrieff/libcpuid/archive/v%{version}/%{name}-%{version}.tar.gz

%description
Small C library for x86 CPU detection and feature extraction.

#----------------------------------------------------------------------------

%package tools
Summary:	Tools for x86 CPU detection and feature extraction
Group:		System/Configuration/Hardware

%description tools
Tools for x86 CPU detection and feature extraction.

%files tools
%{_bindir}/cpuid_tool

#----------------------------------------------------------------------------

%package -n %{libname}
Summary:	Small C library for x86 CPU detection and feature extraction
Group:		System/Libraries
%rename %{oldlibname}

%description -n %{libname}
This package contains the library needed to run programs dynamically
linked with %{name}.

%files -n %{libname}
%{_libdir}/libcpuid.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{devname}
Summary:	Headers for developing programs that will use %{name}
Group:		Development/C
Requires:	%{libname} = %{EVRD}
Provides:	%{name}-devel = %{EVRD}

%description -n %{devname}
This package contains the headers that programmers will need to develop
applications which will use %{name}.

%files -n %{devname}
%dir %{_includedir}/%{name}/
%{_includedir}/%{name}/*
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/*

#----------------------------------------------------------------------------

%prep
%setup -q

%build
autoreconf -fi
%configure --disable-static
%make_build

%install
%make_install
