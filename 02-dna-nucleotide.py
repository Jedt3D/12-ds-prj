import pandas as pd
import streamlit as st
import altair as alt
from PIL import Image

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

"""
# 02 Nucleotide Count
"""
col1, col2, col3 = st.columns([4, 4, 4])
with col1:
    st.write('')
with col2:
    image = Image.open('imgs/dna-logo-white.png')
    st.image(image, use_column_width=True)
with col3:
    st.write('')

st.write("""
## DNA - Nucleotide Count

แอพนี้จะนับจำนวนและองค์ประกอบของนิวคลีโอไทด์ของ DNA 

***
""")

"""
## Input text box
"""
st.header('Enter DNA sequence')
seq_input = ">DNA Query 2\nGAACACGTGGAGGCAAACAGGAAGGTGAAGAAGAACTTATCCTATCAGGACGGAAGGTCCTGTGCTCGGG\nATCTTCCAGACGTCGCGACTCTAAATTGCCCCCTCTGAGGTCAAGGAACACAAGATGGTTTTGGAAATGC\nTGAACCCGATACATTATAACATCACCAGCATCGTGCCTGAAGCCATGCCTGCTGCCACCATGCCAGTCCT"

seq = st.text_area("Sequence input", seq_input, height=250)
seq = seq.splitlines()
seq = seq[1:]
seq = ''.join(seq)

st.write("""***""")
st.header('Input (DNA Query)')
seq

### DNA nucleotide count
st.subheader('1. แสดงผลแบบ dictionary')


def นับนิวคลีโอไทด์(seq):
    d = dict([
        ('A', seq.count('A')),
        ('T', seq.count('T')),
        ('G', seq.count('G')),
        ('C', seq.count('C')),
    ])
    return d


X = นับนิวคลีโอไทด์(seq)
X

st.subheader('2. แสดงผลแบบ text')
st.write('มี ', str(X['A']) + ' adenine (A)')
st.write('มี ', str(X['T']) + ' adenine (T)')
st.write('มี ', str(X['G']) + ' adenine (G)')
st.write('มี ', str(X['C']) + ' adenine (C)')

st.subheader('3. แสดงผล DataFrame')
df = pd.DataFrame.from_dict(X, orient='index')
df = df.rename({0: 'จำนวน'}, axis='columns')
df.reset_index(inplace=True)
df = df.rename(columns={'index': 'นิวคลีโอไทด์'})
st.write(df)

st.subheader('4. แสดง Bar Chart ใช้ Altair')
p = alt.Chart(df).mark_bar().encode(
    x='นิวคลีโอไทด์', y='จำนวน'
)
p = p.properties(
    width=alt.Step(80)
)
st.write(p)