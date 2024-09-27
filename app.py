import streamlit as st
import time


st.header('入力フォーム')

#text_input = st.text_input('Input', 'Input some text here.')

sample_text = """資産の部
　　流動資産
　　　　現金及び預金　　　98,765　　　43,210
　　　　売掛金　　　　　　12,345　　　67,890
"""

# テキストエリア
with st.form("my_form", clear_on_submit=False):
     text_area = st.text_area('Text Area', sample_text , height=500)
     submitted = st.form_submit_button("文字列を変換")
     
     
if submitted:
    with st.spinner('processiong...'):
        time.sleep(3)
        st.write(text_area)