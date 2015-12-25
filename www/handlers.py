#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Bruce Chen'

import re, time, json, logging, hashlib, base64, asyncio

from coroweb import get,  post

from models import User, Comment, Blog, next_id

@get('/')
def index(request):
    users = yield from User.findAll()
    return {
        '__templates__': 'test.html',
        'users' : users
    }