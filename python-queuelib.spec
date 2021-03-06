%global srcname queuelib
%global sum A collection of persistent (disk-based) queues

Name:           python-queuelib
Version:        1.4.2
Release:        4%{?dist}
Summary:        %{sum}

License:        BSD
URL:            https://github.com/scrapy/queuelib
Source0:        https://pypi.python.org/packages/source/q/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python2-devel
BuildRequires:  python2-nose
BuildRequires:  pytest

%description
Queuelib is a collection of persistent (disk-based) queues for
Python. Queuelib goals are speed and simplicity.

%package -n python2-%{srcname}
Summary:        %{sum}
%{?python_provide:%python_provide python2-%{srcname}}

%description -n python2-%{srcname}
Queuelib is a collection of persistent (disk-based) queues for
Python. Queuelib goals are speed and simplicity.

%prep
%autosetup -n %{srcname}-%{version}

%build
%py2_build

%install
%py2_install

%check
nosetests queuelib/tests

%files -n python2-%{srcname}
%doc NEWS README.rst
%license LICENSE
%{python2_sitelib}/%{srcname}/
%{python2_sitelib}/%{srcname}*.egg-info

%changelog
* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.4.2-4
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.2-3
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Nov 14 2015  Fabian Affolter <mail@fabian-affolter.ch> - 1.4.2-1
- Cleanup
- Upate to latest upstream release 1.4.2

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

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
