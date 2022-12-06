import streamlit as st
import functions

todos = functions.get_todos()


def add_todo():
    new_todo = st.session_state["new_todo"] + "\n"
    todos.append(new_todo)
    functions.write_todos(todos)


st.title("My Todo App")
st.subheader("This is my todo app")
st.write("This app is to increase your productivity")


for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]  # This line of code helps to keep updating the session_state object
        # fyi session_state object is a dictionary
        st.experimental_rerun()  # experimental_rerun function reruns the whole code gain
        # to be clear from the very beginning "import streamlit as st" not the for loop.


st.text_input("", placeholder="Add new todo....",
              on_change=add_todo, key="new_todo")

# st.session_state
# print(st.session_state)

