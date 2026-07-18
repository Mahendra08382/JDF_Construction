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

def load_img(fn):
    p = os.path.join(os.path.dirname(os.path.abspath(__file__)), fn)
    return Image.open(p) if os.path.exists(p) else None

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
div[data-testid="column"] {
    padding: 0 !important;
}

/* ── GOLDEN NAV BUTTONS ── */
.stButton > button {
    background-color: #c9a227 !important;
    background: #c9a227 !important;
    color: #ffffff !important;
    border: 2px solid #c9a227 !important;
    border-radius: 8px !important;
    font-weight: 700 !important;
    letter-spacing: 1.5px !important;
    font-size: 0.72em !important;
    padding: 10px 8px !important;
    width: 100% !important;
    box-shadow: 0 4px 15px rgba(201,162,39,0.3) !important;
    transition: all 0.2s !important;
    white-space: nowrap !important;
}
.stButton > button:hover {
    background-color: #a8841f !important;
    background: #a8841f !important;
    color: #ffffff !important;
    border-color: #a8841f !important;
    transform: translateY(-1px) !important;
    box-shadow: 0 6px 20px rgba(201,162,39,0.5) !important;
}
.stButton > button:focus,
.stButton > button:active {
    background-color: #c9a227 !important;
    background: #c9a227 !important;
    color: #ffffff !important;
    border-color: #c9a227 !important;
}

