%define name libstroke
%define version 0.5.1
%define release %mkrel 11

%define fakename stroke

%define major 0
%define libname %mklibname %{fakename} %major
%define libnamedev %mklibname %{fakename} %major -d


Summary:	Stroke interface library
Name:		%{name}
Version:	%{version}
Release:	%{release}
URL:		http://www.etla.net/libstroke/
Source0:	%{name}-%{version}.tar.bz2
Patch0:		libstroke-0.5.1-fix-underquoted-calls.patch
License:	GPL
Group: System/Libraries
%if %{mdkversion} >= 200700
BuildRequires:	libx11-devel
%else
BuildRequires:	X11-devel
%endif
BuildRequires:	gtk+1.2-devel
BuildRequires:	libtool
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
LibStroke is a stroke interface library.  Strokes are motions
of the mouse that can be interpreted by a program as a command.  Strokes
are used extensively in CAD programs.

%package -n	%{libname}
Summary:	Stroke interface library
Group:	System/Libraries

%description -n	%{libname}
LibStroke is a stroke interface library.  Strokes are motions
of the mouse that can be interpreted by a program as a command.  Strokes
are used extensively in CAD programs.

%package -n	%{libnamedev}
Summary:	Development libraries for libStroke
Group:		Development/C
Provides:	%{name}-devel
Requires:	%{libname} = %{version}

%description -n %{libnamedev}
LibStroke is a stroke interface library.  Strokes are motions
of the mouse that can be interpreted by a program as a command.  Strokes
are used extensively in CAD programs.

%prep
%setup -q
%patch0 -p1 -b .underquoted

%build
%configure
# use system libtool (cheap fix, too ancient autotools in this package)
rm -f libtool
ln -s %{_bindir}/libtool .
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
%doc README AUTHORS COPYING NEWS
%{_libdir}/libgstroke.so.0.0.5
%{_libdir}/libgstroke.so.0
%{_libdir}/libstroke.so.0.0.5
%{_libdir}/libstroke.so.0

%files -n %{libnamedev}
%defattr(-,root,root)
%doc INSTALL TODO
%{_datadir}/aclocal/*
%{_libdir}/libgstroke.a
%{_libdir}/libgstroke.la
%{_libdir}/libgstroke.so
%{_libdir}/libstroke.a
%{_libdir}/libstroke.la
%{_libdir}/libstroke.so
%{_includedir}/*


