import streamlit as st
import datetime
import time
import json
import os

# --- CONFIGURATION ---
st.set_page_config(page_title="A Daily Blessing", page_icon="📖", layout="centered")

# --- FILE TRACKER (For "Once Per Day" rule) ---
TRACKER_FILE = "tracker.json"

def get_last_opened_date():
    """Reads the tracker file to see the last date the verse was opened."""
    if os.path.exists(TRACKER_FILE):
        try:
            with open(TRACKER_FILE, "r") as f:
                data = json.load(f)
                return data.get("last_opened")
        except:
            return None
    return None

def set_last_opened_date(date_str):
    """Saves today's date to the tracker file."""
    with open(TRACKER_FILE, "w") as f:
        json.dump({"last_opened": date_str}, f)

# --- REFINED CSS (Soft Pink Background) ---
st.markdown("""
    <style>
    /* Overall App Background changed to Soft Pink */
    .stApp {
        background-color: #FDF1F4; 
    }
    
    h1 {
        color: #4A403A !important;
        font-family: 'Georgia', serif;
        text-align: center;
        padding-top: 30px;
        margin-bottom: 20px;
    }

    /* Verse Box with Fade-in Animation */
    .verse-box {
        background-color: #FFFFFF;
        padding: 30px;
        border-radius: 12px;
        border-left: 6px solid #D4AF37;
        color: #333333;
        font-size: 22px;
        font-family: 'Georgia', serif;
        font-style: italic;
        box-shadow: 0 4px 12px rgba(0,0,0,0.08);
        margin-top: 30px;
        line-height: 1.6;
        text-align: center;
        /* The Animation */
        animation: fadeInReveal 1.5s ease-in-out; 
    }
    
    @keyframes fadeInReveal {
        0% { opacity: 0; transform: translateY(15px); }
        100% { opacity: 1; transform: translateY(0); }
    }
    
    .instruction-text {
        color: #8A7B6D;
        text-align: center;
        font-size: 18px;
        font-family: 'Georgia', serif;
        margin-top: 15px;
    }

    .come-back-text {
        color: #B8860B;
        text-align: center;
        font-size: 20px;
        font-family: 'Georgia', serif;
        font-weight: bold;
        margin-top: 30px;
        animation: fadeInReveal 1s ease-in-out;
    }

    div.stButton > button:first-child {
        background-color: #D4AF37;
        color: white;
        border-radius: 30px;
        border: none;
        padding: 10px 20px;
        font-family: 'Georgia', serif;
        font-size: 18px;
        font-weight: bold;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        transition: all 0.3s ease;
    }
    div.stButton > button:first-child:hover {
        box-shadow: 0 6px 12px rgba(0,0,0,0.2);
        background-color: #B8860B;
        color: white;
        transform: translateY(-2px);
    }
    </style>
""", unsafe_allow_html=True)

# --- BIBLE VERSES ---
verses = [
    "“Ask and it will be given to you; seek and you will find; knock and the door will be opened to you. For everyone who asks receives; the one who seeks finds; and to the one who knocks, the door will be opened.” (Matthew 7:7-8)",
    "“Come to me, all who are weary, and I will give you rest.” (Matthew 11:28)",
    "“Forgive, and you will be forgiven.” (Luke 6:37)",
    "“So do not fear, for I am with you; do not be dismayed, for I am your God. I will strengthen you and help you; I will uphold you with my righteous right hand.” (Isaiah 41:10)",
    "“But those who hope in the Lord will renew their strength. They will soar on wings like eagles; they will run and not grow weary, they will walk and not be faint.” (Isaiah 40:28-31)",
    "“The Lord will keep you from all harm—he will watch over your life; the Lord will watch over your coming and going both now and forevermore.” (Psalms 121:7-8)",
    "“I have told you these things, so that in me you may have peace. In this world you will have trouble. But take heart! I have overcome the world.” (John 16:33)",
    "“I love you, Lord, my strength. The Lord is my rock, my refuge and my savior—my God is my rock, in whom I take refuge.” (Psalms 18:1-2)",
    "“Be on your guard; stand firm in the faith; be courageous; be strong. Do everything in love.” (1Corinthians 16:13-14)"
]

# --- LOGIC ---
today = datetime.date.today()
today_str = str(today)
day_of_year = today.timetuple().tm_yday
index = day_of_year % len(verses)

# Check our tracker file
last_opened = get_last_opened_date()

# --- UI ---
st.markdown("<h1>Welcome! Jeffrey Cassian Xavier ❤️</h1>", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 1.5, 1])

with col2:
    button_clicked = st.button("Open your Daily Verse", use_container_width=True)

if button_clicked:
    # Check if she has already opened it today
    if last_opened == today_str:
        st.markdown('<p class="come-back-text">You have already received your blessing for today. Come back tomorrow! 🌅</p>', unsafe_allow_html=True)
    else:
        # The Animation: A temporary loading message that builds anticipation
        with st.spinner("Revealing your blessing for today..."):
            time.sleep(2) # Pauses for 2 seconds
            
        # Display the verse (CSS handles the fade-in)
        st.markdown(f'<div class="verse-box">{verses[index]}</div>', unsafe_allow_html=True)
        
        # Save today's date so it locks until tomorrow
        set_last_opened_date(today_str)
else:
    st.markdown('<p class="instruction-text">A message from Jesus for you today. ❤️</p>', unsafe_allow_html=True)
