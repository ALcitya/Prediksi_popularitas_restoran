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
- Bagaimana mengetahui rata-rata Kesalahan dari model pelatihan
- Bagaimana mengetahui model apa yang memiliki performa terbaik

### Goals

- Memprediksi popularits restoran berdasarkan rating yang didapatkan
- Mengetahui rata-rata Kesalahan dari model Pelatihan
- Mengetahui model yang memiliki performa terbaik

Nantinya, berdarkan rata-rata rating yang didapatkan, maka model akan dilatih untuk mengetahui bagaimana performa restoran kedepannya.

**Rubrik/Kriteria Tambahan (Opsional)**:


### Solution statements
Membangun model prediksi popularitas restoran menggunakan beberapa algoritma supervised learning seperti **Random Forest Regression**, **Gradient Boosting**, dan **Linear Regression**. Performa model akan dievaluasi menggunakan metrik **MSE**, **RMSE**, dan **R2** untuk mengetahui model mana yang paling optimal.

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
- Menghilangkan kolom tidak penting seperti Website,Phone_No, Latitude, Longitude, Known_For2, Known_For22, Address, Restaurant_Name.
- Menghilangkan nilai NAN dan mengisi dengan nilai mean, dikolom Delivery_Rating: berfungsi untuk meningkatkan akurasi
- Mengubah type data Locality dan Category, menjadi bertype category : untuk mempermudah pelatihan
- Menghilangkan oulier di kolom Dining_Review_Count dan Delivery_Rating_Count, mengunakan metode Clip: agar tidak ada data yang hilang
- Target Encoding untuk kolom untuk kolom Category: berfungsi untuk mengubah nilai kolom category sesuai kolom Dining_Rating
- Target Encoding untuk kolom untuk kolom Locality: berfungsi untuk mengubah nilai kolom Locality sesuai kolom Delivery_Rating
- Menghapus kolom Locality dan Category : untuk mempermudah pelatihan dataset
- Membuat kolom mean_rating : Berfungsi membuat nilai rata-rata dari kolom Dining_Rating atau Delivery_Rating
- Splitting dataset menjadi data latih dan data test
- Melakukan standarisasi terhadap Data pelatihan mengunakan fit.transform
- Melakukan standarisasi terhapap data  Pengujian menggunakan transform

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
***linear Regression***
- MSE: 0.011732630406702327
- RMSE: 0.10831726735245091
- R-squared: 0.5143931241263064
  
**Penjelasan**
 nilai MSE 0.0117 dan RMSE 0.1083 menunjukkan rata-rata yang cukup kecil, yang berarti model dapat memprediksi target dengan kesalahan yang kecil. Nilai R2 0.5143 menunjukkan kalau model dapat memprediksi 51% dari total variasi dari rata-rata rating.

***Random Forest Regression***
- MSE (Random Forest): 0.011843120338983031
- RMSE (Random Forest): 0.10882610136811403
- R-squared (Random Forest): 0.5098200088937941

**Penjelasan**
nilai MSE 0.0118 dan RMSE 0.1088 menunjukkan rata-rata yang cukup kecil, yang berarti model dapat memprediksi target dengan kesalahan yang kecil. Nilai R2 0.5098 menunjukkan kalau model dapat memprediksi lebih dari 50% total variasi dari rata-rata rating.

***Gradient Boosting regression***
- MSE (Gradient Boosting): 0.01105952593128211
- RMSE (Gradient Boosting): 0.10516428068161789
- R-squared (Gradient Boosting): 0.54225253417460147

**Penjelasan**
nilai MSE 0.0110 dan RMSE 0.1051 menunjukkan rata-rata yang cukup kecil, yang berarti model dapat memprediksi target dengan kesalahan yang kecil. Nilai R2 0.5420 menunjukkan kalau model dapat memprediksi lebih dari 54% total variasi dari rata-rata rating.

**Insight**
1. Prediksi Popularitas restaurant dapat dilakukan mengunakan 3 model pelatihan yakni Linar Regression, Random Forest Regression, dan Gradient Boosting Regression
2. Rata-rata Kesalahan dapat diketahui dari MSE dan RMSE dari Algoritma pelatihan.
   - Linear Regression
nilai MSE 0.0117 dan RMSE 0.1083 menunjukkan rata-rata yang cukup kecil
   - Random Forest Regression
nilai MSE 0.0118 dan RMSE 0.1088 menunjukkan rata-rata yang cukup kecil
   - Gradient Boosting Regression
nilai MSE 0.0110 dan RMSE 0.1051 menunjukkan rata-rata yang cukup kecil

**Kesimpulan**
Dapat Ditarik Kesimpulan kalau Gradient Boosting Regression memiliki rat-rata kesalahan yang paling kecil

3. Untuk mengetahui Model dengan performa terbaik dapat diketahui dari nilai R2
   - Linear Regression
Nilai R2 menunjukkan nilai 51%
   - Random Forest Regression
Nilai R2 menunjukkan nilai 50%
   - Gradient Boosting Regression
Nilai R2 menunjukkan nilai 54%

**Kesimpulan**
Gradient Boosting Regression Menunjukkan performa terbaik, karena berhasil memprediksi 54% dari variasi rata-rata rating

**---Ini adalah bagian akhir laporan---**

