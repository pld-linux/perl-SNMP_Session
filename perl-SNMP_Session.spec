#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
Summary:	SNMP_Session - SNMP support for Perl 5
Summary(cs.UTF-8):	Modul SNMP pro Perl
Summary(da.UTF-8):	Perlmodul SNMP
Summary(de.UTF-8):	SNMP Perl Modul
Summary(es.UTF-8):	Módulo de Perl SNMP
Summary(fr.UTF-8):	Module Perl SNMP
Summary(it.UTF-8):	Modulo di Perl SNMP
Summary(ja.UTF-8):	SNMP Perl モジュール
Summary(ko.UTF-8):	SNMP 펄 모줄
Summary(nb.UTF-8):	Perlmodul SNMP
Summary(pl.UTF-8):	SNMP_Session - obsługa SNMP dla Perla 5
Summary(pt.UTF-8):	Módulo de Perl SNMP
Summary(pt_BR.UTF-8):	Módulo Perl SNMP
Summary(ru.UTF-8):	Модуль для Perl SNMP
Summary(sv.UTF-8):	SNMP Perlmodul
Summary(uk.UTF-8):	Модуль для Perl SNMP
Summary(zh_CN.UTF-8):	SNMP Perl 模块
Name:		perl-SNMP_Session
Version:	1.13
Release:	1
License:	Artistic
Group:		Development/Languages/Perl
Source0:	http://snmp-session.googlecode.com/files/SNMP_Session-%{version}.tar.gz
# Source0-md5:	055e1065babf55f1f8606329c6bdb947
URL:		http://code.google.com/p/snmp-session/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains Perl 5 modules SNMP_Session.pm and BER.pm,
which, when used together, provide rudimentary access to remote SNMP
(v1/v2) agents.

%description -l pl.UTF-8
Ten pakiet zawiera moduły Perla 5 SNMP_Session.pm i BER.pm, które,
używane wspólnie, dają dostęp do zewnętrznych serwisów SNMP (v1/v2).

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
