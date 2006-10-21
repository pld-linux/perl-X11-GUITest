#
# Conditional build:
%bcond_with	tests	# do perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	X11
%define		pnam	GUITest
Summary:	X11::GUITest - GUI testing/interaction facilities
Summary(pl):	X11::GUITest - u³atwienia do testowania/interakcji z GUI
Name:		perl-X11-GUITest
Version:	0.21
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	2c7bf7e1079094bda698404961c28ac2
BuildRequires:	XFree86-devel
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This Perl package is intended to facilitate the testing of GUI
applications by means of user emulation. It can be used to
test/interact with GUI applications which have been built upon the X
library or toolkits (i.e., GTK+, Xt, Qt, Motif, etc.) that "wrap" the
X library's functionality.

%description -l pl
Ten pakiet Perla ma u³atwiæ testowanie aplikacji z graficznym
interfejsem u¿ytkownika drog± emulacji u¿ytkownika. Mo¿e byæ u¿ywany
do testowania lub interakcji z aplikacjami GUI opartymi o bibliotekê X
lub toolkity (takie jak GTK+, Xt, Qt, Motif itp.) obudowuj±ce
funkcjonalno¶æ biblioteki X.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

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
%doc README docs/{Changes,ToDo}
%dir %{perl_vendorarch}/X11
%{perl_vendorarch}/X11/GUITest.pm
%dir %{perl_vendorarch}/auto/X11
%dir %{perl_vendorarch}/auto/X11/GUITest
%attr(755,root,root) %{perl_vendorarch}/auto/X11/GUITest/GUITest.so
%{perl_vendorarch}/auto/X11/GUITest/GUITest.bs
%{_mandir}/man3/*
