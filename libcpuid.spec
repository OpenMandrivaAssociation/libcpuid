%define major 14
%define libname %mklibname cpuid %{major}
%define devname %mklibname cpuid -d

Summary:	Small C library for x86 CPU detection and feature extraction 
Name:		libcpuid
# Version extracted from configure.ac file
Version:	0.4.1
Release:	3.git.07.12.2018
License:	BSD
Group:		System/Libraries
Url:		http://libcpuid.sourceforge.net
#Source0:	https://github.com/anrieff/libcpuid/archive/v%{version}.tar.gz?/%{name}-%{version}.tar.gz
Source: %{name}-master-07.12.2018.zip

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
%setup -qn %{name}-master

%build
autoreconf -fi
%configure2_5x --disable-static
%make

%install
%makeinstall_std
