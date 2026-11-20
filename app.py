import base64
import os
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

DRIVE_FOOTBALL_VIEW = "https://drive.google.com/file/d/15sUL-HGn9iEedm3RdQOQ_iXRBR-8lnkY/view?usp=drivesdk"
DRIVE_POV_VIEW = "https://drive.google.com/file/d/1bGhZIyAfgjy2UTyHDIO75wd6Vrdg-BYe/view?usp=drivesdk"
DRIVE_SCHOOL_VIEW = "https://drive.google.com/file/d/1cDwvAh4g9Oldvb-rLKqmeEx3KLRqp_a_/view?usp=drivesdk"
DRIVE_CELEBRATION_VIEW = "https://drive.google.com/file/d/1tDOHYc8wWLObr3QyZSsFr50ulgj4271_/view?usp=drivesdk"
DRIVE_INTERVIEW_VIEW = "https://drive.google.com/file/d/1EB7wlfetH351w9bO9BBTuXWJkfT3RR6Z/view?usp=drivesdk"
DRIVE_SPEAKER_VIEW = "https://drive.google.com/file/d/1Bg1tssHRuPGo-xEiJiLr83dIQKGN8LSw/view?usp=drivesdk"

DRIVE_FOOTBALL_PREVIEW = "https://drive.google.com/file/d/15sUL-HGn9iEedm3RdQOQ_iXRBR-8lnkY/preview"
DRIVE_POV_PREVIEW = "https://drive.google.com/file/d/1bGhZIyAfgjy2UTyHDIO75wd6Vrdg-BYe/preview"
DRIVE_SCHOOL_PREVIEW = "https://drive.google.com/file/d/1cDwvAh4g9Oldvb-rLKqmeEx3KLRqp_a_/preview"
DRIVE_CELEBRATION_PREVIEW = "https://drive.google.com/file/d/1tDOHYc8wWLObr3QyZSsFr50ulgj4271_/preview"
DRIVE_INTERVIEW_PREVIEW = "https://drive.google.com/file/d/1EB7wlfetH351w9bO9BBTuXWJkfT3RR6Z/preview"
DRIVE_SPEAKER_PREVIEW = "https://drive.google.com/file/d/1Bg1tssHRuPGo-xEiJiLr83dIQKGN8LSw/preview"

IG_URL = "https://www.instagram.com/godsongeorge19?dlrf=MXNwbDRmejZsMG1veg=="
TT_URL = "https://www.tiktok.com/@godsongeorge91?_r=1&_t=ZS-9B925sTsYzd"
LI_URL = "https://www.linkedin.com/in/michael-blessing-27799923b?utm_source=share_via&utm_content=profile&utm_medium=member_android"
FB_URL = "https://www.facebook.com/share/1FNNe8m19D/"


def load_local_or_fallback(filename: str, fallback_uri: str) -> str:
    # Loads a local image from the repo (such as assets/ceo_portrait.jpg) if present
    local_candidates = [
        filename,
        os.path.join("assets", filename),
        os.path.join("images", filename),
    ]
    for path in local_candidates:
        if os.path.isfile(path):
            ext = os.path.splitext(path)[1].lower().lstrip(".")
            mime = "image/jpeg" if ext in ("jpg", "jpeg", "") else f"image/{ext}"
            with open(path, "rb") as f:
                b64 = base64.b64encode(f.read()).decode("utf-8")
            return f"data:{mime};base64,{b64}"
    return fallback_uri


