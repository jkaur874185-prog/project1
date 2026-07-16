# ================= IMPORTS =================

import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu
import plotly.express as px
import json
# ================= PAGE CONFIG =================
st.set_page_config(
    page_title="COVID-19 Dashboard",
    page_icon="🦠",
    layout="wide"
)
# ================= CUSTOM CSS =================

st.markdown("""
<style>

/* ================= MAIN BACKGROUND ================= */

.stApp {
    background-color:#FFF4F1;
}



/* ================= SIDEBAR ================= */

section[data-testid="stSidebar"] {
    background-color:#9A7787 !important;
}


section[data-testid="stSidebar"] * {
    color:white !important;
}


section[data-testid="stSidebar"] h1 {
    color:#FED7BF !important;
    font-weight:900;
}



/* ================= OPTION MENU ================= */

.nav-link {

    background-color:#E4AFB0 !important;

    color:#4B3040 !important;

    border-radius:12px !important;

    margin:5px !important;

    font-weight:bold !important;

}


.nav-link:hover {

    background-color:#FED7BF !important;

    color:#9A7787 !important;

}


.nav-link-selected {

    background-color:#FED7BF !important;

    color:#9A7787 !important;

}



/* ================= HEADINGS ================= */

h1,h2,h3,h4 {

    color:#9A7787 !important;

    font-weight:900 !important;

}



/* ================= METRIC CARDS ================= */


div[data-testid="metric-container"] {

    background-color:#E4AFB0 !important;

    border:3px solid #9A7787 !important;

    border-radius:18px !important;

    padding:18px !important;

    box-shadow:0px 5px 15px rgba(154,119,135,0.4);

}


div[data-testid="metric-container"] label {

    color:#4B3040 !important;

    font-weight:bold !important;

}


div[data-testid="metric-container"] [data-testid="stMetricValue"] {

    color:#9A7787 !important;

    font-size:30px !important;

    font-weight:900 !important;

}



/* ================= INFO BOX ================= */

div[data-testid="stAlert"] {

    background-color:#FED7BF !important;

    border-left:8px solid #9A7787 !important;

    border-radius:15px !important;

}



/* ================= SUCCESS BOX ================= */

div.stSuccess {

    background-color:#E4AFB0 !important;

    border:2px solid #9A7787 !important;

    border-radius:15px !important;

}


div.stSuccess p {

    color:#4B3040 !important;

    font-weight:bold !important;

}



/* ================= DIVIDER ================= */

hr {

    border:2px solid #E4AFB0 !important;

}



/* ================= TEXT ================= */

p {

    color:#4B3040;

    font-size:16px;

}



/* ================= DATAFRAME BORDER ================= */

div[data-testid="stDataFrame"] {

    border:3px solid #9A7787 !important;

    border-radius:15px !important;

}



/* ================= SELECT BOX ================= */

div[data-baseweb="select"] {

    border:2px solid #9A7787 !important;

    border-radius:12px !important;

}



/* ================= BUTTON ================= */

.stButton button {

    background-color:#9A7787 !important;

    color:white !important;

    border-radius:12px !important;

    border:2px solid #FED7BF !important;

    font-weight:bold !important;

}


.stButton button:hover {

    background-color:#E4AFB0 !important;

    color:#4B3040 !important;

}


</style>
""", unsafe_allow_html=True)


df = pd.read_csv("country_wise.csv")
df1 = pd.read_csv("covid 19 clean complete.csv")
df2 = pd.read_csv("day_wise.csv")
df3 = pd.read_csv("full grouped.csv")
df4 = pd.read_csv("Lastest Covid-19 india Status.csv")

st.sidebar.image("logo cc.PNG", width=100)
st.markdown("""
<style>
/* Sidebar ka background */
[data-testid="stSidebar"] {
    background-color: #FED7BF;
}

/* Option menu ka background */
.nav {
    background-color: #FED7BF !important;
}

/* Menu items */
.nav-link {
    background-color: #FED7BF !important;
    color: #9A7787 !important;
    border-radius: 10px;
}

/* Selected menu item */
.nav-link-selected {
    background-color: #E4AFB0 !important;
    color: white !important;
}
</style>
""", unsafe_allow_html=True)


with st.sidebar:
    st.title("🦠 COVID-19 Dashboard")
    menu = option_menu("Main Menu",["Overview","Dataset Summary","Data Cleaning","Covid Analysis","Worldwide Analysis","Time Analysis","Insights"],
        icons=["🏡","📂","🔨","📊","🌎","⏰","💡"],
        default_index=0)

