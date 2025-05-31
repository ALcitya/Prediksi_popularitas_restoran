# Laporan Proyek Machine Learning - Moch. Ichwan Alif Kurniawan

## Domain Proyek

Ditengah industri kuliner yang berkembang pesat, Rating dan ulasan sering kali berperan penting apakah restoran tersebut bisa diterima pelanggan atau tidak.Rating mencerminkan, kualitas makanan, kebersihan, suasana tempat, serta layanan yang diberikan. Oleh karena itu, pemiliki restoran harus memberikan segala usaha terbaiknya, agar restorannya mendapatkan rating yang baik. Pemilik restoran harus mengetahui faktor-faktor yang mempengaruhi popularitas restoran mereka. 

Proyek ini bertujuan untuk membantu pemilik restoran dalam mengetahui apakah restoran mereka dapat bertahan kedepannya berdasarkan popularitas yang didapat saat ini. Dan untuk memberitahu bagaimana cara meningkatkan popularitas restoran mereka.
**Rubrik/Kriteria Tambahan (Opsional)**:
- Studi Harvard Business School tentang Dampak Rating Yelp terhadap Pendapatan Restoran

Studi yang dipimpin oleh Profesor Michael Luca dari Harvard Business School menemukan bahwa peningkatan satu bintang pada rating Yelp dapat meningkatkan pendapatan restoran sebesar 5–9%. Penelitian ini menyoroti pentingnya ulasan daring dalam memengaruhi keputusan konsumen dan kinerja bisnis restoran.

