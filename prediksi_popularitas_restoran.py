# -*- coding: utf-8 -*-
"""prediksi_popularitas_restoran.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ZvEO6FHqxryBvxWP_5PvolFOc63VjHOy

# Problem Understanding
- Nama Proyek : Prediksi popularitas Restoran
- Link Dataset : https://www.kaggle.com/datasets/bhanupratapbiswas/zomato
- Tujuan :

*   Memprediksi popularitas suatu restoran berdasarkan Rating yang didapatkan,
*   Mencari Rata-rata dari Dining Rating dan Delivery Rating

# 1. Mempersiapkan Library
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from google.colab import files
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.svm import SVR
from sklearn.multioutput import MultiOutputRegressor
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor

"""# 2. Data Collection"""

uploaded = files.upload()

"""saya menggunakan perintah upload dari library google colab"""

df = pd.read_csv('Restaurants.csv')
df.head()

"""# 3. Data Exploration

Pada bagian ini, berfungsi untuk mempersiapkan dataset agar dapat kita gunakan nantinya.

## 1. Menghilangkan missing value
"""

df.isnull().sum()

"""untuk menghilangkan missing value saya akan mengunakan 2 metode yakni drop columns, dan mengisi nilai **NAN** dengan nilai mean

## Informasi Dataset
"""

df.info()

"""dapat dilihat dari dataset ini memiliki type data meliputi float, interger, dan object

## Statistik Deskriptif
"""

df.describe()

"""informasi yang dapat kita ambil


1.   Dining rating memiliki nilai maksimal 4.9 dengan rata-rata 4.1
2.   Delivery rating memiliki nilai maksimal 4.5 dengan rata-rata 3.9
3.   Nilai Dining Review Count dan Dining Rating Count memiliki nilai yang sangat berbeda dan terdapat outlier

## Menghilangkan kolom tidak penting
"""

df = df.drop(['Website','Phone_No','Latitude','Longitude','Known_For2','Known_For22','Address','Restaurant_Name'], axis=1)

"""Menghilangkan kolum diatas berguna untuk memaksimalkan model machine
learning, karena model ini akan berfokus pada rating restoran.


---
mengunakan fungsi **drop** yang merupakan fungsi bawaan untuk menghapus kolom didalam daaset

## Menghilangkan kolom NAN di Delivery_Rating
"""

df['Delivery_Rating']=df['Delivery_Rating'].fillna(df['Delivery_Rating'].mean())

"""### Mengisi kolom NAN pada delivery rating dengan mean adalah solusi terbaik untuk kolum ini


---

Mengunakan fungsi **fillna** untuk mengisi kolom NAN dalam kolom yang dipilih, dan mengunakanan fungsi **mean** untuk mengambil nilai rata-rata yang akan digunakan untuk mengisi nilai NAN

## Mengecek kolom Duplikasi
"""

df.duplicated().sum()

"""menggunakan fungsi duplicated untuk mengetahui kolom yang terdapat duplikasi

## Mengubah Type Data
"""

# Mengubah kolom object menjadi category
df['Locality'] = df['Locality'].astype('category')
df['Category'] = df['Category'].astype('category')

"""### mengubah kolom menjadi bertype category berfungsi untuk memudahkan model dalam melakukan encoding nantinya


---

Mengunakan fungsi **astype** untuk mendefinisikan secara langsung, type data apa yang akan diterapkan di kolom tersebut nantinya, dalam kasus ini adalah category

### Penanganan Outlier
"""

lower_percentile = df['Dining_Review_Count'].quantile(0.05)
upper_percentile = df['Dining_Review_Count'].quantile(0.95)

df['Dining_Review_Count'] = df['Dining_Review_Count'].clip(lower=lower_percentile, upper=upper_percentile)
display(df['Dining_Review_Count'].describe())

# menghilangkan outlier di delivery rating count
lower_percentile = df['Delivery_Rating_Count'].quantile(0.05)
upper_percentile = df['Delivery_Rating_Count'].quantile(0.95)

pd.set_option('future.no_silent_downcasting', True)
df['Delivery_Rating_Count'] = df['Delivery_Rating_Count'].clip(lower=lower_percentile, upper=upper_percentile)
display(df['Delivery_Rating_Count'].describe())

