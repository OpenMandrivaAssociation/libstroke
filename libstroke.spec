%define oname	stroke
%define major	0
%define libname	%mklibname %{oname} %major
%define devname	%mklibname %{oname} -d

Summary:	Stroke interface library
Name:		libstroke
Version:	0.5.1
Release:	30
License:	GPLv2
Group:		System/Libraries
Url:		https://www.etla.net/libstroke/
# Old original source is no longer available, so let's use Arch mirror:
Source0:  https://sources.archlinux.org/other/packages/libstroke/%{name}-%{version}.tar.gz
#Source0:	http://etla.net/libstroke/%{name}-%{version}.tar.gz

Patch0:		libstroke-0.5.1-fix-underquoted-calls.patch
Patch1:		libstroke-linkage_fix.diff
Patch2:		libstroke-0.5.1-no_gtk1.patch
Patch3:		libstroke-0.5.1-dup-defination.patch
Patch4:		libstroke-0.5.1-drop-unused-comments.patch
Patch5:		libstroke-automake-1.13.patch
BuildRequires:	pkgconfig(x11)

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

%package -n	%{devname}
Summary:	Development libraries for libStroke
Group:		Development/C
Provides:	%{name}-devel = %{version}-%{release}
Requires:	%{libname} = %{version}-%{release}

%description -n %{devname}
This package includes the development files for %{name}.

%prep
%setup -q
%autopatch -p1
autoreconf -fi

%build
%configure --disable-static
%make_build

%install
%make_install

%files -n %{libname}
%{_libdir}/libstroke.so.%{major}*

%files -n %{devname}
%doc INSTALL TODO README AUTHORS COPYRIGHT NEWS
%{_datadir}/aclocal/*
%{_libdir}/libstroke.so
%{_includedir}/*
