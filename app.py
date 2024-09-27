import streamlit as st
import time


st.title("入力フォーム")


#text_input = st.text_input('Input', 'Input some text here.')


# テキストエリア
with st.form("my_form", clear_on_submit=False):
     text_area = st.text_area('Text Area', 'Input some text here.')
     submitted = st.form_submit_button("文字列を変換")
     
     
if submitted:
    with st.spinner('processiong...'):
        time.sleep(3)
        st.write(text_area)