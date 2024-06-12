import streamlit as st
import pandas as pd
import plotly.express as px


st.set_page_config (layout="wide")
df = pd.read_csv ("supermarket_sales.csv", sep=";", decimal=",")
#muda de object para tipo date
df["Date"] = pd.to_datetime(df["Date"])
#ordernar por data
df = df.sort_values("Date")
#ordernar por mes 
df["Month"] = df["Date"].apply(lambda x: str(x.year) + "-" + str(x.month))
month = st.sidebar.selectbox("Mes", df["Month"].unique())
#filtrar as datas
df_filtered = df[df["Month"] == month]


#quando coloca duas colunas assim e como se dividisse a tela em 2
col1, col2 = st.columns(2)
col3, col4, col5 = st.columns(3) #aqui separou em 3

#grafico de faturamento por dia 
fig_date = px.bar(df_filtered, x="Date", y="Total", color="City", title="Faturamento por dia")
col1.plotly_chart(fig_date, use_container_width=True)

#faturamento por tipo de produto
fig_prods = px.bar(df_filtered, x="Date", y="Product line", 
                  color="City", title="Faturamento por produto", 
                  orientation="h")

col2.plotly_chart(fig_prods, use_container_width=True)

#criar um tipo novo de grafico
city_total = df_filtered.groupby("City")[["Total"]].sum().reset_index()
fig_city = px.bar(city_total, x="City", y="Total", 
                  title="Faturamento por filial")

col3.plotly_chart(fig_city, use_container_width=True)

#grafico tipo pie
fig_kind = px.pie(df_filtered, values="Total", names="Payment",
                  title="Faturamento por forma de pagamento")

col4.plotly_chart(fig_kind, use_container_width=True)

city_total = df_filtered.groupby("City")[["Rating"]].mean().reset_index()
fig_rating = px.bar(df_filtered, y="Rating", x="City",
                  title="Avaliação")

col5.plotly_chart(fig_rating, use_container_width=True)


#streamlit run dashboard.py