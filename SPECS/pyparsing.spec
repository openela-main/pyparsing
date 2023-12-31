%global srcname pyparsing
%global sum Python package with an object-oriented approach to text processing

%global build_wheel 1

%global python3_wheelname %{srcname}-%{version}-py2.py3-none-any.whl

Summary:        %{sum}
Name:           pyparsing
Version:        2.1.10
Release:        7%{?dist}

License:        MIT
URL:            http://pyparsing.wikispaces.com/
Source0:        http://downloads.sourceforge.net/pyparsing/pyparsing-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  dos2unix
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%if 0%{?build_wheel}
BuildRequires:  python%{python3_pkgversion}-pip
BuildRequires:  python%{python3_pkgversion}-wheel
%endif

%description
pyparsing is a module that can be used to easily and directly configure syntax
definitions for any number of text parsing applications.


%package        doc
Summary:        Documentation for pyparsing python package

%description    doc
The package contains documentation for pyparsing.


%package -n python3-pyparsing
Summary:        %{sum}
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-pyparsing
pyparsing is a module that can be used to easily and directly configure syntax
definitions for any number of text parsing applications.

This is the Python 3 version.


%prep
%setup -q
mv docs/pyparsingClassDiagram.PNG docs/pyparsingClassDiagram.png
rm docs/pyparsingClassDiagram.JPG
dos2unix -k CHANGES LICENSE README

%build
%if 0%{?build_wheel}
%py3_build_wheel
%else
%py3_build
%endif

%install
%if 0%{?build_wheel}
%py3_install_wheel %{python3_wheelname}
%else
%py3_install
%endif


%files -n python3-pyparsing
%license LICENSE
%doc CHANGES README LICENSE
%{python3_sitelib}/pyparsing.py
%{python3_sitelib}/__pycache__/*
%{python3_sitelib}/pyparsing-*dist-info/

%files doc
%license LICENSE
%doc CHANGES README HowToUsePyparsing.html docs examples htmldoc

%changelog
* Tue May 29 2018 Petr Viktorin <pviktori@redhat.com> - 2.1.10-7
- Remove Python 2 subpackage
  https://bugzilla.redhat.com/show_bug.cgi?id=1567403

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.10-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 24 2018 Miro Hrončok <mhroncok@redhat.com> - 2.1.10-5
- Remove the empty pyparsing package, provide and obsolete it from python2-pyparsing

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Feb 13 2017 Charalampos Stratakis <cstratak@redhat.com> - 2.1.10-3
- Rebuild as wheel

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Dec 30 2016 José Matos <jamatos@fedoraproject.org> - 2.1.10-1
- update to 2.1.10
- do not own __pycache__

* Fri Dec 09 2016 Charalampos Stratakis <cstratak@redhat.com> - 2.1.5-3
- Rebuild for Python 3.6
- Add missing BuildRequires for python-setuptools

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.5-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Jun 16 2016 José Abílio Matos <jamatos@fc.up.pt> - 2.1.5-1
- update to 2.1.5

* Thu May 12 2016 José Matos <jamatos@fedoraproject.org> - 2.1.3-1
- update to 2.1.3

* Sun May  8 2016 José Matos <jamatos@fedoraproject.org> - 2.1.1-1
- update to 2.1.1

* Tue Feb 16 2016 José Matos <jamatos@fedoraproject.org> - 2.1.0-2
- fix typo in provides for the python3 subpackage

* Mon Feb 15 2016 José Matos <jamatos@fedoraproject.org> - 2.1.0-1
- update to 2.1.0
- add a python2 subpackage preserving the upgrade path

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan 08 2016 Terje Rosten <terje.rosten@ntnu.no> - 2.0.7-1
- 2.0.7

* Tue Nov 17 2015 Terje Rosten <terje.rosten@ntnu.no> - 2.0.6-1
- 2.0.6
- Some clean up

* Wed Sep 23 2015 Robert Kuska <rkuska@redhat.com> - 2.0.3-3
- Rebuilt for Python3.5 rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Nov 28 2014 José Matos <jamatos@fedoraproject.org> - 2.0.3-1
- update to 2.0.3
- include the whole documentation set

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 14 2014 Bohuslav Kabrda <bkabrda@redhat.com> - 2.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Sun Oct 27 2013 Terje Rosten <terje.rosten@ntnu.no> - 2.0.1-1
- 2.0.1

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Apr  3 2013 Thomas Spura <tomspur@fedoraproject.org> - 1.5.6-8
- add patch to correct typo in exception handling

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Aug 03 2012 David Malcolm <dmalcolm@redhat.com> - 1.5.6-6
- rebuild for https://fedoraproject.org/wiki/Features/Python_3.3

* Fri Aug  3 2012 David Malcolm <dmalcolm@redhat.com> - 1.5.6-5
- remove rhel logic from with_python3 conditional

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec  6 2011 David Malcolm <dmalcolm@redhat.com> - 1.5.6-2
- fix __pycache__ conditional on RHEL

* Fri Jul  1 2011 José Matos <jamatos@fedoraproject.org> - 1.5.6-1
- New upstream version.

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Oct 21 2010 Terje Rosten <terje.rosten@ntnu.no> - 1.5.5-1
- 1.5.5
- use buildroot macro
- fix wrong file end of line encoding
- convert files to utf-8
- doc subpackage
- python3 subpackage
- rpmlint clean

* Wed Jul 21 2010 David Malcolm <dmalcolm@redhat.com> - 1.5.0-7
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Fri Jul 16 2010 Dan Horák <dan[at]danny.cz> - 1.5.0-6
- include egginfo on EL >= 6

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 1.5.0-3
- Rebuild for Python 2.6

* Mon Aug  4 2008 José Matos <jamatos[AT]fc.up.pt> - 1.5.0-2
- respun (now with the right sources)

* Mon Aug  4 2008 José Matos <jamatos[AT]fc.up.pt> - 1.5.0-1
- new upstream release.

* Tue Apr  1 2008 José Matos <jamatos[AT]fc.up.pt> - 1.4.11-1
- New upstream version, add egg-info for F9+.

* Wed Aug 29 2007 José Matos <jamatos[AT]fc.up.pt> - 1.4.7-1
- New upstream version.

* Sat Apr 21 2007 José Matos <jamatos[AT]fc.up.pt> - 1.4.6-1
- New upstream version.

* Mon Dec 11 2006 José Matos <jamatos[AT]fc.up.pt> - 1.4.4-1
- New upstream version.

* Mon Sep 11 2006 José Matos <jamatos[AT]fc.up.pt> - 1.4.3-1
- New version.

* Wed Aug  3 2005 Ignacio Vazquez-Abrams <ivazquez@ivazquez.net> 1.3-1
- Initial RPM release
