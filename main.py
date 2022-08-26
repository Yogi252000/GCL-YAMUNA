import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st
from plotly.subplots import make_subplots
from streamlit_option_menu import option_menu


st.set_page_config(page_title='GCL Yamuna',layout="wide",page_icon='🚢')
st.header("FLUYT VESSEL")
hide_st_style = """
         <style>
         footer {visibility : hidden;}
         </style>
         """

st.markdown(hide_st_style,unsafe_allow_html=True)
st.subheader("GCL YAMUNA VOYAGE PERFORMANCE")

selected = option_menu(
    menu_title = None,
    options=["Laden", "Ballast","Laden-Speed & Con","Ballast-Speed & con","Laden-Slip(%)","Ballast-Slip(%)","FW Production"],

    icons=["ship","ship","ship","ship","ship","ship","ship"],
    orientation="horizontal",
    default_index=0,
    styles={
        "container": {"padding":"0!important","background-color":"#ADD8E6"},
        "icon":{"color":"orange","font-size":"15px","font-style":"Arial"},
        "nav-link": {
            "font-size":"12px",
            "text-align":"justify",
            "margin": "0px",
            "--hover-color":"eee",

        },
        "nav-link-selected":{"background-color":"#00008B"},
    },
)


if selected == "Laden":
    df1 = pd.read_csv("data1.csv")
    df2 = pd.read_csv('data2.csv')
    df3 = pd.read_csv('data3.csv')
    df4 = pd.read_csv('data4.csv')
    df5 = pd.read_csv('data55.csv')


    fig = make_subplots(specs=[[{"secondary_y": True}]])

    fig.add_trace(
        go.Scatter(x=df1['Voyage No.'], y=df1['Instructed Speed'], name="Instructed Speed"),
        secondary_y=False,
    )
    fig.add_trace(
        go.Scatter(x=df2['Voyage No.'], y=df2['Avg Speed (Voyage)'], name="Avg Speed (Voyage)"),
        secondary_y=True,
    )
    fig.add_trace(
        go.Scatter(x=df3['Voyage No.'], y=df3['Avg Speed (in Good weather)'], name="Avg Speed (in Good weather)"),
        secondary_y=True,
    )

    fig.add_trace(
        go.Scatter(x=df4['Voyage No.'], y=df4['Avg FO cons / day'], name="Avg FO cons / day "),
        secondary_y=True,
    )

    fig.add_trace(
        go.Scatter(x=df5['Voyage No.'], y=df5['CP Fuel cons limit'], name="CP Fuel cons limit"),
        secondary_y=True,
    )

    fig.update_layout(
        title_text="LADEN CONDITION ",
        autosize=False,
        width=1000,
        height=600,

    )

    fig.update_xaxes(title_text="Voyage Number")

    fig.update_yaxes(
        title_text="Avg Speed (Voyage),Avg Speed (in Good weather),Avg FO cons/day,CP Fuel cons limit,Instructed Speed",)
    fig.update_yaxes(range=[0, 50])
    fig.update_yaxes(visible=True,showticklabels=True,title_font=dict(size=12))
    st.plotly_chart(fig, use_container_width=True)
    st.write('Laden data')
    first = pd.read_csv("Voyage.csv")
    st.write(first)

