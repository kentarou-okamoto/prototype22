import re
import time
import streamlit as st
import unicodedata
import pandas as pd

def hoge(txt):
    st.write(len(txt))


    
def main():
   
   st.header('入力フォーム')

   #残骸
   #text_input = st.text_input('Input', 'Input some text here.')
   #placeholder = 

   sample_text = """資産の部
                 　　流動資産
                 　　　　現金及び預金　　　98,765　　　43,210
                 　　　　売掛金　　　　　　12,345　　　67,890
                 """

   # テキストエリア
   with st.form("my_form", clear_on_submit=False):
        text_area = st.text_area('Text Area', sample_text , height=200)
        submitted = st.form_submit_button("文字列を変換")
     
   if submitted:
      with st.spinner('processiong...'):
           time.sleep(3)
           txt=unicodedata.normalize('NFKC', txt) #UNICODE変換：全角を半角に
           s1 =txt.replace(',','')  #数字のカンマを除去
           st.write(s1)

        
if __name__ == '__main__':
    main()
    