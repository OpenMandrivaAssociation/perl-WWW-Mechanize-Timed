%define module WWW-Mechanize-Timed

Summary:	WWW::Mechanize::Timed - Time Mechanize requests
Name:		perl-%{module}
Version:	0.42
Release: %mkrel 3
License:	GPL or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{module}
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/WWW//%{module}-%{version}.tar.bz2
BuildRequires:	perl-devel
BuildRequires:	perl(LWPx::TimedHTTP)
BuildRequires:  perl(WWW::Mechanize)
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
This module is a subclass of WWW::Mechanize that times each stage
of the HTTP request. These can then be used in monitoring systems.


%prep
%setup -q -n %{module}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make
make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc CHANGES README
%{perl_vendorlib}/WWW/Mechanize/Timed.pm
%{_mandir}/*/*

