#
# spec file for package 
#
# Copyright (c) 2013 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/

Name:           crandpass
Version:        6
Release:        1
License:        GPLv3
Summary:        A small, simple password manager.
Url:            http://code.google.com/p/crandpass
Group:          Productivity/Security
Source:         crandpass-%{version}.tar.gz
#Patch:          
#BuildRequires:
#PreReq:         coreutils
Requires:       coreutils,bash
Provides:       crandpass
BuildRoot:      %{_tmppath}/%{name}-build
BuildArch:      noarch


%description
A small, simple, UNIX compliant CLI password creator that is fast, flexible,
and needs no more than a base system.  This will be the only password creator
you will ever need!


%prep
%setup


%build


%install
rm -rf ${RPM_BUILD_ROOT}
mkdir -p ${RPM_BUILD_ROOT}/usr/bin
install  -m 755 src/crandpass ${RPM_BUILD_ROOT}/%{_bindir}

%clean

rm -rf ${RPM_BUILD_ROOT}

%files
%defattr(-,root,root)
%attr(755,root,root) %{_bindir}/crandpass

%changelog
* Fri Aug 02 2013 Faolan Baldwin <faolan.baldwin@gmail.com>
- Initial release for Fedora & SUSE!
