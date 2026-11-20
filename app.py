import base64
import streamlit as st

st.set_page_config(
    page_title="Upside ng — Video Editing & Visual Storytelling Portfolio",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="collapsed",
)

WHATSAPP_NUMBER = "08156774091"
WHATSAPP_INTL = "2348156774091"
EMAIL_ADDRESS = "upside.ng@gmail.com"
FOLDER_URL = "https://drive.google.com/drive/folders/19pFTNObj9PVT9azApfdeeTq8FjURLM6M?usp=drive_link"
DRIVE_FOOTBALL_URL = "https://drive.google.com/file/d/15sUL-HGn9iEedm3RdQOQ_iXRBR-8lnkY/view?usp=drivesdk"
DRIVE_POV_URL = "https://drive.google.com/file/d/1bGhZIyAfgjy2UTyHDIO75wd6Vrdg-BYe/view?usp=drivesdk"
DRIVE_SCHOOL_URL = "https://drive.google.com/file/d/1cDwvAh4g9Oldvb-rLKqmeEx3KLRqp_a_/view?usp=drivesdk"
DRIVE_CELEBRATION_URL = "https://drive.google.com/file/d/1tDOHYc8wWLObr3QyZSsFr50ulgj4271_/view?usp=drivesdk"
DRIVE_INTERVIEW_URL = "https://drive.google.com/file/d/1EB7wlfetH351w9bO9BBTuXWJkfT3RR6Z/view?usp=drivesdk"
DRIVE_SPEAKER_URL = "https://drive.google.com/file/d/1Bg1tssHRuPGo-xEiJiLr83dIQKGN8LSw/view?usp=drivesdk"

IG_URL = "https://www.instagram.com/godsongeorge19?dlrf=MXNwbDRmejZsMG1veg=="
TT_URL = "https://www.tiktok.com/@godsongeorge91?_r=1&_t=ZS-9B925sTsYzd"
LI_URL = "https://www.linkedin.com/in/michael-blessing-27799923b?utm_source=share_via&utm_content=profile&utm_medium=member_android"
FB_URL = "https://www.facebook.com/share/1FNNe8m19D/"


def svg_uri(svg_text: str) -> str:
    return "data:image/svg+xml;base64," + base64.b64encode(svg_text.encode("utf-8")).decode("utf-8")


CEO_PORTRAIT_URI = svg_uri("""<svg xmlns="http://www.w3.org/2000/svg" width="600" height="750" viewBox="0 0 600 750">
  <rect width="600" height="750" fill="#334155"/>
  <rect x="105" y="704" width="390" height="34" rx="10" fill="#0f172a"/>
  <text x="300" y="726" text-anchor="middle" fill="#f8fafc" font-family="sans-serif" font-size="14" font-weight="bold">Michael Blessing • CEO, Upside ng</text>
</svg>""")

SPEAKER_STILL_URI = svg_uri("""<svg xmlns="http://www.w3.org/2000/svg" width="800" height="450" viewBox="0 0 800 450">
  <rect width="800" height="450" fill="#1e293b"/>
  <rect x="70" y="60" width="660" height="330" rx="14" fill="#f1f5f9"/>
  <text x="415" y="165" text-anchor="middle" fill="#991b1b" font-family="sans-serif" font-size="78" font-weight="bold" opacity="0.28">CF</text>
  <rect x="195" y="344" width="410" height="38" rx="10" fill="#0f172a"/>
  <text x="400" y="369" text-anchor="middle" fill="#f8fafc" font-family="sans-serif" font-size="13" font-weight="bold">Campus Fellowship Stage Speaking • Mic &amp; Podium</text>
</svg>""")

INTERVIEW_STILL_URI = svg_uri("""<svg xmlns="http://www.w3.org/2000/svg" width="800" height="450" viewBox="0 0 800 450">
  <rect width="800" height="450" fill="#1e293b"/>
  <rect x="70" y="60" width="660" height="330" rx="14" fill="#475569"/>
  <circle cx="635" cy="105" r="32" fill="#0f172a" stroke="#38bdf8" stroke-width="2.5"/>
  <text x="635" y="102" text-anchor="middle" fill="#ffffff" font-family="sans-serif" font-size="8.5" font-weight="bold">DARAMOLA</text>
  <text x="635" y="114" text-anchor="middle" fill="#34d399" font-family="sans-serif" font-size="8.5" font-weight="bold">DYNASTY</text>
  <rect x="190" y="290" width="420" height="62" rx="10" fill="#0f172a"/>
  <text x="400" y="316" text-anchor="middle" fill="#ffffff" font-family="sans-serif" font-size="14" font-weight="bold">these are the things that</text>
  <text x="400" y="339" text-anchor="middle" fill="#34d399" font-family="sans-serif" font-size="14" font-weight="bold">makes us grow as individuals</text>
</svg>""")

