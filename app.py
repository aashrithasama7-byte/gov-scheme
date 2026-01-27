import streamlit as st
import pandas as pd

# 1. Title of the Chatbot
st.title("🇮🇳 Government Scheme Bot")

# 2. Load the Data
try:
    df = pd.read_csv("schemes.csv")
    st.success("✅ Database Loaded!")
except FileNotFoundError:
    st.error("❌ Error: 'schemes.csv' not found. Please check your GitHub files.")

# 3. Search Feature
st.subheader("Search for a Scheme")
query = st.text_input("Enter a category (e.g., Health, Education, Agriculture):")

if query:
    # Search the 'Category' column for what the user typed
    results = df[df['Category'].str.contains(query, case=False, na=False)]
    
    if not results.empty:
        st.write(f"### Found {len(results)} schemes for you:")
        
        # --- THIS PART MAKES THE LINK CLICKABLE ---
        st.dataframe(
            results,
            column_config={
                "Official Link": st.column_config.LinkColumn(
                    "Official Link",
                    help="Click the link to go to the official website",
                    validate="^https?://",
                    display_text="Open Official Site 🔗" # This makes it look neat
                )
            },
            hide_index=True, # This removes the row numbers for a cleaner look
        )
        # ------------------------------------------
    else:
        st.warning(f"No schemes found for '{query}'. Try searching for 'Health' or 'Education'.")


