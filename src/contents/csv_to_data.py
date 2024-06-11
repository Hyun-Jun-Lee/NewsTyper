from pathlib import Path
import pandas as pd

data_folder = Path(__file__).parent / "datas"
all_quotes_file_path = data_folder / "all_quotes.csv"
anime_quote_file_path = data_folder / "AnimeQuotes.csv"
movie_quote_file_path = data_folder / "movie_quotes.csv"


def get_data():
    all_quotes_df = pd.read_csv(all_quotes_file_path, usecols=["Quote", "Author"])

    anime_quote_df = pd.read_csv(
        anime_quote_file_path, usecols=["Quote", "Character", "Anime"]
    )
    anime_quote_df["Author"] = anime_quote_df.apply(
        lambda row: f"{row['Character']} ({row['Anime']})", axis=1
    )
    anime_quote_data = anime_quote_df[["Quote", "Author"]]

    movie_quote_df = pd.read_csv(
        movie_quote_file_path, usecols=["quote", "movie", "year"]
    )
    movie_quote_df["Author"] = movie_quote_df.apply(
        lambda row: f"{row['movie']} ({row['year']})", axis=1
    )
    movie_quote_df = movie_quote_df.rename(columns={"quote": "Quote"})
    movie_quote_data = movie_quote_df[["Quote", "Author"]]

    # DataFrame 병합
    combined_data = pd.concat(
        [all_quotes_df, anime_quote_data, movie_quote_data], ignore_index=True
    ).rename(columns={"Quote": "en_content", "Author": "author"})
    combined_data["kr_content"] = None
    combined_data["is_custom"] = False
    return combined_data
