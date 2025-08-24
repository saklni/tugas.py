import streamlit as st

st.title("Aplikasi Sederhana")

st.subheader("Kalkulator")

x = st.number_input("Masukkan angka pertama")
y = st.number_input("Masukkan angka kedua")
op = st.selectbox("Pilih operasi", ["+", "-", "*", "/"])

if st.button("Hitung"):
    if op == "+":
        st.write("Hasil =", x + y)
    elif op == "-":
        st.write("Hasil =", x - y)
    elif op == "*":
        st.write("Hasil =", x * y)
    elif op == "/":
        if y == 0:
            st.write("Tidak bisa dibagi 0")
        else:
            st.write("Hasil =", x / y)


st.subheader("Konversi Suhu")

satuan = st.selectbox("Pilih satuan", ["Celcius", "Reamur", "Fahrenheit"])
nilai = st.number_input("Masukkan nilai suhu")

if st.button("Konversi"):
    if satuan == "Celcius":
        c = nilai
    elif satuan == "Reamur":
        c = nilai * 5/4
    elif satuan == "Fahrenheit":
        c = (nilai - 32) * 5/9

    st.write("Celcius =", c)
    st.write("Reamur =", c * 4/5)
    st.write("Fahrenheit =", (c * 9/5) + 32)

st.subheader("Deret Fibonacci")

n = st.number_input("Masukkan jumlah n", min_value=1, step=1)

if st.button("Tampilkan"):
    a, b = 0, 1
    hasil = []
    for i in range(int(n)):
        hasil.append(a)
        a, b = b, a + b
    st.write(hasil)
