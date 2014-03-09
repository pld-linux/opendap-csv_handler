#
# Conditional build:
%bcond_with	tests	# make check (requires BES server)
#
Summary:	CSV module for the OPeNDAP data server
Summary(pl.UTF-8):	Moduł CSV dla serwera danych OPeNDAP
Name:		opendap-csv_handler
Version:	1.0.3
Release:	1
License:	LGPL v2.1+
Group:		Daemons
Source0:	http://www.opendap.org/pub/source/csv_handler-%{version}.tar.gz
# Source0-md5:	a91f219182e71db8455a7ebd39ce4b71
URL:		http://opendap.org/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1:1.10
%{?with_tests:BuildRequires:	bes >= 3.9.0}
BuildRequires:	bes-devel >= 3.9.0
%{?with_tests:BuildRequires:	cppunit-devel >= 1.12.0}
BuildRequires:	libdap-devel >= 3.11.0
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:1.5
BuildRequires:	pkgconfig
Requires:	bes >= 3.9.0
Requires:	libdap >= 3.11.0
# old name (single v3.5.1 release from 2010)
Obsoletes:	opendap-csv_module
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is the CSV module for the OPeNDAP data server. It serves data
stored in CSV-formatted files.

%description -l pl.UTF-8
Ten pakiet zawiera moduł CSV dla serwera danych OPeNDAP. Serwuje dane
zapisane w plikach w formacie CSV.

%prep
%setup -q -n csv_handler-%{version}

%build
# rebuild autotools for -as-needed to work
%{__libtoolize}
%{__aclocal} -I conf
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%{?with_tests:%{__make} check}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/bes/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYRIGHT ChangeLog NEWS README
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/bes/modules/csv.conf
%attr(755,root,root) %{_libdir}/bes/libcsv_module.so
%dir %{_datadir}/hyrax/data/csv
%{_datadir}/hyrax/data/csv/temperature.csv
