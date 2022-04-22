import yfinance as yf
import streamlit as st
import pandas as pd

st.markdown('''
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Chonburi&family=Noto+Sans+Thai:wght@300;400;600&family=Noto+Serif+Thai:wght@300;400;600&display=swap" rel="stylesheet">'''
            , unsafe_allow_html=True)
st.markdown('''
<style>
    h1 {
        font-family: 'Chonburi', cursive;
    }
    h2, h3 {
        font-family: 'Noto Sans Thai', sans-serif;
    }
    p, body {
        font-family: 'Noto Serif Thai', serif;
        font-weight: 300;
    }
    strong, em {
        font-family: 'Noto Sans Thai', sans-serif;
        font-weight: 400;
    }
    
</style>''', unsafe_allow_html=True)

st.write("""
# 01 ราคาหุ้นแบบง่าย ๆ

แสดง **ราคาหุ้นตอนปิดตลาด** และ ***ปริมาณการซื้อขาย***

***Tableau*** เป็นเครื่องมือที่จะช่วยให้คุณสามารถ***นำเสนอและแสดงผลวิเคราะห์ของ 
Data ได้อย่างมืออาชีพ*** 
ด้วยการทำให้การนำเสนอข้อมูลนั้นง่ายต่อการนำไปใช้และเป็นเครื่องมือที่ใช้งานง่าย ทำให้ทุกวันนี้ Tableau ได้กลายมาเป็นตัวเลือกอันดับต้นๆขององค์กรทั่วโลก 

Specifying the port number allows you to launch the app on a fixed port number 
each time you run your debug script.

Once you've updated your launch.json file, you need to navigate to the Run tab 
on the left gutter of the VS code app and tell it which Python config it should 
use to debug the app:

""")

tickerSymbol = 'GOOGL'
tickerData = yf.Ticker(tickerSymbol)
tickerDf = tickerData.history(period='1d', start='2010-5-31', end='2020-5-31')

st.write("""
### ราคาปิดตลาด""")
st.line_chart(tickerDf.Close)

st.write("""
### ปริมาณการซื้อขาย""")
st.line_chart(tickerDf.Volume)