"""### Penanganan outlier pada Dining Review Count dan Delivery Rating Count, mengunakan batas atas dan batas bawah, dimana nila batas yang melebihi batas atas dan kurang dari batas bawah akan diubah

---
variabel lower pencentile akan mengambil data 5 persen, upper_pencentile aka mengambil data 95 persen. fungsi **clip** akan menganti nilai dibawah 5 persen untuk ditimpa dengan variabel lower_pencentile, dan mengambil data diatas 95 persen untuk ditimpa dengan variable upper_percentile

## Visualisasi EDA

Mencari karakteristik dataset dengan melihat hubungan antar kolum melalui diagram.

### Kolum Dining Rating
"""

sns.set(style='whitegrid')
plt.rcParams['figure.figsize'] = (8, 6)

plt.figure()
sns.histplot(df['Dining_Rating'].dropna(), bins=20, kde=True, color='orange')
plt.title('Histogram Dining Rating')
plt.xlabel('Dining Rating')
plt.ylabel('Jumlah Restoran')
plt.show()

"""Terdapat tren penurunan jumlah rating restoran mulai dari rating 4.1 ke atas"""

plt.figure()
sns.histplot(df['Dining_Review_Count'].dropna(), bins=30, kde=True, color='blue')
plt.title('Distribusi Jumlah Dining Review')
plt.xlabel('Dining Review Count')
plt.ylabel('Frekuensi')
plt.show()

""" Dapat dilihat kalau kebanyakan restaurant memiliki review antara 100 sampai 500 review, terdapat kenaikan tajam di review ke 2400 sebagai akibat dari penanganan outlier"""

plt.figure()
sns.scatterplot(x='Dining_Review_Count', y='Dining_Rating', data=df, alpha=0.6)
plt.title('Scatter Plot: Jumlah Review vs Dining Rating')
plt.xlabel('Dining Review Count')
plt.ylabel('Dining Rating')
plt.show()

"""Terdapat penumpukan titik di nilai antara 0-500 menunjukan kalau ,kebanyakan restoran memiliki jumlah rating antara 0-500

### Kolum Delivery Rating dan Delivery Rating Count
"""

plt.figure()
sns.histplot(df['Delivery_Rating'].dropna(), bins=20, kde=True, color='green')
plt.title('Histogram Delivery Rating')
plt.xlabel('Delivery Rating')
plt.ylabel('Jumlah Restoran')
plt.show()

"""Diagram memunjukkan Delivery rating antara 3.8 sampai 4.2, yang berarti kebanyakan pelaggan puas dengan Delivery semua restoran."""

plt.figure()
sns.histplot(df['Delivery_Rating_Count'].dropna(), bins=20, kde=True, color='blue')
plt.title('Histogram Delivery Rating Count')
plt.xlabel('Delivery Rating Count')
plt.ylabel('Frekuensi')
plt.show()

"""Dapat dilihat terdapat kenaikan tajam diawal, meski sudah dilakukan penanganan outlier. Dapat disimpulkan kalau ada 1000 pelanggan yang mengisi rating delivery di Zoomato, antara 1-500 kali . Terdapat penurunan tajam yang berarti hanya terdapat sedikit pelanggan yang mengisi rating lebih dari 500, angka 500 diambil, karena terdapat box setiap 2000 count, yang berarti setiap box berisi 500 Delivery rating."""

plt.figure()
sns.scatterplot(x='Delivery_Rating', y='Delivery_Rating_Count', data=df, alpha=0.6)
plt.title('Scatter Plot: Delivery Rating vs Delivery Rating Count')
plt.xlabel('Delivery Rating')
plt.ylabel('Delivery Rating Rating Count')
plt.show()

"""Dapat dilihat kalau terdapat penumpukan titik antara 3.75 sampai 4.25. yang berarti kalau kebanyakan pelanggan puas dengan pelayanan delivery yang diberikan.

### Visualisasi Price for 2
"""

sns.set(style='whitegrid')
plt.figure(figsize=(14, 6))

