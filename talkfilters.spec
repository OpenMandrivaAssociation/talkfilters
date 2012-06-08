%define major 1
%define libname %mklibname %{name} %{major}
%define libnamedev %mklibname -d %{name}

Summary:	GNU Talk filters
Name:		talkfilters
Version:	2.3.8
Release:	7
Source0:	%{name}-%{version}.tar.gz
Patch:		talkfilters-2.3.7-info-dir.patch
Patch1:		talkfilters-2.3.8-format-strings.patch
License:	GPLv2+
Group:		Toys
Url:		http://www.hyperrealm.com/talkfilters/talkfilters.html
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
