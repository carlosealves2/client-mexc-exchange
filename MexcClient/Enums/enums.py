from enum import Enum


class EnumKlineInterval(Enum):
    ONE_MIN = "1m"
    FIVE_MIN = "5m"
    FIFTEEN_MIN = "15m"
    TIRTY_MIN = "30m"
    SIXTY_MIN = "60m"
    FOUR_HOUR = "4h"
    ONE_DAY = "1d"
    ONE_MONTH = "1M"


class EnumOrderSide(Enum):
    BUY = "BUY"
    SELL = "SELL"


class EnumOrderType(Enum):
    LIMIT = "LIMIT"
    MARKET = "MARKET"
    LIMIT_MARKET = "LIMIT_MARKET"
    IMMEDIATE_OR_CANCEL = "IMMEDIATE_OR_CANCEL"
    FILL_OR_KILL = "FILL_OR_KILL"
