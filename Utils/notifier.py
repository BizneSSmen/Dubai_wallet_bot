from aiohttp import ClientSession

from params import NOTIFY_LINK


class Notify:
    """
    Класс, используемый для отправки уведомления о созданной заявке
    """
    apiUrl: str = NOTIFY_LINK

    async def __call__(self, _id: str) -> None:
        """
        Метод отправки созданной заявки
        :param _id: идентификатор заявки
        :return: None
        """
        async with ClientSession() as client:
            await client.get(self.apiUrl.format(__ID__=_id))
