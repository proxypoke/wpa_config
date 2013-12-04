WPA_CONFIG(1)
=============

NAME
----
wpa_config - a small config manager for wpa_supplicant

DESCRIPTION
-----------
wpa_config makes configuration of wpa_supplicant - the only sane way to use 
WLAN networks - a lot simpler. One of the only drawbacks of using bare 
wpa_supplicant when compared to unwieldy bloatware like NetworkManager, is the 
fact that mucking around in a single, large config file for all networks can
be quite cumbersome.

With wpa_config, every network is its own file in a folder, as are the options 
for the wpa_supplicant. It simply merges all these files into a single file, 
which then becomes your wpa_supplicant.conf. It also provides utility functions 
for quickly generating new entries.

wpa_config does not manage the operation of wpa_supplicant. It's a config 
manager, not a network manager. It might add a facility to restart 
wpa_supplicant using your init system in the future.

FILES
-----
wpa_config uses three primary config files and a directory for network 
configurations. All of these are located in the CONFIG_ROOT directory, which by 
default is /etc/wpa_config.

wpa_config.conf
~~~~~~~~~~~~~~~
The configuration file for wpa_config itself. There are no settings so far, but 
there might be some in the future (for example, choice of init system to 
restart wpa_supplicant).

wpa_supplicant.conf.head
~~~~~~~~~~~~~~~~~~~~~~~~
This file contains settings for wpa_supplicant, for example the ctrl_interface 
or the eapol_version.

wpa_supplicant.conf.tail
~~~~~~~~~~~~~~~~~~~~~~~~
This file is appended to the generated config. It's a great way to migrate your 
currently configured networko, no need to reconfigure them.

networks.d/
~~~~~~~~~~~
This directory contains the configurations for the single networks. Every file 
in it should be in the form "$\{SSID\}.conf".

COMMANDS
--------
wpa_config has severeal subcommands which do all the work.

add
~~~
Create a new file in the network directory. Currently, this only works for WPA 
secured networks. Specifying more options (open networks, WEP, ad-hoc, etc) 
will be added later.

del
~~~
Delete a network in the network directory, if it exists.

list
~~~~
List all networks configured through wpa_config. Note that this does not list 
networks configured in wpa_supplicant.conf.tail.

show
~~~~
Print the configuration of a network.

make
~~~~
Merge all config and network files into wpa_supplicant.conf, writing it to 
WPA_SUPPLICANT_CONFIG (usually /etc/wpa_supplicant/wpa_supplicant.conf).

SEE ALSO
--------
* wpa_supplicant(8)
* wpa_supplicant.conf(8)
