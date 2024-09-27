import streamlit as st

st.title("入力フォーム")


# テキスト入力ボックス
#text_input = st.text_input('Input', 'Input some text here.')
# テキストエリア
text_area = st.text_area('Text Area', 'Input some text here.')

import time

# ボタンを押したら3秒間出力を待つ
if st.button('start'):
    with st.spinner('processiong...'):
        time.sleep(3)
        st.write('押したなぁ～')
        st.write('end!')