if selected == "Ballast":
    df20 = pd.read_csv("data16.csv")
    df21 = pd.read_csv('data17.csv')
    df31 = pd.read_csv('data18.csv')
    df41 = pd.read_csv('data19.csv')
    df51 = pd.read_csv('data20.csv')

    fig11 = make_subplots(specs=[[{"secondary_y": True}]])

    fig11.add_trace(
        go.Scatter(x=df20['Voyage No.'], y=df20['Instructed Speed'], name="Instructed Speed"),
        secondary_y=False,
    )
    fig11.add_trace(
        go.Scatter(x=df21['Voyage No.'], y=df21['Avg Speed (Voyage)'], name="Avg Speed (Voyage)"),
        secondary_y=True,
    )
    fig11.add_trace(
        go.Scatter(x=df31['Voyage No.'], y=df31['Avg Speed (in Good weather)'], name="Avg Speed (in Good weather)"),
        secondary_y=True,
    )

    fig11.add_trace(
        go.Scatter(x=df41['Voyage No.'], y=df41['Avg FO cons / day'], name="Avg FO cons / day "),
        secondary_y=True,
    )

    fig11.add_trace(
        go.Scatter(x=df51['Voyage No.'], y=df51['CP Fuel cons limit'], name="CP Fuel cons limit"),
        secondary_y=True,
    )

    fig11.update_layout(
        title_text="BALLAST CONDITION ",
        autosize=False,
        width=1000,
        height=600

    )

    fig11.update_xaxes(title_text="Voyage Number")
    fig11.update_yaxes(
        title_text="Avg Speed (Voyage),Avg Speed (in Good weather),Avg FO cons/day,CP Fuel cons limit,Instructed Speed")
    fig11.update_yaxes(range=[0, 50])
    fig11.update_yaxes(visible=True, showticklabels=True, title_font=dict(size=12))
    st.plotly_chart(fig11, use_container_width=True)
    st.write('Ballast data')
    second = pd.read_csv("voyage 1.csv")
    st.write(second)

if selected == "Laden-Speed & Con":


    df7 = pd.read_csv('data7.csv')
    df8 = pd.read_csv('data8.csv')
    df9 = pd.read_csv('data9.csv')
    df10 = pd.read_csv('data10.csv')

    fig2 = make_subplots(specs=[[{"secondary_y": True}]])

    fig2.add_trace(
        go.Scatter(x=df7['UTC Date & Time'], y=df7['Instructed Speed'], name="Instructed Speed"),
        secondary_y=False,
    )
    fig2.add_trace(
        go.Scatter(x=df8['UTC Date & Time'], y=df8['CP Fuel Cons. Limit'], name="CP Fuel Cons. Limit"),
        secondary_y=True,
    )
    fig2.add_trace(
        go.Scatter(x=df9['UTC Date & Time'], y=df9['Speed (KTS)'], name="Speed (KTS)"),
        secondary_y=True,
    )

    fig2.add_trace(
        go.Scatter(x=df10['UTC Date & Time'], y=df10['TOTAL FO Consumption / 24 hrs'],
                   name="TOTAL FO Consumption / 24 hrs"),
        secondary_y=True,
    )

    fig2.update_layout(
        title_text="LADEN CONDITION - SPEED AND CONSUMPTION",
        autosize=False,
        width=1000,
        height=600

    )
    fig2.update_xaxes(
        rangeslider_visible=False,
        rangeselector=dict(
            buttons=list([
                dict(count=1, label="1m ", step="month", stepmode="backward"),
                dict(count=6, label="6m ", step="month", stepmode="backward"),
                dict(count=1, label="1Y", step="year", stepmode="backward"),
                dict(step="all")
            ])
        )
    )
    fig2.update_xaxes(title_text="UTC Date & Time")
    fig2.update_layout(legend=dict(yanchor="top", y=0.9, xanchor="left", x=0.7))
    fig2.update_yaxes(title_text="Instructed Speed,CP Fuel Cons. Limit,Speed (KTS),TOTAL FO Consumption / 24 hrs")
    fig2.update_yaxes(range=[0, 60])
    fig2.update_yaxes(visible=True, showticklabels=True, title_font=dict(size=12))
    st.plotly_chart(fig2, use_container_width=True)
    data = pd.read_csv("laden.csv")
    st.write(data)