# ================= OVERVIEW =================
    

if menu == "Overview":
    st.markdown("""
    <style>
    .dashboard-title {
        background-color: #E4AFB0;
        color: black;
        padding: 15px;
        text-align: center;
        border-radius: 12px;
        font-size: 36px;
        font-weight: bold;
        margin-bottom: 20px;
        box-shadow: 0px 4px 8px rgba(0,0,0,0.2);
    }
    </style>

    <div class="dashboard-title">
        🌍 Global COVID-19 Analysis Dashboard
    </div>
    """, unsafe_allow_html=True)




    
    st.write("""
Welcome to the COVID-19 Global Analysis Dashboard.

This interactive dashboard provides a complete analysis
of COVID-19 data worldwide.

It helps users explore:
• Global COVID statistics
• Country-wise cases
• Data visualization
• Pandemic trends

Built using Python, Streamlit, Pandas and Plotly.
""")

    st.divider()

# ================= COUNTRY =================
  



    c1,c2,c3,c4 = st.columns(4)

    with c1:
        # ================= KPI CARD STYLE =================

     st.markdown("""
    <style>

    .metric-card{

        background:white;

        padding:18px;

        border-radius:18px;

        text-align:center;

        border:2px solid #E4AFB0;

        box-shadow:
        0px 5px 15px rgba(154,119,135,0.3);

        transition:0.3s ease-in-out;

    }


    .metric-card:hover{

        transform:translateY(-8px);

        box-shadow:
        0px 12px 25px rgba(154,119,135,0.5);

    }



    .blue-line{

        height:5px;

        background:#1E88E5;

        border-radius:10px;

    }


    .purple-line{

        height:5px;

        background:#9C27B0;

        border-radius:10px;

    }


    .orange-line{

        height:5px;

        background:#FF9800;

        border-radius:10px;

    }


    .green-line{

        height:5px;

        background:#4CAF50;

        border-radius:10px;

    }


    </style>
    """,unsafe_allow_html=True)



    # ==================================================
    # COUNTRY WISE OVERVIEW
    # ==================================================


    st.subheader("🌍 Country-Wise Overview")


    c1,c2,c3,c4 = st.columns(4)



    with c1:

        st.markdown(f"""

        <div class="metric-card">

        <h4>🦠 Confirmed Cases</h4>

        <h2 style="color:#1E88E5;">
        {df['Confirmed'].sum():,}
        </h2>

        <div class="blue-line"></div>

        </div>

        """,unsafe_allow_html=True)




    with c2:

        st.markdown(f"""

        <div class="metric-card">

        <h4>💀 Deaths</h4>

        <h2 style="color:#9C27B0;">
        {df['Deaths'].sum():,}
        </h2>

        <div class="purple-line"></div>

        </div>

        """,unsafe_allow_html=True)




    with c3:

        st.markdown(f"""

        <div class="metric-card">

        <h4>🟠 Active Cases</h4>

        <h2 style="color:#FF9800;">
        {df['Active'].sum():,}
        </h2>

        <div class="orange-line"></div>

        </div>

        """,unsafe_allow_html=True)




    with c4:

        st.markdown(f"""

        <div class="metric-card">

        <h4>💚 Recovered</h4>

        <h2 style="color:#4CAF50;">
        {df['Recovered'].sum():,}
        </h2>

        <div class="green-line"></div>

        </div>

        """,unsafe_allow_html=True)





    st.divider()



