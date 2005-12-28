<?php

$SMBWEBCLIENT_CLASS = 'smbwebclient_config';
include '/usr/share/smbwebclient/smbwebclient.php';
include '/etc/webapps/smbwebclient/config.php';

$swc = new smbwebclient_config;
$swc->Run();
