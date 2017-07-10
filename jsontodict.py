#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-06-16 11:28:31
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import os
import json

data1={'b':789,'c':456,'a':123}
encode_json=json.dumps(data1)#dict to json(str)
print type(encode_json),encode_json

decode_json=json.loads(encode_json)#json to dict
print type(decode_json)
print decode_json['a']
print decode_json