# ==================================================
# STATE WISE OVERVIEW
# ==================================================


    st.subheader("🏛️ State-Wise Overview")

    c1,c2,c3,c4 = st.columns(4)
    with c1:

        st.markdown(f"""

        <div class="metric-card">

        <h4>🦠 Total Cases</h4>

        <h2 style="color:#1E88E5;">
        {df4['Total Cases'].sum():,}
        </h2>

        <div class="blue-line"></div>

        </div>

        """,unsafe_allow_html=True)





    with c2:

        st.markdown(f"""

        <div class="metric-card">

        <h4>💀 Deaths</h4>

        <h2 style="color:#9C27B0;">
        {df4['Deaths'].sum():,}
        </h2>

        <div class="purple-line"></div>

        </div>

        """,unsafe_allow_html=True)





    with c3:

        st.markdown(f"""

        <div class="metric-card">

        <h4>🟠 Active Cases</h4>

        <h2 style="color:#FF9800;">
        {df4['Active'].sum():,}
        </h2>

        <div class="orange-line"></div>

        </div>

        """,unsafe_allow_html=True)





    with c4:

        st.markdown(f"""

        <div class="metric-card">

        <h4>💚 Discharged</h4>

        <h2 style="color:#4CAF50;">
        {df4['Discharged'].sum():,}
        </h2>

        <div class="green-line"></div>

        </div>

        """,unsafe_allow_html=True)
    st.subheader("📌 About Project")

    st.info("""
COVID-19 Global Analysis Dashboard

Project Objectives:
✔ Analyze COVID-19 worldwide data
✔ Compare country-wise cases
✔ Visualize pandemic impact
✔ Generate useful insights

Technologies:
🐍 Python
🎈 Streamlit
🐼 Pandas
📊 Plotly
""")
    
    # ================= GRAPHS =================


    col1,col2 = st.columns(2)



    # COUNTRY GRAPH

    with col1:


        st.subheader("🌍 Country-Wise Analysis")


        country_data = df.sort_values(
            "Confirmed",
            ascending=False
        ).head(10)



        fig_country = px.bar(

            country_data,

            x="Country/Region",

            y="Confirmed",

            color="Country/Region",

            title="Top 10 Countries by Confirmed Cases",

            color_discrete_sequence=[

                "#9A7787",
                "#E4AFB0",
                "#FED7BF",
                "#C98B9A",
                "#A85D75",
                "#F3B7B9",
                "#D98C9C",
                "#B06A80",
                "#E6A6A8",
                "#8F536A"

            ]

        )


        fig_country.update_layout(

            height=450,

            paper_bgcolor="#FFF4F1",

            plot_bgcolor="#FFF4F1",

            showlegend=False

        )


        st.plotly_chart(
            fig_country,
            use_container_width=True
        )



    # STATE GRAPH


    with col2:


        st.subheader("🏛️ State-Wise Analysis")


        state_data = df4.sort_values(
            "Total Cases",
            ascending=False
        ).head(10)



        fig_state = px.bar(

            state_data,

            x="States",

            y="Total Cases",

            color="States",

            title="Top 10 States by Total Cases",

            color_discrete_sequence=[

                "#9A7787",
                "#E4AFB0",
                "#FED7BF",
                "#C98B9A",
                "#A85D75",
                "#F3B7B9",
                "#D98C9C",
                "#B06A80",
                "#E6A6A8",
                "#8F536A"

            ]

        )


        fig_state.update_layout(

            height=450,

            paper_bgcolor="#FFF4F1",

            plot_bgcolor="#FFF4F1",

            showlegend=False

        )


        st.plotly_chart(
            fig_state,
            use_container_width=True
        )



    st.divider()



    # ================= FEATURES =================


    st.subheader("✨ Key Features")


    f1,f2 = st.columns(2)


    with f1:

        st.success("🌍 Global Statistics")

        st.success("📊 Interactive Charts")

        st.success("📍 Country Analysis")



    with f2:

        st.success("🏛️ State Analysis")

        st.success("📈 Trend Visualization")

        st.success("🧹 Clean Dataset")



    st.divider()



    # ================= HIGHLIGHTS =================
    st.subheader("📈 Dashboard Highlights")

    h1, h2 = st.columns(2)

    top = df.loc[df["Confirmed"].idxmax(), "Country/Region"]

    recovery = (df["Recovered"].sum() / df["Confirmed"].sum()) * 100
    death = (df["Deaths"].sum() / df["Confirmed"].sum()) * 100

    # CSS
    st.markdown("""
    <style>
    .metric-card{
        background-color:#FFFFFF;
        padding:20px;
        border-radius:15px;
        box-shadow:0 4px 10px rgba(0,0,0,0.15);
        text-align:center;
        margin-bottom:15px;
        border-left:6px solid #E4AFB0;
    }

    .metric-title{
        font-size:18px;
        color:#444;
        font-weight:bold;
    }

    .metric-value{
        font-size:30px;
        color:#C0392B;
        font-weight:bold;
        margin-top:10px;
    }
    </style>
    """, unsafe_allow_html=True)

    with h1:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-title">🌍 Countries Covered</div>
            <div class="metric-value">{df['Country/Region'].nunique()}</div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-title">🏆 Most Affected Country</div>
            <div class="metric-value">{top}</div>
        </div>
        """, unsafe_allow_html=True)

    with h2:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-title">💚 Recovery Rate</div>
            <div class="metric-value">{recovery:.2f}%</div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-title">❤️ Death Rate</div>
            <div class="metric-value">{death:.2f}%</div>
        </div>
        """, unsafe_allow_html=True)

    
    # ================= DATASET SUMMARY =================


