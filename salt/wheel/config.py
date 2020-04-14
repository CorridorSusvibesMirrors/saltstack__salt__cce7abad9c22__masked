# -*- coding: utf-8 -*-
'''
Manage the master configuration file
'''
from __future__ import absolute_import, print_function, unicode_literals

# Import python libs
import logging
import os

# Import salt libs
import salt.config
import salt.utils.files
import salt.utils.yaml

# Import 3rd-party libs
from salt.ext import six

log = logging.getLogger(__name__)


def values():
    '''
    Return the raw values of the config file
    '''
    data = salt.config.master_config(__opts__['conf_file'])
    return data


def apply(key, value):
    '''
    Set a single key

    .. note::

        This will strip comments from your config file
    '''
    path = __opts__['conf_file']
    if os.path.isdir(path):
        path = os.path.join(path, 'master')
    data = values()
    data[key] = value
    with salt.utils.files.fopen(path, 'w+') as fp_:
        salt.utils.yaml.safe_dump(data, default_flow_style=False)



