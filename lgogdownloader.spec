Name:           lgogdownloader
Version:        3.3
Release:        1%{?dist}
Summary:        Unofficial GOG.com downloader.

License:        WTFPL
URL:            https://github.com/Sude-/lgogdownloader
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake >= 3.0.0, help2man, grep, binutils, pkg-config
BuildRequires:  rhash-devel
BuildRequires:  pkgconfig(libcrypto), pkgconfig(htmlcxx), pkgconfig(jsoncpp), pkgconfig(oauth), pkgconfig(tinyxml2)
BuildRequires:  libcurl-devel >= 7.30.0, boost-devel
#BuildRequires:  libcurl-devel >= 7.32.0, liboauth-devel, rhash-devel, jsoncpp-devel, htmlcxx-devel, tinyxml2-devel, boost-devel, libssh-devel
Requires:       libcurl >= 7.32.0, liboauth, rhash, jsoncpp, htmlcxx, tinyxml2, boost, libssh

#BuildArch:      x86_64, i686

%description
LGOGDownloader is unofficial downloader to GOG.com for Linux users. It uses the same API as the official GOGDownloader. 

%global debug_package %{nil}
%prep
%autosetup


%build
cmake  -DCMAKE_INSTALL_PREFIX=%{_prefix} \
       -DCMAKE_BUILD_TYPE=Release
%make_build
#%{__make} 


%install
%{__make} DESTDIR=%{buildroot} install

%files
%defattr(-,root,root,-)
%license COPYING
%attr(755,root,root) %{_bindir}/%{name}
%{_mandir}/man1/%{name}*



%changelog
* Sun Nov 26 2017 Michael Mansell <michael.mansell@gmail.com>
- First lgogdownloader package
