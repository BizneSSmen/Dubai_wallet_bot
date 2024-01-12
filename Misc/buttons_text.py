from enum import Enum


class MainMenu(Enum):
    aedToRub: str = "🇦🇪 Обменять дирхамы"
    rubToAed: str = "🇷🇺 Обменять рубли"
    course: str = "📊 Текущий курс"
    faq: str = "Что можно?"


class BankList(Enum):
    bank1: str = "🟢 Сбербанк"
    bank2: str = "🟡 Тинькофф"
    bank3: str = "🔴 Альфа-банк"


class LocationList(Enum):
    location1: str = "📍Dubai Mall"
    location2: str = "📍Mall of Emirates"
    location3: str = "📍Dubai Marina Mall"
    location4: str = "📍Nakheel Mall"


class ServiceButtons(Enum):
    cancel: str = "❌ Отменить"
    sharePhoneNumber: str = "Поделиться номером телефона"