DEFAULT_PORTRAIT_URI = load_local_or_fallback(
    "ceo_portrait.jpg",
    """data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSI2MDAiIGhlaWdodD0iNzUwIiB2aWV3Qm94PSIwIDAgNjAwIDc1MCI+CiAgPGRlZnM+CiAgICA8bGluZWFyR3JhZGllbnQgaWQ9ImJnIiB4MT0iMCIgeTE9IjAiIHgyPSIwIiB5Mj0iMSI+CiAgICAgIDxzdG9wIG9mZnNldD0iMCUiIHN0b3AtY29sb3I9IiMwZjE3MmEiLz4KICAgICAgPHN0b3Agb2Zmc2V0PSIxMDAlIiBzdG9wLWNvbG9yPSIjMzEyZTgxIi8+CiAgICA8L2xpbmVhckdyYWRpZW50PgogIDwvZGVmcz4KICA8cmVjdCB3aWR0aD0iNjAwIiBoZWlnaHQ9Ijc1MCIgZmlsbD0idXJsKCNiZykiLz4KICA8Y2lyY2xlIGN4PSIzMDAiIGN5PSIyNDUiIHI9Ijc4IiBmaWxsPSIjZTJlOGYwIi8+CiAgPHBhdGggZD0iTTE2NSA1NjAgQzE2NSA0MjUgMjI1IDM2NSAzMDAgMzY1IEMzNzUgMzY1IDQzNSA0MjUgNDM1IDU2MCBaIiBmaWxsPSIjZjhmYWZjIi8+CiAgPHJlY3QgeD0iMjc4IiB5PSIzNjUiIHdpZHRoPSI0NCIgaGVpZ2h0PSIxOTUiIGZpbGw9IiMwZjE3MmEiLz4KICA8cG9seWdvbiBwb2ludHM9IjMwMCwzODIgMjg2LDQxNSAzMDAsNTQ1IDMxNCw0MTUiIGZpbGw9IiMzNGQzOTkiLz4KICA8cmVjdCB4PSI5NSIgeT0iNjg4IiB3aWR0aD0iNDEwIiBoZWlnaHQ9IjQyIiByeD0iMTIiIGZpbGw9IiMwOTBkMTYiIHN0cm9rZT0iIzM4YmRmOCIgc3Ryb2tlLXdpZHRoPSIxLjUiLz4KICA8dGV4dCB4PSIzMDAiIHk9IjcxNCIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZmlsbD0iI2ZmZmZmZiIgZm9udC1mYW1pbHk9InNhbnMtc2VyaWYiIGZvbnQtc2l6ZT0iMTUiIGZvbnQtd2VpZ2h0PSJib2xkIj5NaWNoYWVsIEJsZXNzaW5nIOKAoiBDRU8sIFVwc2lkZSBuZzwvdGV4dD4KPC9zdmc+""",
)

if "portrait_uri" not in st.session_state:
    st.session_state.portrait_uri = DEFAULT_PORTRAIT_URI

if "uploaded_gallery" not in st.session_state:
    st.session_state.uploaded_gallery = []

