#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : kombu
Version  : 3.0.35
Release  : 23
URL      : https://pypi.python.org/packages/source/k/kombu/kombu-3.0.35.tar.gz
Source0  : https://pypi.python.org/packages/source/k/kombu/kombu-3.0.35.tar.gz
Summary  : Messaging library for Python
Group    : Development/Tools
License  : BSD-3-Clause
Requires: kombu-python
BuildRequires : amqp
BuildRequires : anyjson
BuildRequires : funcsigs-python
BuildRequires : linecache2
BuildRequires : nose
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python-mock
BuildRequires : python3-dev
BuildRequires : setuptools
BuildRequires : six
BuildRequires : traceback2
BuildRequires : unittest2

%description
.. _kombu-index:
========================================
kombu - Messaging library for Python
========================================

%package python
Summary: python components for the kombu package.
Group: Default

%description python
python components for the kombu package.


%prep
%setup -q -n kombu-3.0.35

%build
python2 setup.py build -b py2
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}/usr/lib/python2.7/site-packages python2 setup.py test || :
%install
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