elif menu == "Dataset Summary":

    st.title("📂 Dataset Summary")
    select = st.selectbox("Select Dataset",["Dataset 1","Dataset 2","Dataset 3","Dataset 4","Dataset 5"])
    if select == "Dataset 1":
        data = df
    elif select == "Dataset 2":
        data = df1
    elif select == "Dataset 3":
        data = df2
    elif select == "Dataset 4":
        data = df3
    else:
        data = df4

    tab1, tab2, tab3 = st.tabs(["Data","Statistics","Charts"])
# -------- DATA TAB --------
    with tab1:
        st.subheader("Dataset Preview")
        st.dataframe(data,use_container_width=True)

# -------- STATISTICS TAB --------

    with tab2:
        st.subheader("Statistical Summary")
        st.dataframe(data.describe())
        st.write("Rows:",data.shape[0])
        st.write("Columns:",data.shape[1])
        # st.write("Column Names:")
        # st.write(list(data.columns))
# -------- CHART TAB --------
    st.markdown("""
    <style>

    .js-plotly-plot {

        border: 3px solid #9A7787;
        border-radius: 18px;
        padding: 12px;
        background-color: white;
        box-shadow: 0px 5px 15px rgba(154,119,135,0.4);

    }

    </style>
    """, unsafe_allow_html=True)
    with tab3:
        numeric_cols = (data.select_dtypes(include="number").columns.tolist())
        text_cols = (data.select_dtypes(include="object").columns.tolist())
        if len(text_cols) > 0 and len(numeric_cols) > 0:
            x_col = st.selectbox("Select X Axis",text_cols)
            y_col = st.multiselect("Select Y Axis",numeric_cols,default=numeric_cols[:2])
            if y_col:
                fig = px.bar(data.head(20),x=x_col,y=y_col,barmode="group",title="Dataset Visualization")


                st.plotly_chart(
                    fig,
                    use_container_width=True
                )


        else:

            st.warning(
                "Dataset does not contain suitable columns for chart.")





# ================= DATA CLEANING =================
elif menu == "Data Cleaning":
    st.title("🧹 Data Cleaning")

    st.subheader("📂 Original Dataset Information")

    clean_data = pd.read_csv(
        "covid_19_clean_complete.csv"
    )
    st.markdown("""
    <style>

    /* Metric Cards */

    .info-card{

    background:white;
    padding:18px;
    border-radius:18px;
    text-align:center;

    border:2px solid #E4AFB0;

    box-shadow:
    0px 5px 15px rgba(154,119,135,0.3);

    transition:0.3s;

    }


    .info-card:hover{

    transform:translateY(-8px);

    box-shadow:
    0px 12px 25px rgba(154,119,135,0.5);

    }



    /* Lines */

    .blue-line{

    height:5px;
    background:#2196F3;
    border-radius:10px;

    }


    .purple-line{

    height:5px;
    background:#9C27B0;
    border-radius:10px;

    }


    .orange-line{

    height:5px;
    background:#FF9800;
    border-radius:10px;

    }


    .green-line{

    height:5px;
    background:#4CAF50;
    border-radius:10px;

    }



    /* Cleaning Box */

    .clean-box{

    background:#FED7BF;

    padding:20px;

    border-radius:18px;

    border-left:8px solid #9A7787;

    font-size:16px;

    }


    /* Dataframe */

    div[data-testid="stDataFrame"]{

    border:3px solid #9A7787;

    border-radius:15px;

    box-shadow:
    0px 5px 15px rgba(154,119,135,0.3);

    }


    </style>
    """,unsafe_allow_html=True)



# ---------- ORIGINAL DATASET ----------


    c1,c2,c3,c4 = st.columns(4)



    with c1:

        st.markdown(f"""

        <div class="info-card">

        <h4>📄 Rows</h4>

        <h2 style="color:#2196F3;">
        {clean_data.shape[0]:,}
        </h2>

        <div class="blue-line"></div>

        </div>

        """,unsafe_allow_html=True)



    with c2:

        st.markdown(f"""

        <div class="info-card">

        <h4>📑 Columns</h4>

        <h2 style="color:#9C27B0;">
        {clean_data.shape[1]}
        </h2>

        <div class="purple-line"></div>

        </div>

        """,unsafe_allow_html=True)




    with c3:

        st.markdown(f"""

        <div class="info-card">

        <h4>⚠️ Missing Values</h4>

        <h2 style="color:#FF9800;">
        {clean_data.isnull().sum().sum():,}
        </h2>

        <div class="orange-line"></div>

        </div>

        """,unsafe_allow_html=True)




    with c4:

        st.markdown(f"""

        <div class="info-card">

        <h4>📋 Duplicate Rows</h4>

        <h2 style="color:#4CAF50;">
        {clean_data.duplicated().sum():,}
        </h2>

        <div class="green-line"></div>

        </div>

        """,unsafe_allow_html=True)



    st.divider()



