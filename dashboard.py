import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Judul Dashboard
st.title("📊 Dashboard Analisis E-Commerce - Kelompok 10123222")

# Upload file dataset
st.sidebar.header("📂 Upload Dataset")
customer_file = st.sidebar.file_uploader("Unggah customers_dataset.csv", type=["csv"])
payment_file = st.sidebar.file_uploader("Unggah order_payments_dataset.csv", type=["csv"])
products_file = st.sidebar.file_uploader("Unggah products_dataset.csv", type=["csv"])
sellers_file = st.sidebar.file_uploader("Unggah sellers_dataset.csv", type=["csv"])

# Membaca dataset yang diunggah
if customer_file:
    df_customers = pd.read_csv(customer_file)

if payment_file:
    df_payment = pd.read_csv(payment_file)

if products_file:
    df_products = pd.read_csv(products_file)

if sellers_file:
    df_sellers = pd.read_csv(sellers_file)

# **1. Distribusi Pelanggan Rio de Janeiro**
st.subheader("📍 Pelanggan dari Rio de Janeiro")
if customer_file:
    total_customers = len(df_customers)
    rio_customers = df_customers[df_customers["customer_city"].str.lower() == "rio de janeiro"]
    rio_percentage = (len(rio_customers) / total_customers) * 100

    labels = ['Rio de Janeiro', 'Lainnya']
    sizes = [rio_percentage, 100 - rio_percentage]
    colors = ['skyblue', 'lightgreen']

    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, autopct='%1.1f%%', colors=colors, startangle=90)
    ax.set_title("Distribusi Pelanggan Rio de Janeiro")

    st.pyplot(fig)
    st.write(f"🎯 **Pelanggan dari Rio de Janeiro: {rio_percentage:.2f}% dari total pelanggan.**")

# **2. Pembayaran dengan Credit Card**
st.subheader("💳 Persentase Pembayaran dengan Credit Card")
if payment_file:
    payment_counts = df_payment["payment_type"].value_counts()
    credit_card_percentage = (payment_counts.get('credit_card', 0) / payment_counts.sum()) * 100

    labels = ['Credit Card', 'Lainnya']
    sizes = [credit_card_percentage, 100 - credit_card_percentage]
    colors = ['skyblue', 'lightcoral']

    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, autopct='%1.1f%%', colors=colors, startangle=140)
    ax.set_title("Distribusi Metode Pembayaran")

    st.pyplot(fig)
    st.write(f"🎯 **Transaksi menggunakan Credit Card: {credit_card_percentage:.2f}% dari total transaksi.**")

# **3. Pelanggan dengan Transaksi Terbanyak**
st.subheader("🚀 Pelanggan dengan Transaksi Terbanyak")
if customer_file:
    customer_counts = df_customers["customer_unique_id"].value_counts()
    top_customer = customer_counts.idxmax()
    top_customer_count = customer_counts.max()
    top_customer_percentage = (top_customer_count / customer_counts.sum()) * 100

    # Membuat Pie Chart
    fig, ax = plt.subplots()
    labels = ['Pelanggan Teratas', 'Pelanggan Lainnya']
    sizes = [top_customer_percentage, 100 - top_customer_percentage]
    colors = ['#ff9999', '#66b3ff']

    ax.pie(sizes, labels=labels, autopct='%1.1f%%', colors=colors, startangle=90)
    ax.set_title("Persentase Transaksi Pelanggan Teratas")

    st.pyplot(fig)

    st.write(f"🎯 **Pelanggan dengan transaksi terbanyak:** `{top_customer}` dengan `{top_customer_count}` transaksi (**{top_customer_percentage:.2f}%** dari total transaksi).")



# **4. Analisis Order yang Tidak Delivered**
st.subheader("📦 Order yang Tidak Memiliki Status Delivered")
if payment_file:
    missing_delivered = df_payment[df_payment["payment_sequential"] == 1]  # Misalnya order belum lunas
    missing_percentage = (len(missing_delivered) / len(df_payment)) * 100

    labels = ['Tidak Delivered', 'Delivered']
    sizes = [missing_percentage, 100 - missing_percentage]
    colors = ['#ff9999', '#66b3ff']

    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, autopct='%1.1f%%', colors=colors, startangle=90)
    ax.set_title("Proporsi Order yang Tidak Delivered")

    st.pyplot(fig)
    st.write(f"🎯 **{missing_percentage:.2f}% dari order belum dikirim atau belum lunas.**")

# **5. Barang yang Laku Keras**
st.subheader("🔥 Barang Paling Laku & Persentasenya")
if products_file:
    category_counts = df_products["product_category_name"].value_counts()
    best_selling_category = category_counts.idxmax()
    best_selling_percentage = (category_counts.max() / category_counts.sum()) * 100

    # Membuat pie chart
    fig, ax = plt.subplots()
    ax.pie(category_counts[:5], labels=category_counts.index[:5], autopct='%1.1f%%', colors=['#ff9999','#66b3ff','#99ff99','#ffcc99','#c2c2f0'])
    ax.set_title("Top 5 Kategori Produk Paling Laku")

    st.pyplot(fig)
    
    st.write(f"🎯 **Kategori produk yang paling laku adalah** `{best_selling_category}` dengan kontribusi **{best_selling_percentage:.2f}%** dari total penjualan.")

# **6. Distribusi Seller di São Paulo**
st.subheader("🏢 Distribusi Seller di São Paulo")
if sellers_file:
    total_sellers = len(df_sellers)
    sao_paulo_sellers = df_sellers[df_sellers["seller_city"].str.lower() == "sao paulo"]
    sao_paulo_percentage = (len(sao_paulo_sellers) / total_sellers) * 100

    st.write(f"🎯 **Persentase seller dari São Paulo: {sao_paulo_percentage:.2f}% dari total seller.**")

    zip_distribution = sao_paulo_sellers["seller_zip_code_prefix"].value_counts()

    fig, ax = plt.subplots(figsize=(10, 5))
    zip_distribution.plot(kind="bar", ax=ax)
    ax.set_title("Distribusi Seller São Paulo Berdasarkan Kode Pos")
    ax.set_xlabel("Kode Pos")
    ax.set_ylabel("Jumlah Seller")
    plt.xticks(rotation=45)

    st.pyplot(fig)

st.write("© 2025 - Kelompok 10123222")
