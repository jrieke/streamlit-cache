import numpy as np
import streamlit as st
from coolname import generate_slug

import cache_v2

"# Exploration of `st.cache` v2"

# --------------------------------------------------------------------------------------
"""
## 📚 Cache / Memo function

We still want to have a decorator to cache long-running functions! 

This should look very similar to the existing `st.cache` but be simpler to use 
(especially reduce complexity around hashing). All use cases which bloat up the current
`st.cache` should be handled by the functions below.

**TODO. Could we just use [`functools.cache`](https://docs.python.org/3/library/functools.html#functools.cache) for this?**
"""

# --------------------------------------------------------------------------------------
"""
## 💻 Session state

- `dict`
- Persisted for the current session / browser tab
- Reset when opening a new tab

See existing session state prototypes.
"""


# --------------------------------------------------------------------------------------
"""
## 👤 User state

- `dict`
- Persisted for all sessions of a user (identified via browser cookie or S4T auth)
- Reset when opened from a new user / computer / browser

Initialize with:
"""

with st.echo():
    user_state = st.user_state(a=123)

"Add a value at runtime with:"

with st.echo():
    user_state["b"] = 456

if st.button("Add random value", key="add_user"):
    user_state[generate_slug(2)] = np.random.randint(100)

if st.button("Clear user state", key="clear_user"):
    user_state.clear()

"""
This is the current user state:
"""
st.write(user_state)


# --------------------------------------------------------------------------------------
"""
## 🌐 Global state

- `dict`
- Persisted across all sessions and users
- Reset when streamlit is re-started

Initialize with:
"""

with st.echo():
    global_state = st.global_state(a=123)

"Add a value at runtime with:"

with st.echo():
    global_state["b"] = 456

if st.button("Add random value", key="add_global"):
    global_state[generate_slug(2)] = np.random.randint(100)

if st.button("Clear", key="clear_global"):
    global_state.clear()

"""
This is the current global state:
"""
st.write(global_state)


# --------------------------------------------------------------------------------------
"""
## 🛒 Database

- `dict`-like store (objects need to be JSON-serializable)
- Persisted until eternity, across all users / sessions / restarts
- Reset manually

Data could be stored along with the app in S4A/S4T, locally in a file. In this prototype 
the data is simply put into a JSON-file (`database.json`). 

Initialize with:
"""
with st.echo():
    db = st.database()

"Add a value at runtime with:"
with st.echo():
    db["a"] = 123

if st.button("Add random value", key="add_db"):
    db[generate_slug(2)] = np.random.randint(100)

if st.button("Clear", key="clear_db"):
    db.clear()

"""
This is the current database content:
"""
st.write(db)
