#
# Conditional build:
%bcond_with	tests	# do perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	X11
%define		pnam	GUITest
Summary:	X11::GUITest - GUI testing/interaction facilities
Summary(pl.UTF-8):	X11::GUITest - ułatwienia do testowania/interakcji z GUI
Name:		perl-X11-GUITest
Version:	0.25
Release:	4
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/X11/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	c2ea2418a5cef380e260dce9230c1d8b
URL:		http://search.cpan.org/dist/X11-GUITest/
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXtst-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This Perl package is intended to facilitate the testing of GUI
applications by means of user emulation. It can be used to
test/interact with GUI applications which have been built upon the X
library or toolkits (i.e., GTK+, Xt, Qt, Motif, etc.) that "wrap" the
X library's functionality.

%description -l pl.UTF-8
Ten pakiet Perla ma ułatwić testowanie aplikacji z graficznym
interfejsem użytkownika drogą emulacji użytkownika. Może być używany
do testowania lub interakcji z aplikacjami GUI opartymi o bibliotekę X
lub toolkity (takie jak GTK+, Xt, Qt, Motif itp.) obudowujące
funkcjonalność biblioteki X.

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
%doc docs/{Changes,ToDo,X11-GUITest*}
%dir %{perl_vendorarch}/X11
%{perl_vendorarch}/X11/GUITest.pm
%dir %{perl_vendorarch}/auto/X11
%dir %{perl_vendorarch}/auto/X11/GUITest
%attr(755,root,root) %{perl_vendorarch}/auto/X11/GUITest/GUITest.so
%{_mandir}/man3/*
