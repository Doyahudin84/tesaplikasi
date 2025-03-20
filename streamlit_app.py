import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import io

# Fungsi untuk membaca file Excel
def load_excel(file):
    df = pd.read_excel(file)
    return df

# Fungsi untuk membuat grafik berdasarkan data
def plot_chart(df, x_column, y_column, chart_type):
    # Membuat objek figure dan axes
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Menentukan grafik berdasarkan pilihan
    if chart_type == 'Line':
        ax.plot(df[x_column], df[y_column], marker='o')
        ax.set_title(f'Line Chart: {x_column} vs {y_column}')
        ax.set_xlabel(x_column)
        ax.set_ylabel(y_column)
    elif chart_type == 'Bar':
        ax.bar(df[x_column], df[y_column])
        ax.set_title(f'Bar Chart: {x_column} vs {y_column}')
        ax.set_xlabel(x_column)
        ax.set_ylabel(y_column)
    elif chart_type == 'Scatter':
        ax.scatter(df[x_column], df[y_column])
        ax.set_title(f'Scatter Plot: {x_column} vs {y_column}')
        ax.set_xlabel(x_column)
        ax.set_ylabel(y_column)
    
    # Menampilkan grafik pada Streamlit
    st.pyplot(fig)

    # Mengembalikan objek figure untuk penyimpanan
    return fig

# Layout Streamlit
st.title('Visualisasi Data Excel by Doya')
st.markdown("""
    **Selamat datang di aplikasi Visualisasi Data Excel!**
    - Untuk memulai, silakan **upload file Excel** yang berisi data yang ingin Anda visualisasikan.
    - Setelah file diupload, pilih kolom mana yang akan digunakan untuk sumbu X dan Y.
    - Pilih jenis grafik yang ingin Anda lihat: **Line**, **Bar**, atau **Scatter**.
    - Klik tombol **Generate Chart** untuk melihat hasil visualisasi Anda.
    - Setelah itu, Anda dapat mengunduh grafik dalam format PNG dengan tombol unduh yang tersedia.
""")

# Upload file Excel
uploaded_file = st.file_uploader("Upload an Excel file", type=["xlsx"])

if uploaded_file is not None:
    # Membaca data dari file yang diupload
    df = load_excel(uploaded_file)
    
    # Menampilkan data yang diupload
    st.write("Data yang diupload:")
    st.write(df)
    
    # Pilihan untuk memilih kolom yang akan digambar
    columns = df.columns.tolist()
    
    # Pilih kolom x dan y untuk chart
    x_column = st.selectbox('Pilih kolom untuk sumbu X', columns)
    y_column = st.selectbox('Pilih kolom untuk sumbu Y', columns)
    
    # Pilih jenis chart
    chart_type = st.selectbox('Pilih jenis chart', ['Line', 'Bar', 'Scatter'])
    
    # Menampilkan tombol untuk menghasilkan chart
    st.markdown("### Klik tombol di bawah untuk menghasilkan grafik:")
    if st.button('Generate Chart'):
        # Menghasilkan chart berdasarkan input pengguna
        fig = plot_chart(df, x_column, y_column, chart_type)
        
        # Menyimpan chart sebagai gambar PNG ke dalam buffer
        buf = io.BytesIO()
        fig.savefig(buf, format="png")
        buf.seek(0)
        
        # Menampilkan tombol unduh untuk mengunduh chart sebagai file PNG
        st.download_button(
            label="Download Chart as PNG",
            data=buf,
            file_name="chart.png",
            mime="image/png"
        )
else:
    st.info("Silakan upload file Excel untuk memulai visualisasi.")