# ---------- CLEANING STEPS ----------


    st.subheader("🛠 Cleaning Steps")


    


    st.write(
    """
    ✔ Removed duplicate rows

    ✔ Filled missing values

    ✔ Checked data types

    ✔ Removed unnecessary data
    """
    )





    # ---------- CLEAN DATA ----------


    cleaned_df1 = clean_data.drop_duplicates()


    cleaned_df1 = cleaned_df1.fillna(0)



    st.divider()



# ---------- CLEANED INFORMATION ----------


    st.subheader("✅ Cleaned Dataset Information")



    c1,c2,c3,c4 = st.columns(4)



    with c1:

        st.markdown(f"""

        <div class="info-card">

        <h4>📄 Rows</h4>

        <h2 style="color:#2196F3;">
        {cleaned_df1.shape[0]:,}
        </h2>

        <div class="blue-line"></div>

        </div>

        """,unsafe_allow_html=True)




    with c2:

        st.markdown(f"""

        <div class="info-card">

        <h4>📑 Columns</h4>

        <h2 style="color:#9C27B0;">
        {cleaned_df1.shape[1]}
        </h2>

        <div class="purple-line"></div>

        </div>

        """,unsafe_allow_html=True)




    with c3:

        st.markdown(f"""

        <div class="info-card">

        <h4>⚠️ Missing Values</h4>

        <h2 style="color:#FF9800;">
        {cleaned_df1.isnull().sum().sum():,}
        </h2>

        <div class="orange-line"></div>

        </div>

        """,unsafe_allow_html=True)




    with c4:

        st.markdown(f"""

        <div class="info-card">

        <h4>📋 Duplicate Rows</h4>

        <h2 style="color:#4CAF50;">
        {cleaned_df1.duplicated().sum():,}
        </h2>

        <div class="green-line"></div>

        </div>

        """,unsafe_allow_html=True)




    st.divider()



    # ---------- PREVIEW ----------


    st.subheader("📋 Cleaned Dataset Preview")


    st.dataframe(
        cleaned_df1.head(20),
        use_container_width=True
    )



    # ---------- DATA TYPES ----------


    st.subheader("🔠 Data Types")


    dtype_df1 = pd.DataFrame(
        cleaned_df1.dtypes,
        columns=["Data Type"]
    )


    st.dataframe(
        dtype_df1,
        use_container_width=True
    )


    # ================= COVID ANALYSIS =================



