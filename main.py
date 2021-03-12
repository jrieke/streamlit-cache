import numpy as np
import streamlit as st
from coolname import generate_slug

import cache_v2

"# Exploration of `st.cache` v2"

# --------------------------------------------------------------------------------------
"""
## 💻 Session state

This is a `dict` which is persistent only during the current browser session (i.e. until 
the tab is closed). 

See session state prototypes.
"""


# --------------------------------------------------------------------------------------
"""
## 👤 User state

This is a `dict` which is persistent across all sessions of the same user. 

A user can either be an authenticated user in S4T or we can set a browser cookie to 
identify unique users (this would require a custom component to set cookies).

**TODO**
"""


# --------------------------------------------------------------------------------------
"""
## 🌐 Global state

This is a `dict` which is persistent across all users and sessions (but it's wiped 
if you re-start streamlit). 

Initialize it with:
"""

with st.echo():
    global_state = st.global_state(a=123)

"Add a value at runtime with:"

with st.echo():
    global_state["b"] = 456

add_random = st.button("Add random value")
if add_random:
    global_state[generate_slug(2)] = np.random.randint(100)

clear = st.button("Clear")
if clear:
    global_state.clear()

"""
This is the current global state:
"""
st.write(global_state)


# --------------------------------------------------------------------------------------
"""
## 🛒 Database

This is a `dict`-like store (but contents must be JSON-serializable!) which is 
persistent across all users and session and even if streamlit is re-started.

Ideally, these values would be stored in S4A (and maybe in a file for local 
development?). Here we just fake it by storing everything in a local JSON file 
(`database.json`). 

Initialize with:
"""
with st.echo():
    db = st.database()

"Add a value at runtime with:"
with st.echo():
    db["a"] = 123

if st.button("Add random value to DB"):
    db[generate_slug(2)] = np.random.randint(100)

if st.button("Clear DB"):
    db.clear()

"""
This is the current database content:
"""
st.write(db)

"Restart streamlit to see that the values above are preserved 🎈 "