#!/usr/bin/python3
# -*- coding: utf-8 -*-

import orm, asyncio
from models import User, Blog, Comment

async def test(loop):
    await orm.create_pool(user='www-data', password='www-data', db='blog', loop=loop)

    u = User(name='fhy', email='fanhengyuan1994@gmail.com', passwd='123456f', image='about:blank')

    await u.save()

loop = asyncio.get_event_loop()
loop.run_until_complete(test(loop))
loop.close()
if loop.is_closed():
    exit(0)
