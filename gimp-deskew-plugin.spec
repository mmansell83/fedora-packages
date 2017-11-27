%global gittag master
Name:           gimp-deskew-plugin
Version:        1.1
Release:        1%{?dist}
Summary:        A deskew plug-in for GIMP

License:        GPL v2+
URL:            https://github.com/prokoudine/gimp-deskew-plugin
Source0:        %{url}/archive/%{gittag}/%{name}-%{gittag}.zip

BuildRequires:  automake >= 1.6, autoconf >= 2.54, glib2-devel >= 2.0.0, intltool >= 0.17, gimp-devel >= 2.0, gcc, make
Requires:       gimp >= 2.0, gimp-libs >= 2.0

%description

Copyright (C) 2007 Karl Chen <quarl@cs.berkeley.edu>

http://www.cubewano.org/gimp-deskew-plugin/

Distributed under GPL v2+ (see COPYING).

Uses Radon skew detection algorithm and code from the PageTools project
(http://sourceforge.net/projects/pagetools).  kale4@users.sourceforge.net,
yet@users.sourceforge.net.

%prep
%autosetup -n %{name}-%{gittag}


%build
%{_builddir}/%{name}-%{gittag}/autogen.sh --prefix=/usr
%make_build


%install
rm -rf $RPM_BUILD_ROOT
%make_install

mv %{buildroot}/usr/usr/* %{buildroot}/usr/
rm -rf %{buildroot}/usr/usr

%files
%license COPYING
%{_libdir}/gimp/2.0/plug-ins/deskew
%{_datarootdir}/%{name}/help/en/gimp-help.xml
%{_datarootdir}/%{name}/help/en/index.html
%{_datarootdir}/%{name}/help/images/wilber.png


%changelog
* Sun Nov 26 2017 Michael Mansell <michael.mansell@gmail.com>
- Initial attempt
- Fix for weird path issues and extra files
