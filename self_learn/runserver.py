#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : runserver.py.py
# @Author: Feng
# @Date  : 2019/10/1
# @Desc  :
import os
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash

from self_learn import app
app.run(debug=True)
