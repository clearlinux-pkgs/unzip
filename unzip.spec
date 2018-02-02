Name:           unzip
Version:        6.0
Release:        19
License:        BSD-3-Clause
Summary:        Utility for extracting zip archives
Url:            http://www.info-zip.org
Group:          utils
Source0:        ftp://ftp.info-zip.org/pub/infozip/src/unzip60.tgz
Patch0:         cve-2014-8139.patch
Patch1:         cve-2014-8140.patch
Patch2:         cve-2014-8141.patch
Patch3:         cve-2014-9636.patch
Patch4:         cve-2015-7696.patch
Patch5:         cve-2015-7697.patch
Patch6:         cve-2016-9844.patch
Patch7:         cve-2014-9913.patch

BuildRequires:  bzip2-dev

%description
Utility for extracting zip archives.

%package -n unzip-doc
Summary:        Utility for extracting zip archives
Group:          doc

%description -n unzip-doc
Utility for extracting zip archives.

%prep
%setup -q -n unzip60
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1

%build
export CFLAGS="%{optflags}"
# avoid stripping binaries
sed -i 's/\(LFLAGS2=\)"-s"/\1/' unix/configure
# Makefile calls configure which modifies some of the flags and the default
# flags are not being used. Passing CFLAGS here would enable the default flags
# at a later point.
export DEFAULTFLAGS="${CFLAGS}"
sed -i 's/\(CFLAGSR="\${CFLAGSR} \${CFLAGS_OPT}\)"/\1 ${DEFAULTFLAGS}"/' unix/configure
make -f unix/Makefile STRIP="" generic

%install
make -f unix/Makefile install prefix=%{buildroot}%{_prefix}
install -d %{buildroot}%{_mandir}
mv %{buildroot}%{_prefix}/man/* %{buildroot}%{_mandir}
rmdir %{buildroot}%{_prefix}/man/

%check
make -f unix/Makefile test


%files
/usr/bin/unzip
/usr/bin/zipgrep
/usr/bin/zipinfo
/usr/bin/unzipsfx
/usr/bin/funzip

%files -n unzip-doc
%{_mandir}/man1/*

