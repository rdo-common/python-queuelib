%global with_python3 1
%global srcname queuelib

Name:           python-queuelib
Version:        1.2.2
Release:        1%{?dist}
Summary:        A collection of persistent (disk-based) queues

License:        BSD
URL:            https://github.com/scrapy/queuelib
Source0:        https://pypi.python.org/packages/source/q/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python2-devel
BuildRequires:  python-setuptools
BuildRequires:  python-nose

%description
Queuelib is a collection of persistent (disk-based) queues for
Python. Queuelib goals are speed and simplicity.

%if 0%{?with_python3}
%package -n python3-%{srcname}
Summary:        A collection of persistent (disk-based) queues
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-nose

%description -n python3-%{srcname}
Queuelib is a collection of persistent (disk-based) queues for
Python. Queuelib goals are speed and simplicity.
%endif # if with_python3

%prep
%setup -q -n %{srcname}-%{version}
%if 0%{?with_python3}
rm -rf %{py3dir}
cp -a . %{py3dir}
%endif # if with_python3

%build
%{__python2} setup.py build
%if 0%{?with_python3}
# Python 3
pushd %{py3dir}
%{__python3} setup.py build
popd
%endif # if with_python3

%install
%{__python2} setup.py install -O1 --skip-build --root %{buildroot}
%if 0%{?with_python3}
# Python 3
pushd %{py3dir}
%{__python3} setup.py install -O1 --skip-build --root %{buildroot}
popd
%endif # if with_python3

%check
nosetests queuelib/tests
%if 0%{?with_python3}
# Python 3
pushd %{py3dir}
nosetests queuelib/tests
popd
%endif # if with_python3

%files
%doc LICENSE NEWS README.rst
%{python_sitelib}/%{srcname}/
%{python_sitelib}/%{srcname}*.egg-info

%if 0%{?with_python3}
# Python 3
%files -n python3-%{srcname}
%doc LICENSE NEWS README.rst
%{python3_sitelib}/%{srcname}/
%{python3_sitelib}/%{srcname}*.egg-info
%endif # with_python3

%changelog
* Tue Mar 24 2015 Fabian Affolter <mail@fabian-affolter.ch> - 1.2.2-1
- Update to latest upstream release 1.2.2

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 28 2014 Kalev Lember <kalevlember@gmail.com> - 1.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Sat Jan 04 2014 Fabian Affolter <mail@fabian-affolter.ch> - 1.1.1-1
- Update to latest upstream release 1.1.1

* Mon Oct 07 2013 Fabian Affolter <mail@fabian-affolter.ch> - 1.0-3
- Naming of Py3 package updated

* Mon Sep 09 2013 Fabian Affolter <mail@fabian-affolter.ch> - 1.0-2
- Python macro updated

* Wed Sep 04 2013 Fabian Affolter <mail@fabian-affolter.ch> - 1.0-1
- Initial spec file for Fedora
