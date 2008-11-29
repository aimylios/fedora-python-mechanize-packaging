%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

%define _ver 0.1.6b

Name:           python-mechanize
Version:        0.1.6
Release:        0.3.b%{?dist}
Summary:        Stateful programmatic web browsing

Group:          System Environment/Libraries
License:        BSD
URL:            http://wwwsearch.sourceforge.net/mechanize
Source0:        http://wwwsearch.sourceforge.net/mechanize/src/mechanize-%{_ver}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch

BuildRequires:  python-devel
%if 0%{?fedora} >= 8
BuildRequires: python-setuptools-devel
%else
BuildRequires: python-setuptools
%endif
Requires:       python-clientform


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
%setup -q -n mechanize-%{_ver}


%build
%{__python} setup.py build


%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install --single-version-externally-managed \
                             -O1 --root=$RPM_BUILD_ROOT


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc COPYING.txt README.txt README.html GeneralFAQ.html doc.html examples
%{python_sitelib}/*


%changelog
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
