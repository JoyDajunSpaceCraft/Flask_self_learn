#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : views.py.py
# @Author: Feng
# @Date  : 2019/10/2
# @Desc  :
from self_learn import app

@app.route('/')
def index():
    return 'Hello World!'