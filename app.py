import streamlit as st
import pandas as pd

st.title('Primeira aplicação com Streamlit')
# file = '/Users/murilotuvani/Downloads/F_Frota_por_UF_Municipio_ANO_FAB_MOD_Julho_2024.xlsx'
# dados = pd.read_excel(file)

file = '/Users/murilotuvani/Downloads/acidentes.csv'
dados = pd.read_csv(file)
dados

