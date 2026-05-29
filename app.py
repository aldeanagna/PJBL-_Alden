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
        ["Persegi", "Persegi Panjang", "Lingkaran", "Segitiga", "Jajar Genjang"]
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

        case "Segitiga":
        st.title("Segitiga")
        st.markdown("Menghitung `luas` dan `keliling` Segitiga")

        alas = st.number_input("Masukkan alas")
        tinggi = st.number_input("Masukkan tinggi")
        sisi1 = st.number_input("Masukkan sisi 1")
        sisi2 = st.number_input("Masukkan sisi 2")
        sisi3 = st.number_input("Masukkan sisi 3")

        if st.button("Hitung"):
            luas = 0.5 * alas * tinggi
            keliling = sisi1 + sisi2 + sisi3

            st.success(
                f"Luas Segitiga: {luas:.2f} dan kelilingnya adalah {keliling:.2f}"
            )

            st.balloons()

    case "Jajar Genjang":
        st.title("Jajar Genjang")
        st.markdown("Menghitung `luas` dan `keliling` Jajar Genjang")

        alas = st.number_input("Masukkan alas")
        tinggi = st.number_input("Masukkan tinggi")
        sisi_miring = st.number_input("Masukkan sisi miring")

        if st.button("Hitung"):
            luas = alas * tinggi
            keliling = 2 * (alas + sisi_miring)

            st.success(
                f"Luas Jajar Genjang: {luas:.2f} dan kelilingnya adalah {keliling:.2f}"
            )

            st.balloons()

    case _:
        st.error("Terjadi Kesalahan")
