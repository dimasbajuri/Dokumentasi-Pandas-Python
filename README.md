# Dokumentasi Penggunaan Pandas
Dokumentasi ini akan menjelaskan bagaimana menggunakan pandas (Jika ada kesalahan, bug, atau error dalam dokumentasi ini mohon hubungi akun `dimasbajuri`)

## Persiapan
Install pandas untuk memulai

```
pip install pandas
```
  
pada file Python, import modul pandas
```
import pandas as pd
```

## Content

### > Series
Apa itu Series? Series pada pandas seperti kolom array satu dimensi pada tabel dengan any type of data, contoh ada pada kode dibawah:
```
data_series = [2, 3, 5]

data_series1 = pd.Series(data_series) 
print(data_series1)
```
Hasil:
```
0    2
1    3
2    5
dtype: int64
```
Index pada awalnya dimulai dari 0 hingga seterusnya namun kita bisa menambahkan custom index pada argumen kedua dalam method .Series contohnya pd.Series(data_series, index=["a", "b", "c"]) dan perlu di ingat bahwa jumlah index harus sama dengan jumlah array yang diinput

```
data_adidas_cycling = {
    "day1": 321,
    "day2": 365,
    "day3": 308
}

data_series2 = pd.Series(data_adidas_cycling)
print(data_series2)
```
Hasil:
```
day1    321
day2    365
day3    308
dtype: int64
```

Kita juga bisa menambahkan index pada series dengan cara ditambahkan sebagai Key dalam Dictionary dan kita juga bisa mengambil salah satu dari data Series seperti kita mengambil list pada umumnya, dengan format variableSeries[index]

### > DataFrame
Apa itu DataFrame? Data frame adalah data structure 2 dimensi, atau table dengan baris dan kolom, contoh mudahnya seperti kode dibawah ini:
```
data_bersepeda = {
    "kalori": [321, 365, 308],
    "durasi": [55, 51, 58]
}

data_frame_bersepeda = pd.DataFrame(data_bersepeda)
print(data_frame_bersepeda)
```
Hasil:
```
   kalori  durasi
0     321      55
1     365      51
2     308      58
```
untuk mengambil satu baris atau lebih dari DataFrame gunakan `loc` dengan format `loc[namaIndex]`, contoh:  
`print(data_frame_bersepeda.loc[0])` Hasil:
```
kalori    321
durasi     55
Name: 0, dtype: int64
```
`print(data_frame_bersepeda.loc[[0, 1]])` Hasil
```
   kalori  durasi
0     321      55
1     365      51
```
Pada DataFrames kita juga bisa meng-custom indexnya dengan format pd.DataFrame(data, index=["index1", "index2", ...dst])

### > Membaca CSV

Cara sederhana untuk menyimpan big data adalah denganf file CSV, file CSV mengandung plain text yang dapat dibaca semua orang termasuk Pandas, pada contoh ini kita akan menggunakan data_dummy.csv. Contoh penggunaannya sebagai berikut:
```
data_csv = pd.read_csv('data_dummy.csv')

print(data_csv.to_string()) 
```
Note: Gunakan method `to_string()` untuk print seluruh DataFrame  
Hasil:
```
      Nama  Umur         Kota  Pendapatan
0    Alice    25     New York       70000
1      Bob    30  Los Angeles       80000
2  Charlie    35      Chicago       90000
3    David    40      Houston      100000
4      Eva    45      Phoenix      110000
5     Elon    58         Ohio      200000
```

Secara default, jika DataFrame memiliki banyak baris, Pandas hanya akan menampilkan sejumlah baris tertentu untuk menghindari output yang terlalu panjang dan tidak terbaca. Secara khusus, Pandas akan menampilkan 5 baris pertama dan 5 baris terakhir dari DataFrame. Kita dapat memeriksa dan mengubah jumlah maksimum baris yang ditampilkan menggunakan `pd.options.display.max_rows`. sebagai contoh
```
print(pd.options.display.max_rows)
```
Sebagai contoh, jika hasilnya adalah 60, itu berarti jika DataFrame memiliki lebih dari 60 baris, hanya 5 baris pertama dan 5 baris terakhir yang akan ditampilkan saat Anda mencetak DataFrame (kecuali jika menggunakan method `to_string`). Namun kita juga bisa mengubah jumlah maksimum jumlah yang ditampilkan, misalnya jika ingin menampilkan hingga 100 baris:
```
pd.options.display.max_rows = 100
```

### > Membaca JSON
Set big data sering di simpan atau di ekstrak dalam JSON, sebagai contoh kita akan menggunakan data_dummy_json.json:
```
data_json = pd.read_json('data_dummy_json.json')

print(data_json.to_string())
```
Note: Gunakan method `to_string()` untuk print seluruh DataFrame  
Hasil:
```
   id           name  age         city                      email     phone
0   1       John Doe   28     New York       john.doe@example.com  555-1234
1   2     Jane Smith   34  Los Angeles     jane.smith@example.com  555-5678
2   3  Alice Johnson   45      Chicago  alice.johnson@example.com  555-8765
3   4      Bob Brown   23      Houston      bob.brown@example.com  555-4321
4   5  Charlie Davis   30      Phoenix  charlie.davis@example.com  555-6789
```
Format JSON sama dengan format dictionary di Python, jika JSON tidak berada di dalam file yang berbeda. Kita bisa me-loadnya secara langsung dengan method `DataFrame`:
```
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
```
