#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v3
# autospec commit: c1050fe
#
# Source0 file verified with key 0xD7574483BB57B18D (jr@jriddell.org)
#
Name     : kwayland-server
Version  : 5.24.5
Release  : 31
URL      : https://download.kde.org/stable/plasma/5.24.5/kwayland-server-5.24.5.tar.xz
Source0  : https://download.kde.org/stable/plasma/5.24.5/kwayland-server-5.24.5.tar.xz
Source1  : https://download.kde.org/stable/plasma/5.24.5/kwayland-server-5.24.5.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause LGPL-2.1 LGPL-3.0 MIT
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
BuildRequires : pkgconfig(wayland-protocols)
BuildRequires : plasma-wayland-protocols-dev
BuildRequires : qtbase-dev
BuildRequires : qtbase-dev mesa-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

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
%setup -q -n kwayland-server-5.24.5
cd %{_builddir}/kwayland-server-5.24.5

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1702009776
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
%cmake ..
make  %{?_smp_mflags}
popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1702009776
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kwayland-server
cp %{_builddir}/kwayland-server-%{version}/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/kwayland-server/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c || :
cp %{_builddir}/kwayland-server-%{version}/LICENSES/LGPL-2.1-only.txt %{buildroot}/usr/share/package-licenses/kwayland-server/3c3d7573e137d48253731c975ecf90d74cfa9efe || :
cp %{_builddir}/kwayland-server-%{version}/LICENSES/LGPL-2.1-or-later.txt %{buildroot}/usr/share/package-licenses/kwayland-server/6f1f675aa5f6a2bbaa573b8343044b166be28399 || :
cp %{_builddir}/kwayland-server-%{version}/LICENSES/LGPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/kwayland-server/757b86330df80f81143d5916b3e92b4bcb1b1890 || :
cp %{_builddir}/kwayland-server-%{version}/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/kwayland-server/e458941548e0864907e654fa2e192844ae90fc32 || :
cp %{_builddir}/kwayland-server-%{version}/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/kwayland-server/e458941548e0864907e654fa2e192844ae90fc32 || :
cp %{_builddir}/kwayland-server-%{version}/LICENSES/MIT.txt %{buildroot}/usr/share/package-licenses/kwayland-server/a0193e3fccf86c17dc71e3f6c0ac0b535e06bea3 || :
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
/usr/include/KWaylandServer/abstract_data_source.h
/usr/include/KWaylandServer/abstract_drop_handler.h
/usr/include/KWaylandServer/appmenu_interface.h
/usr/include/KWaylandServer/blur_interface.h
/usr/include/KWaylandServer/clientbuffer.h
/usr/include/KWaylandServer/clientbufferintegration.h
/usr/include/KWaylandServer/clientconnection.h
/usr/include/KWaylandServer/compositor_interface.h
/usr/include/KWaylandServer/contrast_interface.h
/usr/include/KWaylandServer/datacontroldevice_v1_interface.h
/usr/include/KWaylandServer/datacontroldevicemanager_v1_interface.h
/usr/include/KWaylandServer/datacontroloffer_v1_interface.h
/usr/include/KWaylandServer/datacontrolsource_v1_interface.h
/usr/include/KWaylandServer/datadevice_interface.h
/usr/include/KWaylandServer/datadevicemanager_interface.h
/usr/include/KWaylandServer/dataoffer_interface.h
/usr/include/KWaylandServer/datasource_interface.h
/usr/include/KWaylandServer/display.h
/usr/include/KWaylandServer/dpms_interface.h
/usr/include/KWaylandServer/drmclientbuffer.h
/usr/include/KWaylandServer/drmleasedevice_v1_interface.h
/usr/include/KWaylandServer/fakeinput_interface.h
/usr/include/KWaylandServer/filtered_display.h
/usr/include/KWaylandServer/idle_interface.h
/usr/include/KWaylandServer/idleinhibit_v1_interface.h
/usr/include/KWaylandServer/inputmethod_v1_interface.h
/usr/include/KWaylandServer/keyboard_interface.h
/usr/include/KWaylandServer/keyboard_shortcuts_inhibit_v1_interface.h
/usr/include/KWaylandServer/keystate_interface.h
/usr/include/KWaylandServer/kwaylandserver_export.h
/usr/include/KWaylandServer/layershell_v1_interface.h
/usr/include/KWaylandServer/linuxdmabufv1clientbuffer.h
/usr/include/KWaylandServer/output_interface.h
/usr/include/KWaylandServer/outputchangeset_v2.h
/usr/include/KWaylandServer/outputconfiguration_v2_interface.h
/usr/include/KWaylandServer/outputdevice_v2_interface.h
/usr/include/KWaylandServer/outputmanagement_v2_interface.h
/usr/include/KWaylandServer/plasmashell_interface.h
/usr/include/KWaylandServer/plasmavirtualdesktop_interface.h
/usr/include/KWaylandServer/plasmawindowmanagement_interface.h
/usr/include/KWaylandServer/pointer_interface.h
/usr/include/KWaylandServer/pointerconstraints_v1_interface.h
/usr/include/KWaylandServer/pointergestures_v1_interface.h
/usr/include/KWaylandServer/primaryoutput_v1_interface.h
/usr/include/KWaylandServer/primaryselectiondevice_v1_interface.h
/usr/include/KWaylandServer/primaryselectiondevicemanager_v1_interface.h
/usr/include/KWaylandServer/primaryselectionoffer_v1_interface.h
/usr/include/KWaylandServer/primaryselectionsource_v1_interface.h
/usr/include/KWaylandServer/relativepointer_v1_interface.h
/usr/include/KWaylandServer/screencast_v1_interface.h
/usr/include/KWaylandServer/seat_interface.h
/usr/include/KWaylandServer/server_decoration_interface.h
/usr/include/KWaylandServer/server_decoration_palette_interface.h
/usr/include/KWaylandServer/shadow_interface.h
/usr/include/KWaylandServer/shmclientbuffer.h
/usr/include/KWaylandServer/slide_interface.h
/usr/include/KWaylandServer/subcompositor_interface.h
/usr/include/KWaylandServer/surface_interface.h
/usr/include/KWaylandServer/tablet_v2_interface.h
/usr/include/KWaylandServer/textinput.h
/usr/include/KWaylandServer/textinput_v2_interface.h
/usr/include/KWaylandServer/textinput_v3_interface.h
/usr/include/KWaylandServer/touch_interface.h
/usr/include/KWaylandServer/utils.h
/usr/include/KWaylandServer/viewporter_interface.h
/usr/include/KWaylandServer/xdgactivation_v1_interface.h
/usr/include/KWaylandServer/xdgdecoration_v1_interface.h
/usr/include/KWaylandServer/xdgforeign_v2_interface.h
/usr/include/KWaylandServer/xdgoutput_v1_interface.h
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
/usr/lib64/libKWaylandServer.so.5.24.5

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kwayland-server/3c3d7573e137d48253731c975ecf90d74cfa9efe
/usr/share/package-licenses/kwayland-server/6f1f675aa5f6a2bbaa573b8343044b166be28399
/usr/share/package-licenses/kwayland-server/757b86330df80f81143d5916b3e92b4bcb1b1890
/usr/share/package-licenses/kwayland-server/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c
/usr/share/package-licenses/kwayland-server/a0193e3fccf86c17dc71e3f6c0ac0b535e06bea3
/usr/share/package-licenses/kwayland-server/e458941548e0864907e654fa2e192844ae90fc32