if selected == "Ballast-Speed & con":

    df11 = pd.read_csv('data11.csv')
    df12 = pd.read_csv('data12.csv')
    df13 = pd.read_csv('data13.csv')
    df14 = pd.read_csv('data14.csv')

    fig1 = make_subplots(specs=[[{"secondary_y": True}]])

    fig1.add_trace(
        go.Scatter(x=df11['UTC Date & Time'], y=df11['Instructed Speed'], name="Instructed Speed"),
        secondary_y=False,
    )
    fig1.add_trace(
        go.Scatter(x=df12['UTC Date & Time'], y=df12['CP Fuel Cons. limit'], name="CP Fuel Cons. Limit"),
        secondary_y=True,
    )
    fig1.add_trace(
        go.Scatter(x=df13['UTC Date & Time'], y=df13['Speed (KTS)'], name="Speed (KTS)"),
        secondary_y=True,
    )

    fig1.add_trace(
        go.Scatter(x=df14['UTC Date & Time'], y=df14['TOTAL FO Consumption / 24 hrs'],name="TOTAL FO Consumption / 24 hrs"),
        secondary_y=True,
    )

    fig1.update_layout(
        title_text="BALLAST CONDITION - SPEED AND CONSUMPTION",
        autosize=False,
        width=1000,
        height=600
    )
    fig1.update_xaxes(
        rangeslider_visible=False,
        rangeselector=dict(
            buttons=list([
                dict(count=1, label="1m ", step="month", stepmode="backward"),
                dict(count=6, label="6m ", step="month", stepmode="backward"),
                dict(count=1, label="1Y", step="year", stepmode="backward"),
                dict(step="all")
            ])
        )
    )
    fig1.update_xaxes(title_text="UTC Date & Time")
    fig1.update_layout(legend=dict(yanchor="top", y=0.9, xanchor="left", x=0.7))
    fig1.update_yaxes(title_text="Instructed Speed,CP Fuel Cons. Limit,Speed (KTS),TOTAL FO Consumption / 24 hrs")
    fig1.update_yaxes(range=[0, 60])
    fig1.update_yaxes(visible=True, showticklabels=True, title_font=dict(size=12))
    st.plotly_chart(fig1, use_container_width=True)
    data = pd.read_csv("ballast.csv")
    st.write(data)


if selected == "Laden-Slip(%)":
    df = pd.read_csv('data5.csv')
    df['UTC Date & Time'] = pd.to_datetime(df['UTC Date & Time'], format='%Y-%m-%d')
    fig3 = px.scatter(df, x='UTC Date & Time', y='Slip (%)', width=1000, height=600,trendline="ols", title='SLIP(%) - Laden Condition')

    fig3.update_yaxes(range=[0, 50])
    fig3.update_yaxes(visible=True, showticklabels=True, title_font=dict(size=12))
    st.plotly_chart(fig3, use_container_width=True)
    df = pd.read_csv('data5.csv')
    st.write(df)



if selected == "Ballast-Slip(%)":
    df = pd.read_csv('data6.csv')
    df['UTC Date & Time'] = pd.to_datetime(df['UTC Date & Time'], format='%Y-%m-%d')
    fig4 = px.scatter(df, x='UTC Date & Time', y='Slip (%)', width=1000, height=600,trendline='ols', title='SLIP(%) - Ballast Condition')

    fig4.update_yaxes(range=[0, 50])
    fig4.update_yaxes(visible=True, showticklabels=True, title_font=dict(size=12))
    st.plotly_chart(fig4, use_container_width=True)
    df = pd.read_csv('data6.csv')
    st.write(df)

if selected == "FW Production":
    df = pd.read_csv('data15.csv')
    df['UTC Date & Time'] = pd.to_datetime(df['UTC Date & Time'], format='%Y-%m-%d')

    fig5 = px.line(df, x='UTC Date & Time', y='FW production (MT) /24', width=2000,height=600,
                   title='Fresh Water Production - Laden Condition')

    fig5.update_yaxes(range=[0, 50])
    fig5.update_yaxes(visible=True, showticklabels=True, title_font=dict(size=12))
    st.plotly_chart(fig5, use_container_width=True)
    df = pd.read_csv('data15.csv')
    st.write(df)


