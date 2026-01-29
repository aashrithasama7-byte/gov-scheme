import streamlit as st
import pandas as pd
import os

# --- 1. LANGUAGE DICTIONARY ---
# Added Telugu (తెలుగు) to the dictionary
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
    },
    "Telugu": {
        "title": "🇮🇳 ప్రభుత్వ పథకాల బాట్",
        "search_label": "వర్గాన్ని శోధించండి (ఉదా: ఆరోగ్యం, విద్య, వ్యవసాయం):",
        "results_msg": "సరిపోలే పథకాలు కనుగొనబడ్డాయి:",
        "no_results": "ఈ వర్గంలో ఎటువంటి పథకాలు కనుగొనబడలేదు.",
        "db_success": "డేటాబేస్ లోడ్ అయింది!",
        "sidebar_title": "👨‍💻 ప్రాజెక్ట్ వివరాలు",
        "apply_btn": "అధికారిక సైట్‌ని తెరవండి 🔗"
    }
}

# --- 2. SIDEBAR SETUP ---
with st.sidebar:
    # Updated Language Selector for 3 languages
    sel_lang = st.selectbox("🌐 Choose Language / భాషను ఎంచుకోండి", ["English", "Hindi", "Telugu"])
    ln = languages[sel_lang]
    
    st.write("---")
    st.header(ln["sidebar_title"])
    st.write("**Student Name:** [Your Name]")
    st.write("**Roll No:** [Your Roll Number]")
    st.write("**College:** [Your College Name]")

# --- 3. MAIN APP INTERFACE ---
st.title(ln["title"])

# Load Data logic
try:
    base_path = os.path.dirname(__file__)
    file_path = os.path.join(base_path, "schemes.csv")
    df = pd.read_csv(file_path)
    # Cleaning column names just in case there are hidden spaces
    df.columns = df.columns.str.strip()
    st.sidebar.success(ln["db_success"])
except Exception as e:
    st.error("❌ Error: 'schemes.csv' not found. Please upload it to your GitHub folder.")
    st.stop()

# --- 4. SEARCH & FILTER LOGIC ---
query = st.text_input(ln["search_label"])

# Filter data based on the language selected in sidebar
# This looks at the 'Language' column in your CSV
lang_filtered_df = df[df['Language'] == sel_lang]

if query:
    # Search within the filtered language results
    results = lang_filtered_df[lang_filtered_df['Category'].str.contains(query, case=False, na=False)]
    
    if not results.empty:
        st.write(f"### {ln['results_msg']}")
        
        # Display table (Hiding the 'Language' column for a cleaner look)
        st.dataframe(
            results.drop(columns=['Language']) if 'Language' in results.columns else results,
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
