from environs import Env
from dataclasses import dataclass


@dataclass
class DataBase:
    login: str
    password: str
    address: str
    port: int
    dbName: str


@dataclass
class TgBot:
    userToken: str


@dataclass
class Config:
    tgBot: TgBot
    dataBase: DataBase


def loadConfig(path: str) -> Config:
    env: Env = Env()
    env.read_env(path)

    return Config(
        tgBot=TgBot(
            userToken=env("BOT_TOKEN")
        ),
        dataBase=DataBase(
            login=env("DB_LOGIN"),
            password=env("DB_PASSWORD"),
            address=env("DB_ADDRESS"),
            port=int(env("DP_PORT")),
            dbName=env("DB_NAME")
        )
    )