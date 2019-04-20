#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : kombu
Version  : 4.2.2.post1
Release  : 42
URL      : https://files.pythonhosted.org/packages/ca/03/560c2e0089d41459898d9ac573d897e01dc9f24e8e3fa2c7a03cd0dd39bc/kombu-4.2.2.post1.tar.gz
Source0  : https://files.pythonhosted.org/packages/ca/03/560c2e0089d41459898d9ac573d897e01dc9f24e8e3fa2c7a03cd0dd39bc/kombu-4.2.2.post1.tar.gz
Summary  : Messaging library for Python.
Group    : Development/Tools
License  : BSD-3-Clause
Requires: kombu-license = %{version}-%{release}
Requires: kombu-python = %{version}-%{release}
Requires: kombu-python3 = %{version}-%{release}
Requires: PyYAML
Requires: SQLAlchemy
Requires: amqp
Requires: boto3
Requires: kazoo
Requires: pycurl
Requires: pymongo
Requires: qpid-tools
Requires: redis
BuildRequires : amqp
BuildRequires : anyjson
BuildRequires : buildreq-distutils3
BuildRequires : linecache2
BuildRequires : nose
BuildRequires : python-mock
BuildRequires : six
BuildRequires : traceback2
BuildRequires : unittest2

%description
kombu - Messaging library for Python
        ========================================
        
        |build-status| |coverage| |license| |wheel| |pyversion| |pyimp|

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

%description python3
python3 components for the kombu package.


%prep
%setup -q -n kombu-4.2.2.post1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1547711481
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kombu
cp LICENSE %{buildroot}/usr/share/package-licenses/kombu/LICENSE
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kombu/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
