import streamlit as st
import pandas as pd

# 1. Title of the Chatbot
st.title("🇮🇳 Government Scheme Bot")

# 2. Load the Data (Reading your Spreadsheet)
# We use try/except just in case the file name is wrong
try:
    df = pd.read_csv("schemes.csv")
    st.success("✅ Database Loaded!")
except FileNotFoundError:
    st.error("❌ Error: 'schemes.csv' not found in the folder.")

# 3. Simple Search Feature
st.subheader("Search for a Scheme")
query = st.text_input("Enter a category (e.g., Health, Education):")

if query:
    # This line looks for matches in your 'Category' column
    # .str.contains allows it to find partial words
    results = df[df['Category'].str.contains(query, case=False, na=False)]
    
    if not results.empty:
        st.write("Here is what I found:")
        # Show the results in a nice table
        st.dataframe(results)
    else:
        st.write("Sorry, I couldn't find any schemes in that category.")
