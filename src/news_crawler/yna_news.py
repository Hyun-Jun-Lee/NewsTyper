import asyncio
from typing import Dict

from .base import BaseCrawler
from enums.enums import YnaCategory


class YnaCrawler(BaseCrawler):
    def get_article_links(self, category: YnaCategory) -> Dict[str:str]:
        target_url = f"{self.base_url}{category.value}"
        return

    def get_article_content(self, article_url):
        content = "마지막 자이언트 판다 가족인 메이샹과 톈톈, 그리고 아기판다 샤오치지가 중국으로 돌아가는 길을 배웅해주러 이른 아침부터 나온 '찐팬'들로 가득 메워졌다. 철문이 열리며 페덱스 트럭 행렬이 오자 팬들은 애인과 이별하는 듯 눈물바람 속에서 작별 인사를 했다. 실시간 캠 조회수가 1억뷰 이상을 기록했던 워싱턴의 판다 가족은 역대 어느 주미 대사보다도 유능한 중국 외교관이라는 말을 들을 정도로 인기를 모았었다. 경찰의 호위까지 받으며 덜레스 공항에 도착한 판다 가족은 '자이언트 판다 익스프레스' 전용기에 실려 중국 쓰촨성 청두로 향했다. 1972년 리처드 닉슨 대통령의 역사적 방중 이후 중국이 이 동물원에 판다 한 쌍을 선물한 것을 계기로 시작된 중국의 '판다 외교'가 반세기 만에 막을 내리게 됐다는 평가가 나왔다. 그러나 넉달여가 흐른 지금 분위기가 반전됐다. 팬들은 판다를 곧 다시 볼 수 있을 것이란 기대감에 흥분해있다."
        return content
