import asyncio


# python3.5以前，使用该方法
# @asyncio.coroutine
# def hello():
# 	print("Hello world!")
#     # 异步调用asyncio.sleep(1):
# 	r = yield from asyncio.sleep(1)
# 	print("Hello again!")

# # 获取EventLoop:
# loop = asyncio.get_event_loop()
# # 执行coroutine
# loop.run_until_complete(hello())
# loop.close()
# 

#不能使用和模块一样的名字，否则会出现错误

async def hello():
	print('hello world')
	r=await asyncio.sleep(1)
	print('hello again')

loop=asyncio.get_event_loop()
loop.run_until_complete(hello())
loop.close()