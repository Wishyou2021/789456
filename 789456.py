__author__="teacher"
import random
import streamlit as st
confirm_input = st.button('確認產生答案')
if confirm_input:
  a=random.randint(2,99)
  st.session_state.a = a
  
start,end=1,100
b=st.number_input("請輸入1到100之間的整數:")
confirm_input2 = st.button('輸入確認')
if confirm_input2:
  if b==a:
    st.write("恭喜你中獎了")
  elif b>a:
    if b>=end:
      st.write("輸入不合法,請重新輸入:")
    else:
      end=b
  else:
    if b<=start:
      st.write("輸入不合法,請重新輸入:")
    else:
      start=b
