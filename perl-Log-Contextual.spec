#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Log-Contextual
Version  : 0.008001
Release  : 24
URL      : https://cpan.metacpan.org/authors/id/F/FR/FREW/Log-Contextual-0.008001.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/F/FR/FREW/Log-Contextual-0.008001.tar.gz
Summary  : 'Simple logging interface with a contextual log'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-Log-Contextual-license = %{version}-%{release}
Requires: perl-Log-Contextual-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(Data::Dumper::Concise)
BuildRequires : perl(Devel::GlobalDestruction)
BuildRequires : perl(Exporter::Declare)
BuildRequires : perl(Meta::Builder)
BuildRequires : perl(Module::Runtime)
BuildRequires : perl(Moo)
BuildRequires : perl(Role::Tiny)
BuildRequires : perl(Sub::Defer)
BuildRequires : perl(Sub::Exporter::Progressive)
BuildRequires : perl(Test::Fatal)
BuildRequires : perl(Try::Tiny)
BuildRequires : perl(aliased)

%description
NAME
Log::Contextual - Simple logging interface with a contextual log
VERSION
version 0.008001

%package dev
Summary: dev components for the perl-Log-Contextual package.
Group: Development
Provides: perl-Log-Contextual-devel = %{version}-%{release}
Requires: perl-Log-Contextual = %{version}-%{release}

%description dev
dev components for the perl-Log-Contextual package.


%package license
Summary: license components for the perl-Log-Contextual package.
Group: Default

%description license
license components for the perl-Log-Contextual package.


%package perl
Summary: perl components for the perl-Log-Contextual package.
Group: Default
Requires: perl-Log-Contextual = %{version}-%{release}

%description perl
perl components for the perl-Log-Contextual package.


%prep
%setup -q -n Log-Contextual-0.008001
cd %{_builddir}/Log-Contextual-0.008001

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Log-Contextual
cp %{_builddir}/Log-Contextual-0.008001/LICENSE %{buildroot}/usr/share/package-licenses/perl-Log-Contextual/1e40fc1cb7b56a9fab2b5614f9c4b155f40f16db
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Log::Contextual.3
/usr/share/man/man3/Log::Contextual::Easy::Default.3
/usr/share/man/man3/Log::Contextual::Easy::Package.3
/usr/share/man/man3/Log::Contextual::Role::Router.3
/usr/share/man/man3/Log::Contextual::Role::Router::HasLogger.3
/usr/share/man/man3/Log::Contextual::Role::Router::SetLogger.3
/usr/share/man/man3/Log::Contextual::Role::Router::WithLogger.3
/usr/share/man/man3/Log::Contextual::Router.3
/usr/share/man/man3/Log::Contextual::SimpleLogger.3
/usr/share/man/man3/Log::Contextual::TeeLogger.3
/usr/share/man/man3/Log::Contextual::WarnLogger.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Log-Contextual/1e40fc1cb7b56a9fab2b5614f9c4b155f40f16db

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