elif menu == "Covid Analysis":

    st.title("📊 COVID-19 Analysis")


    # ================= CHART STYLE FUNCTION =================

    def chart_style(fig):

        fig.update_layout(

            title_font=dict(
                size=24,
                family="Arial Black",
                color="#9A7787"
            ),

            xaxis_title_font=dict(
                size=16,
                family="Arial Black"
            ),

            yaxis_title_font=dict(
                size=16,
                family="Arial Black"
            ),

            height=550,

            plot_bgcolor="white",

            paper_bgcolor="#FFF4F1"

        )

        return fig



    # ================= TOP 15 COUNTRY =================


    st.subheader("🌍 Top 15 Countries COVID-19 Cases")


    top15_country = df.sort_values(
        "Confirmed",
        ascending=False
    ).head(15)



    fig = px.bar(

        top15_country,

        x="Country/Region",

        y=[
            "Confirmed",
            "Active",
            "Recovered",
            "Deaths"
        ],

        barmode="group",

        title="Top 15 Countries - Confirmed, Active, Recovered & Deaths",

        color_discrete_sequence=px.colors.qualitative.Set2

    )


    st.plotly_chart(
        chart_style(fig),
        use_container_width=True
    )



    st.divider()



    # ================= TOP 15 STATES =================


    st.subheader("🇮🇳 Top 15 States COVID-19 Cases")


    top15_state = df4.sort_values(
        "Total Cases",
        ascending=False
    ).head(15)



    fig2 = px.bar(

        top15_state,

        x="States",

        y=[
            "Total Cases",
            "Active",
            "Deaths",
            "Discharged"
        ],

        barmode="group",

        title="Top 15 States - Total Cases, Active, Deaths & Discharged",

        color_discrete_sequence=px.colors.qualitative.Pastel

    )



    st.plotly_chart(

        chart_style(fig2),

        use_container_width=True

    )



    st.divider()



    # ================= TABS =================


    tab1, tab2, tab3 = st.tabs(

        [
            "🌍 Country Analysis",
            "🇮🇳 State Analysis",
            "⚖ Comparison"
        ]

    )


    def chart_style(fig):

        fig.update_layout(
            paper_bgcolor="#FED7BF",
            plot_bgcolor="#FFF8F6",
            font=dict(
                family="Poppins",
                size=14,
                color="#9A7787"
            ),
            title=dict(
                font=dict(size=22, color="#9A7787"),
                x=0.5
            ),
            margin=dict(l=20, r=20, t=60, b=20),
            shapes=[
                dict(
                    type="rect",
                    xref="paper",
                    yref="paper",
                    x0=0,
                    y0=0,
                    x1=1,
                    y1=1,
                    line=dict(color="#E4AFB0", width=3),
                    fillcolor="rgba(0,0,0,0)"
                )
            ]
        )

        fig.update_xaxes(
            showgrid=True,
            gridcolor="#F5D5D6",
            showline=True,
            linewidth=2,
            linecolor="#E4AFB0",
            mirror=True
        )

        fig.update_yaxes(
            showgrid=True,
            gridcolor="#F5D5D6",
            showline=True,
            linewidth=2,
            linecolor="#E4AFB0",
            mirror=True
        )

        return fig
    # ================= COUNTRY ANALYSIS =================


    with tab1:


        st.subheader("🌍 Country Analysis")



        # Bar Chart


        fig = px.bar(

            top15_country.head(10),

            x="Country/Region",

            y="Recovered",

            title="Top Countries Recovered Cases"

        )

        st.plotly_chart(

            chart_style(fig),

            use_container_width=True

        )




        # Donut Chart


        fig = px.pie(

            top15_country.head(10),

            names="Country/Region",

            values="Deaths",

            hole=0.5,

            title="Country Death Distribution"

        )


        st.plotly_chart(

            chart_style(fig),

            use_container_width=True

        )




        # Scatter


        fig = px.scatter(

            top15_country,

            x="Confirmed",

            y="Deaths",

            size="Recovered",

            color="Country/Region",

            title="Confirmed Cases vs Deaths"

        )


        st.plotly_chart(

            chart_style(fig),

            use_container_width=True

        )





    # ================= STATE ANALYSIS =================


    with tab2:


        st.subheader("State Analysis")



        # Bar


        fig = px.bar(

            top15_state.head(10),

            x="States",

            y="Total Cases",

            title="Top States Total Cases"

        )


        st.plotly_chart(

            chart_style(fig),

            use_container_width=True

        )




        # Donut


        fig = px.pie(

            top15_state.head(10),

            names="States",

            values="Deaths",

            hole=0.5,

            title="State Death Distribution"

        )


        st.plotly_chart(

            chart_style(fig),

            use_container_width=True

        )




        # Area Chart


        fig = px.area(

            top15_state,

            x="States",

            y="Active",

            title="Active Cases Across States"

        )


        st.plotly_chart(

            chart_style(fig),

            use_container_width=True

        )





    # ================= COMPARISON =================


    with tab3:


        st.subheader("⚖ Country vs State Comparison")



        col1, col2 = st.columns(2)




        # COUNTRY SIDE


        with col1:


            st.write("🌍 Country Comparison")



            fig = px.bar(

                top15_country.head(10),

                x="Country/Region",

                y="Confirmed",

                title="Country Confirmed Cases"

            )


            st.plotly_chart(

                chart_style(fig),

                use_container_width=True

            )


            

            fig = px.sunburst(

                top15_country,

                path=["Country/Region"],

                values="Confirmed",

                title="Country Analysis"

            )


            st.plotly_chart(

                chart_style(fig),

                use_container_width=True

        )





        # STATE SIDE


        with col2:


            st.write(" State Comparison")



            fig = px.bar(

                top15_state.head(10),

                x="States",

                y="Total Cases",

                title="State Total Cases"

            )


            st.plotly_chart(

                chart_style(fig),

                use_container_width=True

            )


            
            fig = px.sunburst(

                top15_state,

                path=["States"],

                values="Total Cases",

                title="State Analysis"

            )


            st.plotly_chart(

                chart_style(fig),

                use_container_width=True)



