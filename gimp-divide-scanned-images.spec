%global gittag master
%global gitreponame DivideScannedImages

%global gimpplugindir %(gimptool --gimpplugindir)/plug-ins
%global gimpscriptdir %(gimptool --gimpdatadir)/scripts

Name:           gimp-divide-scanned-images
Version:        201610
Release:        6%{?dist}
Summary:        GIMP script for splitting separate sub-image fomr a composite image.

License:        GPL v2+
URL:            https://github.com/FrancoisMalan/%{gitreponame}
Source0:        %{url}/archive/%{gittag}/%{gitreponame}-%{gittag}.tar.gz

BuildRequires:  gimp-devel-tools >= 2.0
Requires:       gimp >= 2.0, gimp-libs >= 2.0
Recommends:     gimp-deskew-plugin

BuildArch:      noarch

%description
DivideScannedImages.scm
by Francois Malan
Based on a script originally by Rob Antonishen http://ffaat.pointclark.net

Locates each separate element in an image and creates a new image from each.
If option is selected, will call the deskew plugin by Karl Chen https://github.com/prokoudine/gimp-deskew-plugin (if it is installed) on each item.

%prep
%autosetup -n %{gitreponame}-%{gittag}

%build


%install
mkdir -p %{buildroot}/%{gimpscriptdir}

install -m 0755 DivideScannedImages.scm %{buildroot}/%{gimpscriptdir}


%files
%{gimpscriptdir}/DivideScannedImages.scm


%changelog
* Sun Dec 10 2017 Michael Mansell
- Updated gimp paths to use system tooling to determine location

* Sun Nov 26 2017 Michael Mansell
- Initial Build 
