#!/usr/bin/python3
# -*- coding: utf-8 -*-
from pip.utils import logging

__author__ = 'yangyh'

import asyncio
@asyncio.coroutine

def create_pool(loop, **kw):
    logging.info('create database connection pool^')
