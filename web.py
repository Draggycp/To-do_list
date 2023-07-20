import streamlit as st
from modules import functions


todos = functions.get_todos()

def add_todo():
    todo = st.session_state["new_todo"]+"\n"
    todos.append(todo)
    functions.write_todos(todos)

todos = functions.get_todos()
st.title("My Todo App")
st.subheader("This is my to-do app for learning python")
st.write("This app is to increase you productivity")
st.write("To complete/delete a todo, click on the left of it")

for index,todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st._rerun()


st.text_input(label="",placeholder="Enter a new todo",
              on_change=add_todo, key='new_todo')
