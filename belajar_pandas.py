import pandas as pd

# ===Series===

data_series = [2, 3, 5]

data_series1 = pd.Series(data_series) 
print(data_series1)

data_adidas_cycling = {
    "day1": 321,
    "day2": 365,
    "day3": 308
}

data_series2 = pd.Series(data_adidas_cycling)
print(data_series2)

# ===DataFrame===

data_bersepeda = {
    "kalori": [321, 365, 308],
    "durasi": [55, 51, 58]
}

data_frame_bersepeda = pd.DataFrame(data_bersepeda)
print(data_frame_bersepeda)

print(data_frame_bersepeda.loc[0])

print(data_frame_bersepeda.loc[[0, 1]])

# ===CSV===

data_csv = pd.read_csv('data_dummy.csv')

print(data_csv.to_string())

print(pd.options.display.max_rows) 

# ===JSON===

data_json = pd.read_json('data_dummy_json.json')

print(data_json.to_string())

data_json_direct = [
    {
        "id": 1,
        "name": "John Doe",
        "age": 28,
        "city": "New York",
        "email": "john.doe@example.com",
        "phone": "555-1234"
    },
    {
        "id": 2,
        "name": "Jane Smith",
        "age": 34,
        "city": "Los Angeles",
        "email": "jane.smith@example.com",
        "phone": "555-5678"
    },
    {
        "id": 3,
        "name": "Alice Johnson",
        "age": 45,
        "city": "Chicago",
        "email": "alice.johnson@example.com",
        "phone": "555-8765"
    },
    {
        "id": 4,
        "name": "Bob Brown",
        "age": 23,
        "city": "Houston",
        "email": "bob.brown@example.com",
        "phone": "555-4321"
    },
    {
        "id": 5,
        "name": "Charlie Davis",
        "age": 30,
        "city": "Phoenix",
        "email": "charlie.davis@example.com",
        "phone": "555-6789"
    }
]

data_json_direct_pandas = pd.DataFrame(data_json_direct)

print(data_json_direct_pandas)