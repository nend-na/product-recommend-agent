import streamlit as st
import random
import time

st.set_page_config(
    page_title="PROD.AI - Get the Perfect Recommendation",
    layout="wide",
    initial_sidebar_state="collapsed"
)

CUSTOM_CSS = """
<style>
html, body, [data-testid="stApp"] {
    font-family: 'Inter', sans-serif;
    background-color: #f7f9fa;
    color: #212121;
}
#MainMenu, footer {visibility: hidden;}
[data-testid="stToolbar"] {visibility: hidden;}

.main-nav {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 1rem 0;
}
.logo {
    font-size: 1.8rem;
    font-weight: 700;
    color: #007BFF;
}
.nav-links a {
    color: #616161;
    text-decoration: none;
    margin-left: 20px;
    font-size: 0.9rem;
    transition: color 0.2s;
}
.nav-links a:hover {
    color: #007BFF;
}

.hero-container {
    text-align: center;
    padding: 3rem 0 2rem 0;
}
.hero-headline {
    font-size: 3.0rem;
    font-weight: 800;
    line-height: 1.1;
    margin-bottom: 0;
}

.recommendation-heading {
    text-align: center;
    font-size: 1.5rem;
    font-weight: 600;
    color: #212121;
    margin-top: 2rem;
    margin-bottom: 1.5rem;
}

/* PERFECT ALIGNMENT - INPUT & BUTTON */
div[data-testid="stTextInput"] {
    margin-top: 0 !important;
    margin-bottom: 0 !important;
}

div.stTextInput > div > div > input {
    border-radius: 8px !important;
    border: 2px solid #e1e8ed !important;
    padding: 10px 14px !important;
    font-size: 16px !important;
    height: auto !important;
    min-height: 44px !important;
}

div[data-testid="stButton"] {
    margin-top: 0 !important;
    margin-bottom: 0 !important;
}

div.stButton > button {
    background-color: #007BFF !important;
    color: white !important;
    font-weight: 600 !important;
    border-radius: 8px !important;
    border: none !important;
    padding: 10px 20px !important;
    font-size: 16px !important;
    min-height: 44px !important;
    max-width: 160px !important;  /* ~5–6 cm on most screens */
    box-shadow: 0 4px 12px rgba(0,123,255,0.2) !important;
    transition: background-color 0.3s, box-shadow 0.3s, transform 0.2s !important;
}

div.stButton > button:hover {
    background-color: #0056b3 !important;
    box-shadow: 0 8px 20px rgba(0,123,255,0.3) !important;
    transform: translateY(-2px) !important;
}

.feature-card {
    text-align: center;
    padding: 2rem 1rem;
    border-radius: 10px;
    border: 1px solid #e0e0e0;
    height: 100%;
    background: white;
    box-shadow: 0 2px 4px rgba(0,0,0,0.05);
}
.feature-icon {
    font-size: 3rem;
    color: #007BFF;
    margin-bottom: 0.5rem;
}
.feature-title {
    font-weight: 700;
    font-size: 1.15rem;
    margin-bottom: 0.5rem;
}
.feature-description {
    color: #616161;
    font-size: 0.9rem;
}

.site-footer {
    padding: 2rem 0;
    margin-top: 5rem;
    border-top: 1px solid #e0e0e0;
    font-size: 0.8rem;
    color: #616161;
    display: flex;
    justify-content: space-between;
}
.footer-links a {
    color: #616161;
    margin-left: 20px;
    text-decoration: none;
}

.result-card {
    padding: 1.2rem;
    border-radius: 12px;
    background: white;
    border: 1px solid #e0e0e0;
    box-shadow: 0 4px 10px rgba(0,0,0,0.03);
}
.result-title {
    font-weight: 600;
    margin-bottom: 0.25rem;
    color: #007BFF;
}
.result-desc {
    font-size: 0.9rem;
    color: #555555;
    margin-bottom: 0.5rem;
}
.result-tag {
    display: inline-block;
    font-size: 0.75rem;
    color: #007BFF;
    background: #E3F2FD;
    padding: 4px 10px;
    border-radius: 999px;
    margin-right: 4px;
    margin-bottom: 4px;
}
</style>
"""
st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

