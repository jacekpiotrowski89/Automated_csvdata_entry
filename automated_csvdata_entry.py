import pandas as pd 

def automated_data_entry(data, file_path):
    try:

        try:
            existing_data = pd.read_csv(file_path)
        except FileNotFoundError:
            existing_data = pd.DataFrame()

        new_data = pd.DataFrame(data)
        combined_data = pd.concat([existing_data, new_data], ignore_index=True)
        combined_data.to_csv(file_path, index=False)
        print("Data Entry successful!")
    except Exception as e:
        print(f'An error occurred: {e}')

data_to_enter = [
    {'name':'Alice', 'age':20, 'City':'New York'},
    {'name':'Jack', 'age':26, 'City':'Berlin'},
    {'name':'Bob', 'age':25, 'City':'Paris'}
]

csv_path_data = 'data.csv'
automated_data_entry(data_to_enter, csv_path_data)
