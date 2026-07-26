%define upstream_name    WWW-Mechanize-Timed
Name:		perl-%{upstream_name}
Version:	0.44
Release:	6

Summary:	WWW::Mechanize::Timed - Time Mechanize requests
License:	GPL+ or Artistic
Group:		Development/Perl
URL:		https://metacpan.org/dist/WWW-Mechanize-Timed
Source0:	https://cpan.metacpan.org/authors/id/L/LB/LBROCARD/WWW-Mechanize-Timed-%{version}.tar.gz

BuildRequires:	make
BuildRequires:	perl-devel
BuildRequires:	perl(LWPx::TimedHTTP)
BuildRequires:	perl(WWW::Mechanize)
BuildArch:	noarch

%description
This module is a subclass of WWW::Mechanize that times each stage
of the HTTP request. These can then be used in monitoring systems.

%prep
%setup -q -n %{upstream_name}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc CHANGES README
%{perl_vendorlib}/WWW/Mechanize/Timed.pm
%{_mandir}/*/*


%changelog
* Tue Jul 28 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.440.0-1mdv2010.0
+ Revision: 401915
- rebuild using %0.44 Fri Aug 08 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.44-2mdv2009.0
+ Revision: 268876
- rebuild early 2009.0 package (before pixel changes)

* Tue May 06 2008 Olivier Blin <oblin@mandriva.com> 0.44-1mdv2009.0
+ Revision: 201988
- restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request

* Wed Aug 15 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.43-1mdv2008.0
+ Revision: 63966
- update to new version 0.43

* Wed May 09 2007 Oden Eriksson <oeriksson@mandriva.com> 0.42-5mdv2008.0
+ Revision: 25463
- rebuild

* Sun May 06 2007 Olivier Thauvin <nanardon@mandriva.org> 0.42-4mdv2008.0
+ Revision: 23569
- rebuild


* Fri Apr 28 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.42-3mdk
- Fix SPEC according to Perl Policy

* Tue Mar 21 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.42-2mdk
- Add BuildRequires
	- BuildRequires
	- Source URL
- use mkrel

* Thu Jul 14 2005 Oden Eriksson <oeriksson@mandriva.com> 0.42-1mdk
- initial Mandriva package