# Expanded product catalog with categories
PRODUCTS = [
    # Earphones/Headphones (6)
    {
        "name": "AeroFit Wireless Sport Earbuds",
        "category": "earphones",
        "description": "Sweat‑resistant Bluetooth earbuds with secure fit and deep bass, ideal for gym sessions.",
        "tags": ["Audio", "Fitness", "Wireless"],
    },
    {
        "name": "FocusPro Noise Cancelling Headphones",
        "category": "headphones",
        "description": "Over‑ear ANC headphones for deep work, meetings and travel with 30 hours battery.",
        "tags": ["Audio", "Work", "Travel"],
    },
    {
        "name": "SonicBlast Premium Earbuds",
        "category": "earphones",
        "description": "High‑fidelity wireless earbuds with noise cancellation and 8 hour battery life.",
        "tags": ["Audio", "Premium", "Wireless"],
    },
    {
        "name": "CloudComfort Over‑Ear Headphones",
        "category": "headphones",
        "description": "Lightweight over‑ear headphones with memory foam padding for all‑day comfort.",
        "tags": ["Audio", "Comfort", "Work"],
    },
    {
        "name": "NeonWave Gaming Headset",
        "category": "headphones",
        "description": "RGB gaming headset with 7.1 surround sound and detachable microphone.",
        "tags": ["Audio", "Gaming", "RGB"],
    },
    {
        "name": "PocketPulse True Wireless Earbuds",
        "category": "earphones",
        "description": "Compact true wireless earbuds with case, perfect for daily commute and calls.",
        "tags": ["Audio", "Compact", "Wireless"],
    },
    
    # Smartwatches/Fitness Trackers (6)
    {
        "name": "PulseTrack Smartwatch",
        "category": "watch",
        "description": "Tracks heart rate, steps, sleep, and workouts with customizable watch faces.",
        "tags": ["Wearable", "Fitness", "Health"],
    },
    {
        "name": "EliteWrist Pro Smartwatch",
        "category": "watch",
        "description": "Premium smartwatch with GPS, ECG monitoring, and 7‑day battery life.",
        "tags": ["Wearable", "Fitness", "Premium"],
    },
    {
        "name": "FitBand Ultra Fitness Tracker",
        "category": "watch",
        "description": "Lightweight fitness band with blood oxygen tracking and 14‑day battery.",
        "tags": ["Wearable", "Fitness", "Health"],
    },
    {
        "name": "NanoWatch Compact Smart Watch",
        "category": "watch",
        "description": "Slim smartwatch with notifications, weather, and 5‑day battery life.",
        "tags": ["Wearable", "Compact", "Notifications"],
    },
    {
        "name": "VitaWatch Health Monitor",
        "category": "watch",
        "description": "Advanced health monitoring with stress detection and sleep analysis.",
        "tags": ["Wearable", "Health", "Premium"],
    },
    {
        "name": "SnapFit Sport Watch",
        "category": "watch",
        "description": "Rugged sports watch with 100+ workout modes and water resistance.",
        "tags": ["Wearable", "Sports", "Fitness"],
    },
    
    # Running Shoes (6)
    {
        "name": "StrideX Running Shoes",
        "category": "shoes",
        "description": "Lightweight running shoes with breathable mesh and cushioned sole for training.",
        "tags": ["Fitness", "Outdoor", "Shoes"],
    },
    {
        "name": "VelocityMax Marathon Runner",
        "category": "shoes",
        "description": "Professional running shoes designed for long distance with energy return.",
        "tags": ["Running", "Professional", "Shoes"],
    },
    {
        "name": "CloudStep Comfort Running Shoes",
        "category": "shoes",
        "description": "Ultra‑cushioned running shoes perfect for casual jogging and walking.",
        "tags": ["Comfort", "Casual", "Shoes"],
    },
    {
        "name": "TrailBlaze Outdoor Shoes",
        "category": "shoes",
        "description": "All‑terrain running shoes with grip traction for trail and road running.",
        "tags": ["Outdoor", "Trail", "Shoes"],
    },
    {
        "name": "SprintPro Track Shoes",
        "category": "shoes",
        "description": "Lightweight sprint shoes with minimal cushioning for speed and performance.",
        "tags": ["Track", "Professional", "Shoes"],
    },
    {
        "name": "NeutralStride Everyday Shoes",
        "category": "shoes",
        "description": "Versatile running shoes suitable for gym, casual runs, and everyday wear.",
        "tags": ["Casual", "Everyday", "Shoes"],
    },
    
    # Laptop & Workspace (6)
    {
        "name": "FlexDesk Laptop Stand",
        "category": "workspace",
        "description": "Adjustable aluminum laptop stand raising screen to eye level for better posture.",
        "tags": ["Workspace", "Ergonomics", "Laptop"],
    },
    {
        "name": "ProType Mechanical Keyboard",
        "category": "workspace",
        "description": "Compact mechanical keyboard with tactile switches and white backlight.",
        "tags": ["Keyboard", "Coding", "Workspace"],
    },
    {
        "name": "Clarity 4K Webcam",
        "category": "workspace",
        "description": "High‑resolution 4K webcam with auto‑focus and dual microphones.",
        "tags": ["Webcam", "Remote work", "Meetings"],
    },
    {
        "name": "AuraGlow Desk Lamp",
        "category": "workspace",
        "description": "LED desk lamp with adjustable color temperature and brightness.",
        "tags": ["Workspace", "Lighting", "Study"],
    },
    {
        "name": "StudioMic USB Microphone",
        "category": "workspace",
        "description": "Plug‑and‑play USB mic for clear voice on calls, podcasts and streaming.",
        "tags": ["Audio", "Streaming", "Meetings"],
    },
    {
        "name": "UrbanPack Everyday Backpack",
        "category": "workspace",
        "description": "Slim laptop backpack with padded compartment, perfect for commute.",
        "tags": ["Lifestyle", "Laptop", "Travel"],
    },
]

