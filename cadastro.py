import streamlit as st
import os.path
from datetime import date

st.set_page_config(
    page_title="Cadastro de clientes",
    # Para adicionar icones pelo teclado, botão windows + .
    page_icon="📒"
)

def gravar_dados(nome, data_nascimento, tipo_cliente, limite_credito):
    if nome and data_nascimento <= date.today():

        nome_arquivo = "cadastros.txt"
        arquivo_existe = os.path.isfile(nome_arquivo)
        """
        w  write mode
        r  read mode
        a  append mode
        
        w+  create file if it doesn't exist and open it in write mode
        r+  open for reading and writing. Does not create file.
        a+  create file if it doesn't exist and open it in append mode
        """
        with open(nome_arquivo,"a+",encoding='utf8') as file:
            if not arquivo_existe:
                file.write("Nome;Data de Nascimento;Tipo de Cliente;Limite de Crédito")

            file.write(f"\n{nome};{data_nascimento};{tipo_cliente};{limite_credito}")
        st.session_state["Sucesso"] = True
    else:
        st.session_state["Sucesso"] = False
    

st.title("📒 Cadastro de clientes")
st.divider()

nome = st.text_input("Digite o nome do cliente", key="nome_cliente")

data_nascimento = st.date_input("Data de nascimento", format="DD/MM/YYYY")
tipo_cliente = st.selectbox("Tipo de cliente"
                            , options=["Pessoa física", "Pessoa jurídica"], key="tipo_cliente")
limite_credito = st.number_input("Limite de crédito", step=100.00, format="%0.2f", key="limite_credito")

btn_cadastrar = st.button("Cadastrar"
                          , on_click=gravar_dados
                          , args=[nome, data_nascimento, tipo_cliente, limite_credito])
if btn_cadastrar:
    if st.session_state["Sucesso"]:
        st.success("Registro criado com sucesso!", icon="✅")
    else:
        st.warning("Falha com o registro", icon="❗")