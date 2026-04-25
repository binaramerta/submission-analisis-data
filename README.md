# Proyek Analisis Data: E-Commerce Public Dataset 📦
Selamat datang di repositori Proyek Analisis Data E-Commerce. Proyek ini merupakan bagian dari submission kelas Dicoding "Belajar Fundamental Analisis Data". Proyek ini bertujuan untuk melakukan analisis mendalam terhadap dataset E-Commerce (Olist) dan menyajikan hasilnya dalam sebuah dasbor interaktif menggunakan Streamlit.

## 📊 Dashboard Demo
Visualisasi dapat dilihat secara langsung di: [Streamlit App](https://dbs-coding-camp-binara.streamlit.app/)

---

## 📜 Latar Belakang

Dataset ini berisi informasi mengenai pesanan yang dibuat di Olist Store, marketplace terbesar di Brasil. Data ini mencakup berbagai aspek mulai dari informasi pelanggan, lokasi geografis, hingga detail karakteristik produk. Analisis ini difokuskan pada pemetaan persebaran pelanggan untuk strategi pemasaran dan pengelompokan produk berdasarkan berat untuk efisiensi logistik.

---

## 🎯 Pertanyaan Bisnis

Analisis ini dirancang untuk menjawab dua pertanyaan bisnis utama menggunakan metode SMART:

1.  Strategi Pemasaran Geografis: Negara bagian (state) mana yang memiliki basis pelanggan terbanyak untuk pemfokusan alokasi anggaran pemasaran lokal?

2.  Optimalisasi Logistik: Bagaimana proporsi produk jika dikelompokkan berdasarkan kategori beratnya (Ringan, Sedang, Berat) untuk bahan negosiasi tarif pengiriman?

---

## ⚙️ Fitur Dashboard

Dashboard interaktif ini dibangun menggunakan Streamlit dengan fitur utama:

- **Visualisasi Multi-Tab**: Memisahkan analisis pelanggan dan analisis produk agar lebih terstruktur.

- **Informasi Geografis**: Menampilkan Top 5 negara bagian dengan jumlah pelanggan tertinggi.

- **Clustering Produk (Manual Grouping)**: Klasifikasi produk berdasarkan berat (Ringan <1kg, Sedang 1-5kg, Berat >5kg).

- **Insight & Rekomendasi**: Penjelasan langsung mengenai temuan data dan saran aksi bisnis pada setiap tab.

---

## 🛠️ Teknologi yang Digunakan

-   **Analisis Data**: Python, Pandas, NumPy
-   **Visualisasi Data**: Matplotlib, Seaborn
-   **Dashboard Interaktif**: Streamlit

---

## 🚀 Cara Menjalankan Proyek Secara Lokal

Ikuti langkah-langkah berikut untuk menjalankan dasbor ini di mesin lokal Anda.

1.  **Clone Repositori**
    ```bash
    git clone https://github.com/binaramerta/submission-analisis-data.git
    ```
    ```bash
    cd submission-analisis-data
    ```

2.  **Buat Lingkungan Virtual (Opsional tapi Direkomendasikan)**
    ```bash
    python -m venv venv
    ```
    ```bash
    source venv/bin/activate  # Untuk Windows: venv\Scripts\activate
    ```

3.  **Install Dependensi**
    Pastikan Anda memiliki file `requirements.txt` dengan konten berikut:
    ```
    streamlit
    pandas
    numpy
    matplotlib
    seaborn
    ```
    Kemudian, jalankan perintah instalasi:
    ```bash
    pip install -r requirements.txt
    ```

4.  **Jalankan Aplikasi Streamlit**
    Pastikan Anda berada di direktori utama proyek, lalu jalankan:
    ```bash
    streamlit run dashboard/dashboard.py
    ```
    Aplikasi akan terbuka secara otomatis di browser Anda.

---

## 📁 Struktur Repositori
```
.
├── dashboard/
│   └── dashboard.py      # Script utama untuk aplikasi Streamlit
│
├── data/
│   ├── customers_dataset.csv           # Dataset customer
│   └── products_dataset.csv          # Dataset products
│
├── notebook.ipynb        # Notebook Jupyter berisi proses analisis data secara lengkap
├── requirements.txt      # File daftar dependensi Python yang diperlukan
└── README.md             # Dokumentasi proyek (file ini)
```