%define major 25
%define ilmimfmajor 26
%define api		2_5
%define devname	%mklibname %{oname} %{api} -d
%define libname	%mklibname IlmImf %{api} %{major}
#define libname_ilm_util	%mklibname IlmImfUtil %{api} %{major}
%define libname_ilm	%mklibname ilmbase %{api} %{major}
%define develname_ilm	%mklibname ilmbase %{api} -d

%define oname openexr

Summary:	A high dynamic-range (HDR) image file format
Name:		openexr2
Version:	2.5.8
Release:	2
License:	BSD
Group:		Graphics
Url:		https://www.openexr.com
Source0:  https://github.com/AcademySoftwareFoundation/openexr/archive/refs/tags/v%{version}/openexr-%{version}.tar.gz
#BuildRequires:	fltk-devel
BuildRequires:  cmake
#BuildRequires:	pkgconfig(IlmBase) >= 2.2.1
BuildRequires:	pkgconfig(zlib)
BuildRequires:	pkgconfig(python3)
BuildRequires:	cmake(boost_python)
BuildRequires:	python-numpy
BuildRequires:	boost-devel

Provides:	OpenEXR2 = %{version}-%{release}

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

%package -n python-%{name}
Summary:	Python bindings for %{name}
Group:		Development/Python

%description -n python-%{name}
Python bindings for %{name}

%prep
%autosetup -p1 -n openexr-%{version}
%cmake

%build
%make_build -C build

%install
%make_install -C build

# Remove doc files installed by make install, we package them in %files
rm -rf %{buildroot}%{_docdir}/OpenEXR-%{version}
rm -rf %{buildroot}%{_docdir}/OpenEXR

# Headers for Py* stuff are useless, they're used only to build the
# python bindings inside the tree
rm -rf %{buildroot}%{_includedir}/OpenEXR/Py*

for i in %{buildroot}%{_bindir}/*; do
	mv $i ${i}2
done

%files
%{_bindir}/exr*
%doc *.md CODEOWNERS
%doc doc/*

%files -n %{libname}
%{_libdir}/libIlmImf-%{api}.so.%{ilmimfmajor}{,.*}
%{_libdir}/libIlmImfUtil-%{api}.so.%{ilmimfmajor}{,.*}

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

%files -n python-%{name}
%{_libdir}/cmake/PyIlmBase
%{_libdir}/libPyIex_Python*.so*
%{_libdir}/libPyImath_Python*.so*
%{_libdir}/python*/site-packages/*.so
%{_libdir}/pkgconfig/PyIlmBase.pc