# Scatter plot: Pricing vs Dining Rating
plt.subplot(1, 2, 1)
sns.scatterplot(data=df, x='Pricing_for_2', y='Dining_Rating', alpha=0.6, color='green')
plt.title('Pricing for 2 vs Dining Rating')
plt.xlabel('Pricing for 2')
plt.ylabel('Dining Rating')

# Scatter plot: Pricing vs Delivery Rating
plt.subplot(1, 2, 2)
sns.scatterplot(data=df, x='Pricing_for_2', y='Delivery_Rating', alpha=0.6, color='blue')
plt.title('Pricing for 2 vs Delivery Rating')
plt.xlabel('Pricing for 2')
plt.ylabel('Delivery Rating')

plt.tight_layout()
plt.show()

"""Terdapat persebaran titik di semua harga dan rating menunjukkan kalau tidak ada hubungan linear antara **price_for_2** dengan dining rating maupun deliveri rating. meski ada beberapa kesimpulan seperti
terdapat penumpukan data di kiri **price_for_2** dan dining_rating yang berarti semakin murah restoran, maka semakin banyak rating yang didapat
untuk kolom **price_for_2** dengan delivery rating juga menunjukkan pola yang sama, meskipun untuk rating 4 terdapat persebaran merata di semua harga, yang berarti kebanyakan pelanggan memilih rating 4 untuk delivery mereka

## Boxplot

Bagian ini berfungsi untuk melihat outlier melalui boxplot, outlier nantinya akan dihilangkan untuk memaksimalkan akurasi pelatihan.
"""

# Boxlot untuk Dining Review Count
plt.figure(figsize=(10,6))
sns.boxplot(y=df['Dining_Review_Count'])
plt.title('Boxplot Dining Review Count')
plt.ylabel('Dining Review Count')
plt.show()

"""box terbentuk antara rentang **250 - 750** yang berarti setiap restoran rata-rata mendapatkan review antara 250-750 kali"""

plt.figure(figsize=(10,6))
sns.boxplot(y=df['Delivery_Rating_Count'])
plt.title('Boxplot Delivery Rating Count')
plt.ylabel('Delivery Rating Count')
plt.show()

"""box terbentuk antara 0 sampai 3500, yang berarti setiap restoran rata-rata mendapatkan review delivery mereka, antara 0 - 3500 kali.

# 4. Data Preposesing
"""

# Target Encoding untuk kolom Category
category_means = df.groupby('Category', observed=False)['Dining_Rating'].mean()

df['Category_TargetEncoded'] = df['Category'].map(category_means)
display(df[['Category', 'Category_TargetEncoded']].head())

# Target Encoding untuk Kolom locality
locality_means = df.groupby('Locality', observed=False)['Delivery_Rating'].mean()

df['Locality_TargetEncoded'] = df['Locality'].map(locality_means)
df['Locality_TargetEncoded'] = df['Locality_TargetEncoded'].round(1)
display(df[['Locality','Locality_TargetEncoded']].head())

"""Encoding wajib dilakukan karena model regresi hanya menerima nilai numeric.
Target encoding mengubah kolom berdasarkan target yang dipilih, dalam hal ini Dining_Rating dan Delivery_Rating

---

fungsi groupby akan mengambil nilai unique dari setiap baris dari kolom, fungsi mean akan mengambil nilai rata-rata, kedua nilai fungsi ini akan dimasukkan ke variabel masing-masing.
fungsi mapping akan memetakan nilai unique yang didapat didalam variabel, setiap nilai unique akan disesuaikan, dengan variabel dining_rating untuk kolom category dan Delivery_Rating untuk kolom Locality. hasil ini nantinya akan dimasukkan kedalam kolom baru.
fungsi **round(1)** akan membulatkan nilai kolom sehingga hanya memiliki satu nilai dibelakang koma.
"""

df.drop(['Category','Locality'], axis=1, inplace=True)

"""kolom Category dan Locality yang sudah di encode akan dihapus karena model yang akan kita buat hanya menerima nilai numeric

## Menambah fitur mean_rating
"""

dining_rating = df['Dining_Rating']
delivery_rating = df['Delivery_Rating']

mean_rating = (dining_rating + delivery_rating)/2
df['mean_rating'] = mean_rating
df['mean_rating'] = df['mean_rating'].round(1)

