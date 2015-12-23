__author__ = 'Bruce Chen'

import asyncio
import sys

import www.orm as orm
from www.models import User


def test(loop):
    yield from orm.create_pool(loop=loop,user='www-data', password='www-data', database='awesome')

    u = User(name='chen', email='chen@example.com', passwd='1234567890', image='about:blank')

    yield from u.save()


loop = asyncio.get_event_loop()
loop.run_until_complete(test(loop))
loop.close()
if loop.is_closed():
    sys.exit(0)