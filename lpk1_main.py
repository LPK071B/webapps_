import streamlit as st

st.title("APLIKASI PERHITUNGAN NORMALITAS dan KADAR LARUTAN")

#NORMALITAS
st.write("PERHITUNGAN NORMALITAS LARUTAN")

mg = st.number_input('Masukkan bobot zat terlarut (mg)')
FP = st.number_input('Masukkan nilai FP')
mLlarutan = st.number_input('Masukkan volume larutan (mL)')
BE = st.number_input('masukkan nilai BE')

tombol = st.button('Hitung nilai normalitas')

if tombol:
    nilai_normalitas = mg/(FP*mLlarutan*BE)
    st.success(f'nilai normalitas adalah {nilai_normalitas}')

#KADAR DENGAN FP
st.write("PERHITUNGAN KADAR LARUTAN DENGAN FP")

volumetitran = st.number_input('Masukkan volume titran (mL)')
normalitastitran = st.number_input('Masukkan normalitas titran')
BEkadar = st.number_input('Masukkan nilai BE (kadar)')
volumetitrat = st.number_input('Masukkan volume titrat (mL)')
FPkadar = st.number_input('Masukkan nilai FP (kadar)')

tombol = st.button('Hitung nilai kadar (%)')

if tombol:
    nilai_kadar = (volumetitran*normalitastitran*BEkadar*FPkadar*0.1)/volumetitrat
    st.success(f'nilai kadar(%) adalah {nilai_kadar}%')
    
#KADAR TANPA FP
st.write("PERHITUNGAN KADAR LARUTAN TANPA FP")

xvolumetitran = st.number_input('Masukkan volume titran (mL) ')
xnormalitastitran = st.number_input('Masukkan normalitas titran ')
xBEkadar = st.number_input('Masukkan nilai BE (kadar) ')
xvolumetitrat = st.number_input('Masukkan volume titrat (mL) ')

tombol = st.button('Hitung nilai kadar  (%)')

if tombol:
    nilai_kadar = (xvolumetitran*xnormalitastitran*xBEkadar*0.1)/xvolumetitrat
    st.success(f'nilai kadar(%) adalah {nilai_kadar}%')
    
#KADAR Na2CO3
st.write("PERHITUNGAN KADAR Na2CO3 dalam CAMPURAN SECARA ASIDIMETRI")

volHCLa = st.number_input('Masukkan volume HCL (a) (mL)')
volHCLb = st.number_input('Masukkan volume HCL (b) (mL)')
normalitasHCL = st.number_input('Masukkan normalitas HCL')
BENa2CO3 = st.number_input('Masukkan nilai BE Na2CO3')
volumecontoh = st.number_input('Masukkan volume contoh (mL)')

tombol = st.button('Hitung nilai kadar Na2CO3 (%)')

if tombol:
    nilai_kadar_Na2CO3 = (2*(volHCLb-volHCLa))*normalitasHCL*BENa2CO3*0.1/volumecontoh
    st.success(f'nilai kadar(%) adalah {nilai_kadar_Na2CO3}%')

#KADAR NaOH
st.write("PERHITUNGAN KADAR NaOH dalam CAMPURAN SECARA ASIDIMETRI")

XvolHCLa = st.number_input('Masukkan volume HCL (a)  (mL)')
XvolHCLb = st.number_input('Masukkan volume HCL (b)  (mL)')
XnormalitasHCL = st.number_input('Masukkan  normalitas HCL')
BENaOH = st.number_input('Masukkan nilai BE NaOH')
Xvolumecontoh = st.number_input('Masukkan  volume contoh (mL)')

tombol = st.button('Hitung nilai kadar NaOH (%)')

if tombol:
    nilai_kadar_NaOH = (2*XvolHCLa-XvolHCLb)*XnormalitasHCL*BENaOH*0.1/Xvolumecontoh
    st.success(f'nilai kadar(%) adalah {nilai_kadar_NaOH}%')