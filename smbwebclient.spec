Summary:	SmbWebClient - script to use Windows Networks from a web browser
Summary(pl):	SmbWebClient - skrypt do używania sieci Windows z przeglądarki
Name:		smbwebclient
Version:	2.0.10
Release:	1
License:	GPL
Group:		Applications/System
Source0:	%{name}-%{version}.tgz
# Source0-md5:	e7fabb3784f1f1f45be3ca515d19a8a9
URL:		http://www.nivel0.net/SmbWebClient/
Requires:	php
Requires:	samba-client
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define         _phpdir     /home/services/httpd/html

%description
SmbWebClient is a simple script written by Victor M. Varela to use
Windows Networks from a web browser.

%description -l pl
SmbWebClient jest prostym skryptem napisanym przez Victora M. Varela w
celu korzystania z sieci Windows z poziomu przeglądarki internetowej.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_phpdir}

install smbwebclient.php $RPM_BUILD_ROOT%{_phpdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_phpdir}/smbwebclient.php
