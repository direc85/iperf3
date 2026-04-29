# Spec file derived from Fedora 42 packaging.

Name:           iperf3
Version:        3.21
Release:        1
Summary:        Measurement tool for TCP/UDP bandwidth performance

# src/cjson.{c,h} and src/net.{c,h} are MIT
# part of the code is dtoa
# part of src/net.c is BSD-3-Clause-HP
# src/queue.h is BSD-3-Clause
# src/units.{c.h} is NCSA
# src/portable_endian.h is LicenseRef-Fedora-Public-Domain
License:        BSD-3-Clause-LBNL AND MIT AND dtoa AND BSD-3-Clause AND NCSA AND LicenseRef-Fedora-Public-Domain
URL:            https://github.com/esnet/iperf
Source:         %{name}-%{version}.tar.bz2
BuildRequires:  libuuid-devel
BuildRequires:  gcc
BuildRequires:  lksctp-tools-devel
BuildRequires:  openssl-devel
BuildRequires:  make

%description
Iperf is a tool to measure maximum TCP bandwidth, allowing the tuning of
various parameters and UDP characteristics. Iperf reports bandwidth, delay
jitter, data-gram loss.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package doc
Summary:        Documentation for iperf3
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description doc
%{summary}.

%prep
%autosetup -p1 -n %{name}-%{version}/%{name}

%build
%configure --disable-static
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
%make_build

%install
%make_install
rm -f %{buildroot}%{_libdir}/libiperf.la

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%doc README.md LICENSE RELNOTES.md
%{_bindir}/iperf3
%{_libdir}/*.so.*

%files doc
%{_mandir}/man1/iperf3.1.gz
%{_mandir}/man3/libiperf.3.gz

%files devel
%{_includedir}/iperf_api.h
%{_libdir}/*.so