CELEBRATION_STILL_URI = svg_uri("""<svg xmlns="http://www.w3.org/2000/svg" width="800" height="450" viewBox="0 0 800 450">
  <rect width="800" height="450" fill="#1e293b"/>
  <rect x="70" y="60" width="660" height="330" rx="14" fill="#334155"/>
  <path d="M295 165 Q365 110 435 165 Q415 215 365 215 Q315 215 295 165 Z" fill="#fbcfe8"/>
  <path d="M285 375 L310 275 L420 275 L445 375 Z" fill="#fce7f3"/>
  <rect x="195" y="335" width="410" height="40" rx="10" fill="#0f172a"/>
  <text x="400" y="360" text-anchor="middle" fill="#fbcfe8" font-family="sans-serif" font-size="14" font-weight="bold">Celebration &amp; Event Highlight • Peach Gele &amp; Fan</text>
</svg>""")

SCHOOL_STILL_URI = svg_uri("""<svg xmlns="http://www.w3.org/2000/svg" width="800" height="450" viewBox="0 0 800 450">
  <rect width="800" height="450" fill="#0f172a"/>
  <rect x="70" y="60" width="660" height="330" rx="14" fill="#1e3a2f"/>
  <circle cx="635" cy="108" r="32" fill="#0f172a" stroke="#38bdf8" stroke-width="2.5"/>
  <text x="635" y="105" text-anchor="middle" fill="#ffffff" font-family="sans-serif" font-size="8.5" font-weight="bold">DARAMOLA</text>
  <text x="635" y="117" text-anchor="middle" fill="#34d399" font-family="sans-serif" font-size="8.5" font-weight="bold">DYNASTY</text>
  <rect x="165" y="255" width="470" height="42" rx="10" fill="#0f172a"/>
  <text x="400" y="281" text-anchor="middle" fill="#34d399" font-family="sans-serif" font-size="13" font-weight="bold">Daramola Dynasty • Two Schools Outreach (Ishara)</text>
</svg>""")

POV_STILL_URI = svg_uri("""<svg xmlns="http://www.w3.org/2000/svg" width="800" height="450" viewBox="0 0 800 450">
  <rect width="800" height="450" fill="#64748b"/>
  <polygon points="340,210 460,210 680,450 120,450" fill="#334155"/>
  <circle cx="645" cy="68" r="34" fill="#0f172a" stroke="#38bdf8" stroke-width="3"/>
  <text x="645" y="65" text-anchor="middle" fill="#ffffff" font-family="sans-serif" font-size="10" font-weight="bold">DYNASTY</text>
  <text x="645" y="78" text-anchor="middle" fill="#34d399" font-family="sans-serif" font-size="9" font-weight="bold">ACADEMY</text>
  <rect x="195" y="346" width="410" height="58" rx="12" fill="#0f172a"/>
  <text x="400" y="370" text-anchor="middle" fill="#ffffff" font-family="sans-serif" font-size="15" font-weight="bold">POV: that one bro that blame</text>
  <text x="400" y="392" text-anchor="middle" fill="#34d399" font-family="sans-serif" font-size="15" font-weight="bold">everyone except himself</text>
</svg>""")

ACADEMY_STILL_URI = svg_uri("""<svg xmlns="http://www.w3.org/2000/svg" width="800" height="450" viewBox="0 0 800 450">
  <rect width="800" height="225" fill="#cbd5e1"/>
  <rect y="225" width="800" height="225" fill="#1b5e20"/>
  <circle cx="630" cy="70" r="36" fill="#0f172a" stroke="#38bdf8" stroke-width="3"/>
  <text x="630" y="66" text-anchor="middle" fill="#ffffff" font-family="sans-serif" font-size="10.5" font-weight="bold">DYNASTY</text>
  <text x="630" y="80" text-anchor="middle" fill="#34d399" font-family="sans-serif" font-size="9.5" font-weight="bold">FOOTBALL ACADEMY</text>
  <rect x="35" y="382" width="365" height="38" rx="10" fill="#0f172a"/>
  <text x="52" y="406" fill="#ffffff" font-family="sans-serif" font-size="14" font-weight="bold">Dynasty Football Academy • Pitch Action Frame</text>
</svg>""")

