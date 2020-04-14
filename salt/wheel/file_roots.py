# -*- coding: utf-8 -*-
'''
Read in files from the file_root and save files to the file root
'''

# Import python libs
from __future__ import absolute_import, print_function, unicode_literals
import os

# Import salt libs
import salt.utils.files
import salt.utils.path

# Import 3rd-party libs
from salt.ext import six





def list_env(saltenv='base'):
    '''
    Return all of the file paths found in an environment
    '''
    ret = {}
    if saltenv not in __opts__['file_roots']:
        return ret
    for f_root in __opts__['file_roots'][saltenv]:
        ret[f_root] = {}
        for root, dirs, files in salt.utils.path.os_walk(f_root):
            sub = ret[f_root]
            if root != f_root:
                # grab subroot ref
                sroot = root
                above = []
                # Populate the above dict
                while not os.path.samefile(sroot, f_root):
                    base = os.path.basename(sroot)
                    if base:
                        above.insert(0, base)
                    sroot = os.path.dirname(sroot)
                for aroot in above:
                    sub = sub[aroot]
            for dir_ in dirs:
                sub[dir_] = {}
            for fn_ in files:
                sub[fn_] = 'f'
    return ret


def list_roots():
    '''
    Return all of the files names in all available environments
    '''
    ret = {}
    for saltenv in __opts__['file_roots']:
        ret[saltenv] = []
        ret[saltenv].append(list_env(saltenv))
    return ret






