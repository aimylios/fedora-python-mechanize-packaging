%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

Name:           python-mechanize
Version:        0.2.5
Release:        9%{?dist}
Summary:        Stateful programmatic web browsing

Group:          System Environment/Libraries
License:        BSD or ZPLv2.1
URL:            http://wwwsearch.sourceforge.net/mechanize
Source0:        http://wwwsearch.sourceforge.net/mechanize/src/mechanize-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch

BuildRequires:  python-devel
# for tests
BuildRequires:  python-zope-interface python-twisted-web2
BuildRequires: python-setuptools


%description
Stateful programmatic web browsing, after Andy Lester's Perl module
WWW::Mechanize.

The library is layered: mechanize.Browser (stateful web browser),
mechanize.UserAgent (configurable URL opener), plus urllib2 handlers.

Features include: ftp:, http: and file: URL schemes, browser history,
high-level hyperlink and HTML form support, HTTP cookies, HTTP-EQUIV and
Refresh, Referer [sic] header, robots.txt, redirections, proxies, and
Basic and Digest HTTP authentication.  mechanize's response objects are
(lazily-) .seek()able and still work after .close().

Much of the code originally derived from Perl code by Gisle Aas
(libwww-perl), Johnny Lee (MSIE Cookie support) and last but not least
Andy Lester (WWW::Mechanize).  urllib2 was written by Jeremy Hylton.


%prep
%setup -q -n mechanize-%{version}
chmod -x examples/forms/{echo.cgi,example.py,simple.py}


%build
%{__python} setup.py build


%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install --single-version-externally-managed \
                             -O1 --root=$RPM_BUILD_ROOT


%clean
rm -rf $RPM_BUILD_ROOT

%check
# The TestPullParser unit tests are now failing
# https://github.com/jjlee/mechanize/issues/72
rm test/test_pullparser.py

chmod +x examples/forms/{echo.cgi,example.py,simple.py}
%{__python} test.py --log-server
chmod -x examples/forms/{echo.cgi,example.py,simple.py}

%files
%defattr(-,root,root,-)
%doc COPYING.txt README.txt docs/ examples/
%{python_sitelib}/*


%changelog
* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun 30 2014 Toshio Kuratomi <toshio@fedoraproject.org> - 0.2.5-8
- Replace the python-setuptools-devel BR with python-setuptools

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Aug 22 2012 Luke Macken <lmacken@redhat.com> - 0.2.5-4
- Remove a couple of unit tests that are failing. Issue filed upstream.

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Jun 16 2011 Luke Macken <lmacken@redhat.com> - 0.2.5-1
- Update to 0.2.5 (#692836)

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Jan  4 2011 Robin Lee <cheeselee@fedoraproject.org> - 0.2.4-1
- Update to 0.2.4
- Include a missed cgi script and add python-zope-interface and
  python-twisted-web2 to BR to run extra tests
- Remove executable bits from example scripts

* Thu Oct 21 2010 Luke Macken <lmacken@redhat.com> - 0.2.3-1
- Update to 0.2.3 (#3645064)

* Sat Sep 11 2010 Robin Lee <robinlee.sysu@gmail.com> - 0.2.2-1
- Update to 0.2.2
- License specified from 'BSD' to 'BSD or ZPLv2.1'
- Requires: python-clientform removed
- Add %%check section and run test suite

* Thu Jul 22 2010 David Malcolm <dmalcolm@redhat.com> - 0.1.10-4
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Dec 10 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 0.1.10-1
- Update to 0.1.10

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 0.1.6-0.3.b
- Rebuild for Python 2.6

* Sun Sep  2 2007 Luke Macken <lmacken@redhat.com> - 0.1.6-0.2.b
- Update for python-setuptools changes in rawhide

* Sat Mar  3 2007 Luke Macken <lmacken@redhat.com> - 0.1.6-0.1.b
- 0.1.6b

* Fri Nov 24 2006 Luke Macken <lmacken@redhat.com> - 0.1.5-0.1.b
- Rebuild for python 2.5
- 0.1.5b

* Sun Sep  3 2006 Luke Macken <lmacken@redhat.com> - 0.1.1a-5
- Rebuild for FC6

* Sun Jul  9 2006 Luke Macken <lmacken@redhat.com> - 0.1.1a-4
- Remove unnecessary python-abi requirement

* Wed May 17 2006 Luke Macken <lmacken@redhat.com> - 0.1.1a-3
- Add BuildArch: noarch (bug #192155)

* Sun May 14 2006 Luke Macken <lmacken@redhat.com> - 0.1.1a-2
- Add python-abi Requires
- Remove noarch

* Thu May 11 2006 Luke Macken <lmacken@redhat.com> - 0.1.1a-1
- Packaged for Fedora Extras
