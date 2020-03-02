#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : kombu
Version  : 4.6.8
Release  : 53
URL      : https://files.pythonhosted.org/packages/88/2d/abda45e54473821baa33bb7b06defb316e12aca9cb5cc874d8daa75f07f1/kombu-4.6.8.tar.gz
Source0  : https://files.pythonhosted.org/packages/88/2d/abda45e54473821baa33bb7b06defb316e12aca9cb5cc874d8daa75f07f1/kombu-4.6.8.tar.gz
Summary  : Messaging library for Python.
Group    : Development/Tools
License  : BSD-3-Clause
Requires: kombu-license = %{version}-%{release}
Requires: kombu-python = %{version}-%{release}
Requires: kombu-python3 = %{version}-%{release}
Requires: PyYAML
Requires: Pyro4
Requires: SQLAlchemy
Requires: amqp
Requires: azure-servicebus
Requires: boto3
Requires: kazoo
Requires: pycurl
Requires: pymongo
Requires: redis
BuildRequires : PyYAML
BuildRequires : Pyro4
BuildRequires : SQLAlchemy
BuildRequires : amqp
BuildRequires : anyjson
BuildRequires : azure-servicebus
BuildRequires : boto3
BuildRequires : buildreq-distutils3
BuildRequires : kazoo
BuildRequires : linecache2
BuildRequires : nose
BuildRequires : pycurl
BuildRequires : pymongo
BuildRequires : python-mock
BuildRequires : redis
BuildRequires : six
BuildRequires : traceback2
BuildRequires : unittest2

%description
========================================
kombu - Messaging library for Python
========================================

%package license
Summary: license components for the kombu package.
Group: Default

%description license
license components for the kombu package.


%package python
Summary: python components for the kombu package.
Group: Default
Requires: kombu-python3 = %{version}-%{release}

%description python
python components for the kombu package.


%package python3
Summary: python3 components for the kombu package.
Group: Default
Requires: python3-core
Provides: pypi(kombu)

%description python3
python3 components for the kombu package.


%prep
%setup -q -n kombu-4.6.8
cd %{_builddir}/kombu-4.6.8

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1583165415
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kombu
cp %{_builddir}/kombu-4.6.8/LICENSE %{buildroot}/usr/share/package-licenses/kombu/d30a04a42f238f8d091587963dc3f48f862925bc
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kombu/d30a04a42f238f8d091587963dc3f48f862925bc

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
