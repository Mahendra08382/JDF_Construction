import streamlit as st
import folium
from streamlit_folium import st_folium
import os
import base64
from PIL import Image

st.set_page_config(
    page_title="JDF Constructions",
    page_icon="🏗️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

def img_to_b64(fn):
    p = os.path.join(os.path.dirname(os.path.abspath(__file__)), fn)
    if os.path.exists(p):
        with open(p, "rb") as f:
            return base64.b64encode(f.read()).decode()
    return None

if "page" not in st.session_state:
    st.session_state.page = "Home"

def go(p):
    st.session_state.page = p
    st.rerun()

pg = st.session_state.page

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,600;0,700;1,400&family=Montserrat:wght@300;400;500;600;700;800&display=swap');

* { box-sizing: border-box; margin: 0; padding: 0; }
#MainMenu, footer, header { visibility: hidden !important; }
.stDeployButton, div[data-testid="stDecoration"],
div[data-testid="stToolbar"] { display: none !important; }
section[data-testid="stSidebar"] { display: none !important; }

html, body, .stApp {
    background: #f2f0eb !important;
    font-family: 'Montserrat', sans-serif;
    color: #2c2c2c;
}
.block-container {
    padding: 0 !important;
    max-width: 100% !important;
}
div[data-testid="column"] { padding: 0 !important; }
div[data-testid="stVerticalBlock"] > div { padding: 0 !important; }

/* ── GOLDEN NAV BUTTONS ── */
.stButton > button {
    background: #c9a227 !important;
    background-color: #c9a227 !important;
    color: #ffffff !important;
    border: none !important;
    border-radius: 8px !important;
    font-weight: 700 !important;
    letter-spacing: 1px !important;
    font-size: 0.72em !important;
    padding: 10px 6px !important;
    width: 100% !important;
    box-shadow: 0 3px 10px rgba(201,162,39,0.3) !important;
    white-space: nowrap !important;
}
.stButton > button:hover {
    background: #a8841f !important;
    background-color: #a8841f !important;
    color: #ffffff !important;
    border: none !important;
}
.stButton > button:focus,
.stButton > button:active {
    background: #c9a227 !important;
    background-color: #c9a227 !important;
    color: #ffffff !important;
    border: none !important;
    box-shadow: none !important;
}

/* Form */
.stForm [data-testid="stFormSubmitButton"] > button {
    background: linear-gradient(135deg,#c9a227,#e8c040) !important;
    color:#fff !important; border:none !important;
    border-radius:5px !important; width:100% !important;
}
.stTextInput>div>div>input,
.stTextArea>div>div>textarea {
    background:#fff !important; border:1.5px solid #ddd !important;
    color:#333 !important; border-radius:5px !important;
}
.stSelectbox>div>div {
    background:#fff !important; border:1.5px solid #ddd !important;
    color:#333 !important; border-radius:5px !important;
}
.stTextInput label,.stTextArea label,.stSelectbox label {
    color:#333 !important; font-size:0.85em !important; font-weight:600 !important;
}

/* ── CSS GRID LAYOUTS ── */
.grid-4 {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 14px;
    width: 100%;
}
.grid-3 {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 14px;
    width: 100%;
}
.grid-2 {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 14px;
    width: 100%;
}
.grid-1-2 {
    display: grid;
    grid-template-columns: 1fr 1.8fr;
    gap: 20px;
    width: 100%;
}
.grid-2-1 {
    display: grid;
    grid-template-columns: 1.6fr 1fr;
    gap: 20px;
    width: 100%;
}

/* ── MOBILE ── */
@media (max-width: 640px) {
    .grid-4 { grid-template-columns: repeat(2, 1fr) !important; }
    .grid-3 { grid-template-columns: repeat(1, 1fr) !important; }
    .grid-2 { grid-template-columns: repeat(1, 1fr) !important; }
    .grid-1-2 { grid-template-columns: 1fr !important; }
    .grid-2-1 { grid-template-columns: 1fr !important; }
    .hero-row { flex-direction: column !important; }
    .hero-logo { display: none !important; }
    .hero-owner {
        width: 100% !important;
        min-width: 100% !important;
        border-left: none !important;
        border-top: 1px solid rgba(201,162,39,0.2) !important;
        padding: 16px !important;
    }
    .hero-owner-card { width: 140px !important; margin: 0 auto !important; }
    .stats-bar { flex-direction: column !important; }
    .stat-item {
        border-right: none !important;
        border-bottom: 1px solid rgba(201,162,39,0.2) !important;
        padding: 14px 0 !important;
    }
    .info-bar { flex-direction: column !important; gap: 3px !important;
        text-align: center !important; padding: 8px 12px !important; }
    .nav-row { padding-right: 4px !important; }
    .section-wrap { padding: 20px 12px !important; }
    .footer-grid { flex-direction: column !important; gap: 16px !important; }
    .cta-btns { flex-direction: column !important; align-items: center !important; }
    .hero-center { padding: 24px 14px !important; }
    .process-grid { grid-template-columns: repeat(2, 1fr) !important; }
}

@media (max-width: 400px) {
    .grid-4 { grid-template-columns: repeat(1, 1fr) !important; }
    .process-grid { grid-template-columns: repeat(1, 1fr) !important; }
}

::-webkit-scrollbar { width: 5px; }
::-webkit-scrollbar-track { background: #f0ede4; }
::-webkit-scrollbar-thumb { background: #c9a227; border-radius: 3px; }
</style>
""", unsafe_allow_html=True)

# ── INFO BAR
st.markdown(
    '<div class="info-bar" style="background:#9a7a10;padding:8px 40px;display:flex;'
    'justify-content:space-between;align-items:center;flex-wrap:wrap;gap:4px;'
    'font-size:0.78em;color:#fff;font-family:Montserrat,sans-serif">'
    '<span>📍 Near Dwarka Hotel, Habuwada Main Road, Karwar, Karnataka</span>'
    '<span>✉ jdfconstructions@gmail.com &nbsp;'
    '<a href="tel:+919019429427" style="color:#fff;text-decoration:none">'
    '📞 +91 90194 29427</a></span></div>',
    unsafe_allow_html=True
)

# ── NAVBAR
st.markdown(
    '<div style="background:#fff;border-bottom:3px solid #c9a227;'
    'padding:0 24px;min-height:60px;display:flex;align-items:center;'
    'box-shadow:0 2px 10px rgba(0,0,0,0.06)">'
    '<span style="font-family:Cormorant Garamond,serif;font-size:1.4em;'
    'font-weight:700;color:#b8960c;letter-spacing:2px">🏗️ JDF CONSTRUCTIONS</span>'
    '</div>',
    unsafe_allow_html=True
)

# ── NAV BUTTONS (Streamlit columns — kept for interactivity)
nav_cols = st.columns([0.4,1,1,1,1,1,0.4])
with nav_cols[1]:
    if st.button("HOME", key="n1"): go("Home")
with nav_cols[2]:
    if st.button("SERVICES", key="n2"): go("Services")
with nav_cols[3]:
    if st.button("LOCATIONS", key="n3"): go("Locations")
with nav_cols[4]:
    if st.button("ABOUT US", key="n4"): go("About Us")
with nav_cols[5]:
    if st.button("CONTACT", key="n5"): go("Contact Us")

st.markdown('<div style="margin-top:-8px"></div>', unsafe_allow_html=True)

# ── HELPERS
def sec_header(overline, title, desc=""):
    desc_html = (
        f'<p style="color:#777;font-size:0.92em;max-width:520px;'
        f'margin:0 auto;line-height:1.75;padding:0 8px">{desc}</p>'
    ) if desc else ""
    st.markdown(
        f'<div style="text-align:center;margin-bottom:20px;padding:0 8px">'
        f'<span style="font-family:Montserrat,sans-serif;font-size:0.7em;'
        f'letter-spacing:4px;text-transform:uppercase;'
        f'color:#c9a227;font-weight:700;display:block;margin-bottom:6px">{overline}</span>'
        f'<div style="font-family:Cormorant Garamond,serif;'
        f'font-size:clamp(1.7em,4vw,2.5em);'
        f'font-weight:700;color:#1a1a1a;margin:0 0 10px;line-height:1.15">{title}</div>'
        f'{desc_html}'
        f'<div style="width:52px;height:2px;'
        f'background:linear-gradient(90deg,#c9a227,#f5d77e);'
        f'margin:12px auto;border-radius:2px"></div></div>',
        unsafe_allow_html=True
    )

def wrap_open(bg="#f2f0eb", pad="40px 0"):
    st.markdown(
        f'<div style="background:{bg};padding:{pad};width:100%">',
        unsafe_allow_html=True
    )

def wrap_close():
    st.markdown('</div>', unsafe_allow_html=True)

def inner_open():
    st.markdown(
        '<div class="section-wrap" style="max-width:1200px;margin:0 auto;padding:0 30px">',
        unsafe_allow_html=True
    )

def inner_close():
    st.markdown('</div>', unsafe_allow_html=True)

# ═══════════════════════════════════════════════
# HOME PAGE
# ═══════════════════════════════════════════════
if pg == "Home":
    logo_b64  = img_to_b64("jdf_logo.png")
    owner_b64 = img_to_b64("jason_photo.jpg")

    logo_html = (
        f'<img src="data:image/png;base64,{logo_b64}" '
        f'style="width:clamp(80px,10vw,150px);border-radius:8px;'
        f'box-shadow:0 4px 20px rgba(0,0,0,0.5)">'
    ) if logo_b64 else '<span style="font-size:3em">🏗️</span>'

    owner_img = (
        f'<img src="data:image/jpeg;base64,{owner_b64}" '
        f'style="width:100%;height:180px;object-fit:cover;'
        f'object-position:top center;display:block;border-radius:6px 6px 0 0">'
    ) if owner_b64 else (
        '<div style="height:180px;background:#2d2000;border-radius:6px 6px 0 0;'
        'display:flex;align-items:center;justify-content:center;font-size:3em">👤</div>'
    )

    # ── HERO
    st.markdown(
        '<div style="background:linear-gradient(135deg,#1c1400,#2d2000,#1a1200);'
        'border-bottom:4px solid #c9a227;width:100%">'

        # Top row
        '<div class="hero-row" style="display:flex;width:100%;flex-wrap:wrap">'

        # Logo
        f'<div class="hero-logo" style="width:180px;min-width:180px;display:flex;'
        f'align-items:center;justify-content:center;padding:24px;'
        f'border-right:1px solid rgba(201,162,39,0.2)">{logo_html}</div>'

        # Center
        '<div class="hero-center" style="flex:1;min-width:240px;display:flex;'
        'align-items:center;justify-content:center;text-align:center;padding:40px 20px">'
        '<div>'
        '<div style="font-family:Montserrat,sans-serif;font-size:clamp(0.5em,1.2vw,0.65em);'
        'letter-spacing:4px;text-transform:uppercase;color:rgba(201,162,39,0.65);'
        'font-weight:600;margin-bottom:12px">KARNATAKA\'S PREMIER CONSTRUCTION COMPANY</div>'
        '<div style="font-family:Cormorant Garamond,serif;font-size:clamp(2.8em,7vw,5.5em);'
        'font-weight:700;color:#fff;line-height:0.9;letter-spacing:3px">JDF</div>'
        '<div style="font-family:Cormorant Garamond,serif;font-size:clamp(1em,2.5vw,1.8em);'
        'font-weight:600;color:#c9a227;letter-spacing:6px;text-transform:uppercase;'
        'margin:10px 0 12px">CONSTRUCTIONS</div>'
        '<div style="width:50px;height:2px;background:linear-gradient(90deg,#c9a227,#f5d77e);'
        'margin:0 auto 14px"></div>'
        '<div style="font-family:Cormorant Garamond,serif;font-size:clamp(0.9em,2vw,1.25em);'
        'color:#d4c898;font-style:italic;margin-bottom:20px">"Your dream project starts here."</div>'
        '<div style="display:flex;flex-wrap:wrap;justify-content:center;gap:6px">'
        '<span style="border:1px solid rgba(201,162,39,0.5);color:#c9a227;padding:5px 12px;'
        'border-radius:30px;font-size:0.72em;font-weight:600;'
        'background:rgba(201,162,39,0.1)">📍 Karwar</span>'
        '<span style="border:1px solid rgba(201,162,39,0.5);color:#c9a227;padding:5px 12px;'
        'border-radius:30px;font-size:0.72em;font-weight:600;'
        'background:rgba(201,162,39,0.1)">📍 Ankola</span>'
        '<span style="border:1px solid rgba(201,162,39,0.5);color:#c9a227;padding:5px 12px;'
        'border-radius:30px;font-size:0.72em;font-weight:600;'
        'background:rgba(201,162,39,0.1)">📍 Honnawar</span>'
        '<span style="border:1px solid rgba(201,162,39,0.5);color:#c9a227;padding:5px 12px;'
        'border-radius:30px;font-size:0.72em;font-weight:600;'
        'background:rgba(201,162,39,0.1)">📍 Mangalore</span>'
        '</div></div></div>'

        # Owner
        f'<div class="hero-owner" style="width:200px;min-width:200px;display:flex;'
        f'align-items:center;justify-content:center;padding:24px;'
        f'border-left:1px solid rgba(201,162,39,0.2)">'
        f'<div class="hero-owner-card" style="width:160px">'
        f'{owner_img}'
        f'<div style="background:#fff;border-radius:0 0 8px 8px;border-top:3px solid #c9a227;'
        f'padding:12px;text-align:center">'
        f'<div style="font-family:Cormorant Garamond,serif;font-size:1em;'
        f'font-weight:700;color:#1a1a1a">Jason Fernandes</div>'
        f'<div style="font-family:Montserrat,sans-serif;font-size:0.56em;'
        f'letter-spacing:2px;color:#c9a227;text-transform:uppercase;'
        f'font-weight:700;margin:4px 0">Founder &amp; Owner</div>'
        f'<div style="font-family:Montserrat,sans-serif;font-size:0.73em;'
        f'color:#444;font-weight:600">📞 90194 29427</div>'
        f'</div></div></div>'
        '</div>'  # end hero-row

        # Stats bar — pure HTML grid
        '<div class="stats-bar" style="border-top:1px solid rgba(201,162,39,0.2);'
        'display:flex;flex-wrap:wrap;justify-content:space-around;'
        'padding:24px 20px;gap:0">'

        '<div class="stat-item" style="flex:1;min-width:120px;text-align:center;'
        'border-right:1px solid rgba(201,162,39,0.2);padding:10px 12px">'
        '<div style="font-size:1.5em;margin-bottom:4px">🏗️</div>'
        '<div style="font-family:Cormorant Garamond,serif;'
        'font-size:clamp(1.6em,3.5vw,2.8em);font-weight:700;color:#c9a227">500+</div>'
        '<div style="font-family:Montserrat,sans-serif;font-size:clamp(0.5em,1.2vw,0.6em);'
        'text-transform:uppercase;letter-spacing:2px;color:#fff;margin-top:4px">'
        'Projects Completed</div></div>'

        '<div class="stat-item" style="flex:1;min-width:120px;text-align:center;'
        'border-right:1px solid rgba(201,162,39,0.2);padding:10px 12px">'
        '<div style="font-size:1.5em;margin-bottom:4px">📍</div>'
        '<div style="font-family:Cormorant Garamond,serif;'
        'font-size:clamp(1.6em,3.5vw,2.8em);font-weight:700;color:#c9a227">4</div>'
        '<div style="font-family:Montserrat,sans-serif;font-size:clamp(0.5em,1.2vw,0.6em);'
        'text-transform:uppercase;letter-spacing:2px;color:#fff;margin-top:4px">'
        'Cities Served</div></div>'

        '<div class="stat-item" style="flex:1;min-width:120px;text-align:center;'
        'border-right:1px solid rgba(201,162,39,0.2);padding:10px 12px">'
        '<div style="font-size:1.5em;margin-bottom:4px">🏅</div>'
        '<div style="font-family:Cormorant Garamond,serif;'
        'font-size:clamp(1.6em,3.5vw,2.8em);font-weight:700;color:#c9a227">15+</div>'
        '<div style="font-family:Montserrat,sans-serif;font-size:clamp(0.5em,1.2vw,0.6em);'
        'text-transform:uppercase;letter-spacing:2px;color:#fff;margin-top:4px">'
        'Years of Excellence</div></div>'

        '<div class="stat-item" style="flex:1;min-width:120px;text-align:center;'
        'padding:10px 12px">'
        '<div style="font-size:1.5em;margin-bottom:4px">😊</div>'
        '<div style="font-family:Cormorant Garamond,serif;'
        'font-size:clamp(1.6em,3.5vw,2.8em);font-weight:700;color:#c9a227">1000+</div>'
        '<div style="font-family:Montserrat,sans-serif;font-size:clamp(0.5em,1.2vw,0.6em);'
        'text-transform:uppercase;letter-spacing:2px;color:#fff;margin-top:4px">'
        'Happy Clients</div></div>'

        '</div>'  # end stats
        '</div>', # end hero outer
        unsafe_allow_html=True
    )

    # ── SERVICES (pure HTML grid)
    wrap_open("#f2f0eb")
    inner_open()
    sec_header("What We Build", "Our Core Services",
               "From luxury residences to large-scale infrastructure.")
    st.markdown("""
    <div class="grid-4">
      <div style="background:#fff;border-radius:8px;padding:24px 16px;
        box-shadow:0 4px 20px rgba(0,0,0,0.08);border:1px solid #e0dcd0;text-align:center">
        <div style="width:54px;height:54px;background:linear-gradient(135deg,#fff8e1,#ffeaa0);
          border-radius:50%;display:flex;align-items:center;justify-content:center;
          font-size:1.5em;margin:0 auto 14px;border:2px solid #f0d060">🏠</div>
        <div style="font-family:Cormorant Garamond,serif;font-size:1.15em;font-weight:700;
          color:#1a1a1a;margin-bottom:8px">Residential</div>
        <div style="color:#777;font-size:0.83em;line-height:1.7">
          Custom homes, villas and apartments built to your vision.</div>
      </div>
      <div style="background:#fff;border-radius:8px;padding:24px 16px;
        box-shadow:0 4px 20px rgba(0,0,0,0.08);border:1px solid #e0dcd0;text-align:center">
        <div style="width:54px;height:54px;background:linear-gradient(135deg,#fff8e1,#ffeaa0);
          border-radius:50%;display:flex;align-items:center;justify-content:center;
          font-size:1.5em;margin:0 auto 14px;border:2px solid #f0d060">🏢</div>
        <div style="font-family:Cormorant Garamond,serif;font-size:1.15em;font-weight:700;
          color:#1a1a1a;margin-bottom:8px">Commercial</div>
        <div style="color:#777;font-size:0.83em;line-height:1.7">
          Modern offices, retail spaces and commercial complexes.</div>
      </div>
      <div style="background:#fff;border-radius:8px;padding:24px 16px;
        box-shadow:0 4px 20px rgba(0,0,0,0.08);border:1px solid #e0dcd0;text-align:center">
        <div style="width:54px;height:54px;background:linear-gradient(135deg,#fff8e1,#ffeaa0);
          border-radius:50%;display:flex;align-items:center;justify-content:center;
          font-size:1.5em;margin:0 auto 14px;border:2px solid #f0d060">🛣️</div>
        <div style="font-family:Cormorant Garamond,serif;font-size:1.15em;font-weight:700;
          color:#1a1a1a;margin-bottom:8px">Infrastructure</div>
        <div style="color:#777;font-size:0.83em;line-height:1.7">
          Roads, bridges, drainage and large-scale civil works.</div>
      </div>
      <div style="background:#fff;border-radius:8px;padding:24px 16px;
        box-shadow:0 4px 20px rgba(0,0,0,0.08);border:1px solid #e0dcd0;text-align:center">
        <div style="width:54px;height:54px;background:linear-gradient(135deg,#fff8e1,#ffeaa0);
          border-radius:50%;display:flex;align-items:center;justify-content:center;
          font-size:1.5em;margin:0 auto 14px;border:2px solid #f0d060">🔧</div>
        <div style="font-family:Cormorant Garamond,serif;font-size:1.15em;font-weight:700;
          color:#1a1a1a;margin-bottom:8px">Renovation</div>
        <div style="color:#777;font-size:0.83em;line-height:1.7">
          Expert remodelling that transforms existing spaces.</div>
      </div>
    </div>
    """, unsafe_allow_html=True)
    inner_close()
    wrap_close()

    # ── WHY US
    wrap_open("#ffffff")
    inner_open()
    sec_header("Why JDF", "The JDF Difference",
               "Craftsmanship, technology and transparency.")
    st.markdown("""
    <div class="grid-2">
      <div style="background:#f9f7f2;border-radius:8px;padding:16px 18px;
        border:1px solid #e8e4d8;border-left:4px solid #c9a227;
        display:flex;align-items:flex-start;gap:12px">
        <div style="width:42px;height:42px;min-width:42px;
          background:linear-gradient(135deg,#fff8e1,#ffeaa0);border-radius:8px;
          display:flex;align-items:center;justify-content:center;font-size:1.2em">🏅</div>
        <div>
          <div style="font-weight:700;color:#1a1a1a;font-size:0.88em;margin-bottom:3px">
            Premium Quality</div>
          <div style="color:#888;font-size:0.8em;line-height:1.6">
            Top-grade certified materials with strict QC at every stage.</div>
        </div>
      </div>
      <div style="background:#f9f7f2;border-radius:8px;padding:16px 18px;
        border:1px solid #e8e4d8;border-left:4px solid #c9a227;
        display:flex;align-items:flex-start;gap:12px">
        <div style="width:42px;height:42px;min-width:42px;
          background:linear-gradient(135deg,#fff8e1,#ffeaa0);border-radius:8px;
          display:flex;align-items:center;justify-content:center;font-size:1.2em">⏰</div>
        <div>
          <div style="font-weight:700;color:#1a1a1a;font-size:0.88em;margin-bottom:3px">
            On-Time Delivery</div>
          <div style="color:#888;font-size:0.8em;line-height:1.6">
            We honour every deadline with systematic project management.</div>
        </div>
      </div>
      <div style="background:#f9f7f2;border-radius:8px;padding:16px 18px;
        border:1px solid #e8e4d8;border-left:4px solid #c9a227;
        display:flex;align-items:flex-start;gap:12px">
        <div style="width:42px;height:42px;min-width:42px;
          background:linear-gradient(135deg,#fff8e1,#ffeaa0);border-radius:8px;
          display:flex;align-items:center;justify-content:center;font-size:1.2em">💰</div>
        <div>
          <div style="font-weight:700;color:#1a1a1a;font-size:0.88em;margin-bottom:3px">
            Transparent Pricing</div>
          <div style="color:#888;font-size:0.8em;line-height:1.6">
            Honest quotations — what we quote is exactly what you pay.</div>
        </div>
      </div>
      <div style="background:#f9f7f2;border-radius:8px;padding:16px 18px;
        border:1px solid #e8e4d8;border-left:4px solid #c9a227;
        display:flex;align-items:flex-start;gap:12px">
        <div style="width:42px;height:42px;min-width:42px;
          background:linear-gradient(135deg,#fff8e1,#ffeaa0);border-radius:8px;
          display:flex;align-items:center;justify-content:center;font-size:1.2em">👷</div>
        <div>
          <div style="font-weight:700;color:#1a1a1a;font-size:0.88em;margin-bottom:3px">
            Expert Team</div>
          <div style="color:#888;font-size:0.8em;line-height:1.6">
            Certified engineers, architects and experienced workers.</div>
        </div>
      </div>
      <div style="background:#f9f7f2;border-radius:8px;padding:16px 18px;
        border:1px solid #e8e4d8;border-left:4px solid #c9a227;
        display:flex;align-items:flex-start;gap:12px">
        <div style="width:42px;height:42px;min-width:42px;
          background:linear-gradient(135deg,#fff8e1,#ffeaa0);border-radius:8px;
          display:flex;align-items:center;justify-content:center;font-size:1.2em">🌱</div>
        <div>
          <div style="font-weight:700;color:#1a1a1a;font-size:0.88em;margin-bottom:3px">
            Eco-Friendly</div>
          <div style="color:#888;font-size:0.8em;line-height:1.6">
            Sustainable methods protecting Karnataka's coast.</div>
        </div>
      </div>
      <div style="background:#f9f7f2;border-radius:8px;padding:16px 18px;
        border:1px solid #e8e4d8;border-left:4px solid #c9a227;
        display:flex;align-items:flex-start;gap:12px">
        <div style="width:42px;height:42px;min-width:42px;
          background:linear-gradient(135deg,#fff8e1,#ffeaa0);border-radius:8px;
          display:flex;align-items:center;justify-content:center;font-size:1.2em">📞</div>
        <div>
          <div style="font-weight:700;color:#1a1a1a;font-size:0.88em;margin-bottom:3px">
            24/7 Support</div>
          <div style="color:#888;font-size:0.8em;line-height:1.6">
            Always available from first consultation to final handover.</div>
        </div>
      </div>
    </div>
    """, unsafe_allow_html=True)
    inner_close()
    wrap_close()

    # ── TESTIMONIALS
    wrap_open("#f2f0eb")
    inner_open()
    sec_header("Client Stories", "What Our Clients Say")
    st.markdown("""
    <div class="grid-3">
      <div style="background:#fff;border-radius:8px;padding:24px 20px;
        box-shadow:0 4px 18px rgba(0,0,0,0.07);border:1px solid #e0dcd0;
        border-top:3px solid #c9a227">
        <div style="font-family:Georgia,serif;font-size:2.5em;
          color:rgba(201,162,39,0.25);line-height:1;margin-bottom:6px">"</div>
        <div style="color:#555;font-style:italic;font-size:0.87em;
          line-height:1.8;margin-bottom:14px">
          JDF built our dream home in Karwar with incredible precision.
          Professional, timely and beyond every expectation we had set.</div>
        <div style="color:#c9a227;margin-bottom:6px">⭐⭐⭐⭐⭐</div>
        <div style="font-weight:700;font-size:0.84em;color:#1a1a1a">Ramesh Naik</div>
        <div style="color:#c9a227;font-size:0.73em;margin-top:2px">📍 Karwar</div>
      </div>
      <div style="background:#fff;border-radius:8px;padding:24px 20px;
        box-shadow:0 4px 18px rgba(0,0,0,0.07);border:1px solid #e0dcd0;
        border-top:3px solid #c9a227">
        <div style="font-family:Georgia,serif;font-size:2.5em;
          color:rgba(201,162,39,0.25);line-height:1;margin-bottom:6px">"</div>
        <div style="color:#555;font-style:italic;font-size:0.87em;
          line-height:1.8;margin-bottom:14px">
          Outstanding commercial project in Mangalore — on schedule,
          within budget and genuinely impressive quality.</div>
        <div style="color:#c9a227;margin-bottom:6px">⭐⭐⭐⭐⭐</div>
        <div style="font-weight:700;font-size:0.84em;color:#1a1a1a">Priya Shetty</div>
        <div style="color:#c9a227;font-size:0.73em;margin-top:2px">📍 Mangalore</div>
      </div>
      <div style="background:#fff;border-radius:8px;padding:24px 20px;
        box-shadow:0 4px 18px rgba(0,0,0,0.07);border:1px solid #e0dcd0;
        border-top:3px solid #c9a227">
        <div style="font-family:Georgia,serif;font-size:2.5em;
          color:rgba(201,162,39,0.25);line-height:1;margin-bottom:6px">"</div>
        <div style="color:#555;font-style:italic;font-size:0.87em;
          line-height:1.8;margin-bottom:14px">
          JDF transformed our Honnawar building into a modern masterpiece.
          Best construction company on the Karnataka coast.</div>
        <div style="color:#c9a227;margin-bottom:6px">⭐⭐⭐⭐⭐</div>
        <div style="font-weight:700;font-size:0.84em;color:#1a1a1a">Suresh Hegde</div>
        <div style="color:#c9a227;font-size:0.73em;margin-top:2px">📍 Honnawar</div>
      </div>
    </div>
    """, unsafe_allow_html=True)
    inner_close()
    wrap_close()

    # ── CTA
    wrap_open("#f2f0eb", "0 0 50px")
    inner_open()
    st.markdown("""
    <div style="background:linear-gradient(135deg,#c9a227,#e8c040,#c9a227);
      padding:50px 30px;text-align:center;border-radius:10px;
      box-shadow:0 12px 48px rgba(201,162,39,0.35)">
      <div style="font-family:Cormorant Garamond,serif;
        font-size:clamp(1.5em,4vw,2.5em);color:#fff;font-weight:700;margin-bottom:12px">
        Ready to Build Your Dream Project?</div>
      <p style="color:rgba(255,255,255,0.88);font-size:0.95em;
        margin-bottom:24px;padding:0 10px">
        FREE consultation from Karnataka's most trusted experts.</p>
      <div class="cta-btns" style="display:flex;flex-wrap:wrap;
        justify-content:center;gap:12px">
        <a href="tel:+919019429427"
          style="background:#fff;color:#b8960c;padding:13px 32px;border-radius:5px;
          font-size:0.82em;font-weight:800;text-decoration:none;
          letter-spacing:1px;text-transform:uppercase">
          📞 Call: 90194 29427</a>
        <a href="https://wa.me/919019429427" target="_blank"
          style="background:#1a1200;color:#c9a227;padding:13px 32px;border-radius:5px;
          font-size:0.82em;font-weight:800;text-decoration:none;
          letter-spacing:1px;text-transform:uppercase">
          💬 WhatsApp Us</a>
      </div>
      <p style="color:rgba(255,255,255,0.6);font-size:0.78em;margin-top:18px">
        📍 Near Dwarka Hotel, Habuwada Main Road, Karwar</p>
    </div>
    """, unsafe_allow_html=True)
    inner_close()
    wrap_close()


# ═══════════════════════════════════════════════
# SERVICES PAGE
# ═══════════════════════════════════════════════
elif pg == "Services":
    wrap_open("#f2f0eb")
    inner_open()
    sec_header("What We Do", "Our Services",
               "Comprehensive construction solutions across coastal Karnataka.")
    st.markdown("""
    <div class="grid-2">
      <div style="background:#fff;border-radius:8px;padding:22px;
        box-shadow:0 4px 18px rgba(0,0,0,0.07);border:1px solid #e0dcd0">
        <div style="display:flex;align-items:center;gap:12px;margin-bottom:12px">
          <div style="width:48px;height:48px;min-width:48px;
            background:linear-gradient(135deg,#fff8e1,#ffeaa0);border-radius:50%;
            display:flex;align-items:center;justify-content:center;
            font-size:1.4em;border:2px solid #f0d060">🏠</div>
          <div style="font-family:Cormorant Garamond,serif;font-size:1.1em;
            font-weight:700;color:#1a1a1a">Residential Construction</div>
        </div>
        <div style="color:#666;font-size:0.84em;line-height:1.85;margin-bottom:10px">
          Custom bungalows, Multi-storey apartments, Duplex houses, Coastal architecture</div>
        <span style="background:#fff8e1;color:#9a7a10;padding:3px 10px;border-radius:20px;
          font-size:0.7em;font-weight:700;border:1px solid #e8c840">
          📍 Karwar, Ankola, Honnawar, Mangalore</span>
      </div>
      <div style="background:#fff;border-radius:8px;padding:22px;
        box-shadow:0 4px 18px rgba(0,0,0,0.07);border:1px solid #e0dcd0">
        <div style="display:flex;align-items:center;gap:12px;margin-bottom:12px">
          <div style="width:48px;height:48px;min-width:48px;
            background:linear-gradient(135deg,#fff8e1,#ffeaa0);border-radius:50%;
            display:flex;align-items:center;justify-content:center;
            font-size:1.4em;border:2px solid #f0d060">🏢</div>
          <div style="font-family:Cormorant Garamond,serif;font-size:1.1em;
            font-weight:700;color:#1a1a1a">Commercial Construction</div>
        </div>
        <div style="color:#666;font-size:0.84em;line-height:1.85;margin-bottom:10px">
          Office complexes, Shopping centres, Hotels, Warehouses</div>
        <span style="background:#fff8e1;color:#9a7a10;padding:3px 10px;border-radius:20px;
          font-size:0.7em;font-weight:700;border:1px solid #e8c840">
          📍 Mangalore, Karwar</span>
      </div>
      <div style="background:#fff;border-radius:8px;padding:22px;
        box-shadow:0 4px 18px rgba(0,0,0,0.07);border:1px solid #e0dcd0">
        <div style="display:flex;align-items:center;gap:12px;margin-bottom:12px">
          <div style="width:48px;height:48px;min-width:48px;
            background:linear-gradient(135deg,#fff8e1,#ffeaa0);border-radius:50%;
            display:flex;align-items:center;justify-content:center;
            font-size:1.4em;border:2px solid #f0d060">🛣️</div>
          <div style="font-family:Cormorant Garamond,serif;font-size:1.1em;
            font-weight:700;color:#1a1a1a">Infrastructure & Civil Works</div>
        </div>
        <div style="color:#666;font-size:0.84em;line-height:1.85;margin-bottom:10px">
          Roads, Bridges, Drainage, Retaining walls, Government contracts</div>
        <span style="background:#fff8e1;color:#9a7a10;padding:3px 10px;border-radius:20px;
          font-size:0.7em;font-weight:700;border:1px solid #e8c840">
          📍 All Locations</span>
      </div>
      <div style="background:#fff;border-radius:8px;padding:22px;
        box-shadow:0 4px 18px rgba(0,0,0,0.07);border:1px solid #e0dcd0">
        <div style="display:flex;align-items:center;gap:12px;margin-bottom:12px">
          <div style="width:48px;height:48px;min-width:48px;
            background:linear-gradient(135deg,#fff8e1,#ffeaa0);border-radius:50%;
            display:flex;align-items:center;justify-content:center;
            font-size:1.4em;border:2px solid #f0d060">🔧</div>
          <div style="font-family:Cormorant Garamond,serif;font-size:1.1em;
            font-weight:700;color:#1a1a1a">Renovation & Remodelling</div>
        </div>
        <div style="color:#666;font-size:0.84em;line-height:1.85;margin-bottom:10px">
          Complete makeovers, Kitchen upgrades, Premium flooring, Extensions</div>
        <span style="background:#fff8e1;color:#9a7a10;padding:3px 10px;border-radius:20px;
          font-size:0.7em;font-weight:700;border:1px solid #e8c840">
          📍 All Locations</span>
      </div>
      <div style="background:#fff;border-radius:8px;padding:22px;
        box-shadow:0 4px 18px rgba(0,0,0,0.07);border:1px solid #e0dcd0">
        <div style="display:flex;align-items:center;gap:12px;margin-bottom:12px">
          <div style="width:48px;height:48px;min-width:48px;
            background:linear-gradient(135deg,#fff8e1,#ffeaa0);border-radius:50%;
            display:flex;align-items:center;justify-content:center;
            font-size:1.4em;border:2px solid #f0d060">🏗️</div>
          <div style="font-family:Cormorant Garamond,serif;font-size:1.1em;
            font-weight:700;color:#1a1a1a">Foundation & Structural</div>
        </div>
        <div style="color:#666;font-size:0.84em;line-height:1.85;margin-bottom:10px">
          Deep foundation, RCC structures, Steel frame, Earthquake-resistant design</div>
        <span style="background:#fff8e1;color:#9a7a10;padding:3px 10px;border-radius:20px;
          font-size:0.7em;font-weight:700;border:1px solid #e8c840">
          📍 All Locations</span>
      </div>
      <div style="background:#fff;border-radius:8px;padding:22px;
        box-shadow:0 4px 18px rgba(0,0,0,0.07);border:1px solid #e0dcd0">
        <div style="display:flex;align-items:center;gap:12px;margin-bottom:12px">
          <div style="width:48px;height:48px;min-width:48px;
            background:linear-gradient(135deg,#fff8e1,#ffeaa0);border-radius:50%;
            display:flex;align-items:center;justify-content:center;
            font-size:1.4em;border:2px solid #f0d060">🎨</div>
          <div style="font-family:Cormorant Garamond,serif;font-size:1.1em;
            font-weight:700;color:#1a1a1a">Interior Construction</div>
        </div>
        <div style="color:#666;font-size:0.84em;line-height:1.85;margin-bottom:10px">
          False ceilings, Waterproofing, MEP, Modular fixtures, Premium finishes</div>
        <span style="background:#fff8e1;color:#9a7a10;padding:3px 10px;border-radius:20px;
          font-size:0.7em;font-weight:700;border:1px solid #e8c840">
          📍 All Locations</span>
      </div>
    </div>

    <br><br>
    """, unsafe_allow_html=True)

    sec_header("How We Work", "Our Build Process",
               "Transparent — from first meeting to final handover.")
    st.markdown("""
    <div class="grid-3 process-grid">
      <div style="background:#f9f7f2;border-radius:8px;padding:22px 14px;
        text-align:center;border:1px solid #e0dcd0">
        <div style="width:40px;height:40px;background:linear-gradient(135deg,#c9a227,#e8c040);
          border-radius:50%;display:flex;align-items:center;justify-content:center;
          font-family:Cormorant Garamond,serif;font-size:1.2em;font-weight:700;
          color:#fff;margin:0 auto 10px">1</div>
        <div style="font-family:Cormorant Garamond,serif;font-size:1.05em;
          color:#1a1a1a;font-weight:700;margin-bottom:6px">Consultation</div>
        <div style="color:#888;font-size:0.8em;line-height:1.6">
          Free meeting to understand your vision and requirements</div>
      </div>
      <div style="background:#f9f7f2;border-radius:8px;padding:22px 14px;
        text-align:center;border:1px solid #e0dcd0">
        <div style="width:40px;height:40px;background:linear-gradient(135deg,#c9a227,#e8c040);
          border-radius:50%;display:flex;align-items:center;justify-content:center;
          font-family:Cormorant Garamond,serif;font-size:1.2em;font-weight:700;
          color:#fff;margin:0 auto 10px">2</div>
        <div style="font-family:Cormorant Garamond,serif;font-size:1.05em;
          color:#1a1a1a;font-weight:700;margin-bottom:6px">Design</div>
        <div style="color:#888;font-size:0.8em;line-height:1.6">
          Plans, structural drawings and 3D visualisation</div>
      </div>
      <div style="background:#f9f7f2;border-radius:8px;padding:22px 14px;
        text-align:center;border:1px solid #e0dcd0">
        <div style="width:40px;height:40px;background:linear-gradient(135deg,#c9a227,#e8c040);
          border-radius:50%;display:flex;align-items:center;justify-content:center;
          font-family:Cormorant Garamond,serif;font-size:1.2em;font-weight:700;
          color:#fff;margin:0 auto 10px">3</div>
        <div style="font-family:Cormorant Garamond,serif;font-size:1.05em;
          color:#1a1a1a;font-weight:700;margin-bottom:6px">Quotation</div>
        <div style="color:#888;font-size:0.8em;line-height:1.6">
          Transparent itemised estimate with full material specs</div>
      </div>
      <div style="background:#f9f7f2;border-radius:8px;padding:22px 14px;
        text-align:center;border:1px solid #e0dcd0">
        <div style="width:40px;height:40px;background:linear-gradient(135deg,#c9a227,#e8c040);
          border-radius:50%;display:flex;align-items:center;justify-content:center;
          font-family:Cormorant Garamond,serif;font-size:1.2em;font-weight:700;
          color:#fff;margin:0 auto 10px">4</div>
        <div style="font-family:Cormorant Garamond,serif;font-size:1.05em;
          color:#1a1a1a;font-weight:700;margin-bottom:6px">Agreement</div>
        <div style="color:#888;font-size:0.8em;line-height:1.6">
          Clear contract with milestones and payment schedule</div>
      </div>
      <div style="background:#f9f7f2;border-radius:8px;padding:22px 14px;
        text-align:center;border:1px solid #e0dcd0">
        <div style="width:40px;height:40px;background:linear-gradient(135deg,#c9a227,#e8c040);
          border-radius:50%;display:flex;align-items:center;justify-content:center;
          font-family:Cormorant Garamond,serif;font-size:1.2em;font-weight:700;
          color:#fff;margin:0 auto 10px">5</div>
        <div style="font-family:Cormorant Garamond,serif;font-size:1.05em;
          color:#1a1a1a;font-weight:700;margin-bottom:6px">Construction</div>
        <div style="color:#888;font-size:0.8em;line-height:1.6">
          Quality build with real-time updates and site access</div>
      </div>
      <div style="background:#f9f7f2;border-radius:8px;padding:22px 14px;
        text-align:center;border:1px solid #e0dcd0">
        <div style="width:40px;height:40px;background:linear-gradient(135deg,#c9a227,#e8c040);
          border-radius:50%;display:flex;align-items:center;justify-content:center;
          font-family:Cormorant Garamond,serif;font-size:1.2em;font-weight:700;
          color:#fff;margin:0 auto 10px">6</div>
        <div style="font-family:Cormorant Garamond,serif;font-size:1.05em;
          color:#1a1a1a;font-weight:700;margin-bottom:6px">Handover</div>
        <div style="color:#888;font-size:0.8em;line-height:1.6">
          Final inspection, warranty resolution and keys</div>
      </div>
    </div>
    <br>
    """, unsafe_allow_html=True)

    _, ctr, _ = st.columns([2,1,2])
    with ctr:
        if st.button("📞 Get Free Quote", key="svc_cta"): go("Contact Us")

    inner_close()
    wrap_close()


# ═══════════════════════════════════════════════
# LOCATIONS PAGE
# ═══════════════════════════════════════════════
elif pg == "Locations":
    wrap_open("#f2f0eb")
    inner_open()
    sec_header("Where We Work", "Our Locations",
               "Serving the coastal belt from Karwar to Mangalore.")

    loc_data = {
        "Karwar":    {"lat":14.8135,"lon":74.1288,"projects":"200+",
                      "spec":"Residential, Commercial and Infrastructure",
                      "addr":"Near Dwarka Hotel, Habuwada Main Road","hq":True},
        "Ankola":    {"lat":14.6611,"lon":74.3016,"projects":"80+",
                      "spec":"Residential Construction",
                      "addr":"Ankola, Uttara Kannada","hq":False},
        "Honnawar":  {"lat":14.2797,"lon":74.4453,"projects":"70+",
                      "spec":"Residential and Infrastructure",
                      "addr":"Honnawar, Uttara Kannada","hq":False},
        "Mangalore": {"lat":12.9141,"lon":74.8560,"projects":"150+",
                      "spec":"Commercial and High-Rise",
                      "addr":"Mangalore, Dakshina Kannada","hq":False},
    }

    fmap = folium.Map(location=[14.0,74.5], zoom_start=8, tiles=None)
    folium.TileLayer(
        "https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}{r}.png",
        attr="CartoDB Positron"
    ).add_to(fmap)
    folium.PolyLine(
        [(d["lat"],d["lon"]) for d in loc_data.values()],
        color="#c9a227", weight=2.5, opacity=0.6, dash_array="8 5"
    ).add_to(fmap)

    for city, d in loc_data.items():
        sz = 46 if d["hq"] else 36
        sym = "★" if d["hq"] else "●"
        pin = (
            f'<div style="width:{sz}px;height:{sz}px;'
            f'background:linear-gradient(135deg,#9a7510,#c9a227,#f5d77e);'
            f'border-radius:50% 50% 50% 0;transform:rotate(-45deg);'
            f'border:3px solid #fff;box-shadow:0 4px 14px rgba(201,162,39,0.5);'
            f'display:flex;align-items:center;justify-content:center">'
            f'<span style="transform:rotate(45deg);color:#fff;'
            f'font-size:{sz//2-3}px;font-weight:900">{sym}</span></div>'
        )
        popup = (
            f'<div style="background:#fff;border-top:3px solid #c9a227;'
            f'border-radius:8px;padding:14px;min-width:180px;font-family:sans-serif">'
            f'<div style="color:#c9a227;font-weight:700;margin-bottom:8px">'
            f'{"HQ: " if d["hq"] else ""}{city}</div>'
            f'<div style="color:#555;font-size:0.82em;line-height:1.8">'
            f'Projects: <b style="color:#c9a227">{d["projects"]}</b><br>'
            f'Specialty: {d["spec"]}<br>Address: {d["addr"]}</div>'
            f'<div style="margin-top:10px;text-align:center">'
            f'<a href="tel:+919019429427" style="background:#c9a227;color:#fff;'
            f'padding:6px 12px;border-radius:4px;text-decoration:none;font-weight:700">'
            f'📞 Call Jason</a></div></div>'
        )
        folium.Marker(
            [d["lat"],d["lon"]],
            popup=folium.Popup(popup, max_width=220),
            tooltip=f'{city} — {d["projects"]} Projects',
            icon=folium.DivIcon(html=pin, icon_size=(sz,sz), icon_anchor=(sz//2,sz))
        ).add_to(fmap)
        folium.CircleMarker(
            [d["lat"],d["lon"]], radius=18 if d["hq"] else 13,
            color="#c9a227", fill=True, fill_color="#c9a227",
            fill_opacity=0.12, weight=2, opacity=0.5
        ).add_to(fmap)

    st.markdown(
        '<div style="border-radius:10px;overflow:hidden;'
        'box-shadow:0 6px 26px rgba(0,0,0,0.1);border:2px solid #ddd">',
        unsafe_allow_html=True
    )
    st_folium(fmap, width=None, height=460, returned_objects=[])
    st.markdown('</div><br>', unsafe_allow_html=True)

    st.markdown("""
    <div class="grid-4">
      <div style="background:#fff;border-radius:8px;padding:18px 14px;
        box-shadow:0 4px 18px rgba(0,0,0,0.07);border:1px solid #e0dcd0;
        border-top:4px solid #c9a227">
        <div style="color:#c9a227;font-size:0.6em;font-weight:700;
          letter-spacing:2px;text-transform:uppercase;margin-bottom:6px">HEADQUARTERS</div>
        <div style="font-family:Cormorant Garamond,serif;font-size:1.3em;
          color:#1a1a1a;font-weight:700;margin-bottom:6px">📍 Karwar</div>
        <div style="font-family:Cormorant Garamond,serif;font-size:2em;
          color:#c9a227;font-weight:700;margin-bottom:6px">200+</div>
        <div style="color:#666;font-size:0.82em;margin-bottom:8px">
          Residential, Commercial and Infrastructure</div>
        <div style="color:#bbb;font-size:0.72em;border-top:1px solid #f0ede4;
          padding-top:8px">Near Dwarka Hotel, Habuwada Main Road</div>
      </div>
      <div style="background:#fff;border-radius:8px;padding:18px 14px;
        box-shadow:0 4px 18px rgba(0,0,0,0.07);border:1px solid #e0dcd0;
        border-top:4px solid #c9a227">
        <div style="color:#888;font-size:0.6em;font-weight:700;
          letter-spacing:2px;text-transform:uppercase;margin-bottom:6px">ACTIVE OPS</div>
        <div style="font-family:Cormorant Garamond,serif;font-size:1.3em;
          color:#1a1a1a;font-weight:700;margin-bottom:6px">📍 Ankola</div>
        <div style="font-family:Cormorant Garamond,serif;font-size:2em;
          color:#c9a227;font-weight:700;margin-bottom:6px">80+</div>
        <div style="color:#666;font-size:0.82em;margin-bottom:8px">
          Residential Construction</div>
        <div style="color:#bbb;font-size:0.72em;border-top:1px solid #f0ede4;
          padding-top:8px">Ankola, Uttara Kannada</div>
      </div>
      <div style="background:#fff;border-radius:8px;padding:18px 14px;
        box-shadow:0 4px 18px rgba(0,0,0,0.07);border:1px solid #e0dcd0;
        border-top:4px solid #c9a227">
        <div style="color:#888;font-size:0.6em;font-weight:700;
          letter-spacing:2px;text-transform:uppercase;margin-bottom:6px">ACTIVE OPS</div>
        <div style="font-family:Cormorant Garamond,serif;font-size:1.3em;
          color:#1a1a1a;font-weight:700;margin-bottom:6px">📍 Honnawar</div>
        <div style="font-family:Cormorant Garamond,serif;font-size:2em;
          color:#c9a227;font-weight:700;margin-bottom:6px">70+</div>
        <div style="color:#666;font-size:0.82em;margin-bottom:8px">
          Residential and Infrastructure</div>
        <div style="color:#bbb;font-size:0.72em;border-top:1px solid #f0ede4;
          padding-top:8px">Honnawar, Uttara Kannada</div>
      </div>
      <div style="background:#fff;border-radius:8px;padding:18px 14px;
        box-shadow:0 4px 18px rgba(0,0,0,0.07);border:1px solid #e0dcd0;
        border-top:4px solid #c9a227">
        <div style="color:#888;font-size:0.6em;font-weight:700;
          letter-spacing:2px;text-transform:uppercase;margin-bottom:6px">COMMERCIAL HUB</div>
        <div style="font-family:Cormorant Garamond,serif;font-size:1.3em;
          color:#1a1a1a;font-weight:700;margin-bottom:6px">📍 Mangalore</div>
        <div style="font-family:Cormorant Garamond,serif;font-size:2em;
          color:#c9a227;font-weight:700;margin-bottom:6px">150+</div>
        <div style="color:#666;font-size:0.82em;margin-bottom:8px">
          Commercial and High-Rise</div>
        <div style="color:#bbb;font-size:0.72em;border-top:1px solid #f0ede4;
          padding-top:8px">Mangalore, Dakshina Kannada</div>
      </div>
    </div>
    """, unsafe_allow_html=True)

    inner_close()
    wrap_close()


# ═══════════════════════════════════════════════
# ABOUT US PAGE
# ═══════════════════════════════════════════════
elif pg == "About Us":
    owner_b64 = img_to_b64("jason_photo.jpg")

    wrap_open("#f2f0eb")
    inner_open()
    sec_header("Who We Are", "About JDF Constructions")

    owner_img_html = (
        f'<img src="data:image/jpeg;base64,{owner_b64}" '
        f'style="width:100%;border-radius:8px 8px 0 0;object-fit:cover;'
        f'object-position:top center;display:block;max-height:280px">'
    ) if owner_b64 else (
        '<div style="background:#2d2000;border-radius:8px 8px 0 0;height:240px;'
        'display:flex;align-items:center;justify-content:center;font-size:5em">👤</div>'
    )

    st.markdown(f"""
    <div class="grid-1-2">
      <!-- Left: owner card -->
      <div>
        {owner_img_html}
        <div style="background:#fff;border-radius:0 0 8px 8px;padding:20px;
          box-shadow:0 4px 18px rgba(0,0,0,0.07);border:1px solid #e0dcd0;
          border-top:4px solid #c9a227;text-align:center">
          <div style="font-family:Cormorant Garamond,serif;font-size:1.5em;
            font-weight:700;color:#1a1a1a">Jason Fernandes</div>
          <div style="font-family:Montserrat,sans-serif;font-size:0.6em;
            letter-spacing:2px;color:#c9a227;text-transform:uppercase;
            font-weight:700;margin:5px 0 10px">Founder and Managing Director</div>
          <div style="color:#777;font-size:0.82em;line-height:1.7;margin-bottom:12px">
            15+ years building exceptional structures across coastal Karnataka.</div>
          <a href="tel:+919019429427"
            style="display:inline-block;
            background:linear-gradient(135deg,#c9a227,#e8c040);
            color:#fff;padding:10px 22px;border-radius:5px;font-weight:700;
            text-decoration:none;font-size:0.84em">📱 90194 29427</a>
        </div>
      </div>

      <!-- Right: story -->
      <div style="padding:0 0 0 8px">
        <div style="font-family:Cormorant Garamond,serif;font-size:clamp(1.4em,3vw,2em);
          font-weight:700;color:#1a1a1a;margin-bottom:14px">Our Story</div>
        <div style="color:#555;line-height:1.9;font-size:0.9em">
          <p style="margin-bottom:12px">JDF Constructions was founded with a singular
          vision — to bring <strong>world-class construction quality</strong>
          to the beautiful coastal belt of Karnataka.</p>
          <p style="margin-bottom:12px">Under the leadership of
          <strong style="color:#c9a227">Jason Fernandes</strong>, the company has grown
          into one of the most trusted construction brands across Uttara Kannada
          and Dakshina Kannada districts.</p>
          <p style="margin-bottom:12px">Starting from <strong>Karwar</strong>,
          JDF has expanded to <strong>Ankola</strong>, <strong>Honnawar</strong> and
          <strong>Mangalore</strong>.</p>
          <p style="font-family:Cormorant Garamond,serif;font-size:1.15em;
            color:#c9a227;font-style:italic">"Your dream project starts here."</p>
        </div>
        <br>
        <div class="grid-2">
          <div style="background:#fff;border-radius:8px;padding:16px;
            box-shadow:0 2px 10px rgba(0,0,0,0.06);
            border:1px solid #e0dcd0;border-left:3px solid #c9a227">
            <div style="font-size:1.4em;margin-bottom:6px">🎯</div>
            <div style="font-family:Cormorant Garamond,serif;font-size:1em;
              font-weight:700;color:#1a1a1a;margin-bottom:3px">Mission</div>
            <div style="color:#888;font-size:0.8em">
              Superior construction with integrity.</div>
          </div>
          <div style="background:#fff;border-radius:8px;padding:16px;
            box-shadow:0 2px 10px rgba(0,0,0,0.06);
            border:1px solid #e0dcd0;border-left:3px solid #c9a227">
            <div style="font-size:1.4em;margin-bottom:6px">👁️</div>
            <div style="font-family:Cormorant Garamond,serif;font-size:1em;
              font-weight:700;color:#1a1a1a;margin-bottom:3px">Vision</div>
            <div style="color:#888;font-size:0.8em">
              Karnataka's most trusted builder.</div>
          </div>
          <div style="background:#fff;border-radius:8px;padding:16px;
            box-shadow:0 2px 10px rgba(0,0,0,0.06);
            border:1px solid #e0dcd0;border-left:3px solid #c9a227">
            <div style="font-size:1.4em;margin-bottom:6px">💎</div>
            <div style="font-family:Cormorant Garamond,serif;font-size:1em;
              font-weight:700;color:#1a1a1a;margin-bottom:3px">Values</div>
            <div style="color:#888;font-size:0.8em">
              Quality, Integrity, Innovation</div>
          </div>
          <div style="background:#fff;border-radius:8px;padding:16px;
            box-shadow:0 2px 10px rgba(0,0,0,0.06);
            border:1px solid #e0dcd0;border-left:3px solid #c9a227">
            <div style="font-size:1.4em;margin-bottom:6px">🏅</div>
            <div style="font-family:Cormorant Garamond,serif;font-size:1em;
              font-weight:700;color:#1a1a1a;margin-bottom:3px">Commitment</div>
            <div style="color:#888;font-size:0.8em">
              Every project is our own home.</div>
          </div>
        </div>
      </div>
    </div>

    <br><br>
    """, unsafe_allow_html=True)

    sec_header("Expertise", "Skills and Capabilities")
    st.markdown("""
    <div class="grid-2">
      <div>
        <div style="display:flex;justify-content:space-between;margin-bottom:6px">
          <span style="font-size:0.84em;font-weight:600;color:#333">
            Residential Construction</span>
          <span style="color:#c9a227;font-weight:700;font-size:0.84em">95%</span>
        </div>
        <div style="background:#e8e4d8;border-radius:50px;height:6px;overflow:hidden;margin-bottom:16px">
          <div style="height:100%;width:95%;
            background:linear-gradient(90deg,#c9a227,#f5d77e);border-radius:50px"></div>
        </div>
        <div style="display:flex;justify-content:space-between;margin-bottom:6px">
          <span style="font-size:0.84em;font-weight:600;color:#333">
            Infrastructure and Civil</span>
          <span style="color:#c9a227;font-weight:700;font-size:0.84em">82%</span>
        </div>
        <div style="background:#e8e4d8;border-radius:50px;height:6px;overflow:hidden;margin-bottom:16px">
          <div style="height:100%;width:82%;
            background:linear-gradient(90deg,#c9a227,#f5d77e);border-radius:50px"></div>
        </div>
        <div style="display:flex;justify-content:space-between;margin-bottom:6px">
          <span style="font-size:0.84em;font-weight:600;color:#333">
            Project Management</span>
          <span style="color:#c9a227;font-weight:700;font-size:0.84em">93%</span>
        </div>
        <div style="background:#e8e4d8;border-radius:50px;height:6px;overflow:hidden">
          <div style="height:100%;width:93%;
            background:linear-gradient(90deg,#c9a227,#f5d77e);border-radius:50px"></div>
        </div>
      </div>
      <div>
        <div style="display:flex;justify-content:space-between;margin-bottom:6px">
          <span style="font-size:0.84em;font-weight:600;color:#333">
            Commercial Projects</span>
          <span style="color:#c9a227;font-weight:700;font-size:0.84em">88%</span>
        </div>
        <div style="background:#e8e4d8;border-radius:50px;height:6px;overflow:hidden;margin-bottom:16px">
          <div style="height:100%;width:88%;
            background:linear-gradient(90deg,#c9a227,#f5d77e);border-radius:50px"></div>
        </div>
        <div style="display:flex;justify-content:space-between;margin-bottom:6px">
          <span style="font-size:0.84em;font-weight:600;color:#333">
            Interior Construction</span>
          <span style="color:#c9a227;font-weight:700;font-size:0.84em">90%</span>
        </div>
        <div style="background:#e8e4d8;border-radius:50px;height:6px;overflow:hidden;margin-bottom:16px">
          <div style="height:100%;width:90%;
            background:linear-gradient(90deg,#c9a227,#f5d77e);border-radius:50px"></div>
        </div>
        <div style="display:flex;justify-content:space-between;margin-bottom:6px">
          <span style="font-size:0.84em;font-weight:600;color:#333">
            Client Satisfaction</span>
          <span style="color:#c9a227;font-weight:700;font-size:0.84em">98%</span>
        </div>
        <div style="background:#e8e4d8;border-radius:50px;height:6px;overflow:hidden">
          <div style="height:100%;width:98%;
            background:linear-gradient(90deg,#c9a227,#f5d77e);border-radius:50px"></div>
        </div>
      </div>
    </div>

    <br><br>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="grid-4">
      <div style="background:#fff;border-radius:8px;padding:20px 14px;
        text-align:center;box-shadow:0 3px 14px rgba(0,0,0,0.06);border:1px solid #e0dcd0">
        <div style="font-size:1.8em;margin-bottom:8px">🏅</div>
        <div style="font-family:Cormorant Garamond,serif;font-size:0.95em;
          color:#1a1a1a;font-weight:700;margin-bottom:4px">Licensed Contractor</div>
        <div style="color:#aaa;font-size:0.73em">Karnataka PWD Certified</div>
      </div>
      <div style="background:#fff;border-radius:8px;padding:20px 14px;
        text-align:center;box-shadow:0 3px 14px rgba(0,0,0,0.06);border:1px solid #e0dcd0">
        <div style="font-size:1.8em;margin-bottom:8px">📋</div>
        <div style="font-family:Cormorant Garamond,serif;font-size:0.95em;
          color:#1a1a1a;font-weight:700;margin-bottom:4px">RERA Compliant</div>
        <div style="color:#aaa;font-size:0.73em">All projects registered</div>
      </div>
      <div style="background:#fff;border-radius:8px;padding:20px 14px;
        text-align:center;box-shadow:0 3px 14px rgba(0,0,0,0.06);border:1px solid #e0dcd0">
        <div style="font-size:1.8em;margin-bottom:8px">🌱</div>
        <div style="font-family:Cormorant Garamond,serif;font-size:0.95em;
          color:#1a1a1a;font-weight:700;margin-bottom:4px">Green Building</div>
        <div style="color:#aaa;font-size:0.73em">Eco-friendly certified</div>
      </div>
      <div style="background:#fff;border-radius:8px;padding:20px 14px;
        text-align:center;box-shadow:0 3px 14px rgba(0,0,0,0.06);border:1px solid #e0dcd0">
        <div style="font-size:1.8em;margin-bottom:8px">🔒</div>
        <div style="font-family:Cormorant Garamond,serif;font-size:0.95em;
          color:#1a1a1a;font-weight:700;margin-bottom:4px">Quality Standards</div>
        <div style="color:#aaa;font-size:0.73em">ISO-aligned QMS</div>
      </div>
    </div>
    <br>
    """, unsafe_allow_html=True)

    inner_close()
    wrap_close()


# ═══════════════════════════════════════════════
# CONTACT US PAGE
# ═══════════════════════════════════════════════
elif pg == "Contact Us":
    wrap_open("#f2f0eb")
    inner_open()
    sec_header("Get In Touch", "Contact JDF Constructions",
               "Ready to build? Reach out for a free consultation.")

    # Contact form uses st.columns (needed for Streamlit form widgets)
    cf1, cf2 = st.columns([1.5, 1])

    with cf1:
        st.markdown(
            '<div style="background:#fff;border-radius:8px;padding:24px;'
            'box-shadow:0 4px 18px rgba(0,0,0,0.07);border:1px solid #e0dcd0">'
            '<div style="font-family:Cormorant Garamond,serif;font-size:1.3em;'
            'font-weight:700;color:#1a1a1a;margin-bottom:16px;padding-bottom:10px;'
            'border-bottom:2px solid #f0ede4">📝 Send Us a Message</div>',
            unsafe_allow_html=True
        )
        with st.form("enquiry_form", clear_on_submit=True):
            name   = st.text_input("Full Name", placeholder="e.g. Ravi Kumar")
            phone  = st.text_input("Phone Number", placeholder="e.g. 9876543210")
            email  = st.text_input("Email (optional)", placeholder="you@email.com")
            city   = st.selectbox("Your City",
                ["Karwar","Ankola","Honnawar","Mangalore","Other"])
            ptype  = st.selectbox("Project Type", [
                "Residential Home","Commercial Building",
                "Renovation","Infrastructure","Interior Work","Other"])
            budget = st.selectbox("Approximate Budget", [
                "Under Rs.10 Lakhs","Rs.10-25 Lakhs","Rs.25-50 Lakhs",
                "Rs.50 Lakhs-1 Crore","Above Rs.1 Crore"])
            msg    = st.text_area("Project Details",
                placeholder="Describe your site, timeline, requirements...", height=100)
            if st.form_submit_button("Submit Enquiry"):
                if name.strip() and phone.strip():
                    st.success(
                        f"Thank you {name}! Enquiry for {ptype} in {city} received. "
                        f"Jason will call {phone} within 24 hours.")
                    st.balloons()
                else:
                    st.error("Please enter your name and phone number.")
        st.markdown('</div>', unsafe_allow_html=True)

    with cf2:
        st.markdown("""
        <div style="background:#fff;border-radius:8px;padding:20px;
          box-shadow:0 4px 18px rgba(0,0,0,0.07);border:1px solid #e0dcd0;
          margin-bottom:12px">
          <div style="font-family:Cormorant Garamond,serif;font-size:1.15em;
            font-weight:700;color:#1a1a1a;margin-bottom:12px;padding-bottom:8px;
            border-bottom:2px solid #f0ede4">Our Details</div>
          <div style="padding:8px 0;border-bottom:1px solid #f5f2ea">
            <span style="color:#c9a227;font-weight:700;font-size:0.9em">
              Jason Fernandes</span><br>
            <span style="color:#bbb;font-size:0.73em">Founder and Managing Director</span>
          </div>
          <div style="padding:8px 0;border-bottom:1px solid #f5f2ea;font-size:0.86em">
            📱 <strong>90194 29427</strong><br>
            <span style="color:#bbb;font-size:0.74em">Call or WhatsApp</span>
          </div>
          <div style="padding:8px 0;border-bottom:1px solid #f5f2ea;
            font-size:0.84em;color:#444">
            📍 Near Dwarka Hotel, Habuwada Main Road<br>
            <span style="color:#bbb;font-size:0.8em">Karwar, Karnataka — 581 301</span>
          </div>
          <div style="padding:8px 0;border-bottom:1px solid #f5f2ea;
            font-size:0.84em;color:#444">
            🕐 Mon – Sat, 9 AM to 7 PM
          </div>
          <div style="padding:8px 0;font-size:0.84em;color:#444">
            🏙️ Karwar, Ankola, Honnawar, Mangalore
          </div>
        </div>

        <div style="background:#fff;border-radius:8px;padding:20px;
          box-shadow:0 4px 18px rgba(0,0,0,0.07);border:1px solid #e0dcd0">
          <div style="font-family:Cormorant Garamond,serif;font-size:1.15em;
            font-weight:700;color:#1a1a1a;margin-bottom:12px;padding-bottom:8px;
            border-bottom:2px solid #f0ede4">Quick Connect</div>
          <a href="tel:+919019429427"
            style="display:block;text-align:center;padding:11px;border-radius:6px;
            text-decoration:none;font-weight:700;font-size:0.83em;margin-bottom:8px;
            background:linear-gradient(135deg,#c9a227,#e8c040);color:#fff">
            📞 Call: 90194 29427</a>
          <a href="https://wa.me/919019429427" target="_blank"
            style="display:block;text-align:center;padding:11px;border-radius:6px;
            text-decoration:none;font-weight:700;font-size:0.83em;margin-bottom:8px;
            background:linear-gradient(135deg,#25D366,#128C7E);color:#fff">
            💬 WhatsApp Jason</a>
          <a href="https://maps.google.com/?q=Dwarka+Hotel+Habuwada+Karwar"
            target="_blank"
            style="display:block;text-align:center;padding:11px;border-radius:6px;
            text-decoration:none;font-weight:700;font-size:0.83em;
            background:linear-gradient(135deg,#1a73e8,#4285F4);color:#fff">
            🗺️ Get Directions</a>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    sec_header("Find Us", "Our Headquarters in Karwar")
    hq = folium.Map(location=[14.8135,74.1288], zoom_start=15, tiles=None)
    folium.TileLayer(
        "https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}{r}.png",
        attr="CartoDB"
    ).add_to(hq)
    hq_pin = (
        '<div style="width:54px;height:54px;'
        'background:linear-gradient(135deg,#9a7510,#c9a227,#f5d77e);'
        'border-radius:50%;border:3px solid #fff;'
        'box-shadow:0 0 20px rgba(201,162,39,0.7);'
        'display:flex;align-items:center;justify-content:center;font-size:24px">🏗️</div>'
    )
    folium.Marker(
        [14.8135,74.1288],
        popup=folium.Popup(
            '<div style="padding:12px;min-width:180px;font-family:sans-serif">'
            '<b style="color:#c9a227">JDF Constructions HQ</b><br><br>'
            'Near Dwarka Hotel<br>Habuwada Main Road, Karwar<br>'
            'Karnataka 581 301<br><br>'
            '<a href="tel:+919019429427" style="background:#c9a227;color:#fff;'
            'padding:6px 12px;border-radius:4px;text-decoration:none;font-weight:700">'
            '📞 90194 29427</a></div>', max_width=220
        ),
        tooltip="JDF Constructions Headquarters",
        icon=folium.DivIcon(html=hq_pin, icon_size=(54,54), icon_anchor=(27,27))
    ).add_to(hq)
    st.markdown(
        '<div style="border-radius:10px;overflow:hidden;'
        'box-shadow:0 6px 26px rgba(0,0,0,0.1);border:2px solid #ddd">',
        unsafe_allow_html=True
    )
    st_folium(hq, width=None, height=380, returned_objects=[])
    st.markdown('</div>', unsafe_allow_html=True)

    inner_close()
    wrap_close()


# ── FOOTER
st.markdown("""
<div style="background:linear-gradient(135deg,#1c1400,#2d2000,#1a1200);
  padding:40px 30px 24px;width:100%">
  <div class="footer-grid" style="max-width:1100px;margin:0 auto;display:flex;
    justify-content:space-between;flex-wrap:wrap;gap:24px">

    <div style="min-width:200px">
      <div style="font-family:Cormorant Garamond,serif;font-size:1.6em;
        color:#c9a227;font-weight:700;letter-spacing:2px;margin-bottom:6px">
        🏗️ JDF CONSTRUCTIONS</div>
      <div style="color:rgba(201,162,39,0.55);font-style:italic;
        font-family:Cormorant Garamond,serif;font-size:1em;margin-bottom:8px">
        "Your dream project starts here."</div>
      <div style="color:#4a4000;font-size:0.78em">
        Karwar | Ankola | Honnawar | Mangalore</div>
    </div>

    <div style="color:#4a4000;font-size:0.8em;line-height:2.1;min-width:160px">
      <div style="color:rgba(201,162,39,0.55);font-weight:700;
        margin-bottom:6px;letter-spacing:1px;font-size:0.85em">CONTACT</div>
      <div>📍 Habuwada Main Road, Karwar</div>
      <div>📞 +91 90194 29427</div>
      <div>🕐 Mon–Sat, 9 AM to 7 PM</div>
    </div>

    <div style="color:#4a4000;font-size:0.8em;line-height:2.3;min-width:130px">
      <div style="color:rgba(201,162,39,0.55);font-weight:700;
        margin-bottom:6px;letter-spacing:1px;font-size:0.85em">PAGES</div>
      <div>Home | Services | Locations</div>
      <div>About Us | Contact Us</div>
    </div>
  </div>

  <div style="border-top:1px solid #2a2000;margin-top:20px;padding-top:16px;
    text-align:center">
    <div style="color:#3a3000;font-size:0.74em">
      © 2024 JDF Constructions. All Rights Reserved.</div>
  </div>
</div>
""", unsafe_allow_html=True)