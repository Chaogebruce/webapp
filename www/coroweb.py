#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'Bruce Chen'

import asyncio, os, inspect, logging, functools
from urllib import parse
from aiohttp import web
from www.apis import APIError


def get(path):
    """
    Define decorator @get('/path')
    """

    def decorator(func):
        @functools.warps(func)
        def warpper(*args, **kw):
            return func(*args, **kw)

        warpper.__method__ = 'GET'
        warpper.__router__ = path
        return warpper

    return decorator


def post(path):
    """
    Define  decorator @post('/path')
    """

    def decorator(func):
        @functools.wraps(func)
        def warpper(*args, **kw):
            return func(*args, **kw)

        warpper.__method__ = 'POST'
        warpper.__router__ = path
        return warpper

    return decorator


def get_required_kw_args(fn):
    args = []
    params = inspect.signature(fn).parameters
    for name, param in params.items():
        if param.kind == inspect.Parameter.KEYWORD_ONLY and param.default == inspect.Parameter.empty:
            args.append(name)
    return tuple(args)


def get_named_kw_args(fn):
    args = []
    params = inspect.signature(fn).parameters
    for name, param in params.items():
        if param.kind == inspect.Parameter.KEYWORD_ONLY:
            args.append(name)
    return tuple(args)


def has_named_kw_args(fn):
    params = inspect.signature(fn).parameters
    for name, param in params.items():
        if param.kind == inspect.Parameter.KEYWORD_ONLY:
            return True


def has_var_kw_args(fn):
    params = inspect.signature(fn).parameters
    for name, param in params.items():
        if param.kind == inspect.Parameter.VAR_KEYWORD:
            return True


def has_request_args(fn):
    sig = inspect.signature(fn)
    params = sig.parameters
    found = False
    for name, param in params.items():
        if name == 'request':
            found = True
            continue
        if found and (
                    param.kind != inspect.Parameter.VAR_POSITIONAL and param.kind != inspect.Parameter.VAR_KEYWORD and param.kind != inspect.Parameter.KEYWORD_ONLY):
            raise ValueError(
                'request parameter must be  last named parameter in function: %s%s' % (fn.__name__, str(sig)))
    return found


class RequestHandler(object):
    def __init__(self, app, fn):
        self._app = app
        self._func = fn
        self._has_request_args = has_request_args(fn)
        self._has_var_kw_args = has_var_kw_args(fn)
        self._has_named_kw_args = has_named_kw_args(fn)
        self._named_kw_args = get_named_kw_args(fn)
        self._required_kw_args = get_required_kw_args(fn)

    @asyncio.coroutines
    def __call__(self, request):
        kw = None
        if self._has_var_kw_args or self._required_kw_args or self._has_named_kw_args:
            if request.method == 'POST':
                if not request.connect_type:
                    return w



