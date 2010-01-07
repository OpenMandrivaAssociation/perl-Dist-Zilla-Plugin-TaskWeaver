%define upstream_name    Dist-Zilla-Plugin-TaskWeaver
%define upstream_version 0.093450

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Dist::Zilla::Plugin::TaskWeaver's helper
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Dist/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Dist::Zilla)
BuildRequires: perl(Dist::Zilla::Plugin::PodWeaver)
BuildRequires: perl(Moose)
BuildRequires: perl(Moose::Autobox)
BuildRequires: perl(Pod::Elemental)
BuildRequires: perl(Pod::Weaver)
BuildRequires: perl(Test::More)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
The TaskWeaver plugin acts just like the PodWeaver plugin, but gets its
claws just a bit into your Pod::Weaver configuration and then uses them to
figure out prerequisites and grouping for building a Task distribution.

The 'Task::' namespace is used for libraries that do not have any code of
their own, but are just ways of getting a lot of other libraries installed
at once. In other words, they're just prerequisites with no actual logic.

TaskWeaver expects that your _.pm_ file will have Pod like the following:

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%{make}

%check
%{make} test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes LICENSE README
%{_mandir}/man3/*
%perl_vendorlib/*


