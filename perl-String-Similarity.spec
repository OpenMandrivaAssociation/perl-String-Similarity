%define upstream_name    String-Similarity
%define upstream_version 1.04

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:	3

Summary:    Perl extension for calculating the similarity of two strings
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/String/%{upstream_name}-%{upstream_version}.tar.bz2

Buildrequires:  perl-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}

%description
$factor = similarity $string1, $string2, [$limit] 

The similarity-function calculates the similarity index of its two arguments. A
value of 0 means that the strings are entirely different. A value of 1 means
that the strings are identical. Everything else lies between 0 and 1 and
describes the amount of similarity between the strings.

It roughly works by looking at the smallest number of edits to change one
string into the other.

You can add an optional argument $limit (default 0) that gives the minimum
similarity the two strings must satisfy. similarity stops analyzing the string
as soon as the result drops below the given limit, in which case the result
will be invalid but lower than the given $limit. You can use this to speed up
the common case of searching for the most similar string from a set by
specifing the maximum similarity found so far.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%{__make} test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc COPYING Changes README
%{perl_vendorarch}/auto/String
%{perl_vendorarch}/String
%{_mandir}/*/*


%changelog
* Wed Jan 25 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 1.40.0-3
+ Revision: 768358
- svn commit -m mass rebuild of perl extension against perl 5.14.2

* Tue Jul 20 2010 Jérôme Quelin <jquelin@mandriva.org> 1.40.0-2mdv2011.0
+ Revision: 556149
- rebuild for perl 5.12

* Wed Jul 29 2009 Jérôme Quelin <jquelin@mandriva.org> 1.40.0-1mdv2010.0
+ Revision: 404420
- rebuild using %%perl_convert_version

* Mon Jul 06 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.04-1mdv2010.0
+ Revision: 393001
- update to new version 1.04

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 1.03-5mdv2009.0
+ Revision: 258392
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 1.03-4mdv2009.0
+ Revision: 246477
- rebuild

* Tue Jan 15 2008 Thierry Vignaud <tv@mandriva.org> 1.03-2mdv2008.1
+ Revision: 152310
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Sun Jul 01 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.03-1mdv2008.0
+ Revision: 46534
- update to new version 1.03


* Tue Jul 11 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.02-2mdv2007.0
- %%mkrel

* Mon Jun 27 2005 Guillaume Rousse <guillomovitch@mandriva.org> 1.02-1mdk
- New release 1.02

* Tue Jun 07 2005 Guillaume Rousse <guillomovitch@mandriva.org> 1.01-2mdk 
- drop useless empty directories
- make test in %%check

* Mon Apr 25 2005 Guillaume Rousse <guillomovitch@mandriva.org> 1.01-1mdk
- new release
- spec cleanup
- better url

* Mon Nov 15 2004 Michael Scherer <misc@mandrake.org> 1-3mdk
- Rebuild for new perl

* Wed Aug 04 2004 Guillaume Rousse <guillomovitch@mandrake.org> 1-2mdk 
- rebuild

* Wed Apr 21 2004 Guillaume Rousse <guillomovitch@mandrake.org> 1-1mdk
- new version
- rpmbuildupdate aware
- make test

* Wed Feb 25 2004 Guillaume Rousse <guillomovitch@mandrake.org> 0.02-2mdk
- fixed dir ownership (distlint)

* Wed Dec 17 2003 Guillaume Rousse <guillomovitch@mandrake.org> 0.02-1mdk
- first mdk release

