import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px

df = pd.DataFrame(
    np.random.rand(10, 4),
    columns=['Preço', 'Taxa de ocupação', 'Taxa de inadimplência', 'Pessoas por casa']
)

st.title('Dashboard Example')
st.header('Gráfico de Linha')
line_chart = px.line(df, title='Tendência ao longo do tempo')  # Fixing the typo in 'dfm' and 'title'
st.plotly_chart(line_chart, use_container_width=True)

st.header('Dados em Tabela')
st.table(df)