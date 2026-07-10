import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu
import plotly.express as px

# ------------------ Load Dataset ------------------
df = pd.read_csv("country_wise.csv")
df1 = pd.read_csv("covid 19 clean complete.csv")
df2 = pd.read_csv("day_wise.csv")

# ------------------ Page Config ------------------
st.set_page_config(
    page_title="COVID-19 Dashboard",page_icon="🦠",layout="wide")

# ------------------ Sidebar ------------------
with st.sidebar:
    st.title("🦠 COVID-19 Dashboard")

    menu = option_menu("Main Menu",["Overview", "Upload Dataset","Data Cleaning","Covid Analysis""World Map","Time Analysis","Insights"],
        icons=["house","upload","tools","bar-chart","globe","clock","lightbulb"],default_index=0)

# ====================== OVERVIEW ======================
if menu == "Overview":

    st.title("🦠 COVID-19 Dashboard")

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("Confirmed", f"{df['Confirmed'].sum():,}")
    c2.metric("Deaths", f"{df['Deaths'].sum():,}")
    c3.metric("Active", f"{df['Active'].sum():,}")
    c4.metric("Recovered", f"{df['Recovered'].sum():,}")

    st.divider()

    fig = px.bar(
        df.sort_values("Confirmed", ascending=False).head(10),
        x="Country/Region",
        y="Confirmed",
        color="Confirmed",
        title="Top 10 Countries by Confirmed Cases"
    )

    st.plotly_chart(fig, use_container_width=True)

# ====================== Upload Dataset ======================

elif menu == "Upload Dataset":

    st.title("📂 Upload Dataset")

    select = st.selectbox(
        "Select Dataset",
        ["Dataset 1", "Dataset 2", "Dataset 3"]
    )

    if select == "Dataset 1":
        data = df

    elif select == "Dataset 2":
        data = df1

    else:
        data = df2

    tab1, tab2, tab3 = st.tabs(
        ["Data", "Statistics", "Charts"]
    )

    with tab1:
        st.dataframe(data)

    with tab2:
        st.write(data.describe())

    with tab3:
        num = data.select_dtypes(include="number")

        if not num.empty:
            st.bar_chart(num)

# ====================== Data Cleaning ======================

elif menu == "Data Cleaning":

    st.title("🧹 Data Cleaning")

    c1, c2, c3,c4 = st.columns(4)

    c1.metric("Rows", df.shape[0])
    c2.metric("Columns", df.shape[1])
    c3.metric("Missing Values", df.isnull().sum().sum())
    c4.metric("Duplicate Rows",df.isnull().sum().sum())
    st.subheader("Duplicate Rows")

    st.write(df.duplicated().sum())

    st.subheader("Missing Values")

    st.dataframe(df.isnull().sum().reset_index().rename(
        columns={"index":"Column",0:"Missing Values"}))



# ====================== COVID Analysis ======================

elif menu == "Covid Analysis":

    st.title("📊 COVID Analysis")

    chart = st.selectbox(
        "Select Chart",
        ["Bar Chart","Pie Chart","Line Chart"]
    )

    if chart == "Bar Chart":

        fig = px.bar(
            df.sort_values("Confirmed", ascending=False).head(15),
            x="Country",
            y="Confirmed",
            color="Confirmed"
        )

        st.plotly_chart(fig, use_container_width=True)

    elif chart == "Pie Chart":

        fig = px.pie(
            values=[
                df["Confirmed"].sum(),
                df["Recovered"].sum(),
                df["Deaths"].sum(),
                df["Active"].sum()
            ],
            names=[
                "Confirmed",
                "Recovered",
                "Deaths",
                "Active"
            ]
        )

        st.plotly_chart(fig, use_container_width=True)

    else:

        fig = px.line(
            df,
            x="Country",
            y=["Confirmed","Recovered","Deaths"]
        )

        st.plotly_chart(fig, use_container_width=True)

# ====================== World Map ======================

elif menu == "World Map":

    st.title("🌍 World Map")

    st.info("Latitude & Longitude columns hone par yahan Plotly Choropleth ya Scatter Geo map add kiya ja sakta hai.")

# ====================== Time Analysis ======================

elif menu == "Time Analysis":

    st.title("📅 Time Analysis")

    if "Date" in df2.columns:

        df2["Date"] = pd.to_datetime(df2["Date"])

        st.line_chart(
            df2.set_index("Date")[
                ["Confirmed","Recovered","Deaths"]
            ]
        )

    else:

        st.write(df2.head())

# ====================== Insights ======================

elif menu == "Insights":

    st.title("💡 Insights")

    top = df.loc[df["Confirmed"].idxmax()]

    low = df.loc[df["Confirmed"].idxmin()]

    st.success(
        f"Highest Confirmed Cases : {top['Country']} ({top['Confirmed']:,})"
    )

    st.info(
        f"Lowest Confirmed Cases : {low['Country']} ({low['Confirmed']:,})"
    )

    recovery = (df["Recovered"].sum()/df["Confirmed"].sum())*100

    death = (df["Deaths"].sum()/df["Confirmed"].sum())*100

    active = (df["Active"].sum()/df["Confirmed"].sum())*100

    st.metric("Recovery Rate", f"{recovery:.2f}%")
    st.metric("Death Rate", f"{death:.2f}%")
    st.metric("Active Rate", f"{active:.2f}%")