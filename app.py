import streamlit as st
from excuse import generate_excuse
import random
from duck import translate, serious_translate
import time

st.set_page_config(page_title="Simple but Brilliant!", page_icon="👍", layout="wide")
st.title("Simple but Brilliant!")

loading = ["Hacking the mainframe...", "Consulting the oracle...", "Summoning the AI spirits...", "Hacking NASA for data...", "Asking the AI gods for wisdom..."
        "Running on hamster power...", "Consulting the magic 8-ball...", "Asking the AI for a coffee break...", "Asking a monkey...", "Talking to god himself..."]

container = st.container(border=True)


with container:
    st.header("AI Excuse Generator 🎮")
    problem = st.text_input("Enter a problem:", placeholder="Why didn't you do your homework?")
    if st.button("Generate Excuse"):
        if not problem:
            st.warning("My brain is empty! Please enter a problem to generate an excuse.")
        # Placeholder for AI excuse generation logic
        else:
            with st.spinner(random.choice(loading)):
                excuse = generate_excuse(problem)
            st.write(excuse)

container = st.container(border=True)
with container:
    st.header("What-The-Duck Translator 🦆")
    sentence = st.text_input("Enter a sentence to translate into duck language:", placeholder="Hello, how are you?")
    if st.checkbox("Serious Mode (All quacks, no words)"):
        if st.button("Translate in Serious Mode 🦆"):
            with st.spinner(random.choice(loading)):
                time.sleep(0.9)
            with st.spinner("Talking to ducks..."):
                time.sleep(0.9)
            sentence = serious_translate(sentence)
            st.write(sentence)
    if st.button("Translate 🦆"):
        with st.spinner(random.choice(loading)):
            time.sleep(0.9)
        with st.spinner("Talking to ducks..."):
            time.sleep(0.9)
        sentence = translate(sentence)
        st.write(sentence)


        
container = st.container(border=True)
with container:
    st.header("Useless Robot Simulator 🤖")
    with open ("notes.txt", "r") as f:
        notes = f.read()
        # each line 
        notes = notes.split("\n")
    note = st.selectbox("Select a note to read:", notes)
    if st.button("Read Note"):
        with st.spinner(random.choice(loading)):
            time.sleep(0.9)
        st.write(note) 