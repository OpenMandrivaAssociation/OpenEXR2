%define major 25
%define api		2_5
%define devname	%mklibname %{name} %{api} -d
%define libname	%mklibname IlmImf %{api} %{major}
#define libname_ilm_util	%mklibname IlmImfUtil %{api} %{major}
%define libname_ilm	%mklibname ilmbase %{api} %{major}
%define develname_ilm	%mklibname ilmbase %{api} -d


Summary:	A high dynamic-range (HDR) image file format
Name:		openexr2
Version:	2.5.7
Release:	1
License:	BSD
Group:		Graphics
Url:		http://www.openexr.com
Source0:  https://github.com/AcademySoftwareFoundation/openexr/archive/refs/tags/v%{version}/%{name}-%{version}.tar.gz
#BuildRequires:	fltk-devel
BuildRequires:  cmake
#BuildRequires:	pkgconfig(IlmBase) >= 2.2.1
BuildRequires:	pkgconfig(zlib)

Provides:	OpenEXR2 = %{version}-%{release}
Provides:	openexr2 = %{version}-%{release}

%description
Industrial Light & Magic developed the OpenEXR format in response to the demand
for higher color fidelity in the visual effects industry.

%package -n	%{libname}
Summary:	Dynamic libraries from %{name}
Group:		System/Libraries

%description -n	%{libname}
Dynamic libraries from %{name}.

%package -n	%{libname_ilm}
Summary:	Dynamic libraries from ilmbase
Group:		System/Libraries

%description -n	%{libname_ilm}
Dynamic libraries from ilmbase.

%package -n	%{develname_ilm}
Summary:	Header files and static libraries from ilmbase
Group:		Development/C
Requires:	%{libname_ilm} = %{version}-%{release}
Requires:	%{devname} = %{version}-%{release}
Provides:	libilmbase-devel = %{version}-%{release}
Provides:	ilmbase-devel = %{version}-%{release}

%description -n	%{develname_ilm}
Libraries and includes files for developing programs based on ilmbase.

%package -n %{devname}
Summary:	Header files and static libraries from %{name}
Group:		Development/C
Requires:	%{libname} = %{EVRD}
Requires: %{develname_ilm} = %{EVRD}
Requires: %{name} = %{EVRD}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
Libraries and includes files for developing programs based on %{name}.

%prep
%setup -q -n OpenEXR-%{version}
%autopatch -p1

%build
%cmake
%make_build

%install
%make_install -C build

# Remove doc files installed by make install, we package them in %files
rm -rf %{buildroot}%{_docdir}/OpenEXR-%{version}
rm -rf %{buildroot}%{_docdir}/OpenEXR

%files
%{_bindir}/exr*
%doc *.md CODEOWNERS
%doc doc/*

%files -n %{libname}
%{_libdir}/libIlmImf-%{api}.so.%{major}{,.*}
%{_libdir}/libIlmImfUtil-%{api}.so.%{major}{,.*}

%files -n %{libname_ilm}
%{_libdir}/libHalf-%{api}.so.%{major}{,.*}
%{_libdir}/libIex-%{api}.so.%{major}{,.*}
%{_libdir}/libIexMath-%{api}.so.%{major}{,.*}
%{_libdir}/libIlmThread-%{api}.so.%{major}{,.*}
%{_libdir}/libImath-%{api}.so.%{major}{,.*}

%files -n %{devname}
%dir %{_includedir}/OpenEXR
%{_includedir}/OpenEXR/Imf*.h
%{_includedir}/OpenEXR/OpenEXRConfig.h
%{_libdir}/libIlmImf.so
%{_libdir}/libIlmImf-%{api}.so
%{_libdir}/libIlmImfUtil.so
%{_libdir}/libIlmImfUtil-%{api}.so
%{_libdir}/pkgconfig/OpenEXR.pc
%{_libdir}/cmake/OpenEXR/

%files -n %{develname_ilm}
%{_includedir}/OpenEXR/half*.h
%{_includedir}/OpenEXR/Iex*.h
%{_includedir}/OpenEXR/Ilm*.h
%{_includedir}/OpenEXR/Imath*.h
%{_libdir}/libHalf.so
%{_libdir}/libHalf-%{api}.so
%{_libdir}/libIex.so
%{_libdir}/libIex-%{api}.so
%{_libdir}/libIexMath.so
%{_libdir}/libIexMath-%{api}.so
%{_libdir}/libIlmThread.so
%{_libdir}/libIlmThread-%{api}.so
%{_libdir}/libImath.so
%{_libdir}/libImath-%{api}.so
%{_libdir}/pkgconfig/IlmBase.pc
%{_libdir}/cmake/IlmBase/