if "portrait_data_uri" not in st.session_state:
    st.session_state.portrait_data_uri = CEO_PORTRAIT_URI

if "custom_media" not in st.session_state:
    st.session_state.custom_media = []

st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(180deg, #f8fafc 0%, #eef2ff 100%);
        color: #0f172a;
    }
    .stApp p, .stApp label, .stApp div[data-testid="stMarkdownContainer"] p, .stApp div[data-testid="stMarkdownContainer"] li {
        color: #1e293b;
    }
    .upside-hero {
        background: linear-gradient(135deg, #0f172a 0%, #1e1b4b 55%, #312e81 100%);
        padding: 2rem 2.25rem;
        border-radius: 18px;
        color: #ffffff;
        margin-bottom: 1.5rem;
        box-shadow: 0 12px 28px -6px rgba(15, 23, 42, 0.25);
    }
    .upside-hero h1 {
        margin: 0.35rem 0 0.65rem 0;
        font-size: 2.2rem;
        font-weight: 800;
        letter-spacing: -0.02em;
        color: #ffffff;
    }
    .upside-hero p {
        margin: 0;
        color: #e0e7ff;
        font-size: 1.03rem;
        line-height: 1.6;
    }
    .upside-hero .hero-contact-bar {
        margin-top: 1.1rem;
        font-size: 0.92rem;
        color: #f8fafc;
    }
    .upside-badge {
        display: inline-block;
        background: rgba(16, 185, 129, 0.22);
        border: 1px solid rgba(52, 211, 153, 0.55);
        color: #34d399;
        font-size: 0.78rem;
        font-weight: 700;
        padding: 0.25rem 0.75rem;
        border-radius: 999px;
    }
    .surface-card {
        background: #ffffff;
        border: 1px solid #cbd5e1;
        border-radius: 16px;
        padding: 1.35rem;
        box-shadow: 0 4px 14px rgba(15, 23, 42, 0.05);
        height: 100%;
    }
    .portrait-frame {
        border-radius: 16px;
        overflow: hidden;
        border: 3px solid #ffffff;
        box-shadow: 0 14px 28px rgba(15, 23, 42, 0.35);
        background: #0f172a;
    }
    .portrait-frame img {
        width: 100%;
        aspect-ratio: 4 / 5;
        object-fit: cover;
        object-position: top center;
        display: block;
    }
    .card-thumb {
        width: 100%;
        height: 200px;
        object-fit: cover;
        object-position: top center;
        border-radius: 12px;
        margin-bottom: 0.85rem;
        border: 1px solid #e2e8f0;
    }
    .pill-tag {
        display: inline-block;
        font-size: 0.75rem;
        font-weight: 700;
        padding: 0.2rem 0.65rem;
        border-radius: 999px;
        background: #e0e7ff;
        color: #1e1b4b;
        margin-bottom: 0.5rem;
    }
    .pill-tag-green {
        background: #d1fae5;
        color: #065f46;
    }
    a.cta-link {
        display: inline-block;
        margin-top: 0.65rem;
        padding: 0.52rem 0.95rem;
        border-radius: 10px;
        background: #0f172a;
        color: #ffffff;
        text-decoration: none;
        font-weight: 700;
        font-size: 0.86rem;
    }
    a.cta-link:hover {
        background: #1e293b;
        color: #ffffff;
    }
    a.cta-whatsapp {
        background: #059669;
        color: #ffffff;
    }
    a.cta-whatsapp:hover {
        background: #047857;
        color: #ffffff;
    }
    a.cta-social {
        background: #1e1b4b;
        color: #ffffff;
    }
    a.cta-social:hover {
        background: #312e81;
        color: #ffffff;
    }
    .stTextInput label, .stTextArea label, .stSelectbox label, .stFileUploader label {
        color: #0f172a;
        font-weight: 700;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

VIDEOS_DATA = [
    {
        "title": "Campus Fellowship Keynote & Stage Session",
        "category": "Interviews & Talks",
        "source_file": "Shared Drive Clip • Campus Fellowship",
        "thumb_uri": SPEAKER_STILL_URI,
        "summary": (
            "Stage speaking coverage featuring a presenter with microphone and podium beside a "
            "Campus Fellowship backdrop in a patterned vest and dark trousers."
        ),
        "drive_url": DRIVE_SPEAKER_URL,
    },
    {
        "title": "Personal Growth & Individual Development Talk",
        "category": "Interviews & Talks",
        "source_file": "Shared Drive Clip • Daramola Dynasty Foundation",
        "thumb_uri": INTERVIEW_STILL_URI,
        "summary": (
            "Mic'd speaker segment with Daramola Dynasty Foundation branding and clean bold captions "
            "focused on growing as individuals."
        ),
        "drive_url": DRIVE_INTERVIEW_URL,
    },
    {
        "title": "Outdoor Celebration & Traditional Attire Highlight",
        "category": "Events & Celebrations",
        "source_file": "Shared Drive Clip • Outdoor Event",
        "thumb_uri": CELEBRATION_STILL_URI,
        "summary": (
            "Outdoor celebration coverage featuring guests in peach gele headwraps, embroidered attire, "
            "and a feathered hand fan captured in lively movement."
        ),
        "drive_url": DRIVE_CELEBRATION_URL,
    },
    {
        "title": "Two Schools Outreach & Big Dreams (Nov 11)",
        "category": "Outreach & Documentary",
        "source_file": "copy_B1263277-D979-4468-9831-29F203211443.mov",
        "thumb_uri": SCHOOL_STILL_URI,
        "summary": (
            "Captures students in green-checked uniforms inside the classroom with Daramola Dynasty branding, "
            "captioned subtitles, and educational outreach across two schools in Ishara, Ogun State."
        ),
        "drive_url": DRIVE_SCHOOL_URL,
    },
    {
        "title": "POV: Blaming Everyone Except Himself (B&W Reel)",
        "category": "Comedy & POV Reels",
        "source_file": "Shared Drive Clip • Dynasty Football Academy",
        "thumb_uri": POV_STILL_URI,
        "summary": (
            "Black-and-white POV comedy sketch filmed along a tree-lined avenue with "
            "bold centered captioning and the Dynasty Football Academy mark."
        ),
        "drive_url": DRIVE_POV_URL,
    },
    {
        "title": "Dynasty Football Academy — Pitch Action Clip",
        "category": "Sports & Reels",
        "source_file": "Shared Drive Clip • Dynasty Football Academy",
        "thumb_uri": ACADEMY_STILL_URI,
        "summary": (
            "Outdoor turf training and match action featuring players in jersey numbers 04, 14, and 5 "
            "with a throw-in along the enclosed pitch under the Dynasty Football Academy mark."
        ),
        "drive_url": DRIVE_FOOTBALL_URL,
    },
]

top_left, top_right = st.columns([2.4, 1.2], vertical_alignment="center")
with top_left:
    st.markdown("### 🎬 **Upside ng** — Video Editing & Visual Storytelling")
with top_right:
    st.markdown(
        f'<div style="text-align:right;">'
        f'<a class="cta-link cta-whatsapp" href="https://wa.me/{WHATSAPP_INTL}?text=Hello%20Upside%20ng%2C%20I%20would%20like%20to%20work%20with%20you%20on%20a%20video%20edit." target="_blank">'
        f'💬 WhatsApp: {WHATSAPP_NUMBER}</a></div>',
        unsafe_allow_html=True,
    )

hero_col, portrait_col = st.columns([1.85, 1.15], gap="large", vertical_alignment="center")

with hero_col:
    st.markdown(
        f"""
        <div class="upside-hero">
            <span class="upside-badge">● UPSIDE NG • LED BY CEO MICHAEL BLESSING</span>
            <h1>Clean Pacing, Clear Voice &amp; Visuals That Connect</h1>
            <p>
                <strong>Upside ng</strong> edits stage talks and interviews, event celebrations, school outreach documentaries,
                comedy POV reels, and football/sports clips with smooth transitions, motion effects, colour adjustments,
                sound design, captions, and engaging storytelling.
            </p>
            <div class="hero-contact-bar">
                📞 <strong>{WHATSAPP_NUMBER}</strong> &nbsp;•&nbsp; ✉️ <strong>{EMAIL_ADDRESS}</strong>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with portrait_col:
    st.markdown(
        f"""
        <div class="surface-card" style="text-align:center;">
            <div class="portrait-frame">
                <img src="{st.session_state.portrait_data_uri}" alt="Michael Blessing — CEO, Upside ng" />
            </div>
            <div style="margin-top:0.85rem; font-weight:800; font-size:1.05rem; color:#0f172a;">
                Michael Blessing — CEO, Upside ng
            </div>
            <div style="font-size:0.85rem; color:#475569; margin-top:0.15rem;">
                {WHATSAPP_NUMBER} • {EMAIL_ADDRESS}
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    uploaded_portrait = st.file_uploader(
        "Replace or Upload CEO Portrait Photo",
        type=["png", "jpg", "jpeg", "webp"],
        key="portrait_uploader",
    )
    if uploaded_portrait is not None:
        encoded = base64.b64encode(uploaded_portrait.getvalue()).decode("utf-8")
        mime = uploaded_portrait.type or "image/jpeg"
        st.session_state.portrait_data_uri = f"data:{mime};base64,{encoded}"
        st.rerun()

st.divider()

about_col, contact_col = st.columns([1.65, 1.15], gap="large")

with about_col:
    st.markdown(
        f"""
        <div class="surface-card">
            <span class="pill-tag">ABOUT ME – MICHAEL BLESSING (CEO)</span>
            <h2 style="margin:0.25rem 0 0.75rem 0; font-size:1.55rem; font-weight:800; color:#0f172a;">
                About Me – Michael Blessing
            </h2>
            <p style="line-height:1.68; color:#334155;">
                My name is <strong>Michael Blessing</strong>, and I am a passionate video editor with a strong interest in
                creating engaging, creative, and visually appealing video content. My journey into video editing is driven
                by my passion for storytelling, creativity, and the ability to transform ordinary footage into compelling
                visual experiences.
            </p>
            <p style="line-height:1.68; color:#334155; margin-top:0.6rem;">
                I focus on developing my skills in video editing, including smooth transitions, motion effects, colour
                adjustments, sound design, captions, and engaging storytelling. I also have an interest in creating
                short-form content for platforms such as TikTok, Instagram Reels, and YouTube Shorts, particularly in
                the football niche.
            </p>
            <p style="line-height:1.68; color:#334155; margin-top:0.6rem;">
                My goal is to continuously improve my creativity, deliver quality editing services, and bring ideas to life
                through professional and captivating videos.
            </p>
            <div style="display:flex; flex-wrap:wrap; gap:0.55rem; margin-top:0.9rem;">
                <a class="cta-link cta-social" href="{IG_URL}" target="_blank">Instagram ↗</a>
                <a class="cta-link cta-social" href="{TT_URL}" target="_blank">TikTok ↗</a>
                <a class="cta-link cta-social" href="{LI_URL}" target="_blank">LinkedIn ↗</a>
                <a class="cta-link cta-social" href="{FB_URL}" target="_blank">Facebook ↗</a>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with contact_col:
    st.markdown(
        f"""
        <div class="surface-card">
            <span class="pill-tag pill-tag-green">DIRECT BOOKING &amp; SOCIAL CHANNELS</span>
            <h3 style="margin:0.25rem 0 0.75rem 0; font-size:1.3rem; font-weight:800; color:#0f172a;">
                Work With Michael Blessing &amp; Upside ng
            </h3>
            <p style="margin:0.35rem 0; color:#1e293b;"><strong>CEO:</strong> Michael Blessing</p>
            <p style="margin:0.35rem 0; color:#1e293b;"><strong>WhatsApp / Phone:</strong> {WHATSAPP_NUMBER}</p>
            <p style="margin:0.35rem 0; color:#1e293b;"><strong>Email:</strong> {EMAIL_ADDRESS}</p>
            <p style="margin:0.45rem 0 0.25rem 0; color:#1e293b;"><strong>Social Links:</strong></p>
            <div style="font-size:0.88rem; line-height:1.75; color:#334155;">
                • <a href="{IG_URL}" target="_blank">Instagram (@godsongeorge19)</a><br/>
                • <a href="{TT_URL}" target="_blank">TikTok (@godsongeorge91)</a><br/>
                • <a href="{LI_URL}" target="_blank">LinkedIn (Michael Blessing)</a><br/>
                • <a href="{FB_URL}" target="_blank">Facebook Profile</a>
            </div>
            <div style="display:flex; flex-wrap:wrap; gap:0.6rem; margin-top:0.85rem;">
                <a class="cta-link cta-whatsapp" href="https://wa.me/{WHATSAPP_INTL}" target="_blank">Chat on WhatsApp</a>
                <a class="cta-link" href="mailto:{EMAIL_ADDRESS}">Send Email</a>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.divider()

st.markdown("## 🎞️ Edited Videos &amp; Project Stills")
st.markdown(
    f"Featured clips and stills from your links. [Stage Keynote Clip ↗]({DRIVE_SPEAKER_URL}) &nbsp;|&nbsp; "
    f"[Personal Growth Talk ↗]({DRIVE_INTERVIEW_URL}) &nbsp;|&nbsp; [Event Highlight Clip ↗]({DRIVE_CELEBRATION_URL}) &nbsp;|&nbsp; "
    f"[Outreach Drive Folder ↗]({FOLDER_URL}) &nbsp;|&nbsp; [Classroom Clip ↗]({DRIVE_SCHOOL_URL}) &nbsp;|&nbsp; "
    f"[POV Reel Link ↗]({DRIVE_POV_URL}) &nbsp;|&nbsp; [Pitch Clip Link ↗]({DRIVE_FOOTBALL_URL})"
)

filter_col1, filter_col2 = st.columns([1.5, 2.5])
with filter_col1:
    chosen_cat = st.selectbox(
        "Filter by Category",
        ["All", "Interviews & Talks", "Events & Celebrations", "Outreach & Documentary", "Comedy & POV Reels", "Sports & Reels"],
    )

filtered_videos = [
    v for v in VIDEOS_DATA if chosen_cat == "All" or v["category"] == chosen_cat
]
vid_cols = st.columns(3, gap="medium")
for idx, vid in enumerate(filtered_videos):
    with vid_cols[idx % 3]:
        thumb_html = (
            f'<img class="card-thumb" src="{vid["thumb_uri"]}" alt="{vid["title"]}" />'
            if vid.get("thumb_uri")
            else ""
        )
        st.markdown(
            f"""
            <div class="surface-card">
                {thumb_html}
                <span class="pill-tag">{vid["category"]}</span>
                <h3 style="margin:0.2rem 0 0.45rem 0; font-size:1.15rem; font-weight:800; color:#0f172a;">
                    {vid["title"]}
                </h3>
                <div style="font-size:0.78rem; font-weight:600; color:#64748b; margin-bottom:0.65rem;">
                    Source: {vid["source_file"]}
                </div>
                <p style="font-size:0.93rem; line-height:1.58; color:#334155;">
                    {vid["summary"]}
                </p>
                <a class="cta-link" href="{vid["drive_url"]}" target="_blank">Preview on Google Drive ↗</a>
            </div>
            """,
            unsafe_allow_html=True,
        )

st.markdown("### 🖼️ Upload Additional Edited Pictures or Video Clips")
media_files = st.file_uploader(
    "Add your edited pictures (JPG/PNG/WEBP) or short video clips (MP4/MOV) to showcase on the page",
    type=["png", "jpg", "jpeg", "webp", "mp4", "mov"],
    accept_multiple_files=True,
    key="portfolio_media_uploader",
)

if media_files:
    st.session_state.custom_media = [
        {
            "name": f.name,
            "type": f.type or "",
            "bytes": f.getvalue(),
        }
        for f in media_files
    ]

if st.session_state.custom_media:
    st.markdown("#### Showcase Gallery")
    gallery_cols = st.columns(3, gap="medium")
    for idx, item in enumerate(st.session_state.custom_media):
        with gallery_cols[idx % 3]:
            with st.container(border=True):
                if item["type"].startswith("video/") or item["name"].lower().endswith((".mp4", ".mov")):
                    st.video(item["bytes"])
                else:
                    st.image(item["bytes"], use_container_width=True)
                st.caption(f"**{item['name']}** — Upside ng")

st.divider()
st.markdown(
    f"<div style='text-align:center; color:#475569; font-size:0.88rem;'>"
    f"<strong>Upside ng</strong> • CEO: Michael Blessing • WhatsApp/Phone: {WHATSAPP_NUMBER} • Email: {EMAIL_ADDRESS} • "
    f"<a href='{IG_URL}' target='_blank'>Instagram</a> • "
    f"<a href='{TT_URL}' target='_blank'>TikTok</a> • "
    f"<a href='{LI_URL}' target='_blank'>LinkedIn</a> • "
    f"<a href='{FB_URL}' target='_blank'>Facebook</a>"
    f"</div>",
    unsafe_allow_html=True,
)
