%define oname	stroke

%define major		0
%define libname		%mklibname %{oname} %major
%define develname	%mklibname %{oname} -d


Summary:	Stroke interface library
Name:		libstroke
Version:	0.5.1
Release:	%mkrel 17
URL:		http://www.etla.net/libstroke/
Source0:	%{name}-%{version}.tar.bz2
Patch0:		libstroke-0.5.1-fix-underquoted-calls.patch
Patch1:		libstroke-linkage_fix.diff
Patch2:		libstroke-0.5.1-no_gtk1.patch
Patch3:		libstroke-0.5.1-dup-defination.patch
Patch4:		libstroke-0.5.1-drop-unused-comments.patch
License:	GPLv2
Group:		System/Libraries
BuildRequires:	libx11-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
LibStroke is a stroke interface library. Strokes are motions
of the mouse that can be interpreted by a program as a command.  Strokes
are used extensively in CAD programs.

%package -n	%{libname}
Summary:	Stroke interface library
Group:		System/Libraries

%description -n	%{libname}
LibStroke is a stroke interface library. Strokes are motions
of the mouse that can be interpreted by a program as a command.  Strokes
are used extensively in CAD programs.

%package -n	%{develname}
Summary:	Development libraries for libStroke
Group:		Development/C
Provides:	%{name}-devel = %{version}-%{release}
Requires:	%{libname} = %{version}-%{release}
Obsoletes:	%{mklibname stroke 0 -d}

%description -n %{develname}
LibStroke is a stroke interface library. Strokes are motions
of the mouse that can be interpreted by a program as a command.  Strokes
are used extensively in CAD programs.

%prep
%setup -q
%patch0 -p1 -b .underquoted
%patch1 -p1
%patch2 -p1
%patch3 -p0
%patch4 -p0

%build
autoreconf -fi
%configure2_5x
%make

%install
rm -rf %{buildroot}

%makeinstall

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%clean
rm -rf %{buildroot}

%files -n %{libname}
%defattr(-,root,root)
%doc README AUTHORS COPYRIGHT NEWS
%{_libdir}/libstroke.so.%{major}*

%files -n %{develname}
%defattr(-,root,root)
%doc INSTALL TODO
%{_datadir}/aclocal/*
%{_libdir}/libstroke.*a
%{_libdir}/libstroke.so
%{_includedir}/*