/* Form */
.stForm [data-testid="stFormSubmitButton"] > button {
    background: linear-gradient(135deg, #c9a227, #e8c040) !important;
    color: #fff !important;
    border: none !important;
    border-radius: 5px !important;
    padding: 12px 32px !important;
    font-weight: 700 !important;
    width: 100% !important;
}
.stTextInput > div > div > input,
.stTextArea > div > div > textarea {
    background: #fff !important;
    border: 1.5px solid #ddd !important;
    color: #333 !important;
    border-radius: 5px !important;
}
.stSelectbox > div > div {
    background: #fff !important;
    border: 1.5px solid #ddd !important;
    color: #333 !important;
    border-radius: 5px !important;
}
.stTextInput label, .stTextArea label, .stSelectbox label {
    color: #333 !important;
    font-size: 0.85em !important;
    font-weight: 600 !important;
}
div[data-testid="stVerticalBlock"] > div {
    padding: 0 !important;
}

/* ── MOBILE RESPONSIVE ── */
@media (max-width: 768px) {
    .hero-main-row {
        flex-direction: column !important;
        min-height: auto !important;
    }
    .hero-logo-col {
        width: 100% !important;
        min-width: 100% !important;
        border-right: none !important;
        border-bottom: 1px solid rgba(201,162,39,0.2) !important;
        padding: 20px !important;
    }
    .hero-logo-col img {
        width: 100px !important;
    }
    .hero-center-col {
        padding: 30px 20px !important;
    }
    .hero-center-col .jdf-title {
        font-size: 3.5em !important;
    }
    .hero-owner-col {
        width: 100% !important;
        min-width: 100% !important;
        border-left: none !important;
        border-top: 1px solid rgba(201,162,39,0.2) !important;
        padding: 20px !important;
    }
    .stats-bar {
        flex-direction: column !important;
        padding: 20px !important;
        gap: 0 !important;
    }
    .stat-item {
        border-right: none !important;
        border-bottom: 1px solid rgba(201,162,39,0.2) !important;
        padding: 16px 0 !important;
    }
    .stat-item:last-child {
        border-bottom: none !important;
    }
    .info-bar {
        flex-direction: column !important;
        gap: 4px !important;
        padding: 10px 16px !important;
        font-size: 0.7em !important;
    }
    .section-grid-2,
    .section-grid-3,
    .section-grid-4 {
        flex-direction: column !important;
    }
    .card {
        margin: 0 0 16px 0 !important;
        width: 100% !important;
    }
}

::-webkit-scrollbar { width: 5px; }
::-webkit-scrollbar-track { background: #f0ede4; }
::-webkit-scrollbar-thumb { background: #c9a227; border-radius: 3px; }
</style>
""", unsafe_allow_html=True)

# ── TOP INFO BAR
st.markdown(
    '<div class="info-bar" style="background:#9a7a10;padding:8px 50px;display:flex;'
    'justify-content:space-between;align-items:center;flex-wrap:wrap;gap:4px;'
    'font-size:0.78em;color:#fff;font-family:Montserrat,sans-serif">'
    '<span>📍 Near Dwarka Hotel, Habuwada Main Road, Karwar, Karnataka</span>'
    '<span>✉ jdfconstructions@gmail.com &nbsp;&nbsp;'
    '<a href="tel:+919019429427" style="color:#fff;text-decoration:none">📞 +91 90194 29427</a>'
    '</span></div>',
    unsafe_allow_html=True
)

# ── NAVBAR brand
st.markdown(
    '<div style="background:#fff;border-bottom:3px solid #c9a227;'
    'padding:0 20px 0 30px;min-height:64px;display:flex;align-items:center;'
    'justify-content:space-between;flex-wrap:wrap;'
    'box-shadow:0 2px 10px rgba(0,0,0,0.06)">'
    '<span style="font-family:Cormorant Garamond,serif;font-size:1.4em;'
    'font-weight:700;color:#b8960c;letter-spacing:2px;padding:10px 0">'
    '🏗️ JDF CONSTRUCTIONS</span>'
    '</div>',
    unsafe_allow_html=True
)

# ── NAV BUTTONS
n = st.columns([0.5, 1, 1, 1, 1, 1, 0.5])
with n[1]:
    if st.button("HOME", key="n1"): go("Home")
with n[2]:
    if st.button("SERVICES", key="n2"): go("Services")
with n[3]:
    if st.button("LOCATIONS", key="n3"): go("Locations")
with n[4]:
    if st.button("ABOUT US", key="n4"): go("About Us")
with n[5]:
    if st.button("CONTACT", key="n5"): go("Contact Us")

# ── Reduce spacing after nav
st.markdown('<div style="margin-top:-10px"></div>', unsafe_allow_html=True)

# ── HELPER: section header
def sec_header(overline, title, desc=""):
    desc_html = (
        '<p style="color:#777;font-size:0.92em;max-width:520px;'
        'margin:0 auto;line-height:1.75;padding:0 10px">' + desc + '</p>'
    ) if desc else ""
    st.markdown(
        '<div style="text-align:center;margin-bottom:18px;padding:0 10px">'
        '<span style="font-family:Montserrat,sans-serif;font-size:0.7em;'
        'letter-spacing:4px;text-transform:uppercase;'
        'color:#c9a227;font-weight:700;display:block;margin-bottom:6px">'
        + overline + '</span>'
        '<div style="font-family:Cormorant Garamond,serif;font-size:clamp(1.8em,4vw,2.5em);'
        'font-weight:700;color:#1a1a1a;margin:0 0 12px;line-height:1.15">'
        + title + '</div>'
        + desc_html +
        '<div style="width:52px;height:2px;'
        'background:linear-gradient(90deg,#c9a227,#f5d77e);'
        'margin:14px auto;border-radius:2px"></div></div>',
        unsafe_allow_html=True
    )

# ───────────────────────────────────────────────
# HOME PAGE
# ───────────────────────────────────────────────
if pg == "Home":
    logo_b64  = img_to_b64("jdf_logo.png")
    owner_b64 = img_to_b64("jason_photo.jpg")

    logo_html = (
        '<img src="data:image/png;base64,' + logo_b64 + '" '
        'style="width:clamp(80px,12vw,160px);border-radius:8px;'
        'box-shadow:0 4px 20px rgba(0,0,0,0.5)">'
    ) if logo_b64 else '<span style="font-size:4em">🏗️</span>'

    owner_html = (
        '<img src="data:image/jpeg;base64,' + owner_b64 + '" '
        'style="width:100%;height:clamp(140px,20vw,200px);object-fit:cover;'
        'object-position:top center;display:block;border-radius:6px 6px 0 0">'
    ) if owner_b64 else (
        '<div style="height:180px;background:#2d2000;border-radius:6px 6px 0 0;'
        'display:flex;align-items:center;justify-content:center;font-size:4em">👤</div>'
    )

    st.markdown(
        '<div style="background:linear-gradient(135deg,#1c1400 0%,#2d2000 50%,#1a1200 100%);'
        'border-bottom:4px solid #c9a227;width:100%">'

        # TOP ROW
        '<div class="hero-main-row" style="display:flex;width:100%;flex-wrap:wrap;min-height:360px">'

        # LEFT logo
        '<div class="hero-logo-col" style="width:180px;min-width:180px;display:flex;'
        'align-items:center;justify-content:center;padding:24px;'
        'border-right:1px solid rgba(201,162,39,0.2)">'
        + logo_html +
        '</div>'

        # CENTER
        '<div class="hero-center-col" style="flex:1;min-width:260px;display:flex;'
        'align-items:center;justify-content:center;text-align:center;padding:40px 20px">'
        '<div>'
        '<div style="font-family:Montserrat,sans-serif;font-size:clamp(0.5em,1.5vw,0.68em);'
        'letter-spacing:4px;text-transform:uppercase;'
        'color:rgba(201,162,39,0.65);font-weight:600;margin-bottom:14px">'
        "KARNATAKA'S PREMIER CONSTRUCTION COMPANY</div>"
        '<div class="jdf-title" style="font-family:Cormorant Garamond,serif;'
        'font-size:clamp(3em,8vw,5.5em);'
        'font-weight:700;color:#ffffff;line-height:0.9;letter-spacing:3px">JDF</div>'
        '<div style="font-family:Cormorant Garamond,serif;font-size:clamp(1.1em,3vw,1.8em);'
        'font-weight:600;color:#c9a227;letter-spacing:6px;'
        'text-transform:uppercase;margin:10px 0 14px">CONSTRUCTIONS</div>'
        '<div style="width:50px;height:2px;'
        'background:linear-gradient(90deg,#c9a227,#f5d77e);margin:0 auto 16px"></div>'
        '<div style="font-family:Cormorant Garamond,serif;'
        'font-size:clamp(1em,2.5vw,1.3em);'
        'color:#d4c898;font-style:italic;margin-bottom:22px">'
        '"Your dream project starts here."</div>'
        '<div style="display:flex;flex-wrap:wrap;justify-content:center;gap:6px">'
        '<span style="display:inline-block;border:1px solid rgba(201,162,39,0.5);'
        'color:#c9a227;padding:6px 14px;border-radius:30px;font-size:0.72em;'
        'font-weight:600;background:rgba(201,162,39,0.1)">📍 Karwar</span>'
        '<span style="display:inline-block;border:1px solid rgba(201,162,39,0.5);'
        'color:#c9a227;padding:6px 14px;border-radius:30px;font-size:0.72em;'
        'font-weight:600;background:rgba(201,162,39,0.1)">📍 Ankola</span>'
        '<span style="display:inline-block;border:1px solid rgba(201,162,39,0.5);'
        'color:#c9a227;padding:6px 14px;border-radius:30px;font-size:0.72em;'
        'font-weight:600;background:rgba(201,162,39,0.1)">📍 Honnawar</span>'
        '<span style="display:inline-block;border:1px solid rgba(201,162,39,0.5);'
        'color:#c9a227;padding:6px 14px;border-radius:30px;font-size:0.72em;'
        'font-weight:600;background:rgba(201,162,39,0.1)">📍 Mangalore</span>'
        '</div></div></div>'

        # RIGHT owner
        '<div class="hero-owner-col" style="width:200px;min-width:200px;display:flex;'
        'align-items:center;justify-content:center;padding:24px;'
        'border-left:1px solid rgba(201,162,39,0.2)">'
        '<div style="width:160px">'
        + owner_html +
        '<div style="background:#ffffff;border-radius:0 0 8px 8px;'
        'border-top:3px solid #c9a227;padding:12px;text-align:center">'
        '<div style="font-family:Cormorant Garamond,serif;font-size:1em;'
        'font-weight:700;color:#1a1a1a;line-height:1.2">Jason Fernandes</div>'
        '<div style="font-family:Montserrat,sans-serif;font-size:0.58em;'
        'letter-spacing:2px;color:#c9a227;text-transform:uppercase;'
        'font-weight:700;margin:4px 0 5px">Founder &amp; Owner</div>'
        '<div style="font-family:Montserrat,sans-serif;font-size:0.75em;'
        'color:#444;font-weight:600">📞 90194 29427</div>'
        '</div></div></div>'
        '</div>'  # end top row

        # STATS BAR
        '<div class="stats-bar" style="border-top:1px solid rgba(201,162,39,0.25);'
        'padding:28px 40px;display:flex;justify-content:space-around;'
        'align-items:center;flex-wrap:wrap;gap:0">'

        '<div class="stat-item" style="text-align:center;flex:1;min-width:120px;'
        'border-right:1px solid rgba(201,162,39,0.2);padding:8px 16px">'
        '<div style="font-size:1.6em;margin-bottom:4px">🏗️</div>'
        '<div style="font-family:Cormorant Garamond,serif;font-size:clamp(1.8em,4vw,2.8em);'
        'font-weight:700;color:#c9a227;line-height:1">500+</div>'
        '<div style="font-family:Montserrat,sans-serif;font-size:0.6em;'
        'text-transform:uppercase;letter-spacing:2px;color:#fff;margin-top:4px">'
        'Projects Completed</div></div>'

        '<div class="stat-item" style="text-align:center;flex:1;min-width:120px;'
        'border-right:1px solid rgba(201,162,39,0.2);padding:8px 16px">'
        '<div style="font-size:1.6em;margin-bottom:4px">📍</div>'
        '<div style="font-family:Cormorant Garamond,serif;font-size:clamp(1.8em,4vw,2.8em);'
        'font-weight:700;color:#c9a227;line-height:1">4</div>'
        '<div style="font-family:Montserrat,sans-serif;font-size:0.6em;'
        'text-transform:uppercase;letter-spacing:2px;color:#fff;margin-top:4px">'
        'Cities Served</div></div>'

        '<div class="stat-item" style="text-align:center;flex:1;min-width:120px;'
        'border-right:1px solid rgba(201,162,39,0.2);padding:8px 16px">'
        '<div style="font-size:1.6em;margin-bottom:4px">🏅</div>'
        '<div style="font-family:Cormorant Garamond,serif;font-size:clamp(1.8em,4vw,2.8em);'
        'font-weight:700;color:#c9a227;line-height:1">15+</div>'
        '<div style="font-family:Montserrat,sans-serif;font-size:0.6em;'
        'text-transform:uppercase;letter-spacing:2px;color:#fff;margin-top:4px">'
        'Years of Excellence</div></div>'

        '<div class="stat-item" style="text-align:center;flex:1;min-width:120px;padding:8px 16px">'
        '<div style="font-size:1.6em;margin-bottom:4px">😊</div>'
        '<div style="font-family:Cormorant Garamond,serif;font-size:clamp(1.8em,4vw,2.8em);'
        'font-weight:700;color:#c9a227;line-height:1">1000+</div>'
        '<div style="font-family:Montserrat,sans-serif;font-size:0.6em;'
        'text-transform:uppercase;letter-spacing:2px;color:#fff;margin-top:4px">'
        'Happy Clients</div></div>'

        '</div>'  # end stats
        '</div>',  # end outer
        unsafe_allow_html=True
    )

    # ── SERVICES
    st.markdown('<div style="background:#f2f0eb;padding:40px 0;width:100%">', unsafe_allow_html=True)
    _, m, _ = st.columns([0.5, 9, 0.5])
    with m:
        sec_header("What We Build", "Our Core Services",
                   "From luxury residences to large-scale infrastructure — "
                   "excellence across every domain of construction.")

        # Mobile: stack in 1 col, desktop: 4 cols
        s1, s2 = st.columns(2)
        s3, s4 = st.columns(2)
        for col, (ic, t, d) in zip([s1,s2,s3,s4], [
            ("🏠","Residential",   "Custom homes, villas and apartments built to your vision."),
            ("🏢","Commercial",    "Modern offices, retail spaces and commercial complexes."),
            ("🛣️","Infrastructure","Roads, bridges, drainage and large-scale civil works."),
            ("🔧","Renovation",    "Expert remodelling that transforms existing spaces."),
        ]):
            with col:
                st.markdown(
                    '<div style="background:#ffffff;border-radius:8px;padding:24px 16px;'
                    'box-shadow:0 4px 20px rgba(0,0,0,0.08);border:1px solid #e0dcd0;'
                    'text-align:center;margin:0 4px 12px;height:calc(100% - 12px)">'
                    '<div style="width:54px;height:54px;'
                    'background:linear-gradient(135deg,#fff8e1,#ffeaa0);'
                    'border-radius:50%;display:flex;align-items:center;justify-content:center;'
                    'font-size:1.5em;margin:0 auto 14px;border:2px solid #f0d060">'
                    + ic + '</div>'
                    '<div style="font-family:Cormorant Garamond,serif;font-size:1.15em;'
                    'font-weight:700;color:#1a1a1a;margin-bottom:8px">' + t + '</div>'
                    '<div style="color:#777;font-size:0.84em;line-height:1.7">' + d + '</div>'
                    '</div>',
                    unsafe_allow_html=True
                )
    st.markdown('</div>', unsafe_allow_html=True)

    # ── WHY US
    st.markdown('<div style="background:#ffffff;padding:40px 0;width:100%">', unsafe_allow_html=True)
    _, m, _ = st.columns([0.5, 9, 0.5])
    with m:
        sec_header("Why JDF", "The JDF Difference",
                   "Craftsmanship, technology and transparency.")
        w1, w2 = st.columns([1,1])
        feats = [
            ("🏅","Premium Quality",    "Top-grade certified materials with strict QC."),
            ("⏰","On-Time Delivery",   "We honour every deadline — systematic management."),
            ("💰","Transparent Pricing","Honest quotations — what we quote is what you pay."),
            ("👷","Expert Team",        "Certified engineers and experienced workers."),
            ("🌱","Eco-Friendly",       "Sustainable methods protecting Karnataka's coast."),
            ("📞","24/7 Support",       "Always available from consultation to handover."),
        ]
        for i, (ic, t, d) in enumerate(feats):
            with (w1 if i % 2 == 0 else w2):
                st.markdown(
                    '<div style="background:#f9f7f2;border-radius:8px;'
                    'padding:16px 18px;margin-bottom:10px;'
                    'border:1px solid #e8e4d8;border-left:4px solid #c9a227;'
                    'display:flex;align-items:flex-start;gap:12px">'
                    '<div style="width:40px;height:40px;min-width:40px;'
                    'background:linear-gradient(135deg,#fff8e1,#ffeaa0);'
                    'border-radius:8px;display:flex;align-items:center;'
                    'justify-content:center;font-size:1.2em">' + ic + '</div>'
                    '<div>'
                    '<div style="font-family:Montserrat,sans-serif;font-weight:700;'
                    'color:#1a1a1a;font-size:0.85em;margin-bottom:3px">' + t + '</div>'
                    '<div style="color:#888;font-size:0.8em;line-height:1.6">' + d + '</div>'
                    '</div></div>',
                    unsafe_allow_html=True
                )
    st.markdown('</div>', unsafe_allow_html=True)

    # ── TESTIMONIALS
    st.markdown('<div style="background:#f2f0eb;padding:40px 0;width:100%">', unsafe_allow_html=True)
    _, m, _ = st.columns([0.5, 9, 0.5])
    with m:
        sec_header("Client Stories", "What Our Clients Say")
        t1, t2, t3 = st.columns([1,1,1])
        for col, (txt, auth, loc) in zip([t1,t2,t3], [
            ("JDF built our dream home in Karwar with incredible precision. "
             "Professional, timely and beyond every expectation.",
             "Ramesh Naik", "Karwar"),
            ("Outstanding commercial project in Mangalore — on schedule, "
             "within budget and impressive quality throughout.",
             "Priya Shetty", "Mangalore"),
            ("JDF transformed our Honnawar building into a modern masterpiece. "
             "Best construction company on the Karnataka coast.",
             "Suresh Hegde", "Honnawar"),
        ]):
            with col:
                st.markdown(
                    '<div style="background:#ffffff;border-radius:8px;padding:24px 20px;'
                    'box-shadow:0 4px 18px rgba(0,0,0,0.07);border:1px solid #e0dcd0;'
                    'border-top:3px solid #c9a227;margin:0 4px 12px">'
                    '<div style="font-family:Georgia,serif;font-size:2.5em;'
                    'color:rgba(201,162,39,0.25);line-height:1;margin-bottom:6px">"</div>'
                    '<div style="color:#555;font-style:italic;font-size:0.87em;'
                    'line-height:1.8;margin-bottom:14px">' + txt + '</div>'
                    '<div style="color:#c9a227;font-size:0.85em;margin-bottom:6px">'
                    '⭐⭐⭐⭐⭐</div>'
                    '<div style="font-family:Montserrat,sans-serif;color:#1a1a1a;'
                    'font-weight:700;font-size:0.83em">' + auth + '</div>'
                    '<div style="color:#c9a227;font-size:0.73em;margin-top:2px">'
                    '📍 ' + loc + '</div>'
                    '</div>',
                    unsafe_allow_html=True
                )
    st.markdown('</div>', unsafe_allow_html=True)

    # ── CTA
    st.markdown('<div style="background:#f2f0eb;padding:0 0 50px;width:100%">', unsafe_allow_html=True)
    _, m, _ = st.columns([0.5, 9, 0.5])
    with m:
        st.markdown(
            '<div style="background:linear-gradient(135deg,#c9a227,#e8c040,#c9a227);'
            'padding:50px 24px;text-align:center;border-radius:10px;'
            'box-shadow:0 12px 48px rgba(201,162,39,0.35)">'
            '<div style="font-family:Cormorant Garamond,serif;'
            'font-size:clamp(1.6em,4vw,2.5em);'
            'color:#fff;font-weight:700;margin-bottom:12px">'
            'Ready to Build Your Dream Project?</div>'
            '<p style="color:rgba(255,255,255,0.88);font-size:0.95em;margin-bottom:24px;'
            'padding:0 10px">'
            "FREE consultation from Karnataka's most trusted experts.</p>"
            '<div style="display:flex;flex-wrap:wrap;justify-content:center;gap:10px">'
            '<a href="tel:+919019429427" '
            'style="display:inline-block;background:#fff;color:#b8960c;'
            'padding:13px 30px;border-radius:5px;font-size:0.82em;font-weight:800;'
            'text-decoration:none;letter-spacing:1px;text-transform:uppercase">'
            '📞 Call: 90194 29427</a>'
            '<a href="https://wa.me/919019429427" target="_blank" '
            'style="display:inline-block;background:#1a1200;color:#c9a227;'
            'padding:13px 30px;border-radius:5px;font-size:0.82em;font-weight:800;'
            'text-decoration:none;letter-spacing:1px;text-transform:uppercase">'
            '💬 WhatsApp Us</a>'
            '</div>'
            '<p style="color:rgba(255,255,255,0.6);font-size:0.8em;margin-top:18px">'
            '📍 Near Dwarka Hotel, Habuwada Main Road, Karwar</p>'
            '</div>',
            unsafe_allow_html=True
        )
    st.markdown('</div>', unsafe_allow_html=True)


# ───────────────────────────────────────────────
# SERVICES PAGE
# ───────────────────────────────────────────────
elif pg == "Services":

    st.markdown('<div style="background:#f2f0eb;padding:30px 0;width:100%">', unsafe_allow_html=True)
    _, m, _ = st.columns([0.5, 9, 0.5])
    with m:
        sec_header("What We Do", "Our Services",
                   "Comprehensive construction solutions across coastal Karnataka.")

        svcs = [
            ("🏠","Residential Construction",
             "Custom bungalows, Multi-storey apartments, Duplex houses, Coastal architecture",
             "Karwar, Ankola, Honnawar, Mangalore"),
            ("🏢","Commercial Construction",
             "Office complexes, Shopping centres, Hotels, Warehouses",
             "Mangalore, Karwar"),
            ("🛣️","Infrastructure & Civil Works",
             "Roads, Bridges, Storm-water drainage, Retaining walls, Government contracts",
             "All Locations"),
            ("🔧","Renovation & Remodelling",
             "Complete makeovers, Kitchen & bathroom upgrades, Premium flooring",
             "All Locations"),
            ("🏗️","Foundation & Structural",
             "Deep foundation, RCC structures, Steel frame, Earthquake-resistant design",
             "All Locations"),
            ("🎨","Interior Construction",
             "False ceilings, Waterproofing, MEP plumbing, Modular fixtures",
             "All Locations"),
        ]

        for i in range(0, len(svcs), 2):
            ca, cb = st.columns(2)
            for col, idx in zip([ca, cb], [i, i+1]):
                if idx < len(svcs):
                    ic, title, desc, locs = svcs[idx]
                    with col:
                        st.markdown(
                            '<div style="background:#ffffff;border-radius:8px;padding:22px;'
                            'box-shadow:0 4px 18px rgba(0,0,0,0.07);border:1px solid #e0dcd0;'
                            'margin:0 4px 16px">'
                            '<div style="display:flex;align-items:center;gap:12px;margin-bottom:12px">'
                            '<div style="width:48px;height:48px;min-width:48px;'
                            'background:linear-gradient(135deg,#fff8e1,#ffeaa0);'
                            'border-radius:50%;display:flex;align-items:center;'
                            'justify-content:center;font-size:1.4em;border:2px solid #f0d060">'
                            + ic + '</div>'
                            '<div style="font-family:Cormorant Garamond,serif;font-size:1.1em;'
                            'font-weight:700;color:#1a1a1a">' + title + '</div></div>'
                            '<div style="color:#666;font-size:0.84em;line-height:1.85;'
                            'margin-bottom:12px">' + desc + '</div>'
                            '<span style="display:inline-block;background:#fff8e1;color:#9a7a10;'
                            'padding:3px 10px;border-radius:20px;font-size:0.7em;font-weight:700;'
                            'border:1px solid #e8c840">📍 ' + locs + '</span>'
                            '</div>',
                            unsafe_allow_html=True
                        )

        st.markdown("<br>", unsafe_allow_html=True)
        sec_header("How We Work", "Our Build Process",
                   "Transparent — from first meeting to final handover.")

        steps = [
            ("1","Consultation","Free meeting to understand your vision and requirements"),
            ("2","Design","Plans, structural drawings and 3D visualisation"),
            ("3","Quotation","Transparent itemised estimate with full material specs"),
            ("4","Agreement","Clear contract with milestones and payment schedule"),
            ("5","Construction","Quality build with real-time updates"),
            ("6","Handover","Final inspection, warranty and keys"),
        ]
        p1, p2, p3 = st.columns(3)
        for i, (num, t, d) in enumerate(steps):
            with [p1, p2, p3][i % 3]:
                st.markdown(
                    '<div style="background:#f9f7f2;border-radius:8px;padding:22px 14px;'
                    'text-align:center;border:1px solid #e0dcd0;margin-bottom:14px">'
                    '<div style="width:40px;height:40px;'
                    'background:linear-gradient(135deg,#c9a227,#e8c040);border-radius:50%;'
                    'display:flex;align-items:center;justify-content:center;'
                    'font-family:Cormorant Garamond,serif;font-size:1.2em;font-weight:700;'
                    'color:#fff;margin:0 auto 10px">' + num + '</div>'
                    '<div style="font-family:Cormorant Garamond,serif;font-size:1.05em;'
                    'color:#1a1a1a;font-weight:700;margin-bottom:6px">' + t + '</div>'
                    '<div style="color:#888;font-size:0.8em;line-height:1.6">' + d + '</div>'
                    '</div>',
                    unsafe_allow_html=True
                )
        st.markdown("<br>", unsafe_allow_html=True)
        _, ctr, _ = st.columns([2,1,2])
        with ctr:
            if st.button("📞 Get Free Quote", key="svc_cta"): go("Contact Us")
    st.markdown('</div>', unsafe_allow_html=True)


# ───────────────────────────────────────────────
# LOCATIONS PAGE
# ───────────────────────────────────────────────
elif pg == "Locations":

    st.markdown('<div style="background:#f2f0eb;padding:30px 0;width:100%">', unsafe_allow_html=True)
    _, m, _ = st.columns([0.5, 9, 0.5])
    with m:
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
                '<div style="width:' + str(sz) + 'px;height:' + str(sz) + 'px;'
                'background:linear-gradient(135deg,#9a7510,#c9a227,#f5d77e);'
                'border-radius:50% 50% 50% 0;transform:rotate(-45deg);'
                'border:3px solid #fff;box-shadow:0 4px 14px rgba(201,162,39,0.5);'
                'display:flex;align-items:center;justify-content:center">'
                '<span style="transform:rotate(45deg);color:#fff;'
                'font-size:' + str(sz//2-3) + 'px;font-weight:900">'
                + sym + '</span></div>'
            )
            popup = (
                '<div style="background:#fff;border-top:3px solid #c9a227;'
                'border-radius:8px;padding:14px;min-width:180px;font-family:sans-serif">'
                '<div style="color:#c9a227;font-weight:700;font-size:0.95em;margin-bottom:8px">'
                + ("HQ: " if d["hq"] else "") + city + '</div>'
                '<div style="color:#555;font-size:0.82em;line-height:1.8">'
                'Projects: <b style="color:#c9a227">' + d["projects"] + '</b><br>'
                'Specialty: ' + d["spec"] + '<br>'
                'Address: ' + d["addr"] + '</div>'
                '<div style="margin-top:10px;text-align:center">'
                '<a href="tel:+919019429427" style="background:#c9a227;color:#fff;'
                'padding:6px 12px;border-radius:4px;text-decoration:none;'
                'font-weight:700;font-size:0.78em">📞 Call Jason</a></div></div>'
            )
            folium.Marker(
                [d["lat"],d["lon"]],
                popup=folium.Popup(popup, max_width=220),
                tooltip=city + " — " + d["projects"] + " Projects",
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
        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)

        # 2x2 on mobile, 4 cols on desktop
        r1c1, r1c2 = st.columns(2)
        r2c1, r2c2 = st.columns(2)
        loc_list = [
            ("HEADQUARTERS","#c9a227","Karwar"),
            ("ACTIVE OPS","#888","Ankola"),
            ("ACTIVE OPS","#888","Honnawar"),
            ("COMMERCIAL HUB","#888","Mangalore"),
        ]
        for col, (badge, bc, city) in zip([r1c1,r1c2,r2c1,r2c2], loc_list):
            d = loc_data[city]
            with col:
                st.markdown(
                    '<div style="background:#fff;border-radius:8px;padding:18px 14px;'
                    'box-shadow:0 4px 18px rgba(0,0,0,0.07);border:1px solid #e0dcd0;'
                    'border-top:4px solid #c9a227;margin:0 4px 12px">'
                    '<div style="color:' + bc + ';font-family:Montserrat,sans-serif;'
                    'font-size:0.6em;font-weight:700;letter-spacing:2px;'
                    'text-transform:uppercase;margin-bottom:6px">' + badge + '</div>'
                    '<div style="font-family:Cormorant Garamond,serif;font-size:1.3em;'
                    'color:#1a1a1a;font-weight:700;margin-bottom:8px">📍 ' + city + '</div>'
                    '<div style="font-family:Cormorant Garamond,serif;font-size:2em;'
                    'color:#c9a227;font-weight:700;margin-bottom:8px">' + d["projects"] + '</div>'
                    '<div style="color:#666;font-size:0.82em;margin-bottom:8px">'
                    + d["spec"] + '</div>'
                    '<div style="color:#bbb;font-size:0.72em;border-top:1px solid #f0ede4;'
                    'padding-top:8px;line-height:1.7">' + d["addr"] + '</div></div>',
                    unsafe_allow_html=True
                )
    st.markdown('</div>', unsafe_allow_html=True)


# ───────────────────────────────────────────────
# ABOUT US PAGE
# ───────────────────────────────────────────────
elif pg == "About Us":

    owner_b64 = img_to_b64("jason_photo.jpg")

    st.markdown('<div style="background:#f2f0eb;padding:30px 0;width:100%">', unsafe_allow_html=True)
    _, m, _ = st.columns([0.5, 9, 0.5])
    with m:
        sec_header("Who We Are", "About JDF Constructions")

        a1, a2 = st.columns([1, 1.6])

        with a1:
            if owner_b64:
                st.markdown(
                    '<img src="data:image/jpeg;base64,' + owner_b64 + '" '
                    'style="width:100%;border-radius:8px 8px 0 0;'
                    'object-fit:cover;object-position:top center;'
                    'display:block;max-height:280px">',
                    unsafe_allow_html=True
                )
            else:
                st.markdown(
                    '<div style="background:#2d2000;border-radius:8px 8px 0 0;'
                    'height:240px;display:flex;align-items:center;'
                    'justify-content:center;font-size:5em">👤</div>',
                    unsafe_allow_html=True
                )
            st.markdown(
                '<div style="background:#fff;border-radius:0 0 8px 8px;padding:20px;'
                'box-shadow:0 4px 18px rgba(0,0,0,0.07);border:1px solid #e0dcd0;'
                'border-top:4px solid #c9a227;text-align:center">'
                '<div style="font-family:Cormorant Garamond,serif;font-size:1.5em;'
                'font-weight:700;color:#1a1a1a">Jason Fernandes</div>'
                '<div style="font-family:Montserrat,sans-serif;font-size:0.6em;'
                'letter-spacing:2px;color:#c9a227;text-transform:uppercase;'
                'font-weight:700;margin:5px 0 10px">Founder and Managing Director</div>'
                '<div style="color:#777;font-size:0.82em;line-height:1.7;margin-bottom:12px">'
                '15+ years building exceptional structures across coastal Karnataka.</div>'
                '<a href="tel:+919019429427" '
                'style="display:inline-block;'
                'background:linear-gradient(135deg,#c9a227,#e8c040);'
                'color:#fff;padding:10px 22px;border-radius:5px;font-weight:700;'
                'text-decoration:none;font-size:0.84em">📱 90194 29427</a>'
                '</div>',
                unsafe_allow_html=True
            )

        with a2:
            st.markdown(
                '<div style="padding:0 0 0 10px">'
                '<div style="font-family:Cormorant Garamond,serif;font-size:1.8em;'
                'font-weight:700;color:#1a1a1a;margin-bottom:16px">Our Story</div>'
                '<div style="color:#555;line-height:1.9;font-size:0.9em">'
                '<p style="margin-bottom:12px">JDF Constructions was founded with a singular '
                'vision — to bring <strong>world-class construction quality</strong> '
                'to the beautiful coastal belt of Karnataka.</p>'
                '<p style="margin-bottom:12px">Under the leadership of '
                '<strong style="color:#c9a227">Jason Fernandes</strong>, the company has grown '
                'into one of the most trusted construction brands across Uttara Kannada '
                'and Dakshina Kannada districts.</p>'
                '<p style="margin-bottom:12px">Starting from <strong>Karwar</strong>, '
                'JDF has expanded to <strong>Ankola</strong>, <strong>Honnawar</strong> and '
                '<strong>Mangalore</strong>.</p>'
                '<p style="font-family:Cormorant Garamond,serif;font-size:1.15em;'
                'color:#c9a227;font-style:italic">'
                '"Your dream project starts here."</p></div></div>',
                unsafe_allow_html=True
            )

            st.markdown("<br>", unsafe_allow_html=True)
            m1, m2 = st.columns(2)
            for col, (ic, t, d) in zip([m1,m2,m1,m2], [
                ("🎯","Mission",    "Superior construction with integrity."),
                ("👁️","Vision",    "Karnataka's most trusted builder."),
                ("💎","Values",    "Quality, Integrity, Innovation"),
                ("🏅","Commitment","Every project is our own home."),
            ]):
                with col:
                    st.markdown(
                        '<div style="background:#fff;border-radius:8px;padding:16px;'
                        'margin-bottom:10px;box-shadow:0 2px 10px rgba(0,0,0,0.06);'
                        'border:1px solid #e0dcd0;border-left:3px solid #c9a227">'
                        '<div style="font-size:1.5em;margin-bottom:6px">' + ic + '</div>'
                        '<div style="font-family:Cormorant Garamond,serif;font-size:1em;'
                        'font-weight:700;color:#1a1a1a;margin-bottom:3px">' + t + '</div>'
                        '<div style="color:#888;font-size:0.8em">' + d + '</div></div>',
                        unsafe_allow_html=True
                    )

        st.markdown("<br>", unsafe_allow_html=True)
        sec_header("Expertise", "Skills and Capabilities")
        sk1, sk2 = st.columns(2)
        for i, (s, p) in enumerate([
            ("Residential Construction", 95),
            ("Commercial Projects", 88),
            ("Infrastructure and Civil", 82),
            ("Interior Construction", 90),
            ("Project Management", 93),
            ("Client Satisfaction", 98),
        ]):
            with (sk1 if i % 2 == 0 else sk2):
                st.markdown(
                    '<div style="margin-bottom:16px">'
                    '<div style="display:flex;justify-content:space-between;margin-bottom:6px">'
                    '<span style="font-family:Montserrat,sans-serif;color:#333;'
                    'font-size:0.83em;font-weight:600">' + s + '</span>'
                    '<span style="font-family:Montserrat,sans-serif;color:#c9a227;'
                    'font-weight:700;font-size:0.83em">' + str(p) + '%</span></div>'
                    '<div style="background:#e8e4d8;border-radius:50px;height:6px;overflow:hidden">'
                    '<div style="height:100%;width:' + str(p) + '%;'
                    'background:linear-gradient(90deg,#c9a227,#f5d77e);'
                    'border-radius:50px"></div></div></div>',
                    unsafe_allow_html=True
                )

        st.markdown("<br>", unsafe_allow_html=True)
        mc1, mc2 = st.columns(2)
        mc3, mc4 = st.columns(2)
        for col, (ic, t, s) in zip([mc1,mc2,mc3,mc4], [
            ("🏅","Licensed Contractor","Karnataka PWD Certified"),
            ("📋","RERA Compliant","All projects registered"),
            ("🌱","Green Building","Eco-friendly certified"),
            ("🔒","Quality Standards","ISO-aligned QMS"),
        ]):
            with col:
                st.markdown(
                    '<div style="background:#fff;border-radius:8px;padding:20px 14px;'
                    'text-align:center;box-shadow:0 3px 14px rgba(0,0,0,0.06);'
                    'border:1px solid #e0dcd0;margin:0 4px 12px">'
                    '<div style="font-size:1.8em;margin-bottom:8px">' + ic + '</div>'
                    '<div style="font-family:Cormorant Garamond,serif;font-size:0.95em;'
                    'color:#1a1a1a;font-weight:700;margin-bottom:4px">' + t + '</div>'
                    '<div style="font-family:Montserrat,sans-serif;color:#aaa;'
                    'font-size:0.73em">' + s + '</div></div>',
                    unsafe_allow_html=True
                )
    st.markdown('</div>', unsafe_allow_html=True)


# ───────────────────────────────────────────────
# CONTACT US PAGE
# ───────────────────────────────────────────────
elif pg == "Contact Us":

    st.markdown('<div style="background:#f2f0eb;padding:30px 0;width:100%">', unsafe_allow_html=True)
    _, m, _ = st.columns([0.5, 9, 0.5])
    with m:
        sec_header("Get In Touch", "Contact JDF Constructions",
                   "Ready to build? Reach out for a free consultation.")

        cf1, cf2 = st.columns([1.5, 1])

        with cf1:
            st.markdown(
                '<div style="background:#fff;border-radius:8px;padding:24px;'
                'box-shadow:0 4px 18px rgba(0,0,0,0.07);border:1px solid #e0dcd0;'
                'margin-bottom:12px">'
                '<div style="font-family:Cormorant Garamond,serif;font-size:1.3em;'
                'font-weight:700;color:#1a1a1a;margin-bottom:18px;padding-bottom:10px;'
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
                    placeholder="Describe your site, timeline, requirements...",
                    height=100)
                if st.form_submit_button("Submit Enquiry"):
                    if name.strip() and phone.strip():
                        st.success(
                            "Thank you " + name + "! Enquiry for " +
                            ptype + " in " + city + " received. "
                            "Jason will call " + phone + " within 24 hours.")
                        st.balloons()
                    else:
                        st.error("Please enter your name and phone number.")
            st.markdown('</div>', unsafe_allow_html=True)

        with cf2:
            st.markdown(
                '<div style="background:#fff;border-radius:8px;padding:20px;'
                'box-shadow:0 4px 18px rgba(0,0,0,0.07);border:1px solid #e0dcd0;'
                'margin-bottom:12px">'
                '<div style="font-family:Cormorant Garamond,serif;font-size:1.15em;'
                'font-weight:700;color:#1a1a1a;margin-bottom:14px;padding-bottom:8px;'
                'border-bottom:2px solid #f0ede4">Our Details</div>'
                '<div style="padding:8px 0;border-bottom:1px solid #f5f2ea">'
                '<span style="color:#c9a227;font-weight:700;font-size:0.9em">'
                'Jason Fernandes</span><br>'
                '<span style="color:#bbb;font-size:0.74em">Founder and Managing Director</span></div>'
                '<div style="padding:8px 0;border-bottom:1px solid #f5f2ea;font-size:0.87em">'
                '📱 <strong>90194 29427</strong><br>'
                '<span style="color:#bbb;font-size:0.74em">Call or WhatsApp</span></div>'
                '<div style="padding:8px 0;border-bottom:1px solid #f5f2ea;font-size:0.85em;color:#444">'
                '📍 Near Dwarka Hotel, Habuwada Main Road<br>'
                '<span style="color:#bbb;font-size:0.8em">Karwar, Karnataka — 581 301</span></div>'
                '<div style="padding:8px 0;border-bottom:1px solid #f5f2ea;font-size:0.85em;color:#444">'
                '🕐 Mon – Sat, 9 AM to 7 PM</div>'
                '<div style="padding:8px 0;font-size:0.85em;color:#444">'
                '🏙️ Karwar, Ankola, Honnawar, Mangalore</div></div>',
                unsafe_allow_html=True
            )
            st.markdown(
                '<div style="background:#fff;border-radius:8px;padding:20px;'
                'box-shadow:0 4px 18px rgba(0,0,0,0.07);border:1px solid #e0dcd0">'
                '<div style="font-family:Cormorant Garamond,serif;font-size:1.15em;'
                'font-weight:700;color:#1a1a1a;margin-bottom:14px;padding-bottom:8px;'
                'border-bottom:2px solid #f0ede4">Quick Connect</div>'
                '<a href="tel:+919019429427" '
                'style="display:block;text-align:center;padding:11px;border-radius:6px;'
                'text-decoration:none;font-weight:700;font-size:0.83em;margin-bottom:8px;'
                'background:linear-gradient(135deg,#c9a227,#e8c040);color:#fff">'
                '📞 Call: 90194 29427</a>'
                '<a href="https://wa.me/919019429427" target="_blank" '
                'style="display:block;text-align:center;padding:11px;border-radius:6px;'
                'text-decoration:none;font-weight:700;font-size:0.83em;margin-bottom:8px;'
                'background:linear-gradient(135deg,#25D366,#128C7E);color:#fff">'
                '💬 WhatsApp Jason</a>'
                '<a href="https://maps.google.com/?q=Dwarka+Hotel+Habuwada+Karwar" '
                'target="_blank" '
                'style="display:block;text-align:center;padding:11px;border-radius:6px;'
                'text-decoration:none;font-weight:700;font-size:0.83em;'
                'background:linear-gradient(135deg,#1a73e8,#4285F4);color:#fff">'
                '🗺️ Get Directions</a></div>',
                unsafe_allow_html=True
            )

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

    st.markdown('</div>', unsafe_allow_html=True)


# ── FOOTER
st.markdown(
    '<div style="background:linear-gradient(135deg,#1c1400,#2d2000,#1a1200);'
    'padding:40px 30px 24px;width:100%">'
    '<div style="max-width:1100px;margin:0 auto;display:flex;'
    'justify-content:space-between;flex-wrap:wrap;gap:24px">'

    '<div style="min-width:200px">'
    '<div style="font-family:Cormorant Garamond,serif;font-size:1.7em;'
    'color:#c9a227;font-weight:700;letter-spacing:2px;margin-bottom:6px">'
    '🏗️ JDF CONSTRUCTIONS</div>'
    '<div style="color:rgba(201,162,39,0.55);font-style:italic;'
    'font-family:Cormorant Garamond,serif;font-size:1em;margin-bottom:10px">'
    '"Your dream project starts here."</div>'
    '<div style="color:#4a4000;font-size:0.78em">Karwar | Ankola | Honnawar | Mangalore</div></div>'

    '<div style="color:#4a4000;font-size:0.8em;line-height:2.2;min-width:180px">'
    '<div style="color:rgba(201,162,39,0.55);font-weight:700;'
    'margin-bottom:6px;letter-spacing:1px;font-size:0.85em">CONTACT</div>'
    '<div>📍 Habuwada Main Road, Karwar</div>'
    '<div>📞 +91 90194 29427</div>'
    '<div>🕐 Mon–Sat, 9 AM to 7 PM</div></div>'

    '<div style="color:#4a4000;font-size:0.8em;line-height:2.4;min-width:140px">'
    '<div style="color:rgba(201,162,39,0.55);font-weight:700;'
    'margin-bottom:6px;letter-spacing:1px;font-size:0.85em">PAGES</div>'
    '<div>Home | Services | Locations</div>'
    '<div>About Us | Contact Us</div></div>'

    '</div>'
    '<div style="border-top:1px solid #2a2000;margin-top:20px;padding-top:16px;'
    'text-align:center">'
    '<div style="color:#3a3000;font-size:0.74em">'
    '© 2024 JDF Constructions. All Rights Reserved.</div></div></div>',
    unsafe_allow_html=True
)