import orm
from models import User,Blog,Comment
import asyncio

loop = asyncio.get_event_loop()


async def test():
	await orm.create_pool(loop=loop,user='www-data',password='www-data',database='awesome')

	u = User(name='test',email='test@example.com',passwd='123456',image='about:blak')

	await u.save()

loop.run_until_complete(test())