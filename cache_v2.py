"""
This file monkey-patches streamlit with new functions for st.cache v2. Just import it 
into your app and you can use the new functions!
"""

import streamlit as st
import json
import os

from user_id_component import st_user_id


global_store = {}
config = {"initialized": False}


def _global_state(**kwargs):
    # if hasattr(st, "_first_run_done"):
    #     print("First run already done -> not setting global state")
    # else:
    #     print("First run -> setting global state")
    #     st._global_state = {}
    if not config["initialized"]:
        global_store.update(kwargs)
        config["initialized"] = True
    # st._first_run_done = True
    return global_store


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


def _database():
    return JSONDatabase("database.json")


user_store = {}


def _user_state(**kwargs):

    # TODO: Do we need to set `key` here? Maybe if this is called multiple times?
    user_id = st_user_id()
    print("User ID:", user_id)

    if user_id not in user_store:
        print("New user")
        user_store[user_id] = kwargs.copy()

    return user_store[user_id]


st.global_state = _global_state
st.user_state = _user_state
st.database = _database
