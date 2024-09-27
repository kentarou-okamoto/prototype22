import re
import time
import unicodedata
import streamlit as st
import pandas as pd

def hoge(txt):
    st.write(len(txt))

def fn_hoge(i):
   x = re.split(" +", i) #半角スペースで分割
   if x[0]=='': x.pop(0)   # 先頭のスペース群 ''を除去
   return x
    
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
           txt=unicodedata.normalize('NFKC', text_area ) #UNICODE変換：全角を半角に
           s1 =txt.replace(',','')  #数字のカンマを除去
           #st.write(s1)
           lst =s1.splitlines()  
           lst1=[fn_hoge(i) for i in lst]  #上記リスト(行単位)で１行ずつ中の項目をリスト化

           df = pd.DataFrame( lst1
                            , columns=['f1', 'f2', 'f3'])  #上記リストをデータフレームオブジェクトに変換
           df = df.dropna(subset=['f3'], axis=0)  #一番右の３列目の値がNoneの行(e.g.文字列Aetc...)を削除
           del df['f2'] #２列目（前年度の数字の列）を削除
           st.table(df)

           col1, col2 = st.columns(2)
           df_left , df_right = df["f1"], df["f3"]
           
           col1 = st.write(df_left )
           col2 = st.write(df_right )


        
if __name__ == '__main__':
    main()
    