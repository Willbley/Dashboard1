import pandas as pd
import numpy as np
import streamlit as st

# Criando um DataFrame de exemplo
df = pd.DataFrame(
    np.random.rand(10, 4),
    columns=['Preço', 'Taxa de ocupação', 'Taxa de inadimplência', 'Pessoas por casa']
)

# Título principal
st.title('Dashboard Example')

# Gráfico de Linha usando st.line_chart do próprio Streamlit
st.header('Gráfico de Linha')
st.line_chart(df)

# Dados em Tabela
st.header('Dados em Tabela')
st.table(df)
