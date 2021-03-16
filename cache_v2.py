"""
This file monkey-patches streamlit with new functions for st.cache v2. Just import it 
into your app and you can use the new functions!
"""

import streamlit as st
import json
import os

from user_id_component import st_user_id


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
    def __init__(self, filename):
        super().__init__()
        self.filename = filename
        if os.path.exists(self.filename):
            with open(self.filename, "r") as f:
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
        with open(self.filename, "w") as f:
            json.dump(self, f)


def database():
    return JSONDatabase("database.json")


st.global_state = global_state
st.database = database
