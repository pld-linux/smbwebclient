Summary:	SmbWebClient - script to use Windows Networks from a web browser
Summary(pl):	SmbWebClient - skrypt do u¿ywania sieci Windows z przegl±darki
Name:		smbwebclient
Version:	2.9
Release:	1.3
License:	GPL
Group:		Applications/WWW
Source0:	http://dl.sourceforge.net/smbwebclient/%{name}-%{version}.php.gz
# Source0-md5:	9c4a18d2bc477989a85d55f8ba55bc50
Source1:	%{name}.conf
URL:		http://smbwebclient.sourceforge.net/
BuildRequires:	rpmbuild(macros) >= 1.226
Requires:	php
Requires:	samba-client
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_phpdir		%{_datadir}/%{name}

%description
SmbWebClient is a simple script written by Victor M. Varela to use
Windows Networks from a web browser.

%description -l pl
SmbWebClient jest prostym skryptem napisanym przez Victora M. Varela w
celu korzystania z sieci Windows z poziomu przegl±darki internetowej.

%prep
gunzip -dc %{SOURCE0} > %{name}.php

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_phpdir},%{_sysconfdir}/httpd}
install %{name}.php $RPM_BUILD_ROOT%{_phpdir}/smbwebclient.php
install %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/apache-%{name}.conf

%clean
rm -rf $RPM_BUILD_ROOT

%triggerin -- apache1 >= 1.3.33-2
%apache_config_install -v 1 -c %{_sysconfdir}/apache-%{name}.conf

%triggerun -- apache1 >= 1.3.33-2
%apache_config_uninstall -v 1

%triggerin -- apache >= 2.0.0
%apache_config_install -v 2 -c %{_sysconfdir}/apache-%{name}.conf

%triggerun -- apache >= 2.0.0
%apache_config_uninstall -v 2

%files
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/apache-%{name}.conf
%{_phpdir}
