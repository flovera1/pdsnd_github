import pandas as pd

# Funtion load_data!
def load_data(file_path):
    try:
        df = pd.read_csv(file_path)
        return df
    except FileNotFoundError:
        print("File not found.")
        return None


def show_basic_stats(df):
    if df is None:
        return

    print("\nNumber of rows:", df.shape[0])
    print("Number of columns:", df.shape[1])

    if 'Start Time' in df.columns:
        df['Start Time'] = pd.to_datetime(df['Start Time'])
        print("Earliest start time:", df['Start Time'].min())
        print("Latest start time:", df['Start Time'].max())


def main():
    file_path = "new_york_city.csv"
    df = load_data(file_path)
    show_basic_stats(df)


if __name__ == "__main__":
    main()