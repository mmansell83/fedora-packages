%global gittag master
Name:           gimp-divide-scanned-images
Version:        201610
Release:        1%{?dist}
Summary:        GIMP script for splitting separate sub-image fomr a composite image.

License:        GPL v2+
URL:            https://github.com/FrancoisMalan/DivideScannedImages
Source0:        %{url}/archive/%{gittag}/DivideScannedImages-%{gittag}.tar.gz

Requires:       gimp >= 2.0.0

BuildArch:      noarch

%description
DivideScannedImages.scm
by Francois Malan
Based on a script originally by Rob Antonishen http://ffaat.pointclark.net

Locates each separate element in an image and creates a new image from each.
If option is selected, will call the deskew plugin by Karl Chen https://github.com/prokoudine/gimp-deskew-plugin (if it is installed) on each item.

%prep
%autosetup -n DivideScannedImages-%{gittag}

%build


%install
mkdir -p %{buildroot}/%{_datarootdir}/gimp/2.0/scripts

install -m 0755 DivideScannedImages.scm %{buildroot}/%{_datarootdir}/gimp/2.0/scripts


%files
%{_datarootdir}/gimp/2.0/scripts/DivideScannedImages.scm


%changelog
* Sun Nov 26 2017 Michael Mansell
- Initial Build 
