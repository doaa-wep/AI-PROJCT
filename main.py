import pandas as pd

def main():

    file_name = "new dataset.csv"

    try:
        data = pd.read_csv(file_name)

        print("\nDataset loaded successfully ✅")
        print("Shape:", data.shape)

        print("\nFirst 5 rows:\n")
        print(data.head())

    except FileNotFoundError:
        print(f"❌ File '{file_name}' not found in this folder.")

if __name__ == "__main__":
    main()