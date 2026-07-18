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

/* ── NAV BUTTONS ── */
.nav-bar-buttons {
    background: #ffffff;
    margin-top: -64px;
    position: relative;
    z-index: 1000;
    display: flex;
    justify-content: flex-end;
    padding-right: 20px;
    padding-top: 0;
    padding-bottom: 0;
}
.nav-bar-buttons > div {
    width: 100%;
}
.nav-bar-buttons .stButton button {
    background: linear-gradient(135deg, #c9a227, #e8c040) !important;
    color: #fff !important;
    border: none !important;
    border-radius: 6px !important;
    padding: 10px 22px !important;
    font-weight: 700 !important;
    font-size: 0.78em !important;
    letter-spacing: 1.5px !important;
    box-shadow: 0 3px 12px rgba(201,162,39,0.35) !important;
}
.nav-bar-buttons .stButton button:hover {
    background: linear-gradient(135deg, #b8960c, #c9a227) !important;
    color: #fff !important;
    box-shadow: 0 6px 20px rgba(201,162,39,0.5) !important;
}

/* Remove excess padding below nav */
.nav-bar-buttons + div,
.nav-bar-buttons ~ div[data-testid="stVerticalBlock"] > div:first-child {
    margin-top: 0 !important;
    padding-top: 0 !important;
}

/* Form styles */
.stForm [data-testid="stFormSubmitButton"] > button {
    background: linear-gradient(135deg, #c9a227, #e8c040) !important;
    color: #fff !important;
    border: none !important;
    border-radius: 5px !important;
    padding: 12px 32px !important;
    font-weight: 700 !important;
    width: 100% !important;
    box-shadow: none !important;
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

::-webkit-scrollbar { width: 5px; }
::-webkit-scrollbar-track { background: #f0ede4; }
::-webkit-scrollbar-thumb { background: #c9a227; border-radius: 3px; }
</style>
""", unsafe_allow_html=True)

# ── TOP INFO BAR
st.markdown(
    '<div style="background:#9a7a10;padding:8px 50px;display:flex;'
    'justify-content:space-between;align-items:center;'
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
    'padding-left:50px;height:64px;display:flex;align-items:center;'
    'box-shadow:0 2px 10px rgba(0,0,0,0.06)">'
    '<span style="font-family:Cormorant Garamond,serif;font-size:1.6em;'
    'font-weight:700;color:#b8960c;letter-spacing:2px">'
    '🏗️ JDF CONSTRUCTIONS</span>'
    '</div>',
    unsafe_allow_html=True
)

# ── NAV BUTTONS (golden, aligned)
st.markdown("""
<style>
/* This WILL work - targets Streamlit's actual rendered HTML */
.stButton > button {
    background-color: #c9a227 !important;
    background: #c9a227 !important;
    color: #ffffff !important;
    border: 2px solid #c9a227 !important;
    border-radius: 10px !important;
    font-weight: 700 !important;
    letter-spacing: 2px !important;
    font-size: 0.78em !important;
    padding: 14px 20px !important;
    width: 100% !important;
    box-shadow: 0 4px 15px rgba(201,162,39,0.3) !important;
}
.stButton > button:hover {
    background-color: #a8841f !important;
    background: #a8841f !important;
    color: #ffffff !important;
    border-color: #a8841f !important;
    transform: translateY(-2px) !important;
    box-shadow: 0 6px 20px rgba(201,162,39,0.5) !important;
}
.stButton > button:focus,
.stButton > button:active {
    background-color: #c9a227 !important;
    background: #c9a227 !important;
    color: #ffffff !important;
    border-color: #c9a227 !important;
    box-shadow: none !important;
}
</style>
""", unsafe_allow_html=True)
st.markdown('<div class="nav-bar-buttons">', unsafe_allow_html=True)
n = st.columns([3.5, 1, 1, 1, 1, 1.2])
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
st.markdown('</div>', unsafe_allow_html=True)

# ── Negative margin spacer to pull content up (reduces gap on all pages)
st.markdown(
    '<div style="margin-top:-38px"></div>',
    unsafe_allow_html=True
)

# ───────────────────────────────────────────────
# HERO  (Home only) — stats EMBEDDED inside hero
# ───────────────────────────────────────────────
if pg == "Home":
    logo_b64  = img_to_b64("jdf_logo.png")
    owner_b64 = img_to_b64("jason_photo.jpg")

    logo_html = (
        '<img src="data:image/png;base64,' + logo_b64 + '" '
        'style="width:160px;border-radius:8px;'
        'box-shadow:0 4px 20px rgba(0,0,0,0.5)">'
    ) if logo_b64 else '<span style="font-size:4em">🏗️</span>'

    owner_html = (
        '<img src="data:image/jpeg;base64,' + owner_b64 + '" '
        'style="width:100%;height:200px;object-fit:cover;'
        'object-position:top center;display:block;border-radius:6px 6px 0 0">'
    ) if owner_b64 else (
        '<div style="height:200px;background:#2d2000;border-radius:6px 6px 0 0;'
        'display:flex;align-items:center;justify-content:center;font-size:4em">👤</div>'
    )

    st.markdown(
        # ── OUTER WRAPPER (dark bg, full width)
        '<div style="background:linear-gradient(135deg,#1c1400 0%,#2d2000 50%,#1a1200 100%);'
        'border-bottom:4px solid #c9a227;width:100%">'

        # ── TOP ROW: logo | text | owner
        '<div style="display:flex;width:100%;min-height:400px">'

        # LEFT logo
        '<div style="width:200px;min-width:200px;display:flex;align-items:center;'
        'justify-content:center;padding:30px;'
        'border-right:1px solid rgba(201,162,39,0.2)">'
        + logo_html +
        '</div>'

        # CENTER text
        '<div style="flex:1;display:flex;align-items:center;justify-content:center;'
        'text-align:center;padding:50px 40px">'
        '<div>'
        '<div style="font-family:Montserrat,sans-serif;font-size:0.68em;'
        'letter-spacing:5px;text-transform:uppercase;'
        'color:rgba(201,162,39,0.65);font-weight:600;margin-bottom:16px">'
        "KARNATAKA'S PREMIER CONSTRUCTION COMPANY</div>"
        '<div style="font-family:Cormorant Garamond,serif;font-size:5.5em;'
        'font-weight:700;color:#ffffff;line-height:0.9;letter-spacing:3px">JDF</div>'
        '<div style="font-family:Cormorant Garamond,serif;font-size:1.8em;'
        'font-weight:600;color:#c9a227;letter-spacing:10px;'
        'text-transform:uppercase;margin:10px 0 14px">CONSTRUCTIONS</div>'
        '<div style="width:50px;height:2px;'
        'background:linear-gradient(90deg,#c9a227,#f5d77e);margin:0 auto 18px"></div>'
        '<div style="font-family:Cormorant Garamond,serif;font-size:1.3em;'
        'color:#d4c898;font-style:italic;margin-bottom:26px">'
        '"Your dream project starts here."</div>'
        '<div>'
        '<span style="display:inline-block;border:1px solid rgba(201,162,39,0.5);'
        'color:#c9a227;padding:7px 20px;border-radius:30px;font-size:0.78em;'
        'font-weight:600;margin:4px;background:rgba(201,162,39,0.1)">📍 Karwar</span>'
        '<span style="display:inline-block;border:1px solid rgba(201,162,39,0.5);'
        'color:#c9a227;padding:7px 20px;border-radius:30px;font-size:0.78em;'
        'font-weight:600;margin:4px;background:rgba(201,162,39,0.1)">📍 Ankola</span>'
        '<span style="display:inline-block;border:1px solid rgba(201,162,39,0.5);'
        'color:#c9a227;padding:7px 20px;border-radius:30px;font-size:0.78em;'
        'font-weight:600;margin:4px;background:rgba(201,162,39,0.1)">📍 Honnawar</span>'
        '<span style="display:inline-block;border:1px solid rgba(201,162,39,0.5);'
        'color:#c9a227;padding:7px 20px;border-radius:30px;font-size:0.78em;'
        'font-weight:600;margin:4px;background:rgba(201,162,39,0.1)">📍 Mangalore</span>'
        '</div></div></div>'

        # RIGHT owner
        '<div style="width:220px;min-width:220px;display:flex;align-items:center;'
        'justify-content:center;padding:30px;'
        'border-left:1px solid rgba(201,162,39,0.2)">'
        '<div style="width:170px">'
        + owner_html +
        '<div style="background:#ffffff;border-radius:0 0 8px 8px;'
        'border-top:3px solid #c9a227;padding:14px;text-align:center">'
        '<div style="font-family:Cormorant Garamond,serif;font-size:1.1em;'
        'font-weight:700;color:#1a1a1a;line-height:1.2">Jason Fernandes</div>'
        '<div style="font-family:Montserrat,sans-serif;font-size:0.6em;'
        'letter-spacing:2px;color:#c9a227;text-transform:uppercase;'
        'font-weight:700;margin:4px 0 6px">Founder &amp; Owner</div>'
        '<div style="font-family:Montserrat,sans-serif;font-size:0.78em;'
        'color:#444;font-weight:600">📞 90194 29427</div>'
        '</div></div></div>'
        '</div>'  # end top row

        # ── STATS BAR (inside the dark hero, below top row)
        '<div style="border-top:1px solid rgba(201,162,39,0.25);'
        'padding:32px 60px;display:flex;justify-content:space-around;'
        'align-items:center;flex-wrap:wrap;gap:16px">'

        # Stat 1
        '<div style="text-align:center;flex:1;min-width:140px;'
        'border-right:1px solid rgba(201,162,39,0.2);padding:0 20px">'
        '<div style="font-size:2em;margin-bottom:4px">🏗️</div>'
        '<div style="font-family:Cormorant Garamond,serif;font-size:2.8em;'
        'font-weight:700;color:#c9a227;line-height:1">500+</div>'
        '<div style="font-family:Montserrat,sans-serif;font-size:0.62em;'
        'text-transform:uppercase;letter-spacing:2px;color:#fff;margin-top:4px">'
        'Projects Completed</div>'
        '</div>'

        # Stat 2
        '<div style="text-align:center;flex:1;min-width:140px;'
        'border-right:1px solid rgba(201,162,39,0.2);padding:0 20px">'
        '<div style="font-size:2em;margin-bottom:4px">📍</div>'
        '<div style="font-family:Cormorant Garamond,serif;font-size:2.8em;'
        'font-weight:700;color:#c9a227;line-height:1">4</div>'
        '<div style="font-family:Montserrat,sans-serif;font-size:0.62em;'
        'text-transform:uppercase;letter-spacing:2px;color:#fff;margin-top:4px">'
        'Cities Served</div>'
        '</div>'

        # Stat 3
        '<div style="text-align:center;flex:1;min-width:140px;'
        'border-right:1px solid rgba(201,162,39,0.2);padding:0 20px">'
        '<div style="font-size:2em;margin-bottom:4px">🏅</div>'
        '<div style="font-family:Cormorant Garamond,serif;font-size:2.8em;'
        'font-weight:700;color:#c9a227;line-height:1">15+</div>'
        '<div style="font-family:Montserrat,sans-serif;font-size:0.62em;'
        'text-transform:uppercase;letter-spacing:2px;color:#fff;margin-top:4px">'
        'Years of Excellence</div>'
        '</div>'

        # Stat 4
        '<div style="text-align:center;flex:1;min-width:140px;padding:0 20px">'
        '<div style="font-size:2em;margin-bottom:4px">😊</div>'
        '<div style="font-family:Cormorant Garamond,serif;font-size:2.8em;'
        'font-weight:700;color:#c9a227;line-height:1">1000+</div>'
        '<div style="font-family:Montserrat,sans-serif;font-size:0.62em;'
        'text-transform:uppercase;letter-spacing:2px;color:#fff;margin-top:4px">'
        'Happy Clients</div>'
        '</div>'

        '</div>'  # end stats bar
        '</div>',  # end outer wrapper
        unsafe_allow_html=True
    )

# ───────────────────────────────────────────────
# HELPERS
# ───────────────────────────────────────────────
def sec_header(overline, title, desc=""):
    desc_html = (
        '<p style="color:#777;font-size:0.92em;max-width:520px;'
        'margin:0 auto;line-height:1.75">' + desc + '</p>'
    ) if desc else ""
    st.markdown(
        '<div style="text-align:center;margin-bottom:18px">'
        '<span style="font-family:Montserrat,sans-serif;font-size:0.7em;'
        'letter-spacing:4px;text-transform:uppercase;'
        'color:#c9a227;font-weight:700;display:block;margin-bottom:6px">'
        + overline + '</span>'
        '<div style="font-family:Cormorant Garamond,serif;font-size:2.5em;'
        'font-weight:700;color:#1a1a1a;margin:0 0 12px;line-height:1.15">'
        + title + '</div>'
        + desc_html +
        '<div style="width:52px;height:2px;'
        'background:linear-gradient(90deg,#c9a227,#f5d77e);'
        'margin:14px auto;border-radius:2px"></div></div>',
        unsafe_allow_html=True
    )

# ───────────────────────────────────────────────
# HOME PAGE  (sections after hero — NO stats here)
# ───────────────────────────────────────────────
if pg == "Home":

    # SERVICES
    st.markdown('<div style="background:#f2f0eb;padding:25px 0;width:100%">', unsafe_allow_html=True)
    _, m, _ = st.columns([1, 8, 1])
    with m:
        sec_header("What We Build", "Our Core Services",
                   "From luxury residences to large-scale infrastructure — "
                   "excellence across every domain of construction.")
        s1, s2, s3, s4 = st.columns(4)
        for col, (ic, t, d) in zip([s1,s2,s3,s4], [
            ("🏠", "Residential",    "Custom homes, villas and apartments built to your vision."),
            ("🏢", "Commercial",     "Modern offices, retail spaces and commercial complexes."),
            ("🛣️","Infrastructure", "Roads, bridges, drainage and large-scale civil works."),
            ("🔧", "Renovation",     "Expert remodelling that transforms existing spaces."),
        ]):
            with col:
                st.markdown(
                    '<div style="background:#ffffff;border-radius:8px;padding:30px 20px;'
                    'box-shadow:0 4px 20px rgba(0,0,0,0.08);border:1px solid #e0dcd0;'
                    'text-align:center;height:100%;margin:0 4px">'
                    '<div style="width:60px;height:60px;'
                    'background:linear-gradient(135deg,#fff8e1,#ffeaa0);'
                    'border-radius:50%;display:flex;align-items:center;justify-content:center;'
                    'font-size:1.7em;margin:0 auto 16px;border:2px solid #f0d060">'
                    + ic + '</div>'
                    '<div style="font-family:Cormorant Garamond,serif;font-size:1.25em;'
                    'font-weight:700;color:#1a1a1a;margin-bottom:10px">' + t + '</div>'
                    '<div style="color:#777;font-size:0.86em;line-height:1.7">' + d + '</div>'
                    '</div>',
                    unsafe_allow_html=True
                )
    st.markdown('</div>', unsafe_allow_html=True)

    # WHY US
    st.markdown('<div style="background:#ffffff;padding:25px 0;width:100%">', unsafe_allow_html=True)
    _, m, _ = st.columns([1, 8, 1])
    with m:
        sec_header("Why JDF", "The JDF Difference",
                   "Craftsmanship, technology and transparency — "
                   "delivering experiences that exceed every expectation.")
        w1, w2 = st.columns(2)
        feats = [
            ("🏅","Premium Quality",    "Top-grade certified materials with strict QC at every stage."),
            ("⏰","On-Time Delivery",   "We honour every deadline — systematic project management."),
            ("💰","Transparent Pricing","Honest quotations — what we quote is exactly what you pay."),
            ("👷","Expert Team",        "Certified engineers, architects and experienced workers."),
            ("🌱","Eco-Friendly",       "Sustainable methods protecting Karnataka's coast."),
            ("📞","24/7 Support",       "Always available from first consultation to handover."),
        ]
        for i, (ic, t, d) in enumerate(feats):
            with (w1 if i % 2 == 0 else w2):
                st.markdown(
                    '<div style="background:#f9f7f2;border-radius:8px;'
                    'padding:18px 22px;margin-bottom:12px;'
                    'border:1px solid #e8e4d8;border-left:4px solid #c9a227;'
                    'display:flex;align-items:flex-start;gap:15px">'
                    '<div style="width:44px;height:44px;min-width:44px;'
                    'background:linear-gradient(135deg,#fff8e1,#ffeaa0);'
                    'border-radius:8px;display:flex;align-items:center;'
                    'justify-content:center;font-size:1.3em">' + ic + '</div>'
                    '<div>'
                    '<div style="font-family:Montserrat,sans-serif;font-weight:700;'
                    'color:#1a1a1a;font-size:0.9em;margin-bottom:4px">' + t + '</div>'
                    '<div style="color:#888;font-size:0.84em;line-height:1.6">' + d + '</div>'
                    '</div></div>',
                    unsafe_allow_html=True
                )
    st.markdown('</div>', unsafe_allow_html=True)

    # TESTIMONIALS
    st.markdown('<div style="background:#f2f0eb;padding:25px 0;width:100%">', unsafe_allow_html=True)
    _, m, _ = st.columns([1, 8, 1])
    with m:
        sec_header("Client Stories", "What Our Clients Say")
        t1, t2, t3 = st.columns(3)
        for col, (txt, auth, loc) in zip([t1,t2,t3], [
            ("JDF built our dream home in Karwar with incredible precision. "
             "Professional, timely and beyond every expectation we had set.",
             "Ramesh Naik", "Karwar"),
            ("Outstanding commercial project in Mangalore — on schedule, "
             "within budget and genuinely impressive quality throughout.",
             "Priya Shetty", "Mangalore"),
            ("JDF transformed our Honnawar building into a modern masterpiece. "
             "Best construction company on the entire Karnataka coast.",
             "Suresh Hegde", "Honnawar"),
        ]):
            with col:
                st.markdown(
                    '<div style="background:#ffffff;border-radius:8px;padding:28px 24px;'
                    'box-shadow:0 4px 18px rgba(0,0,0,0.07);border:1px solid #e0dcd0;'
                    'border-top:3px solid #c9a227;margin:0 4px">'
                    '<div style="font-family:Georgia,serif;font-size:3em;'
                    'color:rgba(201,162,39,0.25);line-height:1;margin-bottom:6px">"</div>'
                    '<div style="color:#555;font-style:italic;font-size:0.9em;'
                    'line-height:1.82;margin-bottom:16px">' + txt + '</div>'
                    '<div style="color:#c9a227;font-size:0.9em;margin-bottom:8px">'
                    '⭐⭐⭐⭐⭐</div>'
                    '<div style="font-family:Montserrat,sans-serif;color:#1a1a1a;'
                    'font-weight:700;font-size:0.85em">' + auth + '</div>'
                    '<div style="color:#c9a227;font-size:0.75em;margin-top:2px">'
                    '📍 ' + loc + '</div>'
                    '</div>',
                    unsafe_allow_html=True
                )
    st.markdown('</div>', unsafe_allow_html=True)

    # CTA
    st.markdown('<div style="background:#f2f0eb;padding:0 0 60px;width:100%">', unsafe_allow_html=True)
    _, m, _ = st.columns([1, 8, 1])
    with m:
        st.markdown(
            '<div style="background:linear-gradient(135deg,#c9a227,#e8c040,#c9a227);'
            'padding:60px 40px;text-align:center;border-radius:10px;'
            'box-shadow:0 12px 48px rgba(201,162,39,0.35)">'
            '<div style="font-family:Cormorant Garamond,serif;font-size:2.5em;'
            'color:#fff;font-weight:700;margin-bottom:12px">'
            'Ready to Build Your Dream Project?</div>'
            '<p style="color:rgba(255,255,255,0.88);font-size:0.97em;margin-bottom:28px">'
            "FREE consultation and detailed quotation from Karnataka's most trusted experts.</p>"
            '<a href="tel:+919019429427" '
            'style="display:inline-block;background:#fff;color:#b8960c;'
            'padding:14px 44px;border-radius:5px;font-size:0.84em;font-weight:800;'
            'text-decoration:none;letter-spacing:1.5px;text-transform:uppercase;margin:6px">'
            '📞 Call: 90194 29427</a>'
            '<a href="https://wa.me/919019429427" target="_blank" '
            'style="display:inline-block;background:#1a1200;color:#c9a227;'
            'padding:14px 44px;border-radius:5px;font-size:0.84em;font-weight:800;'
            'text-decoration:none;letter-spacing:1.5px;text-transform:uppercase;margin:6px">'
            '💬 WhatsApp Us</a>'
            '<p style="color:rgba(255,255,255,0.6);font-size:0.82em;margin-top:20px">'
            '📍 Near Dwarka Hotel, Habuwada Main Road, Karwar, Karnataka</p>'
            '</div>',
            unsafe_allow_html=True
        )
    st.markdown('</div>', unsafe_allow_html=True)


# ───────────────────────────────────────────────
# SERVICES PAGE
# ───────────────────────────────────────────────
elif pg == "Services":

    st.markdown('<div style="background:#f2f0eb;padding:20px 0;width:100%">', unsafe_allow_html=True)
    _, m, _ = st.columns([1, 8, 1])
    with m:
        sec_header("What We Do", "Our Services",
                   "Comprehensive construction solutions across coastal Karnataka.")

        svcs = [
            ("🏠","Residential Construction",
             "Custom bungalows and villas, Multi-storey apartments, "
             "Duplex houses, Coastal architecture, Gated communities",
             "Karwar, Ankola, Honnawar, Mangalore"),
            ("🏢","Commercial Construction",
             "Office complexes, Shopping centres, Hotels and resorts, "
             "Warehouses, Mixed-use developments",
             "Mangalore, Karwar"),
            ("🛣️","Infrastructure and Civil Works",
             "Roads and highways, Bridges and culverts, "
             "Storm-water drainage, Retaining walls, Government contracts",
             "All Locations"),
            ("🔧","Renovation and Remodelling",
             "Complete makeovers, Commercial refurbishments, "
             "Kitchen and bathroom upgrades, Premium flooring, Extensions",
             "All Locations"),
            ("🏗️","Foundation and Structural",
             "Deep foundation, RCC structures, Steel frame construction, "
             "Earthquake-resistant design, Soil testing",
             "All Locations"),
            ("🎨","Interior Construction",
             "False ceilings and partitions, Advanced waterproofing, "
             "MEP plumbing and electrical, Modular fixtures, Premium finishes",
             "All Locations"),
        ]

        for i in range(0, len(svcs), 2):
            ca, cb = st.columns(2)
            for col, idx in zip([ca, cb], [i, i+1]):
                if idx < len(svcs):
                    ic, title, desc, locs = svcs[idx]
                    with col:
                        st.markdown(
                            '<div style="background:#ffffff;border-radius:8px;padding:26px;'
                            'box-shadow:0 4px 18px rgba(0,0,0,0.07);border:1px solid #e0dcd0;'
                            'margin:0 4px 20px">'
                            '<div style="display:flex;align-items:center;gap:14px;margin-bottom:14px">'
                            '<div style="width:54px;height:54px;min-width:54px;'
                            'background:linear-gradient(135deg,#fff8e1,#ffeaa0);'
                            'border-radius:50%;display:flex;align-items:center;'
                            'justify-content:center;font-size:1.6em;border:2px solid #f0d060">'
                            + ic + '</div>'
                            '<div style="font-family:Cormorant Garamond,serif;font-size:1.18em;'
                            'font-weight:700;color:#1a1a1a">' + title + '</div></div>'
                            '<div style="color:#666;font-size:0.86em;line-height:1.9;'
                            'margin-bottom:14px">' + desc + '</div>'
                            '<span style="display:inline-block;background:#fff8e1;color:#9a7a10;'
                            'padding:4px 12px;border-radius:20px;font-size:0.72em;font-weight:700;'
                            'border:1px solid #e8c840">📍 ' + locs + '</span>'
                            '</div>',
                            unsafe_allow_html=True
                        )
    st.markdown('</div>', unsafe_allow_html=True)

    # BUILD PROCESS
    st.markdown('<div style="background:#ffffff;padding:25px 0;width:100%">', unsafe_allow_html=True)
    _, m, _ = st.columns([1, 8, 1])
    with m:
        sec_header("How We Work", "Our Build Process",
                   "Transparent and client-centric — from first meeting to final handover.")
        steps = [
            ("1","Consultation","Free meeting to understand your vision, site and requirements"),
            ("2","Design","Plans, structural drawings and 3D visualisation"),
            ("3","Quotation","Transparent itemised estimate with full material specs"),
            ("4","Agreement","Clear contract with milestones, timeline and payments"),
            ("5","Construction","Quality build with real-time updates and site access"),
            ("6","Handover","Final inspection, defect resolution, warranty and keys"),
        ]
        p1, p2, p3 = st.columns(3)
        for i, (num, t, d) in enumerate(steps):
            with [p1, p2, p3][i % 3]:
                st.markdown(
                    '<div style="background:#f9f7f2;border-radius:8px;padding:26px 18px;'
                    'text-align:center;border:1px solid #e0dcd0;margin-bottom:16px">'
                    '<div style="width:42px;height:42px;'
                    'background:linear-gradient(135deg,#c9a227,#e8c040);border-radius:50%;'
                    'display:flex;align-items:center;justify-content:center;'
                    'font-family:Cormorant Garamond,serif;font-size:1.3em;font-weight:700;'
                    'color:#fff;margin:0 auto 12px">' + num + '</div>'
                    '<div style="font-family:Cormorant Garamond,serif;font-size:1.1em;'
                    'color:#1a1a1a;font-weight:700;margin-bottom:6px">' + t + '</div>'
                    '<div style="color:#888;font-size:0.83em;line-height:1.6">' + d + '</div>'
                    '</div>',
                    unsafe_allow_html=True
                )
        st.markdown("<br>", unsafe_allow_html=True)
        _, ctr, _ = st.columns([2, 1, 2])
        with ctr:
            if st.button("📞 Get Free Quote", key="svc_cta"):
                go("Contact Us")
    st.markdown('</div>', unsafe_allow_html=True)


# ───────────────────────────────────────────────
# LOCATIONS PAGE
# ───────────────────────────────────────────────
elif pg == "Locations":

    st.markdown('<div style="background:#f2f0eb;padding:20px 0;width:100%">', unsafe_allow_html=True)
    _, m, _ = st.columns([1, 8, 1])
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
                'border-radius:8px;padding:16px;min-width:200px;font-family:sans-serif">'
                '<div style="color:#c9a227;font-weight:700;font-size:1em;margin-bottom:10px">'
                + ("HQ: " if d["hq"] else "") + city + '</div>'
                '<div style="color:#555;font-size:0.84em;line-height:1.8">'
                'Projects: <b style="color:#c9a227">' + d["projects"] + '</b><br>'
                'Specialty: ' + d["spec"] + '<br>'
                'Address: ' + d["addr"] + '</div>'
                '<div style="margin-top:12px;text-align:center">'
                '<a href="tel:+919019429427" style="background:#c9a227;color:#fff;'
                'padding:7px 14px;border-radius:4px;text-decoration:none;'
                'font-weight:700;font-size:0.8em">📞 Call Jason</a></div></div>'
            )
            folium.Marker(
                [d["lat"],d["lon"]],
                popup=folium.Popup(popup, max_width=240),
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
        st_folium(fmap, width=None, height=520, returned_objects=[])
        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown("<br><br>", unsafe_allow_html=True)

        cc = st.columns(4)
        for col, (badge, bc, city) in zip(cc, [
            ("HEADQUARTERS","#c9a227","Karwar"),
            ("ACTIVE OPS","#888","Ankola"),
            ("ACTIVE OPS","#888","Honnawar"),
            ("COMMERCIAL HUB","#888","Mangalore"),
        ]):
            d = loc_data[city]
            with col:
                st.markdown(
                    '<div style="background:#fff;border-radius:8px;padding:22px 18px;'
                    'box-shadow:0 4px 18px rgba(0,0,0,0.07);border:1px solid #e0dcd0;'
                    'border-top:4px solid #c9a227;margin:0 4px">'
                    '<div style="color:' + bc + ';font-family:Montserrat,sans-serif;'
                    'font-size:0.65em;font-weight:700;letter-spacing:2px;'
                    'text-transform:uppercase;margin-bottom:8px">' + badge + '</div>'
                    '<div style="font-family:Cormorant Garamond,serif;font-size:1.5em;'
                    'color:#1a1a1a;font-weight:700;margin-bottom:10px">📍 ' + city + '</div>'
                    '<div style="font-family:Montserrat,sans-serif;color:#bbb;font-size:0.65em;'
                    'text-transform:uppercase;letter-spacing:1px;margin-bottom:3px">Projects</div>'
                    '<div style="font-family:Cormorant Garamond,serif;font-size:2.2em;'
                    'color:#c9a227;font-weight:700;margin-bottom:10px">' + d["projects"] + '</div>'
                    '<div style="color:#666;font-size:0.84em;margin-bottom:10px">'
                    + d["spec"] + '</div>'
                    '<div style="color:#bbb;font-size:0.74em;border-top:1px solid #f0ede4;'
                    'padding-top:10px;line-height:1.7">' + d["addr"] + '</div></div>',
                    unsafe_allow_html=True
                )
    st.markdown('</div>', unsafe_allow_html=True)


# ───────────────────────────────────────────────
# ABOUT US PAGE
# ───────────────────────────────────────────────
elif pg == "About Us":

    owner_b64 = img_to_b64("jason_photo.jpg")

    st.markdown('<div style="background:#f2f0eb;padding:20px 0;width:100%">', unsafe_allow_html=True)
    _, m, _ = st.columns([1, 8, 1])
    with m:
        sec_header("Who We Are", "About JDF Constructions")

        a1, a2 = st.columns([1, 1.8])

        with a1:
            if owner_b64:
                st.markdown(
                    '<img src="data:image/jpeg;base64,' + owner_b64 + '" '
                    'style="width:100%;border-radius:8px 8px 0 0;'
                    'object-fit:cover;object-position:top center;'
                    'display:block;max-height:300px">',
                    unsafe_allow_html=True
                )
            else:
                st.markdown(
                    '<div style="background:#2d2000;border-radius:8px 8px 0 0;'
                    'height:260px;display:flex;align-items:center;'
                    'justify-content:center;font-size:5em">👤</div>',
                    unsafe_allow_html=True
                )
            st.markdown(
                '<div style="background:#fff;border-radius:0 0 8px 8px;padding:22px;'
                'box-shadow:0 4px 18px rgba(0,0,0,0.07);border:1px solid #e0dcd0;'
                'border-top:4px solid #c9a227;text-align:center">'
                '<div style="font-family:Cormorant Garamond,serif;font-size:1.6em;'
                'font-weight:700;color:#1a1a1a">Jason Fernandes</div>'
                '<div style="font-family:Montserrat,sans-serif;font-size:0.63em;'
                'letter-spacing:2px;color:#c9a227;text-transform:uppercase;'
                'font-weight:700;margin:5px 0 11px">Founder and Managing Director</div>'
                '<div style="color:#777;font-size:0.84em;line-height:1.7;margin-bottom:14px">'
                '15+ years building exceptional structures across coastal Karnataka.</div>'
                '<a href="tel:+919019429427" '
                'style="display:inline-block;'
                'background:linear-gradient(135deg,#c9a227,#e8c040);'
                'color:#fff;padding:10px 24px;border-radius:5px;font-weight:700;'
                'text-decoration:none;font-size:0.86em">📱 90194 29427</a>'
                '</div>',
                unsafe_allow_html=True
            )

        with a2:
            st.markdown(
                '<div style="padding-left:20px">'
                '<div style="font-family:Cormorant Garamond,serif;font-size:2em;'
                'font-weight:700;color:#1a1a1a;margin-bottom:18px">Our Story</div>'
                '<div style="color:#555;line-height:1.95;font-size:0.93em">'
                '<p style="margin-bottom:14px">JDF Constructions was founded with a singular '
                'vision — to bring <strong style="color:#1a1a1a">world-class construction '
                'quality</strong> to the beautiful coastal belt of Karnataka.</p>'
                '<p style="margin-bottom:14px">Under the leadership of '
                '<strong style="color:#c9a227">Jason Fernandes</strong>, the company has grown '
                'into one of the most trusted construction brands across Uttara Kannada '
                'and Dakshina Kannada districts.</p>'
                '<p style="margin-bottom:14px">Starting from '
                '<strong>Karwar</strong>, JDF has expanded to '
                '<strong>Ankola</strong>, <strong>Honnawar</strong> and '
                '<strong>Mangalore</strong> — serving hundreds of families, '
                'businesses and government institutions.</p>'
                '<p style="font-family:Cormorant Garamond,serif;font-size:1.2em;'
                'color:#c9a227;font-style:italic">'
                '"Your dream project starts here."</p></div></div>',
                unsafe_allow_html=True
            )

            st.markdown("<br>", unsafe_allow_html=True)
            m1, m2 = st.columns(2)
            for col, (ic, t, d) in zip([m1,m2,m1,m2], [
                ("🎯","Mission",     "Superior construction with integrity and excellence."),
                ("👁️","Vision",     "Karnataka's most trusted construction brand."),
                ("💎","Values",     "Quality, Integrity, Innovation, Sustainability"),
                ("🏅","Commitment","Every project treated as if it were our own home."),
            ]):
                with col:
                    st.markdown(
                        '<div style="background:#fff;border-radius:8px;padding:18px;'
                        'margin-bottom:12px;box-shadow:0 2px 10px rgba(0,0,0,0.06);'
                        'border:1px solid #e0dcd0;border-left:3px solid #c9a227">'
                        '<div style="font-size:1.6em;margin-bottom:8px">' + ic + '</div>'
                        '<div style="font-family:Cormorant Garamond,serif;font-size:1.05em;'
                        'font-weight:700;color:#1a1a1a;margin-bottom:4px">' + t + '</div>'
                        '<div style="color:#888;font-size:0.83em">' + d + '</div></div>',
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
                    '<div style="margin-bottom:18px">'
                    '<div style="display:flex;justify-content:space-between;margin-bottom:8px">'
                    '<span style="font-family:Montserrat,sans-serif;color:#333;'
                    'font-size:0.86em;font-weight:600">' + s + '</span>'
                    '<span style="font-family:Montserrat,sans-serif;color:#c9a227;'
                    'font-weight:700;font-size:0.86em">' + str(p) + '%</span></div>'
                    '<div style="background:#e8e4d8;border-radius:50px;height:7px;overflow:hidden">'
                    '<div style="height:100%;width:' + str(p) + '%;'
                    'background:linear-gradient(90deg,#c9a227,#f5d77e);'
                    'border-radius:50px"></div></div></div>',
                    unsafe_allow_html=True
                )

        st.markdown("<br>", unsafe_allow_html=True)
        mc = st.columns(4)
        for col, (ic, t, s) in zip(mc, [
            ("🏅","Licensed Contractor","Karnataka PWD Certified"),
            ("📋","RERA Compliant","All projects registered"),
            ("🌱","Green Building","Eco-friendly certified"),
            ("🔒","Quality Standards","ISO-aligned QMS"),
        ]):
            with col:
                st.markdown(
                    '<div style="background:#fff;border-radius:8px;padding:24px 16px;'
                    'text-align:center;box-shadow:0 3px 14px rgba(0,0,0,0.06);'
                    'border:1px solid #e0dcd0;margin:0 4px">'
                    '<div style="font-size:2em;margin-bottom:10px">' + ic + '</div>'
                    '<div style="font-family:Cormorant Garamond,serif;font-size:1em;'
                    'color:#1a1a1a;font-weight:700;margin-bottom:5px">' + t + '</div>'
                    '<div style="font-family:Montserrat,sans-serif;color:#aaa;'
                    'font-size:0.76em">' + s + '</div></div>',
                    unsafe_allow_html=True
                )
    st.markdown('</div>', unsafe_allow_html=True)


# ───────────────────────────────────────────────
# CONTACT US PAGE
# ───────────────────────────────────────────────
elif pg == "Contact Us":

    st.markdown('<div style="background:#f2f0eb;padding:20px 0;width:100%">', unsafe_allow_html=True)
    _, m, _ = st.columns([1, 8, 1])
    with m:
        sec_header("Get In Touch", "Contact JDF Constructions",
                   "Ready to build your dream project? "
                   "Reach out for a free consultation and quotation.")

        cf1, cf2 = st.columns([1.6, 1])

        with cf1:
            st.markdown(
                '<div style="background:#fff;border-radius:8px;padding:30px;'
                'box-shadow:0 4px 18px rgba(0,0,0,0.07);border:1px solid #e0dcd0">'
                '<div style="font-family:Cormorant Garamond,serif;font-size:1.4em;'
                'font-weight:700;color:#1a1a1a;margin-bottom:20px;padding-bottom:12px;'
                'border-bottom:2px solid #f0ede4">📝 Send Us a Message</div>',
                unsafe_allow_html=True
            )
            with st.form("enquiry_form", clear_on_submit=True):
                name   = st.text_input("Full Name", placeholder="e.g. Ravi Kumar")
                phone  = st.text_input("Phone Number", placeholder="e.g. 9876543210")
                email  = st.text_input("Email (optional)", placeholder="you@email.com")
                city   = st.selectbox("Your City", ["Karwar","Ankola","Honnawar","Mangalore","Other"])
                ptype  = st.selectbox("Project Type", [
                    "Residential Home","Commercial Building",
                    "Renovation","Infrastructure","Interior Work","Other"])
                budget = st.selectbox("Approximate Budget", [
                    "Under Rs.10 Lakhs","Rs.10-25 Lakhs","Rs.25-50 Lakhs",
                    "Rs.50 Lakhs-1 Crore","Above Rs.1 Crore"])
                msg    = st.text_area("Project Details",
                    placeholder="Describe your site, timeline, requirements...", height=110)
                if st.form_submit_button("Submit Enquiry"):
                    if name.strip() and phone.strip():
                        st.success(
                            "Thank you " + name + "! Your enquiry for " +
                            ptype + " in " + city + " is received. " +
                            "Jason will call " + phone + " within 24 hours.")
                        st.balloons()
                    else:
                        st.error("Please enter your name and phone number.")
            st.markdown('</div>', unsafe_allow_html=True)

        with cf2:
            st.markdown(
                '<div style="background:#fff;border-radius:8px;padding:24px;'
                'box-shadow:0 4px 18px rgba(0,0,0,0.07);border:1px solid #e0dcd0;'
                'margin-bottom:16px">'
                '<div style="font-family:Cormorant Garamond,serif;font-size:1.25em;'
                'font-weight:700;color:#1a1a1a;margin-bottom:16px;padding-bottom:10px;'
                'border-bottom:2px solid #f0ede4">Our Details</div>'
                '<div style="padding:10px 0;border-bottom:1px solid #f5f2ea">'
                '<span style="color:#c9a227;font-weight:700;font-family:Montserrat,sans-serif">'
                'Jason Fernandes</span><br>'
                '<span style="color:#bbb;font-size:0.76em">Founder and Managing Director</span></div>'
                '<div style="padding:10px 0;border-bottom:1px solid #f5f2ea;'
                'font-family:Montserrat,sans-serif;font-size:0.9em">'
                '📱 <strong>90194 29427</strong><br>'
                '<span style="color:#bbb;font-size:0.76em">Call or WhatsApp</span></div>'
                '<div style="padding:10px 0;border-bottom:1px solid #f5f2ea;'
                'font-family:Montserrat,sans-serif;font-size:0.88em;color:#444">'
                '📍 Near Dwarka Hotel, Habuwada Main Road, Karwar<br>'
                '<span style="color:#bbb;font-size:0.82em">Karnataka — 581 301</span></div>'
                '<div style="padding:10px 0;border-bottom:1px solid #f5f2ea;'
                'font-family:Montserrat,sans-serif;font-size:0.88em;color:#444">'
                '🕐 Monday to Saturday, 9 AM to 7 PM</div>'
                '<div style="padding:10px 0;font-family:Montserrat,sans-serif;'
                'font-size:0.88em;color:#444">'
                '🏙️ Karwar, Ankola, Honnawar, Mangalore</div></div>',
                unsafe_allow_html=True
            )
            st.markdown(
                '<div style="background:#fff;border-radius:8px;padding:24px;'
                'box-shadow:0 4px 18px rgba(0,0,0,0.07);border:1px solid #e0dcd0">'
                '<div style="font-family:Cormorant Garamond,serif;font-size:1.25em;'
                'font-weight:700;color:#1a1a1a;margin-bottom:16px;padding-bottom:10px;'
                'border-bottom:2px solid #f0ede4">Quick Connect</div>'
                '<a href="tel:+919019429427" '
                'style="display:block;text-align:center;padding:12px;border-radius:6px;'
                'text-decoration:none;font-weight:700;font-size:0.85em;margin-bottom:10px;'
                'background:linear-gradient(135deg,#c9a227,#e8c040);color:#fff;'
                'font-family:Montserrat,sans-serif">📞 Call: 90194 29427</a>'
                '<a href="https://wa.me/919019429427" target="_blank" '
                'style="display:block;text-align:center;padding:12px;border-radius:6px;'
                'text-decoration:none;font-weight:700;font-size:0.85em;margin-bottom:10px;'
                'background:linear-gradient(135deg,#25D366,#128C7E);color:#fff;'
                'font-family:Montserrat,sans-serif">💬 WhatsApp Jason</a>'
                '<a href="https://maps.google.com/?q=Dwarka+Hotel+Habuwada+Karwar" '
                'target="_blank" '
                'style="display:block;text-align:center;padding:12px;border-radius:6px;'
                'text-decoration:none;font-weight:700;font-size:0.85em;'
                'background:linear-gradient(135deg,#1a73e8,#4285F4);color:#fff;'
                'font-family:Montserrat,sans-serif">🗺️ Get Directions</a></div>',
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
                '<div style="padding:14px;min-width:190px;font-family:sans-serif">'
                '<b style="color:#c9a227">JDF Constructions HQ</b><br><br>'
                'Near Dwarka Hotel<br>Habuwada Main Road, Karwar<br>'
                'Karnataka 581 301<br><br>'
                '<a href="tel:+919019429427" style="background:#c9a227;color:#fff;'
                'padding:6px 12px;border-radius:4px;text-decoration:none;font-weight:700">'
                '📞 90194 29427</a></div>', max_width=240
            ),
            tooltip="JDF Constructions Headquarters",
            icon=folium.DivIcon(html=hq_pin, icon_size=(54,54), icon_anchor=(27,27))
        ).add_to(hq)
        st.markdown(
            '<div style="border-radius:10px;overflow:hidden;'
            'box-shadow:0 6px 26px rgba(0,0,0,0.1);border:2px solid #ddd">',
            unsafe_allow_html=True
        )
        st_folium(hq, width=None, height=400, returned_objects=[])
        st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)


# ── FOOTER
st.markdown(
    '<div style="background:linear-gradient(135deg,#1c1400,#2d2000,#1a1200);'
    'padding:50px 60px 28px;width:100%">'
    '<div style="max-width:1200px;margin:0 auto;display:flex;'
    'justify-content:space-between;flex-wrap:wrap;gap:30px">'
    '<div>'
    '<div style="font-family:Cormorant Garamond,serif;font-size:1.9em;'
    'color:#c9a227;font-weight:700;letter-spacing:3px;margin-bottom:8px">'
    '🏗️ JDF CONSTRUCTIONS</div>'
    '<div style="color:rgba(201,162,39,0.55);font-style:italic;'
    'font-family:Cormorant Garamond,serif;font-size:1.05em;margin-bottom:12px">'
    '"Your dream project starts here."</div>'
    '<div style="color:#4a4000;font-size:0.8em;font-family:Montserrat,sans-serif">'
    'Karwar | Ankola | Honnawar | Mangalore</div></div>'
    '<div style="color:#4a4000;font-family:Montserrat,sans-serif;'
    'font-size:0.82em;line-height:2.2">'
    '<div style="color:rgba(201,162,39,0.55);font-weight:700;'
    'margin-bottom:8px;letter-spacing:1px">CONTACT</div>'
    '<div>📍 Near Dwarka Hotel, Habuwada Main Road, Karwar</div>'
    '<div>📞 +91 90194 29427</div>'
    '<div>🕐 Mon to Sat, 9 AM to 7 PM</div></div>'
    '<div style="color:#4a4000;font-family:Montserrat,sans-serif;'
    'font-size:0.82em;line-height:2.4">'
    '<div style="color:rgba(201,162,39,0.55);font-weight:700;'
    'margin-bottom:8px;letter-spacing:1px">PAGES</div>'
    '<div>Home | Services | Locations</div>'
    '<div>About Us | Contact Us</div></div></div>'
    '<div style="border-top:1px solid #2a2000;margin-top:24px;padding-top:18px;'
    'text-align:center">'
    '<div style="color:#3a3000;font-family:Montserrat,sans-serif;font-size:0.76em">'
    '2024 JDF Constructions. All Rights Reserved. '
    'Building Karnataka\'s Coastal Future</div></div></div>',
    unsafe_allow_html=True
)