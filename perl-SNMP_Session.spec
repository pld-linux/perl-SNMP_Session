#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
Summary:	SNMP_Session - SNMP support for Perl 5
Summary(pl):	SNMP_Session - obs³uga SNMP dla Perla 5
Name:		perl-SNMP_Session
Version:	1.00
Release:	1
License:	Artistic
Group:		Development/Languages/Perl
Source0:	ftp://ftp.switch.ch/software/sources/network/snmp/perl/SNMP_Session-%{version}.tar.gz
# Source0-md5:	1a609ca5427213f74884127013622942
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains Perl 5 modules SNMP_Session.pm and BER.pm,
which, when used together, provide rudimentary access to remote SNMP
(v1/v2) agents.

%description -l pl
Ten pakiet zawiera modu³y Perla 5 SNMP_Session.pm i BER.pm, które,
u¿ywane wspólnie, daj± dostêp do zewnêtrznych serwisów SNMP (v1/v2).

%prep
%setup -q -n SNMP_Session-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README* index.html test
%{perl_vendorlib}/*.pm
