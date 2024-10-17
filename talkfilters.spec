%define major 1
%define libname %mklibname %{name} %{major}
%define libnamedev %mklibname -d %{name}

Summary:	GNU Talk filters
Name:		talkfilters
Version:	2.3.8
Release:	8
Source0:	%{name}-%{version}.tar.gz
Patch:		talkfilters-2.3.7-info-dir.patch
Patch1:		talkfilters-2.3.8-format-strings.patch
License:	GPLv2+
Group:		Toys
Url:		https://www.hyperrealm.com/talkfilters/talkfilters.html
BuildRequires:	texinfo
BuildRequires:	flex

%description
The GNU Talk Filters are filter programs that convert ordinary English
text into text that mimics a stereotyped or otherwise humorous
dialect. These filters have been in the public domain for many years,
but now for the first time they are provided as a single integrated
package. The filters include austro, b1ff, brooklyn, chef, cockney,
drawl, dubya, fudd, funetak, jethro, jive, kraut, pansy, pirate,
postmodern, redneck, valspeak, and warez. Each program reads from
standard input and writes to standard output. The package also
provides the filters as a C library, so they can be easily used by
other programs.

%package -n %{libname}
Summary:	GNU Talk filters shared library
Group:		System/Libraries

%description -n %{libname}
The GNU Talk Filters are filter programs that convert ordinary English
text into text that mimics a stereotyped or otherwise humorous
dialect. These filters have been in the public domain for many years,
but now for the first time they are provided as a single integrated
package. The filters include austro, b1ff, brooklyn, chef, cockney,
drawl, dubya, fudd, funetak, jethro, jive, kraut, pansy, pirate,
postmodern, redneck, valspeak, and warez. Each program reads from
standard input and writes to standard output. The package also
provides the filters as a C library, so they can be easily used by
other programs.

%package -n %{libnamedev}
Summary:	GNU Talk filters shared library
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{libnamedev}
The GNU Talk Filters are filter programs that convert ordinary English
text into text that mimics a stereotyped or otherwise humorous
dialect. These filters have been in the public domain for many years,
but now for the first time they are provided as a single integrated
package. The filters include austro, b1ff, brooklyn, chef, cockney,
drawl, dubya, fudd, funetak, jethro, jive, kraut, pansy, pirate,
postmodern, redneck, valspeak, and warez. Each program reads from
standard input and writes to standard output. The package also
provides the filters as a C library, so they can be easily used by
other programs.

%prep
%setup -q
%patch -p1 -b .info-dir
%patch1 -p1

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%files
%doc README AUTHORS
%{_bindir}/*
%{_mandir}/man1/*

%files -n %{libname}
%{_libdir}/libtalkfilters.so.%{major}*

%files -n %{libnamedev}
%doc ChangeLog
%{_libdir}/libtalkfilters.so
%{_libdir}/libtalkfilters.a
%{_libdir}/pkgconfig/*
%{_includedir}/*
%{_infodir}/talkfilters.info*


%changelog
* Fri Jun 08 2012 Andrey Bondrov <abondrov@mandriva.org> 2.3.8-7
+ Revision: 803281
- Drop some legacy junk

* Fri Aug 05 2011 Götz Waschk <waschk@mandriva.org> 2.3.8-6
+ Revision: 693304
- update build deps
- rebuild

* Mon Aug 03 2009 Götz Waschk <waschk@mandriva.org> 2.3.8-5mdv2011.0
+ Revision: 407700
- update license
- fix format strings

* Sat Aug 02 2008 Thierry Vignaud <tv@mandriva.org> 2.3.8-4mdv2009.0
+ Revision: 261372
- rebuild

* Tue Jul 29 2008 Thierry Vignaud <tv@mandriva.org> 2.3.8-3mdv2009.0
+ Revision: 254109
- rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Sun Dec 30 2007 Götz Waschk <waschk@mandriva.org> 2.3.8-1mdv2008.1
+ Revision: 139618
- new version

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Jul 20 2007 Götz Waschk <waschk@mandriva.org> 2.3.7-3mdv2008.0
+ Revision: 53859
- fix devel provides

* Fri Jul 20 2007 Götz Waschk <waschk@mandriva.org> 2.3.7-2mdv2008.0
+ Revision: 53858
- add proper info dir entry

* Fri Jul 20 2007 Götz Waschk <waschk@mandriva.org> 2.3.7-1mdv2008.0
+ Revision: 53804
- Import talkfilters



* Fri Jul 20 2007 Götz Waschk <waschk@mandriva.org> 2.3.7-1mdv2008.0
- initial package
