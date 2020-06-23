#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xEC94D18F7F05997E (jr@jriddell.org)
#
Name     : kwayland-server
Version  : 5.19.2
Release  : 4
URL      : https://download.kde.org/stable/plasma/5.19.2/kwayland-server-5.19.2.tar.xz
Source0  : https://download.kde.org/stable/plasma/5.19.2/kwayland-server-5.19.2.tar.xz
Source1  : https://download.kde.org/stable/plasma/5.19.2/kwayland-server-5.19.2.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : LGPL-2.1 LGPL-3.0
Requires: kwayland-server-data = %{version}-%{release}
Requires: kwayland-server-lib = %{version}-%{release}
Requires: kwayland-server-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules pkgconfig(egl)
BuildRequires : extra-cmake-modules pkgconfig(wayland-client)
BuildRequires : extra-cmake-modules qtwayland-dev
BuildRequires : extra-cmake-modules wayland
BuildRequires : extra-cmake-modules-data
BuildRequires : kwayland-dev
BuildRequires : pkg-config
BuildRequires : pkgconfig(wayland-protocols)
BuildRequires : plasma-wayland-protocols-dev
BuildRequires : qtbase-dev
BuildRequires : qtbase-dev mesa-dev
BuildRequires : weston-dev weston

%description
# KWayland
KWayland is a Qt-style API to interact with the wayland-client and wayland-server API.

%package data
Summary: data components for the kwayland-server package.
Group: Data

%description data
data components for the kwayland-server package.


%package dev
Summary: dev components for the kwayland-server package.
Group: Development
Requires: kwayland-server-lib = %{version}-%{release}
Requires: kwayland-server-data = %{version}-%{release}
Provides: kwayland-server-devel = %{version}-%{release}
Requires: kwayland-server = %{version}-%{release}

%description dev
dev components for the kwayland-server package.


%package lib
Summary: lib components for the kwayland-server package.
Group: Libraries
Requires: kwayland-server-data = %{version}-%{release}
Requires: kwayland-server-license = %{version}-%{release}

%description lib
lib components for the kwayland-server package.


%package license
Summary: license components for the kwayland-server package.
Group: Default

%description license
license components for the kwayland-server package.


%prep
%setup -q -n kwayland-server-5.19.2
cd %{_builddir}/kwayland-server-5.19.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1592948457
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1592948457
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kwayland-server
cp %{_builddir}/kwayland-server-5.19.2/COPYING.LIB %{buildroot}/usr/share/package-licenses/kwayland-server/9a1929f4700d2407c70b507b3b2aaf6226a9543c
cp %{_builddir}/kwayland-server-5.19.2/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/kwayland-server/e458941548e0864907e654fa2e192844ae90fc32
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/qlogging-categories5/kwaylandserver.categories

%files dev
%defattr(-,root,root,-)
/usr/include/KWaylandServer/appmenu_interface.h
/usr/include/KWaylandServer/blur_interface.h
/usr/include/KWaylandServer/buffer_interface.h
/usr/include/KWaylandServer/clientconnection.h
/usr/include/KWaylandServer/compositor_interface.h
/usr/include/KWaylandServer/contrast_interface.h
/usr/include/KWaylandServer/datadevice_interface.h
/usr/include/KWaylandServer/datadevicemanager_interface.h
/usr/include/KWaylandServer/dataoffer_interface.h
/usr/include/KWaylandServer/datasource_interface.h
/usr/include/KWaylandServer/display.h
/usr/include/KWaylandServer/dpms_interface.h
/usr/include/KWaylandServer/eglstream_controller_interface.h
/usr/include/KWaylandServer/fakeinput_interface.h
/usr/include/KWaylandServer/filtered_display.h
/usr/include/KWaylandServer/global.h
/usr/include/KWaylandServer/idle_interface.h
/usr/include/KWaylandServer/idleinhibit_interface.h
/usr/include/KWaylandServer/keyboard_interface.h
/usr/include/KWaylandServer/keystate_interface.h
/usr/include/KWaylandServer/kwaylandserver_export.h
/usr/include/KWaylandServer/linuxdmabuf_v1_interface.h
/usr/include/KWaylandServer/output_interface.h
/usr/include/KWaylandServer/outputchangeset.h
/usr/include/KWaylandServer/outputconfiguration_interface.h
/usr/include/KWaylandServer/outputdevice_interface.h
/usr/include/KWaylandServer/outputmanagement_interface.h
/usr/include/KWaylandServer/plasmashell_interface.h
/usr/include/KWaylandServer/plasmavirtualdesktop_interface.h
/usr/include/KWaylandServer/plasmawindowmanagement_interface.h
/usr/include/KWaylandServer/pointer_interface.h
/usr/include/KWaylandServer/pointerconstraints_interface.h
/usr/include/KWaylandServer/pointergestures_interface.h
/usr/include/KWaylandServer/qtsurfaceextension_interface.h
/usr/include/KWaylandServer/region_interface.h
/usr/include/KWaylandServer/relativepointer_interface.h
/usr/include/KWaylandServer/remote_access_interface.h
/usr/include/KWaylandServer/resource.h
/usr/include/KWaylandServer/seat_interface.h
/usr/include/KWaylandServer/server_decoration_interface.h
/usr/include/KWaylandServer/server_decoration_palette_interface.h
/usr/include/KWaylandServer/shadow_interface.h
/usr/include/KWaylandServer/shell_interface.h
/usr/include/KWaylandServer/slide_interface.h
/usr/include/KWaylandServer/subcompositor_interface.h
/usr/include/KWaylandServer/surface_interface.h
/usr/include/KWaylandServer/tablet_interface.h
/usr/include/KWaylandServer/textinput_interface.h
/usr/include/KWaylandServer/touch_interface.h
/usr/include/KWaylandServer/xdgdecoration_interface.h
/usr/include/KWaylandServer/xdgforeign_interface.h
/usr/include/KWaylandServer/xdgoutput_interface.h
/usr/include/KWaylandServer/xdgshell_interface.h
/usr/include/kwaylandserver_version.h
/usr/lib64/cmake/KWaylandServer/KWaylandServerConfig.cmake
/usr/lib64/cmake/KWaylandServer/KWaylandServerConfigVersion.cmake
/usr/lib64/cmake/KWaylandServer/KWaylandServerTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KWaylandServer/KWaylandServerTargets.cmake
/usr/lib64/libKWaylandServer.so

%files lib
%defattr(-,root,root,-)
/usr/lib64/libKWaylandServer.so.5
/usr/lib64/libKWaylandServer.so.5.19.2

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kwayland-server/9a1929f4700d2407c70b507b3b2aaf6226a9543c
/usr/share/package-licenses/kwayland-server/e458941548e0864907e654fa2e192844ae90fc32
