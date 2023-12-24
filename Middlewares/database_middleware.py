from typing import Callable, Dict, Any, Awaitable

from aiogram import BaseMiddleware
from aiogram.types import Message, CallbackQuery
from aiomysql import Pool


class DataBaseMiddleWare(BaseMiddleware):
    def __init__(self, pool: Pool):
        self.pool = pool

    async def __call__(
            self,
            handler: Callable[[CallbackQuery, Dict[str, Any]], Awaitable[Any]],
            event: Message,
            data: Dict[str, Any]
    ) -> Any:
        """
        Метод проброса пула соединений в хэндлер
        """
        data["pool"] = self.pool
        await handler(event, data)
