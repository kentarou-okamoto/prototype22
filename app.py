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
                 　　　現金及び預金　　98,765　　43,210
                 　　　売掛金　　　　　12,345　　67,890
                 """




   # テキストエリア
   with st.form("my_form", clear_on_submit=False):
        text_area = st.text_area('Text Area', sample_text , height=200)
        col1, col2, col3 = st.columns(3)
        unit = col1.radio("単位", ('百万円', '千円'), index=0, horizontal=True)
        vle_clm = col2.radio("取得する数字列", ('真ん中列', '右列''), index=1, horizontal=True)
        oo = st.checkbox("'1列のみ[削除しない]")
        submitted = col3.form_submit_button("文字列を変換")
     
   if submitted:
      with st.spinner('processiong...'):
           time.sleep(3)
           #st.write( unit )
           #st.write(f"{vle_clm  }")
           txt=unicodedata.normalize('NFKC', text_area ) #UNICODE変換：全角を半角に
           s1 =txt.replace(',','')  #数字のカンマを除去
           s1= re.sub(r'※\d+', '', s1) #注釈マークをトル
           #st.write(s1)
           lst =s1.splitlines()  
           lst1=[fn_hoge(i) for i in lst]  #上記リスト(行単位)で１行ずつ中の項目をリスト化


           y=lst1[0]
           print(y)


           #上記リスト[lst1]をデータフレームオブジェクトに変換
           df = pd.DataFrame( lst1)
           x = df.shape[1]

           #列リストの設定
           if vle_clm =='1列のみ[削除しない]' and x==2:
              clist=['f1', 'f2']
           else:
              clist=['f1', 'f2', 'f3']


           df.columns =clist  

           #列の削除
           if oo:
              time.sleep(1)
              if x==3:
                 del df['f2']
                 st.warning('1列のみを選択したのに数字列が２列あり!⇒右列を取得します')
           else:
              if vle_clm =='右列':
                 del df['f2']
              else
                 del df['f3'] 
                 
           #st.table(df)
              
           df.columns = ['f1', 'f_vle' ]
           df = df.dropna(subset=['f_vle'], axis=0)  #f_vle列の値がNoneの行(e.g.文字列Aetc...)を削除
           df = df.reset_index(drop=True)
           df.index = df.index + 1
      
           #数字列の整形:ダーシ/△/カッコ
           df['f_vle'] = df['f_vle'].replace('-', '')
           df['f_vle'] = df['f_vle'].replace('△', '-', regex=True)
           #df['f_vle'] = df['f_vle'].replace('(', '-')
           #df['f_vle'] = df['f_vle'].replace(')', '')
           
           #科目列の整形:1株/1年etc...
           df['f1'] = df['f1'].replace('1年', '１年', regex=True)
           df['f1'] = df['f1'].replace('1株', '１株', regex=True)
           df['f1'] = df['f1'].replace('\(', '（', regex=True)
           df['f1'] = df['f1'].replace('\)', '）', regex=True)
           
           
           #千円の場合100の単位で切り捨て
           if unit =='千円':df['f_vle'] = df['f_vle'].astype('int') // 1000
           
           st.table(df)

           col4 , col5 = st.columns(2)
           col4.write("勘定科目群")
           col4.dataframe(df["f1"], width=400,hide_index=False)
           col5.write("項目数値群")
           col5.dataframe(df["f_vle"],  width=200, hide_index=False)
           
           st.success('変換成功!')


        
if __name__ == '__main__':
    main()
    