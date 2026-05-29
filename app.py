import streamlit as st

st.set_page_config(
    page_title="Matematika Geometri",
    page_icon="🔢",
)

with st.sidebar:
    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:
        st.image("geometry.png")

    st.title("Bangun Datar")

    pilihan = st.selectbox(
        "Pilihan Bangun Datar",
        ["Persegi", "Persegi Panjang", "Lingkaran"]
    )

    st.caption("Dibuat dengan :fire: oleh **Alden Agna**")

match pilihan:

    case "Persegi":
        st.title("Persegi")
        st.markdown("Menghitung `luas` dan `keliling` Persegi")

        sisi = st.number_input("Masukkan panjang sisi")

        if st.button("Hitung"):
            luas = sisi * sisi
            keliling = 4 * sisi

            st.success(
                f"Luas Persegi: {luas:.2f} dan kelilingnya adalah {keliling:.2f}"
            )

            st.balloons()

    case "Persegi Panjang":
        st.title("Persegi Panjang")
        st.markdown("Menghitung `luas` dan `keliling` Persegi Panjang")

        panjang = st.number_input("Masukkan panjang")
        lebar = st.number_input("Masukkan lebar")

        if st.button("Hitung"):
            luas = panjang * lebar
            keliling = 2 * (panjang + lebar)

            st.success(
                f"Luas Persegi Panjang: {luas:.2f} dan kelilingnya adalah {keliling:.2f}"
            )

            st.balloons()

    case "Lingkaran":
        st.title("Lingkaran")
        st.markdown("Menghitung `luas` dan `keliling` Lingkaran")

        jari = st.number_input("Masukkan jari-jari")

        if st.button("Hitung"):
            luas = 3.14 * jari * jari
            keliling = 2 * 3.14 * jari

            st.success(
                f"Luas Lingkaran: {luas:.2f} dan kelilingnya adalah {keliling:.2f}"
            )

            st.balloons()

    case _:
        st.error("Terjadi Kesalahan")