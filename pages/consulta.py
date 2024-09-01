import streamlit as st
import pandas as pd
import os.path

st.set_page_config(
    page_title="Consulta de clientes",
    # Para adicionar icones pelo teclado, botão windows + .
    page_icon="🔍"
)

st.title("🔍 Consulta de clientes")
st.divider()

nome_arquivo = "cadastros.txt"
arquivo_existe = os.path.isfile(nome_arquivo)
if arquivo_existe:
    dados = pd.read_csv(nome_arquivo, sep=';', encoding='utf8')
    st.dataframe(dados)
else:
    st.text("Sem dados para exibir!")
