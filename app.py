import streamlit as st
import numpy as np

st.set_page_config(
    page_title="Kalkulator Matriks",
    page_icon="🧮",
    layout="centered"
)

st.title("🧮 Kalkulator Matriks")
st.write("Kalkulator matriks berbasis web")

st.divider()

# =========================
# PILIH UKURAN MATRIKS
# =========================

ukuran = st.selectbox(
    "Pilih ukuran matriks",
    [2, 3, 4, 5],
    index=0
)

st.subheader(f"Matriks {ukuran} × {ukuran}")

# =========================
# INPUT MATRIKS A
# =========================

st.write("### Matriks A")

A = []

for i in range(ukuran):

    kolom = st.columns(ukuran)

    baris = []

    for j in range(ukuran):

        nilai = kolom[j].number_input(
            f"A{i+1}{j+1}",
            value=0.0,
            step=1.0,
            key=f"A_{i}_{j}"
        )

        baris.append(nilai)

    A.append(baris)

A = np.array(A, dtype=float)

# =========================
# INPUT MATRIKS B
# =========================

st.write("### Matriks B")

B = []

for i in range(ukuran):

    kolom = st.columns(ukuran)

    baris = []

    for j in range(ukuran):

        nilai = kolom[j].number_input(
            f"B{i+1}{j+1}",
            value=0.0,
            step=1.0,
            key=f"B_{i}_{j}"
        )

        baris.append(nilai)

    B.append(baris)

B = np.array(B, dtype=float)

# =========================
# PILIH OPERASI
# =========================

st.divider()

st.subheader("Pilih Operasi")

operasi = st.selectbox(
    "Operasi matriks",
    [
        "A + B",
        "A - B",
        "A × B",
        "Transpose A",
        "Transpose B",
        "Determinan A",
        "Determinan B",
        "Invers A",
        "Invers B"
    ]
)

# =========================
# TOMBOL HITUNG
# =========================

if st.button("🧮 HITUNG", use_container_width=True):

    st.divider()

    st.subheader("Hasil")

    # A + B
    if operasi == "A + B":

        hasil = A + B

        st.write("A + B =")

        st.dataframe(
            hasil,
            use_container_width=True
        )

    # A - B
    elif operasi == "A - B":

        hasil = A - B

        st.write("A - B =")

        st.dataframe(
            hasil,
            use_container_width=True
        )

    # A × B
    elif operasi == "A × B":

        hasil = A @ B

        st.write("A × B =")

        st.dataframe(
            hasil,
            use_container_width=True
        )

    # Transpose A
    elif operasi == "Transpose A":

        hasil = A.T

        st.write("Aᵀ =")

        st.dataframe(
            hasil,
            use_container_width=True
        )

    # Transpose B
    elif operasi == "Transpose B":

        hasil = B.T

        st.write("Bᵀ =")

        st.dataframe(
            hasil,
            use_container_width=True
        )

    # Determinan A
    elif operasi == "Determinan A":

        hasil = np.linalg.det(A)

        st.metric(
            "Determinan A",
            f"{hasil:.6f}"
        )

    # Determinan B
    elif operasi == "Determinan B":

        hasil = np.linalg.det(B)

        st.metric(
            "Determinan B",
            f"{hasil:.6f}"
        )

    # Invers A
    elif operasi == "Invers A":

        try:

            hasil = np.linalg.inv(A)

            st.write("A⁻¹ =")

            st.dataframe(
                hasil,
                use_container_width=True
            )

        except np.linalg.LinAlgError:

            st.error(
                "Matriks A tidak mempunyai invers."
            )

    # Invers B
    elif operasi == "Invers B":

        try:

            hasil = np.linalg.inv(B)

            st.write("B⁻¹ =")

            st.dataframe(
                hasil,
                use_container_width=True
            )

        except np.linalg.LinAlgError:

            st.error(
                "Matriks B tidak mempunyai invers."
            )
