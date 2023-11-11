from aiohttp import ClientSession

from params import NOTYFY_LINK


class Notify:
    apiUrl: str = NOTYFY_LINK

    async def __call__(self, _id: str):
        async with ClientSession() as client:
            await client.get(self.apiUrl.format(__ID__=_id))
