from enum import Enum


class NewsAgency(Enum):
    NAVER = "NAVER"
    GOOGLE = "GOOGLE"
    HANGYUNG = "HANGYUNG"


class NewsCategory(Enum):
    SPORTS = "SPORTS"
    ECONOMY = "ECONOMY"
    INTERNATIONAL = "INTERNATIONAL"
    SOCIETY = "SOCIETY"
    OPINION = "OPINION"
    TECH = "TECH"
