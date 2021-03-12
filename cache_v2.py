import streamlit as st
import json
import os


def global_state(**kwargs):
    if hasattr(st, "_first_run_done"):
        print("First run already done -> not setting global state")
    else:
        print("First run -> setting global state")
        st._global_state = {}
        for k, v in kwargs.items():
            st._global_state[k] = v
        st._first_run_done = True
    return st._global_state


class JSONDatabase(dict):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if os.path.exists("database.json"):
            with open("database.json", "r") as f:
                saved_data = json.load(f)
                for k, v in saved_data.items():
                    self[k] = v
        else:
            self.save()

    def __setitem__(self, key, value):
        super().__setitem__(key, value)
        self.save()

    def clear(self):
        super().clear()
        self.save()

    def save(self):
        with open("database.json", "w") as f:
            json.dump(self, f)


def database():
    return JSONDatabase()


st.global_state = global_state
st.database = database
