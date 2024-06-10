import pandas as pd
from sqlalchemy.sql.expression import func
from sqlalchemy.exc import SQLAlchemyError
from tenacity import retry, stop_after_attempt, wait_fixed


from db.session import get_db, engine
from contents.models import Quote
from contents.csv_to_data import get_data


class DataManager:

    def is_empty(self):
        """
        데이터베이스가 비어있는지 확인합니다.
        """
        with get_db() as db:
            return db.query(Quote).count() == 0

    def load_quotes(self):
        """
        준비된 Quotes들을 데이터베이스에 저장합니다.
        """
        try:
            data = get_data()
            data.to_sql("quote", con=engine, if_exists="replace", index=False)
        except FileNotFoundError as e:
            print(f"파일을 찾을 수 없습니다: {e}")
            return False
        except SQLAlchemyError as e:
            print(f"데이터베이스 오류: {e}")
            return False
        except Exception as e:
            print(f"예상치 못한 오류 발생: {e}")
            return False
        return True

    @retry(stop=stop_after_attempt(3), wait=wait_fixed(1))
    def get_random_quote(self):
        """
        데이터베이스에서 무작위 명언을 가져옵니다.
        """
        with get_db() as db:
            quote = db.query(Quote).order_by(func.random()).first()
            if quote is not None:
                return quote
            else:
                return None
