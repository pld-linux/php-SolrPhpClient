%define		pkgname	SolrPhpClient
%define		php_min_version 5.2.0
%include	/usr/lib/rpm/macros.php
Summary:	Apache Solr PHP Client
Name:		php-%{pkgname}
Version:	0.60
Release:	1
License:	New BSD License
Group:		Development/Languages/PHP
Source0:	https://solr-php-client.googlecode.com/files/SolrPhpClient.r60.2011-05-04.tgz
# Source0-md5:	ba91be2862215f3ab0c70aebdf918d13
URL:		https://code.google.com/p/solr-php-client/
BuildRequires:	/usr/bin/php
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.461
Requires:	php-common >= 4:%{php_min_version}
Requires:	php-json
Requires:	php-pcre
Requires:	php-spl
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdir			%{php_data_dir}/%{pkgname}
%define		_phpdocdir		%{_docdir}/phpdoc

%description
A PHP library for indexing and searching documents within an Apache
Solr installation.

%package phpdoc
Summary:	Online manual for SolrPhpClient
Summary(pl.UTF-8):	Dokumentacja online do SolrPhpClient
Group:		Documentation
Requires:	php-dirs

%description phpdoc
Documentation for SolrPhpClient.

%description phpdoc -l pl.UTF-8
Dokumentacja do SolrPhpClient.

%prep
%setup -qc -n %{pkgname}-%{version}
mv SolrPhpClient/* .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_data_dir}
cp -a Apache $RPM_BUILD_ROOT%{php_data_dir}

install -d $RPM_BUILD_ROOT%{_phpdocdir}/%{pkgname}
cp -a phpdocs/* $RPM_BUILD_ROOT%{_phpdocdir}/%{pkgname}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog
%dir %{php_data_dir}/Apache
%{php_data_dir}/Apache/Solr

%files phpdoc
%defattr(644,root,root,755)
%{_phpdocdir}/%{pkgname}
