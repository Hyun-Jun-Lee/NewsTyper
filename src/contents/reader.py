import pandas as pd

df = pd.read_csv("/datas/all_quotes.csv")


data = df[["quote", "author"]]


if __name__ == "__main__":
    print(data, data.shape)
