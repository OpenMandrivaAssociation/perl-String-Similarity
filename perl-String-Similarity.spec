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
