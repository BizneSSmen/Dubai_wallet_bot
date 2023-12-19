from _decimal import Decimal
from pydantic import BaseModel, Field


class Official(BaseModel):
    value: float | None = Field(serialization_alias='value', default=None)
    sumRangeFrom: float | None = Field(alias='sum_range_from', default=None)
    sumRangeTo: float | None = Field(alias='sum_range_to', default=None)


class Sell(BaseModel):
    value: float | None = Field(serialization_alias='value', default=0)
    sumRangeFrom: float | None = Field(alias='sum_range_from', default=None)
    sumRangeTo: float | None = Field(alias='sum_range_to', default=None)


class Buy(BaseModel):
    value: float | None = Field(serialization_alias='value', default=0)
    sumRangeFrom: float | None = Field(alias='sum_range_from', default=None)
    sumRangeTo: float | None = Field(alias='sum_range_to', default=None)


class SellBig(BaseModel):
    value: float = Field(serialization_alias='value', default=0)
    sumRangeFrom: float | None = Field(alias='sum_range_from', default=None)
    sumRangeTo: float | None = Field(alias='sum_range_to', default=None)


class BuyBig(BaseModel):
    value: float | None = Field(serialization_alias='value', default=0)
    sumRangeFrom: float | None = Field(alias='sum_range_from', default=None)
    sumRangeTo: float | None = Field(alias='sum_range_to', default=None)


class Rates(BaseModel):
    official: Official = Field(default=Official())
    sell: Sell = Field(default=Sell())
    buy: Buy = Field(default=Buy())
    sellBig: SellBig = Field(default=SellBig(), alias='sellbig')
    buyBig: BuyBig = Field(default=BuyBig(), alias='buybig')



a = {'buy': {'description': 'buy',
         'sum_range_from': Decimal('2000.00'),
         'sum_range_to': Decimal('19999.99'),
         'value': Decimal('24.01')},
 'buybig': {'description': 'buybig',
            'sum_range_from': Decimal('20000.00'),
            'sum_range_to': None,
            'value': Decimal('24.50')},
 'official': {'description': 'official',
              'sum_range_from': None,
              'sum_range_to': None,
              'value': Decimal('24.73')},
 'sell': {'description': 'sell',
          'sum_range_from': Decimal('50000.00'),
          'sum_range_to': Decimal('499999.99'),
          'value': Decimal('26.00')},
 'sellbig': {'description': 'sellbig',
             'sum_range_from': Decimal('500000.00'),
             'sum_range_to': None,
             'value': Decimal('25.00')}}

b = Rates(**a)
print(b)
