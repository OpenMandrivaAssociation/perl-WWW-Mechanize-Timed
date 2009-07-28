%define upstream_name    WWW-Mechanize-Timed
%define upstream_version 0.44

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:	WWW::Mechanize::Timed - Time Mechanize requests
License:	GPL+ or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{upstream_name}
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/WWW//%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl(LWPx::TimedHTTP)
BuildRequires:  perl(WWW::Mechanize)
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
This module is a subclass of WWW::Mechanize that times each stage
of the HTTP request. These can then be used in monitoring systems.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
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
