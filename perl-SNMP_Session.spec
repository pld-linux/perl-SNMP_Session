%include	/usr/lib/rpm/macros.perl
Summary:	SNMP perl module
Summary(pl):	Modu³ perla do obs³ugi SNMP
Name:		perl-SNMP_Session
Version:	0.91
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Group(cs):	Vývojové prostøedky/Programovací jazyky/Perl
Group(da):	Udvikling/Sprog/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(es):	Desarrollo/Lenguajes/Perl
Group(fr):	Development/Langues/Perl
Group(is):	Þróunartól/Forritunarmál/Perl
Group(it):	Sviluppo/Linguaggi/Perl
Group(ja):	³«È¯/¸À¸ì/Perl
Group(no):	Utvikling/Programmeringsspråk/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Group(pt):	Desenvolvimento/Linguagens/Perl
Group(ru):	òÁÚÒÁÂÏÔËÁ/ñÚÙËÉ/Perl
Group(sl):	Razvoj/Jeziki/Perl
Group(sv):	Utveckling/Språk/Perl
Source0:	ftp://ftp.switch.ch/software/sources/network/snmp/perl/SNMP_Session-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6.1
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
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf README*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz test
%{perl_sitelib}/*.pm
