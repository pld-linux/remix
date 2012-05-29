Summary:	Audio sequencing and mixing library
Summary(pl.UTF-8):	Biblioteka sekwencera i miksera dźwięku
Name:		remix
Version:	0.2.4
Release:	1
License:	LGPL v2+
Group:		Libraries
Source0:	http://www.metadecks.org/software/remix/download/%{name}-%{version}.tar.gz
# Source0-md5:	ab3bd134a9011fc981794093dcd7ddf7
Patch0:		%{name}-link.patch
URL:		http://www.metadecks.org/software/remix/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	doxygen
BuildRequires:	libsndfile-devel >= 1.0.0
BuildRequires:	libtool
Requires:	libsndfile >= 1.0.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Remix is an audio sequencing and mixing library that provides a
multichannel, sparse audio data container (streams), a structured
mixing abstraction (decks), and widely useful means of generating
control data (via envelopes) and of caching audio data.
 
%description -l pl.UTF-8
Remix to biblioteka sekwencera i miksera dźwięku, udostępniająca
wielokanałowy, rzadki kontener danych (strumieni) dźwiękowych,
strukturalną abstrakcję miksowania (decki) oraz różne przydatne
sposoby generowania danych kontrolnych (poprzez opakowania) oraz
buforowania danych dźwiękowych.

%package devel
Summary:	Header files for libremix library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libremix
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libsndfile-devel >= 1.0.0

%description devel
Header files for libremix library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libremix.

%package static
Summary:	Static libremix library
Summary(pl.UTF-8):	Statyczna biblioteka libremix
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libremix library.

%description static -l pl.UTF-8
Statyczna biblioteka libremix.

%package apidocs
Summary:	libremix API documentation
Summary(pl.UTF-8):	Dokumentacja API biblioteki libremix
Group:		Documentation

%description apidocs
API and internal documentation for libremix library.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki libremix.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la
# dlopened modules
%{__rm} $RPM_BUILD_ROOT%{_libdir}/remix/*.{a,la}
# packaged as HTML in -apidocs
%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/remix/{html,latex}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ACKNOWLEDGEMENTS AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_libdir}/libctxdata.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libctxdata.so.0
%attr(755,root,root) %{_libdir}/libremix.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libremix.so.0
%dir %{_libdir}/remix
%attr(755,root,root) %{_libdir}/remix/libremix_ladspa.so*
%attr(755,root,root) %{_libdir}/remix/libremix_noise.so*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libctxdata.so
%attr(755,root,root) %{_libdir}/libremix.so
%{_includedir}/ctxdata.h
%{_includedir}/remix
%{_pkgconfigdir}/ctxdata.pc
%{_pkgconfigdir}/remix.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libctxdata.a
%{_libdir}/libremix.a

%files apidocs
%defattr(644,root,root,755)
%doc doc/libremix/html/*