"""mean rating dibuat berdasarkan nilai rata-rata dari dining_rating dan delivery_rating. tujuan kolom ini dibuat untuk menyederhanakan model agar hanya memiliki satu kolom target

# 5. Splitting data
"""

X = df.drop(['mean_rating', 'Dining_Rating', 'Delivery_Rating'], axis=1)
y = df['mean_rating']

X_train,X_test, y_train, y_test = train_test_split(X,y, test_size=0.3, random_state=42)

"""fungsi dijalankan lagi agar model tidak mengintip jawaban dari kolom di variabel X
Disini data dibagi menjadi Training dan testing dengan perbandingan 80:20 mengunakan fungsi **train_test_split** dari libray sklearn
test_size merupakan persentase dari jumlah data testing, nilai 0.3 artinya data mengambil 30 persen dataset untuk pelatihan
fungsi random_state=42 gunanya untuk memastikan agar setiap dilakukan pembagian model, data yang dibagi akan sama selama mengunakan random_state yang sama.

## melakukan standarisasi
"""

numeric_column = ['Pricing_for_2', 'Dining_Review_Count', 'Delivery_Rating_Count',
                  'Category_TargetEncoded','Locality_TargetEncoded']
scaler = StandardScaler()
X_train[numeric_column]= scaler.fit_transform(X_train[numeric_column])
X_test[numeric_column]= scaler.transform(X_test[numeric_column])

"""varibel numeric_column akan mengambil nama kolom didalam tuple. variabel scaler akan memanggil fungsi StandartScaler dari library sklearn.
fungsi scaler.fit_transform akan melakukan stadarisasi yang sama terhadap data pelatihan.
Fungsi Scaler.transform melakukan standarisasi terhadap data uji

# 6. Model Selection
"""

# Linear Regression
linear = LinearRegression()
linear.fit(X_train, y_train)
y_pred_linear= linear.predict(X_test)

# Random Forest Regression
rf_model = RandomForestRegressor(n_estimators=100, random_state=42)
rf_model.fit(X_train, y_train)
y_pred_rf = rf_model.predict(X_test)

# Gradient Boosting
gb_model = GradientBoostingRegressor(n_estimators=100, random_state=42)
gb_model.fit(X_train, y_train)
y_pred_gb =  gb_model.predict(X_test)

"""variabel linaer, rf_model, gb_model akan menampung model dari setiap metode pelatihan.
fungsi fit mengambil data pelatihan dari X_train dan y_train
fungsi predict akan membuat nilai prediksi berdasarkan data testing
parameter yang digunakan didalam **random forest regresor** dan **gradient boosting** adalah **n_estimator** dan **random_state**.
n_estimator merupakan jumlah pohon didalam suatu model, sedangkan random_state=42 memastikan agar data tetap sama selama mengunakan random_state yang sama

# 7. Evaluasi Model
"""

# Evaluasi model Linear Regression
mse = mean_squared_error(y_test, y_pred_linear)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred_linear)

print(f'MSE: {mse}')
print(f'RMSE: {rmse}')
print(f'R-squared: {r2}')

# Evaluasi model Random Forest Regressor
mse_rf = mean_squared_error(y_test, y_pred_rf)
rmse_rf = np.sqrt(mse_rf)
r2_rf = r2_score(y_test, y_pred_rf)

print(f'MSE (Random Forest): {mse_rf}')
print(f'RMSE (Random Forest): {rmse_rf}')
print(f'R-squared (Random Forest): {r2_rf}')

# Evaluasi Model Gradient Bossting
mse_gb = mean_squared_error(y_test, y_pred_gb)
rmse_gb = np.sqrt(mse_gb)
r2_gb = r2_score(y_test, y_pred_gb)

print(f'MSE (Gradient Boosting): {mse_gb}')
print(f'RMSE (Gradient Boosting): {rmse_gb}')
print(f'R-squared (Gradient Boosting): {r2_gb}')

"""fungsi mse akan mengambil kuadrat kesalahan dari model.

---


fungsi rmse akan mengambil nilai akar dari mse.

---
fungsi r2 akang mengukur seberapa baik model menjelaskna variasi data dalam kolom target, dalam hal ini mean_rating


"""