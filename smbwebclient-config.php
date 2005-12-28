<?php
class smbwebclient_config extends smbwebclient {

###################################################################
# CONFIGURATION SECTION - Change for your needs
###################################################################

###################################################################
# You can set this constant to see a single domain (or workgroup),
# a domain and a server, a domain/server/shared resource
# and (even) a path into a domain/server/shared.
# For example to see only folder Bilbo in 'Bolson' shared resource
# at 'HOBBIT' server in 'TIERRAMEDIA' domain would be:
# var $cfgSambaRoot = 'TIERRAMEDIA/HOBBIT/Bolson/Bilbo';
# Note: Do not put any slash at beginning/end.
# Tip: To share only their home directory in your SAMBA server to
#      users (auth req.) you must set cfgSambaRoot to
#      'DOMAIN/SERVER/homes'
#
#var $cfgSambaRoot = '';


###################################################################
# Anonymoys login is disallowed by default.
# If you have public shares in your network, turn on this flag
# i.e. var $cfgAnonymous = true;
#
#var $cfgAnonymous = false;


###################################################################
# Path at web server to store downloaded files. This script will
# check when it need to update the cached file. This path must be
# writable to the user that runs your web server.
# If you set this value to '' cache will be disabled.
# Note: this feature is a security risk.
#
#var $cfgCachePath = false;


###################################################################
# This script try to set language from web browser. If browser
# language is not supported you can set a default language.
#
#var $cfgDefaultLanguage = 'en';


###################################################################
# Default charset (as suggested by Norbert Malecki)
#
#var $cfgDefaultCharset = 'ISO-8859-1';


###################################################################
# Default browse server for your network. A browse server is where
# you run smbclient -L subcommand to read available domains and/or
# workgroups. Set to 'localhost' if you are running SAMBA server
# in your web server. Maybe you will need cfgDefaultUser and
# cfgDefaultPassword if no anonymous browsing is allowed.
#
#var $cfgDefaultServer = 'localhost';


###################################################################
# Path to smbclient program.
# i.e. var $cfgSmbClient = '/usr/bin/smbclient';
#
#var $cfgSmbClient = 'smbclient';


###################################################################
# Authentication method with smbclient
# 'SMB_AUTH_ENV' USER environment variable (more secure)
# 'SMB_AUTH_ARG' smbclient -U param
#
#var $cfgAuthMode = 'SMB_AUTH_ARG';


###################################################################
# If you have Apache mod_rewrite installed you can put this
# .htaccess file in same path of smbwebclient.php:
#
#  <IfModule mod_rewrite.c>
#   RewriteEngine on
#   RewriteCond    %{REQUEST_FILENAME}  -d
#   RewriteRule ^(.*/[^\./]*[^/])$ $1/
#   RewriteRule ^(.*)$ smbwebclient.php?path=$1 [QSA,L]
#  </IfModule>
#
# Then you will be able to access to use "pretty" URLs
# i.e: http://server/windows-network/DOMAIN/SERVER/SHARE/PATH
#
# To do this, all you have to set is cfgBaseUrl and set
# cfgModRewrite = true
# (i.e. http://server/windows-network/)
#
# Note - Change this if you want to use mod_rewrite
#var $cfgModRewrite = false;
#var $cfgBaseUrl = '';


###################################################################
# Do not show dot files (like .cshrc)
#
#var $cfgHideDotFiles = true;


###################################################################
# Do not show system shared resources (like admin$ or C$)
#
#var $cfgHideSystemShares = true;


###################################################################
# Do not show printer resources
#
#var $cfgHidePrinterShares = false;


###################################################################
# Log level
# -1 = no messages
#  0 = log actions performed
#  1 = smbclient calls
# >1 = smbclient output
#
#var $cfgLogLevel = 0;


###################################################################
# Log facility
#
#var $cfgFacility = LOG_DAEMON;


###################################################################
# User authentication (BasicAuth or FormAuth)
#
#var $cfgUserAuth = 'BasicAuth';


###################################################################
# Change PHP session name ('' to use default session name)
#
#var $cfgSessionName = 'SMBWebClientID';

###################################################################
# Virus scanner to upload files -- suggested by Bill R <wjries@hotmail.com>
# Only ClamAV is available in this revision, set to false to
# disable virus scanning.
#
#var $cfgAntivirus = 'ClamAV';

###################################################################
# Format to upload compressed folders: tar, tgz or zip
#
#var $cfgArchiver = 'tgz';

}
