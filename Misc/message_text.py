from dataclasses import dataclass


@dataclass
class Service:
    start: str =\
'''
Ваш кассир по обмену валюты в Дубае 🌴🕌🎡

Что можно:

🇦🇪 Получить наличные в дирхамах, а отдать переводом в рублях на карту.

💳 Отдать наличные в дирхамах, а получить в рублях на карту.

✅ Список доступных банков: Сбербанк, Тинькофф, Альфабанк.

📍 Курс сегодня: 
AED ➡️ RUB:  {__AED_TO_RUB__}
RUB ➡️ AED:  {__RUB_TO_AED__}
'''
    cancelled: str = "Отменено"
    course: str = \
'''
📍 Курс сегодня: 

AED ➡️ RUB:  {__AED_TO_RUB__}
RUB ➡️ AED:  {__RUB_TO_AED__}
'''
    faq: str = \
'''
Что можно:

🇦🇪 Получить наличные в дирхамах, а отдать переводом в рублях на карту.

💳 Отдать наличные в дирхамах, а получить в рублях на карту.

✅ Список доступных банков: Сбербанк, Тинькофф, Альфабанк.
'''


@dataclass
class AedToRub:
    changeKbMessage: str = "🇦🇪AED ➡️ 🇷🇺RUB"
    enterAmount: str = "Введите сумму в дирхамах, которую хотите обменять:"
    amountError: str = "Минимальная сумма обмена - 2000 AED. Попробуйте ещё раз"
    chooseBank: str = \
'''
Сумма обмена: {__TARGET_AMOUNT__} AED (наличные)
Текущий курс: {__COURSE__}
Сумма, которую получите: {__FINAL_AMOUNT__} RUB (на карту российского банка)

Выберите банк на который вы планируете получить перевод в рублях во время встречи:
'''
    chooseLocation: str = \
'''
Сумма обмена: {__TARGET_AMOUNT__} AED (наличные)
Текущий курс: {__COURSE__}
Сумма, которую получите: {__FINAL_AMOUNT__} RUB (на карту российского банка)
Банк: {__BANK__}

Выберите локацию, где хотели бы провести встречу:
'''
    phoneNumber: str = \
'''
Сумма обмена: {__TARGET_AMOUNT__} AED (наличные)
Текущий курс: {__COURSE__}
Сумма, которую получите: {__FINAL_AMOUNT__} RUB (на карту российского банка)
Банк: {__BANK__}
Локация обмена: {__LOCATION__}

Введите номер телефона для связи:
'''
    phoneNumberError: str = "Некорректный номер телефона. Повторите попытку"
    description : srt = \
'''
Сумма обмена: {__TARGET_AMOUNT__} AED (наличные)
Текущий курс: {__COURSE__}
Сумма, которую получите: {__FINAL_AMOUNT__} RUB (на карту российского банка)
Банк: {__BANK__}
Локация обмена: {__LOCATION__}
Номер телефона для связи: {__PHONE__}
'''
    result: str = \
'''
✅ <b>Подтвердите данные заявки</b>:
Номер заявки: {__CLAIM_ID__}

Сумма обмена: {__TARGET_AMOUNT__} AED (наличные)
Текущий курс: {__COURSE__}
Сумма, которую получите: {__FINAL_AMOUNT__} RUB (на карту российского банка)
Банк: {__BANK__}
Локация обмена: {__LOCATION__}
Номер телефона для связи: {__PHONE__}
'''
    instruction: str = \
'''
❗️Ожидайте звонка, с вами свяжется оператор и вы договоритесь о времени и месте встречи. 

🔸 Затем на встрече кассир переведёт на вашу российскую карту сумму в рублях, и примет у Вас наличные в дирхамах.
'''


@dataclass
class RubToAed:
    changeKbMessage: str = "🇷🇺RUB ➡️ 🇦🇪AED"
    enterAmount: str = "Введите сумму в рублях, которую хотите обменять:"
    amountError: str = "Минимальная сумма обмена 50 000 RUB. Попробуйте ещё раз"
    chooseBank: str = \
'''
Сумма обмена: {__TARGET_AMOUNT__} RUB (наличные)
Текущий курс: {__COURSE__}
Сумма, которую получите наличными: {__FINAL_AMOUNT__} AED

Выберите банк, с которого вы планируете совершить перевод в рублях во время встречи:
'''
    chooseLocation: str = \
'''
Сумма обмена: {__TARGET_AMOUNT__} RUB
Текущий курс: {__COURSE__}
Сумма, которую получите: {__FINAL_AMOUNT__} AED
Банк: {__BANK__}

Выберите локацию, где хотели бы провести встречу:
'''
    phoneNumber: str = \
'''
Сумма обмена: {__TARGET_AMOUNT__} RUB
Текущий курс: {__COURSE__}
Сумма, которую получите: {__FINAL_AMOUNT__} AED
Банк: {__BANK__}
Локация обмена: {__LOCATION__}

Введите номер телефона для связи:
'''
    phoneNumberError: str = "Некорректный номер телефона. Повторите попытку"
    description: str = \
'''
Сумма обмена: {__TARGET_AMOUNT__} RUB
Текущий курс: {__COURSE__}
Сумма, которую получите: {__FINAL_AMOUNT__} AED
Банк: {__BANK__}
Локация обмена: {__LOCATION__}
Номер телефона для связи: {__PHONE__}
'''
    result: str = \
'''
✅ <b>Подтвердите данные заявки</b>:
Номер заявки: {__CLAIM_ID__}

Сумма обмена: {__TARGET_AMOUNT__} RUB
Текущий курс: {__COURSE__}
Сумма, которую получите: {__FINAL_AMOUNT__} AED
Банк: {__BANK__}
Локация обмена: {__LOCATION__}
Номер телефона для связи: {__PHONE__}
'''
    instruction: str = \
'''
❗️Ожидайте звонка, с вами свяжется оператор и вы договоритесь о времени и месте встречи. 

🔸 Затем на встрече кассир выдаст Вам наличную сумму в Дирхамах, и примет у Вас перевод с карты в Рублях.
'''
