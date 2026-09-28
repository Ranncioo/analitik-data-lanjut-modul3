import streamlit as st
import pandas as pd

# Judul aplikasi
st.title('Streamlit Simple App')

# Menambahkan navigasi di sidebar
page = st.sidebar.radio("Pilih halaman", ["Dataset", "Visualisasi"])

if page == "Dataset":
    st.header("Halaman Dataset")

    # Baca file CSV
    data = pd.read_csv("pddikti_example.csv")

    # Tampilkan data di Streamlit
    st.write(data)

elif page == "Visualisasi":
    st.header("Halaman Visualisasi")

    # Baca file CSV
    data = pd.read_csv("pddikti_example.csv")

    # Filter berdasarkan universitas
    selected_university = st.selectbox('Pilih Universitas', data['universitas'].unique())
    filtered_data = data[data['universitas'] == selected_university]

    st.write(f"Visualisasi Data untuk {selected_university}")

    # Buat pivot table: semester sebagai index, program_studi sebagai kolom
    pivot_data = filtered_data.pivot_table(
        index='semester', columns='program_studi', values='jumlah', aggfunc='sum'
    )

    # Tampilkan line chart bawaan Streamlit
    st.line_chart(pivot_data)