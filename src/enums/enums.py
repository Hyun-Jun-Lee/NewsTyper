from enum import Enum


class NewsAgency(Enum):
    YNA = "YNA"
    HANKYUNG = "HANKYUNG"


class HankyungsCategory(Enum):
    ECONOMY = "economy"
    FINANCE = "finance"
    REALESTATE = "realestate"
    INDUSTRY = "industry"
    SOCIETY = "society"
    INTERNATIONAL = "internaional"
    IT = "it"
    LIFE = "life"
    OPINION_01 = "opinion/0001"
    OPINION_02 = "opinion/0002"


class YnaCategory(Enum):
    ECONOMY = "economy/all"
    INDUSTRY = "industry/all"
    SOCIETY = "society/all"
    INTERNATIONAL = "internaional/all"
    CULTURE = "culture/all"
    OPINION_01 = "opinion/advisory"
    OPINION_02 = "opinion/editorials"