# High-contrast styling: white/light-indigo text inside .upside-hero, dark text on light cards
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(180deg, #f8fafc 0%, #eef2ff 100%);
        color: #0f172a;
    }
    .upside-hero {
        background: linear-gradient(135deg, #0f172a 0%, #1e1b4b 55%, #312e81 100%);
        padding: 2rem 2.25rem;
        border-radius: 18px;
        margin-bottom: 1.5rem;
        box-shadow: 0 12px 28px -6px rgba(15, 23, 42, 0.25);
    }
    .upside-hero .upside-badge {
        display: inline-block;
        background: rgba(16, 185, 129, 0.24);
        border: 1px solid rgba(52, 211, 153, 0.65);
        color: #6ee7b7;
        font-size: 0.78rem;
        font-weight: 700;
        padding: 0.25rem 0.75rem;
        border-radius: 999px;
    }
    .upside-hero h1 {
        margin: 0.45rem 0 0.7rem 0;
        font-size: 2.2rem;
        font-weight: 800;
        letter-spacing: -0.02em;
        color: #ffffff;
    }
    .upside-hero p.hero-body {
        margin: 0;
        color: #ffffff;
        font-size: 1.04rem;
        line-height: 1.65;
        font-weight: 400;
    }
    .upside-hero p.hero-body strong {
        color: #ffffff;
        font-weight: 700;
    }
    .upside-hero .hero-contact-bar {
        margin-top: 1.15rem;
        font-size: 0.95rem;
        color: #f8fafc;
    }
    .upside-hero .hero-contact-bar strong {
        color: #ffffff;
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
        box-shadow: 0 14px 28px rgba(15, 23, 42, 0.25);
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
        height: 190px;
        object-fit: cover;
        object-position: center;
        border-radius: 12px;
        margin-bottom: 0.75rem;
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
        margin-top: 0.6rem;
        padding: 0.5rem 0.9rem;
        border-radius: 10px;
        background: #0f172a;
        color: #ffffff;
        text-decoration: none;
        font-weight: 700;
        font-size: 0.85rem;
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
    </style>
    """,
    unsafe_allow_html=True,
)

VIDEOS_DATA = [
    {
        "title": "Campus Fellowship Keynote & Stage Session",
        "category": "Interviews & Talks",
        "source_file": "Shared Drive Clip • Campus Fellowship",
        "thumb_uri": load_local_or_fallback("speaker_still.jpg", """data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSI4MDAiIGhlaWdodD0iNDUwIiB2aWV3Qm94PSIwIDAgODAwIDQ1MCI+CiAgPHJlY3Qgd2lkdGg9IjgwMCIgaGVpZ2h0PSI0NTAiIGZpbGw9IiMwZjE3MmEiLz4KICA8cmVjdCB4PSI2MCIgeT0iNTAiIHdpZHRoPSI2ODAiIGhlaWdodD0iMzUwIiByeD0iMTYiIGZpbGw9IiMxZTI5M2IiLz4KICA8dGV4dCB4PSI0MDAiIHk9IjE4NSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZmlsbD0iI2ZmZmZmZiIgZm9udC1mYW1pbHk9InNhbnMtc2VyaWYiIGZvbnQtc2l6ZT0iNTQiIGZvbnQtd2VpZ2h0PSJib2xkIiBvcGFjaXR5PSIwLjIyIj5DQU1QVVMgRkVMTE9XU0hJUDwvdGV4dD4KICA8cmVjdCB4PSIxNTAiIHk9IjMyNSIgd2lkdGg9IjUwMCIgaGVpZ2h0PSI0NiIgcng9IjEyIiBmaWxsPSIjMDkwZDE2Ii8+CiAgPHRleHQgeD0iNDAwIiB5PSIzNTQiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZpbGw9IiMzNGQzOTkiIGZvbnQtZmFtaWx5PSJzYW5zLXNlcmlmIiBmb250LXNpemU9IjE1IiBmb250LXdlaWdodD0iYm9sZCI+Q2FtcHVzIEZlbGxvd3NoaXAgU3RhZ2UgU2Vzc2lvbiDigKIgTWljICZhbXA7IFBvZGl1bTwvdGV4dD4KPC9zdmc+"""),
        "summary": (
            "Stage speaking coverage featuring a presenter with microphone and podium beside a "
            "Campus Fellowship backdrop in a patterned vest and dark trousers."
        ),
        "preview_url": DRIVE_SPEAKER_PREVIEW,
        "drive_url": DRIVE_SPEAKER_VIEW,
    },
    {
        "title": "Personal Growth & Individual Development Talk",
        "category": "Interviews & Talks",
        "source_file": "Shared Drive Clip • Daramola Dynasty Foundation",
        "thumb_uri": load_local_or_fallback("interview_still.jpg", """data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSI4MDAiIGhlaWdodD0iNDUwIiB2aWV3Qm94PSIwIDAgODAwIDQ1MCI+CiAgPHJlY3Qgd2lkdGg9IjgwMCIgaGVpZ2h0PSI0NTAiIGZpbGw9IiMwZjE3MmEiLz4KICA8cmVjdCB4PSI2MCIgeT0iNTAiIHdpZHRoPSI2ODAiIGhlaWdodD0iMzUwIiByeD0iMTYiIGZpbGw9IiMxZTFiNGIiLz4KICA8Y2lyY2xlIGN4PSI2NDUiIGN5PSIxMTIiIHI9IjM4IiBmaWxsPSIjMDkwZDE2IiBzdHJva2U9IiMzOGJkZjgiIHN0cm9rZS13aWR0aD0iMi41Ii8+CiAgPHRleHQgeD0iNjQ1IiB5PSIxMDkiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZpbGw9IiNmZmZmZmYiIGZvbnQtZmFtaWx5PSJzYW5zLXNlcmlmIiBmb250LXNpemU9IjkiIGZvbnQtd2VpZ2h0PSJib2xkIj5EQVJBTU9MQTwvdGV4dD4KICA8dGV4dCB4PSI2NDUiIHk9IjEyMiIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZmlsbD0iIzM0ZDM5OSIgZm9udC1mYW1pbHk9InNhbnMtc2VyaWYiIGZvbnQtc2l6ZT0iOSIgZm9udC13ZWlnaHQ9ImJvbGQiPkRZTkFTVFk8L3RleHQ+CiAgPHJlY3QgeD0iMTY1IiB5PSIyOTUiIHdpZHRoPSI0NzAiIGhlaWdodD0iNjYiIHJ4PSIxMiIgZmlsbD0iIzA5MGQxNiIvPgogIDx0ZXh0IHg9IjQwMCIgeT0iMzIzIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmaWxsPSIjZmZmZmZmIiBmb250LWZhbWlseT0ic2Fucy1zZXJpZiIgZm9udC1zaXplPSIxNiIgZm9udC13ZWlnaHQ9ImJvbGQiPnRoZXNlIGFyZSB0aGUgdGhpbmdzIHRoYXQ8L3RleHQ+CiAgPHRleHQgeD0iNDAwIiB5PSIzNDgiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZpbGw9IiMzNGQzOTkiIGZvbnQtZmFtaWx5PSJzYW5zLXNlcmlmIiBmb250LXNpemU9IjE2IiBmb250LXdlaWdodD0iYm9sZCI+bWFrZXMgdXMgZ3JvdyBhcyBpbmRpdmlkdWFsczwvdGV4dD4KPC9zdmc+"""),
        "summary": (
            "Mic'd speaker segment with Daramola Dynasty Foundation branding and clean bold captions "
            "focused on growing as individuals."
        ),
        "preview_url": DRIVE_INTERVIEW_PREVIEW,
        "drive_url": DRIVE_INTERVIEW_VIEW,
    },
    {
        "title": "Outdoor Celebration & Traditional Attire Highlight",
        "category": "Events & Celebrations",
        "source_file": "Shared Drive Clip • Outdoor Event",
        "thumb_uri": load_local_or_fallback("celebration_still.jpg", """data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSI4MDAiIGhlaWdodD0iNDUwIiB2aWV3Qm94PSIwIDAgODAwIDQ1MCI+CiAgPHJlY3Qgd2lkdGg9IjgwMCIgaGVpZ2h0PSI0NTAiIGZpbGw9IiMwZjE3MmEiLz4KICA8cmVjdCB4PSI2MCIgeT0iNTAiIHdpZHRoPSI2ODAiIGhlaWdodD0iMzUwIiByeD0iMTYiIGZpbGw9IiMzMTJlODEiLz4KICA8cGF0aCBkPSJNMjk1IDE2NSBRMzY1IDExMCA0MzUgMTY1IFE0MTUgMjE1IDM2NSAyMTUgUTMxNSAyMTUgMjk1IDE2NSBaIiBmaWxsPSIjZmJjZmU4Ii8+CiAgPHBhdGggZD0iTTI4NSAzNzUgTDMxMCAyNzUgTDQyMCAyNzUgTDQ0NSAzNzUgWiIgZmlsbD0iI2ZjZTdmMyIvPgogIDxyZWN0IHg9IjE3NSIgeT0iMzM1IiB3aWR0aD0iNDUwIiBoZWlnaHQ9IjQyIiByeD0iMTIiIGZpbGw9IiMwOTBkMTYiLz4KICA8dGV4dCB4PSI0MDAiIHk9IjM2MiIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZmlsbD0iI2ZiY2ZlOCIgZm9udC1mYW1pbHk9InNhbnMtc2VyaWYiIGZvbnQtc2l6ZT0iMTUiIGZvbnQtd2VpZ2h0PSJib2xkIj5DZWxlYnJhdGlvbiAmYW1wOyBFdmVudCBIaWdobGlnaHQg4oCiIFBlYWNoIEdlbGUgJmFtcDsgRmFuPC90ZXh0Pgo8L3N2Zz4="""),
        "summary": (
            "Outdoor celebration coverage featuring guests in peach gele headwraps, embroidered attire, "
            "and a feathered hand fan captured in lively movement."
        ),
        "preview_url": DRIVE_CELEBRATION_PREVIEW,
        "drive_url": DRIVE_CELEBRATION_VIEW,
    },
    {
        "title": "Two Schools Outreach & Big Dreams (Nov 11)",
        "category": "Outreach & Documentary",
        "source_file": "copy_B1263277-D979-4468-9831-29F203211443.mov",
        "thumb_uri": load_local_or_fallback("school_still.jpg", """data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSI4MDAiIGhlaWdodD0iNDUwIiB2aWV3Qm94PSIwIDAgODAwIDQ1MCI+CiAgPHJlY3Qgd2lkdGg9IjgwMCIgaGVpZ2h0PSI0NTAiIGZpbGw9IiMwZjE3MmEiLz4KICA8cmVjdCB4PSI2MCIgeT0iNTAiIHdpZHRoPSI2ODAiIGhlaWdodD0iMzUwIiByeD0iMTYiIGZpbGw9IiMxMzRlNGEiLz4KICA8Y2lyY2xlIGN4PSI2NDUiIGN5PSIxMTIiIHI9IjM4IiBmaWxsPSIjMDkwZDE2IiBzdHJva2U9IiMzOGJkZjgiIHN0cm9rZS13aWR0aD0iMi41Ii8+CiAgPHRleHQgeD0iNjQ1IiB5PSIxMDkiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZpbGw9IiNmZmZmZmYiIGZvbnQtZmFtaWx5PSJzYW5zLXNlcmlmIiBmb250LXNpemU9IjkiIGZvbnQtd2VpZ2h0PSJib2xkIj5EQVJBTU9MQTwvdGV4dD4KICA8dGV4dCB4PSI2NDUiIHk9IjEyMiIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZmlsbD0iIzM0ZDM5OSIgZm9udC1mYW1pbHk9InNhbnMtc2VyaWYiIGZvbnQtc2l6ZT0iOSIgZm9udC13ZWlnaHQ9ImJvbGQiPkRZTkFTVFk8L3RleHQ+CiAgPHJlY3QgeD0iMTU1IiB5PSIyODUiIHdpZHRoPSI0OTAiIGhlaWdodD0iNDYiIHJ4PSIxMiIgZmlsbD0iIzA5MGQxNiIvPgogIDx0ZXh0IHg9IjQwMCIgeT0iMzE0IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmaWxsPSIjMzRkMzk5IiBmb250LWZhbWlseT0ic2Fucy1zZXJpZiIgZm9udC1zaXplPSIxNSIgZm9udC13ZWlnaHQ9ImJvbGQiPkRhcmFtb2xhIER5bmFzdHkg4oCiIFR3byBTY2hvb2xzIE91dHJlYWNoIChJc2hhcmEpPC90ZXh0Pgo8L3N2Zz4="""),
        "summary": (
            "Captures students in green-checked uniforms inside the classroom with Daramola Dynasty branding, "
            "captioned subtitles, and educational outreach across two schools in Ishara, Ogun State."
        ),
        "preview_url": DRIVE_SCHOOL_PREVIEW,
        "drive_url": DRIVE_SCHOOL_VIEW,
    },
    {
        "title": "POV: Blaming Everyone Except Himself (B&W Reel)",
        "category": "Comedy & POV Reels",
        "source_file": "Shared Drive Clip • Dynasty Football Academy",
        "thumb_uri": load_local_or_fallback("pov_still.jpg", """data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSI4MDAiIGhlaWdodD0iNDUwIiB2aWV3Qm94PSIwIDAgODAwIDQ1MCI+CiAgPHJlY3Qgd2lkdGg9IjgwMCIgaGVpZ2h0PSI0NTAiIGZpbGw9IiMwZjE3MmEiLz4KICA8cmVjdCB4PSI2MCIgeT0iNTAiIHdpZHRoPSI2ODAiIGhlaWdodD0iMzUwIiByeD0iMTYiIGZpbGw9IiMxZTI5M2IiLz4KICA8Y2lyY2xlIGN4PSI2NDUiIGN5PSIxMDgiIHI9IjM2IiBmaWxsPSIjMDkwZDE2IiBzdHJva2U9IiMzOGJkZjgiIHN0cm9rZS13aWR0aD0iMi41Ii8+CiAgPHRleHQgeD0iNjQ1IiB5PSIxMDUiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZpbGw9IiNmZmZmZmYiIGZvbnQtZmFtaWx5PSJzYW5zLXNlcmlmIiBmb250LXNpemU9IjEwIiBmb250LXdlaWdodD0iYm9sZCI+RFlOQVNUWTwvdGV4dD4KICA8dGV4dCB4PSI2NDUiIHk9IjExOCIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZmlsbD0iIzM0ZDM5OSIgZm9udC1mYW1pbHk9InNhbnMtc2VyaWYiIGZvbnQtc2l6ZT0iOSIgZm9udC13ZWlnaHQ9ImJvbGQiPkFDQURFTVk8L3RleHQ+CiAgPHJlY3QgeD0iMTc1IiB5PSIzMTAiIHdpZHRoPSI0NTAiIGhlaWdodD0iNjIiIHJ4PSIxMiIgZmlsbD0iIzA5MGQxNiIvPgogIDx0ZXh0IHg9IjQwMCIgeT0iMzM2IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmaWxsPSIjZmZmZmZmIiBmb250LWZhbWlseT0ic2Fucy1zZXJpZiIgZm9udC1zaXplPSIxNSIgZm9udC13ZWlnaHQ9ImJvbGQiPlBPVjogdGhhdCBvbmUgYnJvIHRoYXQgYmxhbWU8L3RleHQ+CiAgPHRleHQgeD0iNDAwIiB5PSIzNTkiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZpbGw9IiMzNGQzOTkiIGZvbnQtZmFtaWx5PSJzYW5zLXNlcmlmIiBmb250LXNpemU9IjE1IiBmb250LXdlaWdodD0iYm9sZCI+ZXZlcnlvbmUgZXhjZXB0IGhpbXNlbGY8L3RleHQ+Cjwvc3ZnPg=="""),
        "summary": (
            "Black-and-white POV comedy sketch filmed along a tree-lined avenue with "
            "bold centered captioning and the Dynasty Football Academy mark."
        ),
        "preview_url": DRIVE_POV_PREVIEW,
        "drive_url": DRIVE_POV_VIEW,
    },
    {
        "title": "Dynasty Football Academy — Pitch Action Clip",
        "category": "Sports & Reels",
        "source_file": "Shared Drive Clip • Dynasty Football Academy",
        "thumb_uri": load_local_or_fallback("academy_still.jpg", """data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSI4MDAiIGhlaWdodD0iNDUwIiB2aWV3Qm94PSIwIDAgODAwIDQ1MCI+CiAgPHJlY3Qgd2lkdGg9IjgwMCIgaGVpZ2h0PSIyMjUiIGZpbGw9IiMxZTI5M2IiLz4KICA8cmVjdCB5PSIyMjUiIHdpZHRoPSI4MDAiIGhlaWdodD0iMjI1IiBmaWxsPSIjMTQ1MzJkIi8+CiAgPGNpcmNsZSBjeD0iNjQwIiBjeT0iMTA1IiByPSI0MCIgZmlsbD0iIzA5MGQxNiIgc3Ryb2tlPSIjMzhiZGY4IiBzdHJva2Utd2lkdGg9IjMiLz4KICA8dGV4dCB4PSI2NDAiIHk9IjEwMSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZmlsbD0iI2ZmZmZmZiIgZm9udC1mYW1pbHk9InNhbnMtc2VyaWYiIGZvbnQtc2l6ZT0iMTAuNSIgZm9udC13ZWlnaHQ9ImJvbGQiPkRZTkFTVFk8L3RleHQ+CiAgPHRleHQgeD0iNjQwIiB5PSIxMTUiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZpbGw9IiMzNGQzOTkiIGZvbnQtZmFtaWx5PSJzYW5zLXNlcmlmIiBmb250LXNpemU9IjkiIGZvbnQtd2VpZ2h0PSJib2xkIj5GT09UQkFMTCBBQ0FERU1ZPC90ZXh0PgogIDxyZWN0IHg9IjE1NSIgeT0iMzY1IiB3aWR0aD0iNDkwIiBoZWlnaHQ9IjQyIiByeD0iMTIiIGZpbGw9IiMwOTBkMTYiLz4KICA8dGV4dCB4PSI0MDAiIHk9IjM5MSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZmlsbD0iI2ZmZmZmZiIgZm9udC1mYW1pbHk9InNhbnMtc2VyaWYiIGZvbnQtc2l6ZT0iMTUiIGZvbnQtd2VpZ2h0PSJib2xkIj5EeW5hc3R5IEZvb3RiYWxsIEFjYWRlbXkg4oCiIFBpdGNoIEFjdGlvbiBGcmFtZTwvdGV4dD4KPC9zdmc+"""),
        "summary": (
            "Outdoor turf training and match action featuring players in jersey numbers 04, 14, and 5 "
            "with a throw-in along the enclosed pitch under the Dynasty Football Academy mark."
        ),
        "preview_url": DRIVE_FOOTBALL_PREVIEW,
        "drive_url": DRIVE_FOOTBALL_VIEW,
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
            <p class="hero-body">
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
                <img src="{st.session_state.portrait_uri}" alt="Michael Blessing — CEO, Upside ng" />
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
        "Optional: Swap CEO Portrait Photo in This Session",
        type=["png", "jpg", "jpeg", "webp"],
        key="portrait_uploader",
    )
    if uploaded_portrait is not None:
        encoded = base64.b64encode(uploaded_portrait.getvalue()).decode("utf-8")
        mime = uploaded_portrait.type or "image/jpeg"
        st.session_state.portrait_uri = f"data:{mime};base64,{encoded}"
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
    f"Toggle embedded Google Drive video players or open any file directly. [Outreach Drive Folder ↗]({FOLDER_URL})"
)

filter_col1, filter_col2, filter_col3 = st.columns([1.4, 1.3, 1.8])
with filter_col1:
    chosen_cat = st.selectbox(
        "Filter by Category",
        ["All", "Interviews & Talks", "Events & Celebrations", "Outreach & Documentary", "Comedy & POV Reels", "Sports & Reels"],
    )
with filter_col2:
    embed_players = st.toggle("Embed Drive Video Players", value=True)

filtered_videos = [
    v for v in VIDEOS_DATA if chosen_cat == "All" or v["category"] == chosen_cat
]
vid_cols = st.columns(3, gap="medium")
for idx, vid in enumerate(filtered_videos):
    with vid_cols[idx % 3]:
        with st.container(border=True):
            if embed_players:
                st.components.v1.iframe(vid["preview_url"], height=215)
            else:
                st.markdown(
                    f'<img class="card-thumb" src="{vid["thumb_uri"]}" alt="{vid["title"]}" />',
                    unsafe_allow_html=True,
                )
            st.markdown(f'<span class="pill-tag">{vid["category"]}</span>', unsafe_allow_html=True)
            st.markdown(f"#### {vid['title']}")
            st.caption(f"Source: {vid['source_file']}")
            st.write(vid["summary"])
            st.markdown(
                f'<a class="cta-link" href="{vid["drive_url"]}" target="_blank">Open on Google Drive ↗</a>',
                unsafe_allow_html=True,
            )

st.markdown("### 🖼️ Optional Extra Gallery Uploads")
media_files = st.file_uploader(
    "Upload extra pictures or MP4/MOV clips for this session",
    type=["png", "jpg", "jpeg", "webp", "mp4", "mov"],
    accept_multiple_files=True,
    key="portfolio_media_uploader",
)

if media_files:
    st.session_state.uploaded_gallery = [
        {
            "name": f.name,
            "type": f.type or "",
            "bytes": f.getvalue(),
        }
        for f in media_files
    ]

if st.session_state.uploaded_gallery:
    st.markdown("#### Session Gallery")
    gallery_cols = st.columns(3, gap="medium")
    for idx, item in enumerate(st.session_state.uploaded_gallery):
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
