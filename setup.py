#!/usr/share/python2
# -*- coding: utf-8 -*-
#
# wpa_config - a config manager for wpa_supplicant
#
# Author: slowpoke <mail+git@slowpoke.io>
#
# This program is Free Software under the non-terms
# of the Anti-License. Do whatever the fuck you want.
#
# Github: https://github.com/proxypoke/wpa_config

from distutils.core import setup

setup(
    name='wpa_config',
    version='0.1',
    description='a simple config manager for wpa_supplicant',
    author='slowpoke',
    author_email='mail+pypi@slowpoke.io',
    url='https://github.com/proxypoke/wpa_config',
    download_url='https://github.com/proxypoke/wpa_config/archive/0.1.tar.gz',
    scripts=[
        'wpa_config',
    ],
    data_files=[
        ('/etc/wpa_config', [
            'files/wpa_supplicant.conf.head',
            'files/wpa_supplicant.conf.tail',
        ]),
        ('/etc/wpa_config/networks.d', []),
        ('/usr/share/doc/wpa_config', ['README.txt']),
        ('/usr/share/man/man8', ['man/wpa_config.8.bz2']),
    ],
    classifiers=[
        'Environment :: Console',
        'Development Status :: 4 - Beta',
        'Intended Audience :: System Administrators',
        'License :: Public Domain',
        'Operating System :: Unix',
        'Programming Language :: Python :: 2.7',
        'Topic :: System :: Networking',
        'Topic :: System :: Systems Administration',
        'Topic :: Utilities',
    ]
)
