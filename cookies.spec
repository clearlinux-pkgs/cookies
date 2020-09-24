#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : cookies
Version  : 2.2.1
Release  : 8
URL      : https://files.pythonhosted.org/packages/f3/95/b66a0ca09c5ec9509d8729e0510e4b078d2451c5e33f47bd6fc33c01517c/cookies-2.2.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/f3/95/b66a0ca09c5ec9509d8729e0510e4b078d2451c5e33f47bd6fc33c01517c/cookies-2.2.1.tar.gz
Summary  : Friendlier RFC 6265-compliant cookie parser/renderer
Group    : Development/Tools
License  : MIT
Requires: cookies-python = %{version}-%{release}
Requires: cookies-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
What is this and what is it for?
--------------------------------
cookies.py is a Python module for working with HTTP cookies: parsing and
rendering 'Cookie:' request headers and 'Set-Cookie:' response headers,
and exposing a convenient API for creating and modifying cookies. It can be
used as a replacement of Python's Cookie.py (aka http.cookies).

%package python
Summary: python components for the cookies package.
Group: Default
Requires: cookies-python3 = %{version}-%{release}

%description python
python components for the cookies package.


%package python3
Summary: python3 components for the cookies package.
Group: Default
Requires: python3-core
Provides: pypi(cookies)

%description python3
python3 components for the cookies package.


%prep
%setup -q -n cookies-2.2.1
cd %{_builddir}/cookies-2.2.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1582913466
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
