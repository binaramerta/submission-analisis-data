import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import numpy as np

st.set_page_config(page_title="E-Commerce Dashboard", page_icon="📦", layout="wide")

@st.cache_data
def load_data():
    customers_df = pd.read_csv("./data/customers_dataset.csv")
    products_df = pd.read_csv("./data/products_dataset.csv")
    
    products_df['product_weight_g'] = products_df['product_weight_g'].fillna(products_df['product_weight_g'].median())
    products_df['product_category_name'] = products_df['product_category_name'].fillna('unknown')
    
    bins = [0, 1000, 5000, np.inf]
    labels = ['Ringan (<1kg)', 'Sedang (1-5kg)', 'Berat (>5kg)']
    products_df['weight_category'] = pd.cut(products_df['product_weight_g'], bins=bins, labels=labels)
    
    return customers_df, products_df

customers_df, products_df = load_data()

with st.sidebar:
    st.markdown("**Nama:** Wahyu")
    st.markdown("**Email:** go.wahyu28@gmail.com")
    st.markdown("**ID Dicoding:** binara")
    st.markdown("---")
    st.write("Dashboard ini menampilkan analisis persebaran geografis pelanggan dan klasifikasi berat produk katalog.")

st.header("Dashboard Analisis Data")
st.markdown("Selamat datang di dashboard. Silakan pilih tab di bawah ini untuk melihat analisis spesifik.")

tab1, tab2 = st.tabs(["👥 Analisis Pelanggan", "📦 Analisis Produk"])

with tab1:
    st.subheader("Negara Bagian dengan Pelanggan Terbanyak")
    
    top_n = st.slider("Geser untuk memilih jumlah negara bagian (Top N):", min_value=3, max_value=15, value=5)
    
    bystate_df = customers_df.groupby(by="customer_state").customer_id.nunique().reset_index()
    bystate_df.rename(columns={"customer_id": "customer_count"}, inplace=True)
    bystate_df = bystate_df.sort_values(by="customer_count", ascending=False).head(top_n)
    
    sns.set_style("white")
    fig, ax = plt.subplots(figsize=(10, 5))
    
    colors_ = ["#1f77b4"] + ["#D3D3D3"] * (top_n - 1)

    sns.barplot(
        x="customer_count", 
        y="customer_state",
        data=bystate_df,
        palette=colors_,
        hue="customer_state",
        legend=False,
        edgecolor='black',
        linewidth=0.7,
        ax=ax
    )
    
    ax.set_title(f"Persebaran Geografis Pelanggan (Top {top_n})", loc="center", fontsize=14, fontweight='bold')
    ax.set_ylabel(None)
    ax.set_xlabel("Jumlah Pelanggan")
    ax.grid(axis='x', linestyle='--', alpha=0.7)
    
    st.pyplot(fig)
    
    with st.expander("Lihat Insight Pelanggan"):
        st.write("Negara bagian SP (São Paulo) mendominasi dengan lebih dari 40.000 pelanggan, menjadikannya target utama alokasi pemasaran lokal.")

with tab2:
    st.subheader("Distribusi Produk Berdasarkan Kategori Berat")
    
    semua_kategori = products_df['product_category_name'].unique().tolist()
    kategori_pilihan = st.multiselect(
        "Pilih Kategori Produk untuk dianalisis:",
        options=semua_kategori,
        default=['cama_mesa_banho', 'beleza_saude', 'esporte_lazer']
    )
    
    if kategori_pilihan:
        filtered_products_df = products_df[products_df['product_category_name'].isin(kategori_pilihan)]
    else:
        filtered_products_df = products_df

    weight_dist_df = filtered_products_df.groupby(by="weight_category", observed=True).product_id.nunique().reset_index()
    weight_dist_df.rename(columns={"product_id": "product_count"}, inplace=True)

    sns.set_style("white")
    fig2, ax2 = plt.subplots(figsize=(10, 5))

    sns.barplot(
        x="weight_category", 
        y="product_count",
        data=weight_dist_df,
        palette="viridis",
        hue="weight_category",
        legend=False,
        edgecolor='black',
        linewidth=0.7,
        ax=ax2
    )
    
    ax2.set_title("Proporsi Katalog berdasarkan Berat", loc="center", fontsize=14, fontweight='bold')
    ax2.set_ylabel("Jumlah Produk")
    ax2.set_xlabel("Kategori Berat")
    ax2.grid(axis='y', linestyle='--', alpha=0.7)
    
    st.pyplot(fig2)
    
    with st.expander("Lihat Insight Produk"):
        st.write("Mayoritas produk di katalog kita adalah barang Ringan (< 1kg), yang membuka peluang bagus untuk negosiasi tarif logistik *flat-rate*.")

st.caption("Copyright © Binara Submission 2026")