Summary:	SmbWebClient - script to use Windows Networks from a web browser
Summary(pl.UTF-8):	SmbWebClient - skrypt do używania sieci Windows z przeglądarki
Name:		smbwebclient
Version:	2.9
Release:	3
License:	GPL
Group:		Applications/WWW
Source0:	http://dl.sourceforge.net/smbwebclient/%{name}-%{version}.php.gz
# Source0-md5:	9c4a18d2bc477989a85d55f8ba55bc50
Source1:	%{name}.conf
Source2:	%{name}-config.php
Source3:	%{name}-wrapper.php
URL:		http://smbwebclient.sourceforge.net/
BuildRequires:	rpmbuild(macros) >= 1.268
Requires:	samba-client
Requires:	webapps
Requires:	webserver(php) >= 4.1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_webapps	/etc/webapps
%define		_webapp		%{name}
%define		_sysconfdir	%{_webapps}/%{_webapp}
%define		_appdir		%{_datadir}/%{_webapp}

%description
SmbWebClient is a simple script written by Victor M. Varela to use
Windows Networks from a web browser.

%description -l pl.UTF-8
SmbWebClient jest prostym skryptem napisanym przez Victora M. Varela w
celu korzystania z sieci Windows z poziomu przeglądarki internetowej.

%prep
gunzip -dc %{SOURCE0} > %{name}.php

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_appdir},%{_sysconfdir}/httpd}
install %{name}.php $RPM_BUILD_ROOT%{_appdir}/smbwebclient.php
install %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/apache.conf
install %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/httpd.conf
install %{SOURCE2} $RPM_BUILD_ROOT%{_sysconfdir}/config.php
install %{SOURCE3} $RPM_BUILD_ROOT%{_appdir}/index.php

%clean
rm -rf $RPM_BUILD_ROOT

%triggerin -- apache1 < 1.3.37-3, apache1-base
%webapp_register apache %{_webapp}

%triggerun -- apache1 < 1.3.37-3, apache1-base
%webapp_unregister apache %{_webapp}

%triggerin -- apache < 2.2.0, apache-base
%webapp_register httpd %{_webapp}

%triggerun -- apache < 2.2.0, apache-base
%webapp_unregister httpd %{_webapp}

%triggerpostun -- %{name} < 2.9-1.5
if [ -f /etc/apache-%{name}.conf.rpmsave ]; then
	if [ -d /etc/apache/webapps.d ]; then
		cp -f %{_sysconfdir}/apache.conf{,.rpmnew}
		cp -f /etc/apache-%{name}.conf.rpmsave %{_sysconfdir}/apache.conf
	fi

	if [ -d /etc/httpd/webapps.d ]; then
		cp -f %{_sysconfdir}/httpd.conf{,.rpmnew}
		cp -f /etc/apache-%{name}.conf.rpmsave %{_sysconfdir}/httpd.conf
	fi
	rm -f /etc/apache-%{name}.conf.rpmsave
fi

if [ -L /etc/apache/conf.d/99_%{name}.conf ]; then
	rm -f /etc/apache/conf.d/99_%{name}.conf
	/usr/sbin/webapp register apache %{_webapp}
	%service -q apache reload
fi
if [ -L /etc/httpd/httpd.conf/99_%{name}.conf ]; then
	rm -f /etc/httpd/httpd.conf/99_%{name}.conf
	/usr/sbin/webapp register httpd %{_webapp}
	%service -q httpd reload
fi

%files
%defattr(644,root,root,755)
%dir %attr(750,root,http) %{_sysconfdir}
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/apache.conf
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/httpd.conf
%attr(640,root,http) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/*.php
%{_appdir}