- Pengaruh Online customer Review terhadap pembelian di tiktokshop
Berdasarkan penelitian yang dilakukan, online customer review, online customer rating, dan cash on delivery berpengaruh positif terhadap keputusan pembelian
-  Artikel selengkapnya dapat dilihat [di sini](https://www.gq.com/story/bad-yelp-reviews)
- Atau melelui google scholar disini [Scholar](https://ejournal.unsrat.ac.id/index.php/emba/article/view/43393)

## Business Understanding

Bagian laporan ini mencakup:

### Problem Statements

- Bagaimana memprediksi Popularitas Restoran berdasarkan rating yang didapat
- Bagaimana mengetahui rata-rata rating yang didapat, berdasarkan dining rating dan delivery rating

### Goals

- Memprediksi popularits restoran berdasarkan rating yang didapatkan
- Mengetahui rata-rata rating restoran

Nantinya, berdarkan rata-rata rating yang didapatkan, maka model akan dilatih untuk mengetahui bagaimana performa restoran kedepannya.

**Rubrik/Kriteria Tambahan (Opsional)**:


### Solution statements
Membangun model prediksi popularitas restoran menggunakan beberapa algoritma supervised learning seperti **Random Forest Regression**, **Gradient Boosting**, dan **Logistic Regression**. Performa model akan dievaluasi menggunakan metrik **MSE**, **RMSE**, dan **R2** untuk mengetahui model mana yang paling optimal.

## Data Understanding
Dataset yang diambil merupakan dataset yang dibuat oleh Zomato, sebuah website delivery makanan yang sudah bekerjasama dengan banyak restoran. Link tautan dataset dapat diunduh disini [Kaggle](https://www.kaggle.com/datasets/bhanupratapbiswas/zomato).

### Fitur dari Dataset
- Terdapat 1965 baris dalam dataset
- Terdapat 15 kolom dalam dataset

### Variabel-variabel pada Zomato dataset adalah sebagai berikut:
- Restauran_Name : merupakan nama dari restaurant
- Category : merupakan category makanan yang diberikan oleh restoran
- Pricing_For_2 : merupakan harga yang diberikan restaurant untuk 2 orang
- Locality : Merupakan Lokasi Restaurant
- Dining_Rating : Merupakan rating yang diterima Restaurant
- Dining_Review_Count : Merupakan jumlah review yang diterima oleh restaurant
- Delivery_Rating : Merupakan rating pengantaran makanan dari Aplikasi Zoomato
- Delivery_Rating_Count : Merupakan jumlah rating pengantaran makanan yang diterima restaurant, melalui aplikasi zoomato
- Website : Merupakan link Restaurant di Aplikasi Zoomato
- Address : Alamat asli dari restaurant di dunia nyata
- Phone_No : Nomor Telepon dari restaurant
- Latitude : Garis lintang dari koordinat restaurant
- Longitude : Garis Bujur dari Koordinat Restaurant
- Known_For2 : Menu Favorit dari Restaurant
- Known_For22 : Menjelaskan fitur unik restaurant, seperti suasana, decorasi dll
  
### Kondisi awal dataset
Terdapat **Missing Value** dari tiga kolom, yakni :
- Delivery_Rating: 402 missing value
- Known_For2 : 405 missing value
- Known_For22 : 841 missing value 

**Rubrik/Kriteria Tambahan (Opsional)**:
- Melihat perbadingan antar kolom menggunakan **Histogram**, dan **Scatter Plot**, melihat outlier menggunakan **Box Plot**

## Data Preparation

**Urutan data Preparation saya Meliputi**
- Target Encoding untuk kolom untuk kolom Category: berfungsi untuk mengubah nilai kolom category sesuai kolom Dining_Rating
- Target Encoding untuk kolom untuk kolom Locality: berfungsi untuk mengubah nilai kolom Locality sesuai kolom Delivery_Rating
- Membuat kolom mean_rating : Berfungsi membuat nilai rata-rata dari kolom Dining_Rating atau Delivery_Rating
- Splitting dataset menjadi data latih dan data test
- Melakukan standarisasi terhadap kolom numeric: berfungsi untuk menyetarakan nilai kolum numeric

## Modeling

**Model yang Digunakan**
1. Linear Regresion : Mampu membuat hubungan linear berdasarkan input dan target yang diharapkan
2. Random Forest Regression : Membuat banyak pohon keputusan untuk membuat satu keputusan akhir
3. Gradient Boosting : Membaut pohon keputusan secara berurutan, model ini memperbaiki pohon sebelumnya, sehingga prediksi akhir dapat mendekati sempurna
   
**Parameter yang digunakan**
- Linear Regression, menggunakan parameter default bawaan model
- Random Forest Regression, mennggunakan n-estimator=100, dan random_state-42
- Gradient Boosting Regression, mennggunakan n-estimator=100, dan random_state-42.\
  
**Penjelasan Parameter**
- n-estimator = 100, membuat 100 pohon didalam model
- random_state = 42, memastikan agar pengunaan data tetap sama setiap pelatihan selama mengunakan random state yang sama
    
**Rubrik/Kriteria Tambahan (Opsional)**: 

1. Linear Regression
   
   **Kelebihan**
    - Sederhana dan mudah diimplementasi
    - cepat dilatih
    - Membutuhkan komputasi yang rendah
      
   **Kekurangan**
    - Rentan terhadap outlier
    - Tidak cocok untuk data non-liniear
      
2. Random Forest Regression
   
    **Kelebihan**
    - Mampu menangani hubungan non-linear dan interaksi antar fitur secara efektif.
    - Lebih tahan terhadap overfitting.
    - Dapat menangani jumlah fitur yang besar.
      
    **Kekurangan**
    - Kurang bisa diintegrasi karena merupakan ensemble dari banyak pohon
    - Membutuhkan lebih banyak daya komputasi
    - Hasil prediksi bisa kurang baik
      
3. Gradient Boosting Regression
   
    **Kelebihan**
    - Memberikan performa yang sangat tinggi
    - Mampu menangani hubungan yang kompleks
    - Fleksibel dan dapat digunakan di berbagai fungsi
      
    **Kekurangan**
    - Rentan terhadap Overfitting
    - Membutuhkan komputasi lebih banyak
    - Sulit diinterpretasikan
      
**Model terbaik**
Gradient Boosting merupakan model terbaik karena dapat memberikan performa yang lebih tinggi

## Evaluation

**Metriks yang digunakan**
***MSE***
    Mengukur rata-rata dari kuadrat perbedaan antara nilai prediksi model dan nilai aktual
***RMSE***
    Akar Kuadrat dari MSE
***R2***
    Menjelaskan variasi nilai dari target yang digunakan

**Hasil Proyek**
***Logistik Regression***
- MSE       : 0.011732630406702327
- RMSE      : 0.10831726735245091
- R-squared : 0.514393124126306
  
**Penjelasan**
 nilai MSE 0.0117 dan RMSE 0.1083 menunjukkan rata-rata yang cukup kecil, yang berarti model dapat memprediksi target dengan kesalahan yang kecil. Nilai R2 0.5143 menunjukkan kalau model dapat memprediksi 51% dari total variasi dari rata-rata rating.

***Random Forest Regression***
- MSE         : 0.011859347457627099
- RMSE        : 0.10890063111675294
- R-squared   : 0.5091483777151049

**Penjelasan**
nilai MSE 0.0118 dan RMSE 0.1089 menunjukkan rata-rata yang cukup kecil, yang berarti model dapat memprediksi target dengan kesalahan yang kecil. Nilai R2 0.5091 menunjukkan kalau model dapat memprediksi lebih dari 50% total variasi dari rata-rata rating.

***Gradient Boosting regression***
- MSE         : 0.011063820940422877
- RMSE        : 0.10518469917446585
- R-squared   : 0.542074766197737

**Penjelasan**
nilai MSE 0.0110 dan RMSE 0.1051 menunjukkan rata-rata yang cukup kecil, yang berarti model dapat memprediksi target dengan kesalahan yang kecil. Nilai R2 0.5420 menunjukkan kalau model dapat memprediksi lebih dari 54% total variasi dari rata-rata rating.

**---Ini adalah bagian akhir laporan---**
