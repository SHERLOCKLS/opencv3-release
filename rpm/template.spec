Name:           ros-jade-opencv3
Version:        3.0.0
Release:        0%{?dist}
Summary:        ROS opencv3 package

Group:          Development/Libraries
License:        BSD
URL:            http://opencvg.org
Source0:        %{name}-%{version}.tar.gz

Requires:       ffmpeg-devel
Requires:       jasper-devel
Requires:       libjpeg-turbo-devel
Requires:       libpng-devel
Requires:       numpy
Requires:       python
Requires:       python-devel
Requires:       qt-x11
Requires:       ros-jade-catkin
Requires:       vtk-devel
Requires:       zlib-devel
BuildRequires:  cmake
BuildRequires:  ffmpeg-devel
BuildRequires:  jasper-devel
BuildRequires:  libjpeg-turbo-devel
BuildRequires:  libpng-devel
BuildRequires:  libtiff
BuildRequires:  libv4l-devel
BuildRequires:  numpy
BuildRequires:  python
BuildRequires:  python-devel
BuildRequires:  qt-devel
BuildRequires:  qt-x11
BuildRequires:  vtk-devel
BuildRequires:  zlib-devel

%description
OpenCV 3.0

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/jade" \
        -DCMAKE_PREFIX_PATH="/opt/ros/jade" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/jade

%changelog
* Sat Sep 26 2015 Vincent Rabaud <vincent.rabaud@gmail.com> - 3.0.0-0
- Autogenerated by Bloom

