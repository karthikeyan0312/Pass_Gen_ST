from nltk import text
import streamlit as st
import random
def passwd():
    #passlen = int(input("enter the length of password"))
    s="abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
    p = "".join(random.sample(s,20))
    return p


st.title(" Password Generator")
st.markdown("***")
placeholder = st.empty()

input = placeholder.text("Click hit me button")
st.markdown("***")
col1, col2, col3 , col4, col5 = st.beta_columns(5)

with col1:
    pass
with col2:
    pass
with col4:
    pass
with col5:
    pass
with col3 :
    submit = st.button("Hit me")



if submit:
    test=placeholder.text(passwd())

