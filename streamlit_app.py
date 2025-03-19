import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Fungsi untuk membaca file Excel
def load_excel(file):
    df = pd.read_excel(file)
    return df

# Fungsi untuk membuat grafik berdasarkan data
def plot_chart(df, x_column, y_column, chart_type):
    plt.figure(figsize=(10, 6))
    
    if chart_type == 'Line':
        plt.plot(df[x_column], df[y_column], marker='o')
        plt.title(f'Line Chart: {x_column} vs {y_column}')
        plt.xlabel(x_column)
        plt.ylabel(y_column)
    elif chart_type == 'Bar':
        plt.bar(df[x_column], df[y_column])
        plt.title(f'Bar Chart: {x_column} vs {y_column}')
        plt.xlabel(x_column)
        plt.ylabel(y_column)
    elif chart_type == 'Scatter':
        plt.scatter(df[x_column], df[y_column])
        plt.title(f'Scatter Plot: {x_column} vs {y_column}')
        plt.xlabel(x_column)
        plt.ylabel(y_column)

    # Tampilkan grafik
    st.pyplot(plt)

# Layout Streamlit
st.title('Excel Data Upload and Custom Chart Generator')

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
    
    # Menampilkan grafik berdasarkan pilihan
    if st.button('Generate Chart'):
        plot_chart(df, x_column, y_column, chart_type)