def get_recommendations(query: str):
    """Smart recommendation engine with category matching"""
    time.sleep(0.8)
    q = query.lower()
    
    # Category keywords mapping
    category_keywords = {
        "watch": ["watch", "smartwatch", "fitness tracker", "tracker", "fitbit"],
        "shoes": ["shoes", "running shoes", "sneakers", "runners", "trainers"],
        "earphones": ["earphone", "earbuds", "headphone", "headphones", "audio", "wireless", "earbud"],
        "workspace": ["laptop", "desk", "keyboard", "webcam", "microphone", "lamp", "stand", "backpack"],
    }
    
    # Detect category from query
    detected_category = None
    for cat, keywords in category_keywords.items():
        if any(kw in q for kw in keywords):
            detected_category = cat
            break
    
    # If specific category detected, return 3 items from that category
    if detected_category:
        category_items = [p for p in PRODUCTS if p["category"] == detected_category]
        if len(category_items) >= 3:
            return category_items[:3]
        elif category_items:
            return category_items
    
    # Fallback: keyword-based scoring
    scored = []
    for p in PRODUCTS:
        text = (p["name"] + " " + p["description"] + " " + " ".join(p["tags"])).lower()
        score = 0
        for word in q.split():
            if word in text:
                score += 1
        scored.append((score, p))
    
    scored.sort(key=lambda x: x[0], reverse=True)
    top = [p for score, p in scored[:3] if score > 0]
    
    # If no matches, return random 3
    if not top:
        top = random.sample(PRODUCTS, min(3, len(PRODUCTS)))
    
    return top

# Header
st.markdown("""
<div class="main-nav">
    <div class="logo">PROD.AI</div>
    <div class="nav-links">
        <a href="#how-it-works">How It Works</a>
        <a href="#demo">Demo</a>
        <a href="#about">About</a>
    </div>
</div>
""", unsafe_allow_html=True)

# Hero
st.markdown("""
<div class="hero-container">
    <h1 class="hero-headline">📦 Get the Perfect Recommendation. Every Time.</h1>
</div>
""", unsafe_allow_html=True)

st.markdown('<div id="demo" class="recommendation-heading">What are you looking for?</div>', unsafe_allow_html=True)

# PERFECTLY ALIGNED search bar + button
col1, col2 = st.columns([0.80, 0.20], gap="small")

with col1:
    user_query = st.text_input(
        "",
        placeholder="Enter your need (e.g., wireless earphones, running shoes, smartwatch)",
        label_visibility="collapsed",
        key="query_input"
    )

with col2:
    search_clicked = st.button("Recommend", key="recommend_button", use_container_width=True)

recommendations = []
if search_clicked:
    if user_query.strip():
        with st.spinner(f'Analyzing "{user_query}"...'):
            recommendations = get_recommendations(user_query)
    else:
        st.warning("Please enter a query to get started!")

# Display Results
if recommendations:
    st.subheader("Your Personalized Recommendations:")
    rec_cols = st.columns(len(recommendations))
    for i, rec in enumerate(recommendations):
        with rec_cols[i]:
            st.markdown(
                f"""
                <div class="result-card">
                    <p class="result-title">{rec['name']}</p>
                    <p class="result-desc">{rec['description']}</p>
                    <div>
                        {''.join(f'<span class="result-tag">{t}</span>' for t in rec['tags'])}
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )

st.markdown("---")

# Features Section
st.markdown('<div id="how-it-works" style="padding-top: 5rem;">', unsafe_allow_html=True)
st.markdown('<h2 style="text-align: center; font-weight: 700; margin-bottom: 3rem;">Why Choose Our Agent?</h2>', unsafe_allow_html=True)

features_data = [
    {"title": "Built with Python", "icon": "🐍", "description": "Uses solid Python fundamentals so it is easy to extend, debug, and deploy."},
    {"title": "Hyper‑Relevant Results", "icon": "🎯", "description": "Understands intent from your text and surfaces products that actually match your use case."},
    {"title": "Real‑Time Experience", "icon": "⚡", "description": "Fast responses with a clean interface that works smoothly on both laptop and mobile."},
]

f_col1, f_col2, f_col3 = st.columns(3)
for i, col in enumerate([f_col1, f_col2, f_col3]):
    feature = features_data[i]
    with col:
        st.markdown(
            f"""
            <div class="feature-card">
                <span class="feature-icon">{feature['icon']}</span>
                <p class="feature-title">{feature['title']}</p>
                <p class="feature-description">{feature['description']}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown("""
<div class="site-footer">
    <span>© 2025 PROD.AI. All rights reserved.</span>
    <div class="footer-links">
        <a href="#about">About</a>
        <a href="https://github.com/your-repo" target="_blank">GitHub Repository</a>
        <a href="#">Contact</a>
        <a href="#">Privacy Policy</a>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown('<div id="about"></div>', unsafe_allow_html=True)
