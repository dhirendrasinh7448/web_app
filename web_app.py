import streamlit as st
import read_write_


todos = read_write_.read_todos()

def add_todo():
    new_todo = st.session_state["new_todo"] + "\n"
    todos.append(new_todo)
    read_write_.write_todos(todos)

st.title("Todo App")
st.subheader("Your Current Todos")
st.write("This app helps you become productive.")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        read_write_.write_todos(todos)
        del st.session_state[todo]
        st.rerun()
st.text_input(label="", placeholder="Enter a todo here...",
              on_change=add_todo, key="new_todo")

