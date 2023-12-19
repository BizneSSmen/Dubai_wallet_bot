import aiomysql
from aiomysql import Pool
from Entities import Rates


async def createPool(user: str, password: str, address: str, port: str, db: str, loop):
    return await aiomysql.create_pool(host=address,
                                      port=port,
                                      user=user,
                                      password=password,
                                      db=db,
                                      loop=loop,
                                      autocommit=True,
                                      cursorclass=aiomysql.DictCursor)


class Database:
    def __init__(self, pool: Pool):
        self.pool = pool

    async def insertСlaim(self, claim: dict) -> int:
        sql = """
        INSERT INTO claims (
            operation_type, description, tel, status, sum_A, sum_B, exchange_applied_rate, fee, currency_A,
            currency_B
        )
        VALUES (
            %(operationType)s, %(description)s, %(phoneNumber)s,
            %(status)s, %(targetAmount)s, %(finalAmount)s, %(exchangeAppliedRate)s,
            %(fee)s, %(currency_A)s,
            %(currency_B)s
        )
        """

        async with self.pool.acquire() as connection:
            async with connection.cursor() as cursor:
                try:
                    await cursor.execute(sql, claim)
                    await connection.commit()
                    return cursor.lastrowid  # Возвращает ID новой записи
                except Exception as e:
                    print(f"Error executing SQL query: {e}")

    async def updateClaimById(self, claim_id: int, updates: dict):
        queries: list[str] = [f"UPDATE claims SET {field} WHERE id = %s" for field in [f'{key} = %s' for key in updates.keys()]]
        values: list = list(updates.values())
        resultQueries = list(zip(queries, list(zip(values, [claim_id]*len(values)))))

        async with self.pool.acquire() as connection:
            async with connection.cursor() as cursor:
                for query in resultQueries:
                    try:
                        await cursor.execute(*query)
                        await connection.commit()
                    except Exception as e:
                        print(f"Error executing SQL query: {e}")

    async def getRates(self):
        query = f"SELECT * FROM rates"
        async with self.pool.acquire() as connection:
            async with connection.cursor() as cursor:
                try:
                    await cursor.execute(query)
                    result = await cursor.fetchall()
                    return Rates(**{f'{_["description"]}': _ for _ in result})
                except Exception as e:
                    print(f"Error executing SQL query: {e}")