# ================= Worldwide Analysis =================
elif menu == "Worldwide Analysis":

    st.title("🌍 COVID-19 World Map")


    # -------- SELECT METRIC --------

    metric = st.selectbox(
        "Select COVID Metric",
        [
            "Confirmed",
            "Active",
            "Recovered",
            "Deaths"
        ]
    )



    st.subheader(
        f"🌎 Worldwide COVID-19 {metric} Cases"
    )


    fig = px.choropleth(

        df,

        locations="Country/Region",

        locationmode="country names",

        color=metric,

        hover_name="Country/Region",

        hover_data={
            "Confirmed": True,
            "Active": True,
            "Recovered": True,
            "Deaths": True
        },

        color_continuous_scale="Reds",

        title=f"Worldwide COVID-19 {metric} Cases"

    )


    fig.update_layout(

        title_font=dict(
            size=22,
            family="Arial Black"
        ),

        geo=dict(
            showframe=False,
            showcoastlines=True
        ),

        height=600

    )


    st.plotly_chart(
        fig,
        use_container_width=True
    )
    import json

    with open("india_state.geojson", "r", encoding="utf-8") as f:
        india_states = json.load(f)

    fig = px.choropleth(
        data_frame=df4,                 # ✅ DataFrame
        geojson=india_states,
        locations="States",             # Ya "State/UTs" agar wahi column hai
        featureidkey="properties.NAME_1",
        color="Total Cases",
        hover_name="States",            # Ya "State/UTs"
        hover_data=["Active", "Discharged", "Deaths"],
        color_continuous_scale="Reds"
    )

    fig.update_geos(
        fitbounds="locations",
        visible=False
    )

    st.plotly_chart(fig, use_container_width=True)
 # ================= TIME ANALYSIS =================

elif menu == "Time Analysis":
    st.title("⏳ COVID-19 Time Analysis")

    # ================= COPY DATASET =================
    time_df = df3.copy()

    # Convert Date column
    time_df["Date"] = pd.to_datetime(time_df["Date"])

    # Sort by Date
    time_df = time_df.sort_values("Date")

    # ================= DATE RANGE =================
    st.subheader("📅 Select Date Range")

    from datetime import timedelta

    min_date = time_df["Date"].min()
    max_date = time_df["Date"].max()

    # Default = Last 30 Days
    default_start = max(min_date, max_date - timedelta(days=30))

    selected_date = st.slider(
        "Choose Date Range",
        min_value=min_date.to_pydatetime(),
        max_value=max_date.to_pydatetime(),
        value=(
            default_start.to_pydatetime(),
            max_date.to_pydatetime()
        ),
        format="DD/MM/YYYY"
    )

    # Filter Data
    filtered_df = time_df[
        (time_df["Date"] >= pd.to_datetime(selected_date[0])) &
        (time_df["Date"] <= pd.to_datetime(selected_date[1]))
    ]

    st.divider()

    # ================= CHART STYLE =================

    def time_chart_style(fig):

        fig.update_layout(
            title_font=dict(size=22, family="Arial Black"),
            xaxis_title_font=dict(size=16, family="Arial Black"),
            yaxis_title_font=dict(size=16, family="Arial Black"),
            template="plotly_white",
            hovermode="x unified",
            height=550,
            legend_title=""
        )

        st.plotly_chart(fig, use_container_width=True)

    # ================= LINE CHART =================

    st.subheader("📈 Daily COVID Cases Trend")

    fig1 = px.line(
        filtered_df,
        x="Date",
        y=["New cases", "New deaths", "New Recovered"],
        markers=True,
        title="Daily New Cases, Deaths & Recovery"
    )

    time_chart_style(fig1)

    st.divider()

    # ================= AREA CHART =================

    st.subheader("🌊 Confirmed vs Active Cases")

    fig2 = px.area(
        filtered_df,
        x="Date",
        y=["Confirmed", "Active"],
        title="Confirmed vs Active Cases"
    )

    time_chart_style(fig2)

    st.divider()

    # ================= BAR CHART =================

    st.subheader("📊 Daily New Cases")

    fig3 = px.bar(
        filtered_df,
        x="Date",
        y="New cases",
        title="Daily New COVID Cases",
        color="New cases",
        color_continuous_scale="Blues"
    )

    time_chart_style(fig3)

    st.divider()

    # ================= DEATH VS RECOVERY =================

    st.subheader("💀 Deaths vs 💚 Recovery")

    fig4 = px.line(
        filtered_df,
        x="Date",
        y=["New deaths", "New Recovered"],
        markers=True,
        title="Deaths vs Recovery"
    )

    time_chart_style(fig4)

    st.divider()

    # ================= DATA TABLE =================

    st.subheader("📋 Filtered Data")

    st.dataframe(filtered_df, use_container_width=True)



    # Copy dataset

    time_df = df3.copy()


    # Convert Date

    time_df["Date"] = pd.to_datetime(
        time_df["Date"]
    )


    
    #=========INsights===================== 
