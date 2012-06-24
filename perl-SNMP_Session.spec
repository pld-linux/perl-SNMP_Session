#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
Summary:	SNMP Perl module
Summary(cs):	Modul SNMP pro Perl
Summary(da):	Perlmodul SNMP
Summary(de):	SNMP Perl Modul
Summary(es):	M�dulo de Perl SNMP
Summary(fr):	Module Perl SNMP
Summary(it):	Modulo di Perl SNMP
Summary(ja):	SNMP Perl �⥸�塼��
Summary(ko):	SNMP �� ����
Summary(no):	Perlmodul SNMP
Summary(pl):	Modu� perla do obs�ugi SNMP
Summary(pt):	M�dulo de Perl SNMP
Summary(pt_BR):	M�dulo Perl SNMP
Summary(ru):	������ ��� Perl SNMP
Summary(sv):	SNMP Perlmodul
Summary(uk):	������ ��� Perl SNMP
Summary(zh_CN):	SNMP Perl ģ��
Name:		perl-SNMP_Session
Version:	0.95
Release:	2
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.switch.ch/software/sources/network/snmp/perl/SNMP_Session-%{version}.tar.gz
# Source0-md5:	13ad848599633967603a4bc39b34b9fc
BuildRequires:	perl-devel >= 5.6.1
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains Perl 5 modules SNMP_Session.pm and BER.pm,
which, when used together, provide rudimentary access to remote SNMP
(v1/v2) agents.

%description -l pl
Ten pakiet zawiera modu�y Perla 5 SNMP_Session.pm i BER.pm, kt�re,
u�ywane wsp�lnie, daj� dost�p do zewn�trznych serwis�w SNMP (v1/v2).

%prep
%setup -q -n SNMP_Session-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}
%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README* test
%{perl_vendorlib}/*.pm
