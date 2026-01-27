import streamlit as st
import pandas as pd
import os

# --- 1. LANGUAGE DICTIONARY ---
# This stores all the text for the app in two languages
languages = {
    "English": {
        "title": "🇮🇳 Government Scheme Bot",
        "search_label": "Search for a category (e.g., Health, Education, Agriculture):",
        "results_msg": "Matching Schemes Found:",
        "no_results": "No schemes found for this category.",
        "db_success": "Database Loaded!",
        "sidebar_title": "👨‍💻 Project Details",
        "apply_btn": "Open Official Site 🔗"
    },
    "Hindi": {
        "title": "🇮🇳 सरकारी योजना बॉट",
        "search_label": "श्रेणी खोजें (जैसे: स्वास्थ्य, शिक्षा, कृषि):",
        "results_msg": "मिलती-जुलती योजनाएं:",
        "no_results": "इस श्रेणी के लिए कोई योजना नहीं मिली।",
        "db_success": "डेटाबेस लोड हो गया!",
        "sidebar_title": "👨‍💻 प्रोजेक्ट विवरण",
        "apply_btn": "आधिकारिक साइट खोलें 🔗"
    }
}

# --- 2. SIDEBAR SETUP ---
with st.sidebar:
    # Language Selector
    sel_lang = st.selectbox("🌐 Choose Language / भाषा चुनें", ["English", "Hindi"])
    ln = languages[sel_lang] # Shortcut to current language dictionary
    
    st.write("---")
    st.header(ln["sidebar_title"])
    st.write("**Student Name:** [Your Name]")
    st.write("**Roll No:** [Your Roll Number]")
    st.write("**College:** [Your College Name]")

# --- 3. MAIN APP INTERFACE ---
st.title(ln["title"])

# Load Data logic
try:
    # This helps find the file correctly on both your PC and GitHub
    base_path = os.path.dirname(__file__)
    file_path = os.path.join(base_path, "schemes.csv")
    df = pd.read_csv(file_path)
    # We only show the success message in the sidebar to keep it clean
    st.sidebar.success(ln["db_success"])
except Exception as e:
    st.error("❌ Error: 'schemes.csv' not found. Please upload it to your GitHub folder.")
    st.stop() # Stops the app from running further if file is missing

# --- 4. SEARCH LOGIC ---
query = st.text_input(ln["search_label"])

if query:
    # Look for matches in the 'Category' column of your CSV
    # Make sure your CSV has a column named "Category"
    results = df[df['Category'].str.contains(query, case=False, na=False)]
    
    if not results.empty:
        st.write(f"### {ln['results_msg']}")
        
        # Display the table with Clickable Links
        # Make sure your CSV has a column named "Official Link"
        st.dataframe(
            results,
            column_config={
                "Official Link": st.column_config.LinkColumn(
                    "Official Link",
                    display_text=ln["apply_btn"]
                )
            },
            hide_index=True,
            use_container_width=True
        )
    else:
        st.warning(ln["no_results"])


