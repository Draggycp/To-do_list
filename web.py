import streamlit as st
from modules import functions


todos = functions.get_todos()
st.title("My Todo App")
st.subheader("This is my to-do app for learning python")
st.write("This app is to increase you productivity")

for index,todo in enumerate(todos):
    st.checkbox(todo, key=index)

st.text_input(label="",placeholder="Enter a new todo")