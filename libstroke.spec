%define oname	stroke

%define major		0
%define libname		%mklibname %{oname} %major
%define develname	%mklibname %{oname} -d


Summary:	Stroke interface library
Name:		libstroke
Version:	0.5.1
Release:	%mkrel 19
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



%changelog
* Mon May 09 2011 Funda Wang <fwang@mandriva.org> 0.5.1-17mdv2011.0
+ Revision: 672776
- rebuild

* Wed Sep 02 2009 Christophe Fergeau <cfergeau@mandriva.com> 0.5.1-16mdv2011.0
+ Revision: 425753
- rebuild

* Fri Apr 10 2009 Funda Wang <fwang@mandriva.org> 0.5.1-15mdv2009.1
+ Revision: 365806
- add patches

* Tue Aug 05 2008 Adam Williamson <awilliamson@mandriva.org> 0.5.1-14mdv2009.0
+ Revision: 264109
- package COPYRIGHT not COPYING
- clean file lists
- drop gtk+ 1.2 build dependency, and so (ancient and unneeded) GTK+ 1.2 support
- drop pre-2007.0 conditional
- clean some unnecessary defines
- new license policy
- new devel policy

* Sat Jun 28 2008 Oden Eriksson <oeriksson@mandriva.com> 0.5.1-13mdv2009.0
+ Revision: 229826
- added P1 to fix linkage

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Mon Feb 18 2008 Thierry Vignaud <tv@mandriva.org> 0.5.1-11mdv2008.1
+ Revision: 170958
- rebuild
- fix "foobar is blabla" summary (=> "blabla") so that it looks nice in rpmdrake
- rebuild
- kill re-definition of %%buildroot on Pixel's request
- buildrequires X11-devel instead of XFree86-devel

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot


* Mon Jan 29 2007 Per Øyvind Karlsen <pkarlsen@mandriva.com> 0.5.1-9mdv2007.0
+ Revision: 115067
- fix P0

* Mon Jan 29 2007 Per Øyvind Karlsen <pkarlsen@mandriva.com> 0.5.1-8mdv2007.1
+ Revision: 114805
- fix underquoted calls (P0)

* Tue Jan 16 2007 Gwenole Beauchesne <gbeauchesne@mandriva.com> 0.5.1-7mdv2007.1
+ Revision: 109586
- fix build on modern platforms

* Fri Oct 07 2005 Lenny Cartier <lenny@mandriva.com> 0.5.1-6mdk
- rebuild

* Fri Aug 20 2004 Lenny Cartier <lenny@mandrakesoft.com> 0.5.1-5mdk
- rebuild

