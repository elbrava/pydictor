#!/usr/bin/env python
# coding:utf-8
#
"""
Copyright (c) 2016-2019 LandGrey (https://github.com/LandGrey/pydictor)
License: GNU GENERAL PUBLIC LICENSE Version 3
"""

from __future__ import unicode_literals

from collections import OrderedDict
from lib.fun.fun import cool
from lib.data.data import pystrs

pydictor_art_text = \
    '''                              _ _      _
              _ __  _   _  __| (_) ___| |_ ___  _ __
             | '_ \| | | |/ _` | |/ __| __/ _ \| '__|
             | |_) | |_| | (_| | | (__| || (_) | |
             | .__/ \__, |\__,_|_|\___|\__\___/|_|
             |_|    |___/                            {0}
'''.format(cool.orange(pystrs.version))

helpmsg = \
    '''                   {0}
                                            {1}
    ----------------------------[ {2} ]---------------------------
    [+]help desc             [+]exit/quit            [+]clear/cls
    [+]show option           [+]set option arguments [+]rm option
    [+]len minlen maxlen     [+]head prefix          [+]tail suffix
    [+]encode type           [+]occur L d s          [+]types L d s
    [+]repeat L d s          [+]regex string         [+]level code
    [+]leet code             [+]output directory     [+]run

    ----------------------------[ {3} ]----------------------------
    [+]{4}                 [+]{5}                [+]{6}
    [+]{7}                 [+]{8}              [+]{9}
    [+]{10}                [+]{11}               [+]{12}
    [+]{13}              [+]{14}             [+]{15}
    [+]{16}                [+]{17}            [+]{18}
'''.format(cool.orange("Social Engineering Dictionary Builder"), cool.green("Build by LandGrey"), cool.yellow("command")
           , cool.yellow("option"), pystrs.sedb_range[0], pystrs.sedb_range[1], pystrs.sedb_range[2],
           pystrs.sedb_range[3], pystrs.sedb_range[4], pystrs.sedb_range[5], pystrs.sedb_range[6],
           pystrs.sedb_range[7], pystrs.sedb_range[8], pystrs.sedb_range[9], pystrs.sedb_range[10],
           pystrs.sedb_range[11], pystrs.sedb_range[12], pystrs.sedb_range[13], pystrs.sedb_range[14], )

help_dict = OrderedDict([
    # settings help message
    (pystrs.sedb_range[0], " {:10}     Chinese name's phonetic        ?????????????????????".format(pystrs.sedb_range[0])),
    (pystrs.sedb_range[1], " {:10}     English name                   ?????????".format(pystrs.sedb_range[1])),
    (pystrs.sedb_range[2], " {:10}     Simple name spellings          ????????????".format(pystrs.sedb_range[2])),
    (pystrs.sedb_range[3], " {:10}     Birthday [yyyyMMdd]            ??????".format(pystrs.sedb_range[3])),
    (pystrs.sedb_range[4], " {:10}     Used password                  ????????????".format(pystrs.sedb_range[4])),
    (pystrs.sedb_range[5], " {:10}     Cell phone number              ?????????".format(pystrs.sedb_range[5])),
    (pystrs.sedb_range[6], " {:10}     Previous phone number          ???????????????".format(pystrs.sedb_range[6])),
    (pystrs.sedb_range[7], " {:10}     HomePhone number               ???????????????".format(pystrs.sedb_range[7])),
    (pystrs.sedb_range[8], " {:10}     Email accounts                 ??????????????????".format(pystrs.sedb_range[8])),
    (pystrs.sedb_range[9], " {:10}     Postal code                    ??????????????????".format(pystrs.sedb_range[9])),
    (pystrs.sedb_range[10], " {:10}     Commonly used nickname         ????????????".format(pystrs.sedb_range[10])),
    (pystrs.sedb_range[11], " {:10}     Identity card number           ????????????".format(pystrs.sedb_range[11])),
    (pystrs.sedb_range[12], " {:10}     Job or student number          ??????????????????????????????".format(pystrs.sedb_range[12])),
    (pystrs.sedb_range[13], " {:10}     Others date [yyyyMMdd]         ?????????????????????????????????".format(pystrs.sedb_range[13])),
    (pystrs.sedb_range[14], " {:10}     Commonly used characters       ???????????????????????????????????????".format(pystrs.sedb_range[14]))
])
