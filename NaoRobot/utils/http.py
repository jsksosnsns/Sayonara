from asyncio import gather
import aiohttp

async def get(url: str, *args, **kwargs):
    async with aiohttp.aiohttpsession.get(url, *args, **kwargs) as resp:
        try:
            data = await resp.json()
        except Exception:
            data = await resp.text()
    return data


async def head(url: str, *args, **kwargs):
    async with aiohttp.aiohttpsession.head(url, *args, **kwargs) as resp:
        try:
            data = await resp.json()
        except Exception:
            data = await resp.text()
    return data


async def post(url: str, *args, **kwargs):
    async with aiohttp.aiohttpsession.post(url, *args, **kwargs) as resp:
        try:
            data = await resp.json()
        except Exception:
            data = await resp.text()
    return data


async def multiget(url: str, times: int, *args, **kwargs):
    return await gather(
        *[get(url, *args, **kwargs) for _ in range(times)]
    )


async def multihead(url: str, times: int, *args, **kwargs):
    return await gather(
        *[head(url, *args, **kwargs) for _ in range(times)]
    )


async def multipost(url: str, times: int, *args, **kwargs):
    return await gather(
        *[post(url, *args, **kwargs) for _ in range(times)]
    )


async def resp_get(url: str, *args, **kwargs):
    return await aiohttp.aiohttpsession.get(url, *args, **kwargs)


async def resp_post(url: str, *args, **kwargs):
    return await aiohttp.aiohttpsession.post(url, *args, **kwargs)