elif menu == "Insights":
    st.title("💡 COVID-19 Insights")


    # ================= OVERALL SUMMARY =================

    st.markdown("""
    <style>

    /* Metric Card Design */
    div[data-testid="stMetric"] {
        background-color: #FED7BF;
        border: 3px solid #E4AFB0;
        padding: 20px;
        border-radius: 20px;
        box-shadow: 0px 5px 15px rgba(154,119,135,0.25);
        transition: 0.3s;
    }

    /* Hover Animation */
    div[data-testid="stMetric"]:hover {
        transform: translateY(-8px);
        box-shadow: 0px 10px 25px rgba(154,119,135,0.45);
    }


    /* Metric Label */
    div[data-testid="stMetricLabel"] {
        color: #9A7787;
        font-size: 18px;
        font-weight: bold;
    }


    /* Metric Value */
    div[data-testid="stMetricValue"] {
        color: #9A7787;
        font-size: 32px;
        font-weight: 800;
    }


    /* Divider */
    hr {
        border: 1px solid #E4AFBO;
    }

    </style>
    """, unsafe_allow_html=True)
    
    
    st.subheader("📌 Overall COVID-19 Summary")

    total_confirmed = df["Confirmed"].sum()
    total_active = df["Active"].sum()
    total_recovered = df["Recovered"].sum()
    total_deaths = df["Deaths"].sum()


    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "🦠 Total Cases",
            f"{total_confirmed:,}"
        )


    with col2:
        st.metric(
            "⚡ Active Cases",
            f"{total_active:,}"
        )


    with col3:
        st.metric(
            "😊 Recovered",
            f"{total_recovered:,}"
        )


    with col4:
        st.metric(
            "☠ Deaths",
            f"{total_deaths:,}"
        )



    st.divider()



    # ================= RATES =================


    st.subheader("📊 Recovery & Death Rate")


    recovery_rate = (
        total_recovered / total_confirmed * 100
    )

    death_rate = (
        total_deaths / total_confirmed * 100
    )


    col1, col2 = st.columns(2)


    with col1:

        st.success(
            f"😊 Recovery Rate : {recovery_rate:.2f}%"
        )


    with col2:

        st.error(
            f"☠ Death Rate : {death_rate:.2f}%"
        )



    st.divider()



    # ================= TOP COUNTRIES =================


    st.subheader("🌍 Top 5 Most Affected Countries")


    top_country = (
        df.groupby("Country/Region")["Confirmed"]
        .sum()
        .sort_values(ascending=False)
        .head(5)
    )


    # Bar Chart with Theme
    fig = px.bar(
        top_country.reset_index(),
        x="Country/Region",
        y="Confirmed",
        title="Top 5 Countries Confirmed Cases",
        color="Confirmed",
        color_continuous_scale=[
            "#FED7BF",
            "#E4AFB0",
            "#9A7787"
        ]
    )


    # Apply previous chart style
    st.plotly_chart(
        (fig),
        use_container_width=True
    )


# Country Details
    for country, cases in top_country.items():

        st.write(
            f"🔹 **{country}** reported **{cases:,}** confirmed cases"
        )


    st.divider()

# ================= INDIA STATE INSIGHTS =================


    st.subheader("🇮🇳 Top 5 Affected Indian States")


    top_states = (
        df4.sort_values(
            "Total Cases",
            ascending=False
        )
        .head(5)
    )


    fig = px.bar(
        top_states,
        x="States",
        y="Total Cases",
        color="Total Cases",
        title="Top 5 States by COVID Cases",
        color_continuous_scale="Reds"
    )


    st.plotly_chart(
        fig,
        use_container_width=True
    )



    st.divider()



    # ================= AUTOMATIC INSIGHTS =================


    st.subheader("🧠 Key Findings")


    max_country = (
        top_country.idxmax()
    )


    max_state = (
        top_states.iloc[0]["States"]
    )


    st.info(
        f"""
        🌍 The country with highest confirmed cases is **{max_country}**.

        🇮🇳 In India, **{max_state}** recorded the highest number of cases.

        📈 Overall recovery rate is **{recovery_rate:.2f}%**.

        ⚠️ Overall death rate is **{death_rate:.2f}%**.
        """
    )