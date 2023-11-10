from lxml import etree
from aiohttp import ClientSession
from bs4 import BeautifulSoup


class GetCourse:
    def __init__(self, url: str, xPath):
        self.url = url
        self.xPath: str = xPath
        self.courses: float = 0

    async def __call__(self, *args, **kwargs) -> float:
        async with ClientSession() as client:
            return round(float(etree.HTML(str(BeautifulSoup(await self.fetch(client), "html.parser"))).xpath(self.xPath)[0].text), 2)

    async def fetch(self, client: ClientSession):
        async with client.get(self.url) as response:
            return await response.text()
