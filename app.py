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

CEO_PORTRAIT_URI = "data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSI2MDAiIGhlaWdodD0iNzUwIiB2aWV3Qm94PSIwIDAgNjAwIDc1MCI+CiAgPGRlZnM+CiAgICA8bGluZWFyR3JhZGllbnQgaWQ9ImJ3YmciIHgxPSIwIiB5MT0iMCIgeDI9IjAiIHkyPSIxIj4KICAgICAgPHN0b3Agb2Zmc2V0PSIwJSIgc3RvcC1jb2xvcj0iI2UyZThmMCIvPgogICAgICA8c3RvcCBvZmZzZXQ9IjU1JSIgc3RvcC1jb2xvcj0iIzk0YTNiOCIvPgogICAgICA8c3RvcCBvZmZzZXQ9IjEwMCUiIHN0b3AtY29sb3I9IiMzMzQxNTUiLz4KICAgIDwvbGluZWFyR3JhZGllbnQ+CiAgPC9kZWZzPgogIDxyZWN0IHdpZHRoPSI2MDAiIGhlaWdodD0iNzUwIiBmaWxsPSJ1cmwoI2J3YmcpIi8+CiAgPHBvbHlnb24gcG9pbnRzPSIyNDUsMjUwIDM1NSwyNTAgNDc1LDc1MCAxMjUsNzUwIiBmaWxsPSIjNDc1NTY5Ii8+CiAgPGNpcmNsZSBjeD0iMzAwIiBjeT0iMTg1IiByPSI1NCIgZmlsbD0iIzFlMjkzYiIvPgogIDxyZWN0IHg9IjI2NiIgeT0iMTcwIiB3aWR0aD0iNjgiIGhlaWdodD0iMjIiIHJ4PSI2IiBmaWxsPSIjMGYxNzJhIi8+CiAgPHBvbHlnb24gcG9pbnRzPSIyNTIsMjUwIDM0OCwyNTAgMzc1LDU0NSAyMjUsNTQ1IiBmaWxsPSIjMTExODI3Ii8+CiAgPHBvbHlnb24gcG9pbnRzPSIyODIsMjUwIDMxOCwyNTAgMzAwLDMyMCIgZmlsbD0iI2Y4ZmFmYyIvPgogIDxwb2x5Z29uIHBvaW50cz0iMjk1LDI3NSAzMDUsMjc1IDMwOSwzODUgMzAwLDM5OCAyOTEsMzg1IiBmaWxsPSIjMWYyOTM3Ii8+CiAgPHJlY3QgeD0iMjY1IiB5PSI1NDUiIHdpZHRoPSIzMCIgaGVpZ2h0PSIxNDUiIGZpbGw9IiMxZjI5MzciLz4KICA8cmVjdCB4PSIzMDUiIHk9IjU0NSIgd2lkdGg9IjMwIiBoZWlnaHQ9IjE0NSIgZmlsbD0iIzFmMjkzNyIvPgogIDxyZWN0IHg9IjI2MCIgeT0iNjg1IiB3aWR0aD0iMzgiIGhlaWdodD0iMTgiIHJ4PSI2IiBmaWxsPSIjMGYxNzJhIi8+CiAgPHJlY3QgeD0iMzAyIiB5PSI2ODUiIHdpZHRoPSIzOCIgaGVpZ2h0PSIxOCIgcng9IjYiIGZpbGw9IiMwZjE3MmEiLz4KICA8cmVjdCB4PSIxMDUiIHk9IjcwNCIgd2lkdGg9IjM5MCIgaGVpZ2h0PSIzNCIgcng9IjEwIiBmaWxsPSIjMGYxNzJhIiBvcGFjaXR5PSIwLjkiLz4KICA8dGV4dCB4PSIzMDAiIHk9IjcyNiIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZmlsbD0iI2Y4ZmFmYyIgZm9udC1mYW1pbHk9InNhbnMtc2VyaWYiIGZvbnQtc2l6ZT0iMTQiIGZvbnQtd2VpZ2h0PSJib2xkIj5NaWNoYWVsIEJsZXNzaW5nIOKAoiBDRU8sIFVwc2lkZSBuZzwvdGV4dD4KPC9zdmc+"
ACADEMY_STILL_URI = "data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSI4MDAiIGhlaWdodD0iNDUwIiB2aWV3Qm94PSIwIDAgODAwIDQ1MCI+CiAgPGRlZnM+CiAgICA8bGluZWFyR3JhZGllbnQgaWQ9InNreSIgeDE9IjAiIHkxPSIwIiB4Mj0iMCIgeTI9IjEiPgogICAgICA8c3RvcCBvZmZzZXQ9IjAlIiBzdG9wLWNvbG9yPSIjY2JkNWUxIi8+CiAgICAgIDxzdG9wIG9mZnNldD0iMTAwJSIgc3RvcC1jb2xvcj0iI2UyZThmMCIvPgogICAgPC9saW5lYXJHcmFkaWVudD4KICAgIDxsaW5lYXJHcmFkaWVudCBpZD0idHVyZiIgeDE9IjAiIHkxPSIwIiB4Mj0iMCIgeTI9IjEiPgogICAgICA8c3RvcCBvZmZzZXQ9IjAlIiBzdG9wLWNvbG9yPSIjMmU3ZDMyIi8+CiAgICAgIDxzdG9wIG9mZnNldD0iMTAwJSIgc3RvcC1jb2xvcj0iIzFiNWUyMCIvPgogICAgPC9saW5lYXJHcmFkaWVudD4KICA8L2RlZnM+CiAgPHJlY3Qgd2lkdGg9IjgwMCIgaGVpZ2h0PSIyMjUiIGZpbGw9InVybCgjc2t5KSIvPgogIDxyZWN0IHk9IjIyNSIgd2lkdGg9IjgwMCIgaGVpZ2h0PSIyMjUiIGZpbGw9InVybCgjdHVyZikiLz4KICA8bGluZSB4MT0iMCIgeTE9IjIyNSIgeDI9IjgwMCIgeTI9IjIyNSIgc3Ryb2tlPSIjOTRhM2I4IiBzdHJva2Utd2lkdGg9IjQiLz4KICA8cGF0aCBkPSJNOTAgMzYwIFEyMTAgMzE1IDM0MCAzNjAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iI2ZmZmZmZiIgc3Ryb2tlLXdpZHRoPSIzIiBvcGFjaXR5PSIwLjc1Ii8+CiAgPGNpcmNsZSBjeD0iNjMwIiBjeT0iNjgiIHI9IjM2IiBmaWxsPSIjMGYxNzJhIiBzdHJva2U9IiMzOGJkZjgiIHN0cm9rZS13aWR0aD0iMyIvPgogIDx0ZXh0IHg9IjYzMCIgeT0iNjQiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZpbGw9IiNmZmZmZmYiIGZvbnQtZmFtaWx5PSJzYW5zLXNlcmlmIiBmb250LXNpemU9IjExIiBmb250LXdlaWdodD0iYm9sZCI+RFlOQVNUWTwvdGV4dD4KICA8dGV4dCB4PSI2MzAiIHk9Ijc4IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmaWxsPSIjMzRkMzk5IiBmb250LWZhbWlseT0ic2Fucy1zZXJpZiIgZm9udC1zaXplPSIxMCIgZm9udC13ZWlnaHQ9ImJvbGQiPkZPT1RCQUxMIEFDQURFTVk8L3RleHQ+CiAgPGNpcmNsZSBjeD0iNDAwIiBjeT0iMTk1IiByPSIxNCIgZmlsbD0iIzFlMjkzYiIvPgogIDxyZWN0IHg9IjM4MCIgeT0iMjEyIiB3aWR0aD0iNDAiIGhlaWdodD0iNTgiIHJ4PSI4IiBmaWxsPSIjODU0ZDBlIi8+CiAgPHRleHQgeD0iNDAwIiB5PSIyNDYiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZpbGw9IiNmZmZmZmYiIGZvbnQtZmFtaWx5PSJzYW5zLXNlcmlmIiBmb250LXNpemU9IjE4IiBmb250LXdlaWdodD0iYm9sZCI+MDQ8L3RleHQ+CiAgPGNpcmNsZSBjeD0iNDg1IiBjeT0iMTkyIiByPSIxMSIgZmlsbD0iIzFlMjkzYiIvPgogIDxyZWN0IHg9IjQ3MCIgeT0iMjA2IiB3aWR0aD0iMzAiIGhlaWdodD0iNDYiIHJ4PSI2IiBmaWxsPSIjMGQ5NDg4Ii8+CiAgPHRleHQgeD0iNDg1IiB5PSIyMzMiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZpbGw9IiNmZmZmZmYiIGZvbnQtZmFtaWx5PSJzYW5zLXNlcmlmIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iYm9sZCI+MTQ8L3RleHQ+CiAgPGNpcmNsZSBjeD0iNjIwIiBjeT0iMTg0IiByPSIxNSIgZmlsbD0iIzFlMjkzYiIvPgogIDxyZWN0IHg9IjU5OCIgeT0iMjAyIiB3aWR0aD0iNDQiIGhlaWdodD0iNjQiIHJ4PSI4IiBmaWxsPSIjMGY3NjZlIi8+CiAgPHRleHQgeD0iNjIwIiB5PSIyMzkiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZpbGw9IiNmZmZmZmYiIGZvbnQtZmFtaWx5PSJzYW5zLXNlcmlmIiBmb250LXNpemU9IjIwIiBmb250LXdlaWdodD0iYm9sZCI+NTwvdGV4dD4KICA8cmVjdCB4PSIyNCIgeT0iMzg2IiB3aWR0aD0iMzUwIiBoZWlnaHQ9IjM4IiByeD0iMTAiIGZpbGw9IiMwZjE3MmEiIG9wYWNpdHk9IjAuODgiLz4KICA8dGV4dCB4PSI0MCIgeT0iNDEwIiBmaWxsPSIjZmZmZmZmIiBmb250LWZhbWlseT0ic2Fucy1zZXJpZiIgZm9udC1zaXplPSIxNCIgZm9udC13ZWlnaHQ9ImJvbGQiPkR5bmFzdHkgRm9vdGJhbGwgQWNhZGVteSDigKIgUGl0Y2ggQWN0aW9uIEZyYW1lPC90ZXh0Pgo8L3N2Zz4="
POV_STILL_URI = "data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSI4MDAiIGhlaWdodD0iNDUwIiB2aWV3Qm94PSIwIDAgODAwIDQ1MCI+CiAgPGRlZnM+CiAgICA8bGluZWFyR3JhZGllbnQgaWQ9ImJ3IiB4MT0iMCIgeTE9IjAiIHgyPSIwIiB5Mj0iMSI+CiAgICAgIDxzdG9wIG9mZnNldD0iMCUiIHN0b3AtY29sb3I9IiNlMmU4ZjAiLz4KICAgICAgPHN0b3Agb2Zmc2V0PSI1NSUiIHN0b3AtY29sb3I9IiM5NGEzYjgiLz4KICAgICAgPHN0b3Agb2Zmc2V0PSIxMDAlIiBzdG9wLWNvbG9yPSIjNjQ3NDhiIi8+CiAgICA8L2xpbmVhckdyYWRpZW50PgogIDwvZGVmcz4KICA8cmVjdCB3aWR0aD0iODAwIiBoZWlnaHQ9IjQ1MCIgZmlsbD0idXJsKCNidykiLz4KICA8cG9seWdvbiBwb2ludHM9IjM0MCwyMTAgNDYwLDIxMCA2ODAsNDUwIDEyMCw0NTAiIGZpbGw9IiM0NzU1NjkiLz4KICA8Y2lyY2xlIGN4PSI2NTUiIGN5PSI2NCIgcj0iMzQiIGZpbGw9IiMwZjE3MmEiIHN0cm9rZT0iIzM4YmRmOCIgc3Ryb2tlLXdpZHRoPSIzIi8+CiAgPHRleHQgeD0iNjU1IiB5PSI2MSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZmlsbD0iI2ZmZmZmZiIgZm9udC1mYW1pbHk9InNhbnMtc2VyaWYiIGZvbnQtc2l6ZT0iMTAiIGZvbnQtd2VpZ2h0PSJib2xkIj5EWU5BU1RZPC90ZXh0PgogIDx0ZXh0IHg9IjY1NSIgeT0iNzQiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZpbGw9IiMzNGQzOTkiIGZvbnQtZmFtaWx5PSJzYW5zLXNlcmlmIiBmb250LXNpemU9IjkiIGZvbnQtd2VpZ2h0PSJib2xkIj5BQ0FERU1ZPC90ZXh0PgogIDxjaXJjbGUgY3g9IjQwNSIgY3k9IjIzNSIgcj0iMTMiIGZpbGw9IiMxZTI5M2IiLz4KICA8cGF0aCBkPSJNMzg1IDI1MiBMNDI1IDI1MiBMNDIwIDMxNSBMMzkwIDMxNSBaIiBmaWxsPSIjMzM0MTU1Ii8+CiAgPHBhdGggZD0iTTM4NSAyNTggTDM2OCAyMzIgTTQyNSAyNTggTDQ0MiAyMzIiIHN0cm9rZT0iIzFlMjkzYiIgc3Ryb2tlLXdpZHRoPSI2IiBzdHJva2UtbGluZWNhcD0icm91bmQiLz4KICA8cmVjdCB4PSIxOTUiIHk9IjM0OCIgd2lkdGg9IjQxMCIgaGVpZ2h0PSI1OCIgcng9IjEyIiBmaWxsPSIjMGYxNzJhIiBvcGFjaXR5PSIwLjkiLz4KICA8dGV4dCB4PSI0MDAiIHk9IjM3MiIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZmlsbD0iI2ZmZmZmZiIgZm9udC1mYW1pbHk9InNhbnMtc2VyaWYiIGZvbnQtc2l6ZT0iMTUiIGZvbnQtd2VpZ2h0PSJib2xkIj5QT1Y6IHRoYXQgb25lIGJybyB0aGF0IGJsYW1lPC90ZXh0PgogIDx0ZXh0IHg9IjQwMCIgeT0iMzk0IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmaWxsPSIjMzRkMzk5IiBmb250LWZhbWlseT0ic2Fucy1zZXJpZiIgZm9udC1zaXplPSIxNSIgZm9udC13ZWlnaHQ9ImJvbGQiPmV2ZXJ5b25lIGV4Y2VwdCBoaW1zZWxmPC90ZXh0Pgo8L3N2Zz4="
SCHOOL_STILL_URI = "data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSI4MDAiIGhlaWdodD0iNDUwIiB2aWV3Qm94PSIwIDAgODAwIDQ1MCI+CiAgPGRlZnM+CiAgICA8bGluZWFyR3JhZGllbnQgaWQ9ImJnIiB4MT0iMCIgeTE9IjAiIHgyPSIxIiB5Mj0iMSI+CiAgICAgIDxzdG9wIG9mZnNldD0iMCUiIHN0b3AtY29sb3I9IiMxZTI5M2IiLz4KICAgICAgPHN0b3Agb2Zmc2V0PSIxMDAlIiBzdG9wLWNvbG9yPSIjMGYxNzJhIi8+CiAgICA8L2xpbmVhckdyYWRpZW50PgogIDwvZGVmcz4KICA8cmVjdCB3aWR0aD0iODAwIiBoZWlnaHQ9IjQ1MCIgZmlsbD0idXJsKCNiZykiLz4KICA8cmVjdCB4PSI2MCIgeT0iNTUiIHdpZHRoPSI2ODAiIGhlaWdodD0iMzQwIiByeD0iMTQiIGZpbGw9IiMzMzQxNTUiLz4KICA8cmVjdCB4PSI4NSIgeT0iODAiIHdpZHRoPSI2MzAiIGhlaWdodD0iMjI1IiByeD0iMTAiIGZpbGw9IiMxZTNhMmYiLz4KICA8Y2lyY2xlIGN4PSI2NDUiIGN5PSIxMTIiIHI9IjMwIiBmaWxsPSIjMGYxNzJhIiBzdHJva2U9IiMzOGJkZjgiIHN0cm9rZS13aWR0aD0iMi41Ii8+CiAgPHRleHQgeD0iNjQ1IiB5PSIxMDkiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZpbGw9IiNmZmZmZmYiIGZvbnQtZmFtaWx5PSJzYW5zLXNlcmlmIiBmb250LXNpemU9IjkiIGZvbnQtd2VpZ2h0PSJib2xkIj5EQVJBTU9MQTwvdGV4dD4KICA8dGV4dCB4PSI2NDUiIHk9IjEyMSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZmlsbD0iIzM0ZDM5OSIgZm9udC1mYW1pbHk9InNhbnMtc2VyaWYiIGZvbnQtc2l6ZT0iOSIgZm9udC13ZWlnaHQ9ImJvbGQiPkRZTkFTVFk8L3RleHQ+CiAgPGNpcmNsZSBjeD0iNDA1IiBjeT0iMTc1IiByPSIyNCIgZmlsbD0iIzFlMjkzYiIvPgogIDxwYXRoIGQ9Ik0zNTUgMjEwIEw0NTUgMjEwIEw0NzAgMzA1IEwzNDAgMzA1IFoiIGZpbGw9IiMxNmEzNGEiLz4KICA8cmVjdCB4PSIyMDUiIHk9IjI1NiIgd2lkdGg9IjM5MCIgaGVpZ2h0PSIzOCIgcng9IjgiIGZpbGw9IiMwZjE3MmEiIG9wYWNpdHk9IjAuOTIiLz4KICA8dGV4dCB4PSI0MDAiIHk9IjI4MCIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZmlsbD0iI2ZmZmZmZiIgZm9udC1mYW1pbHk9InNhbnMtc2VyaWYiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSJib2xkIj5idXQgd2hhdCBtYWtlcyBhIHNjaG9vbCBzcGVjaWFsIGlzbid0IGp1c3Qgd2hhdCB3ZSBsZWFybiBpbnNpZGU8L3RleHQ+CiAgPHJlY3QgeD0iODUiIHk9IjMyNSIgd2lkdGg9IjQ0MCIgaGVpZ2h0PSI0MiIgcng9IjEwIiBmaWxsPSIjMGYxNzJhIi8+CiAgPHRleHQgeD0iMTAzIiB5PSIzNTEiIGZpbGw9IiMzNGQzOTkiIGZvbnQtZmFtaWx5PSJzYW5zLXNlcmlmIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iYm9sZCI+RGFyYW1vbGEgRHluYXN0eSDigKIgVHdvIFNjaG9vbHMgT3V0cmVhY2ggKElzaGFyYSk8L3RleHQ+Cjwvc3ZnPg=="
CELEBRATION_STILL_URI = "data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSI4MDAiIGhlaWdodD0iNDUwIiB2aWV3Qm94PSIwIDAgODAwIDQ1MCI+CiAgPGRlZnM+CiAgICA8bGluZWFyR3JhZGllbnQgaWQ9ImJnIiB4MT0iMCIgeTE9IjAiIHgyPSIxIiB5Mj0iMSI+CiAgICAgIDxzdG9wIG9mZnNldD0iMCUiIHN0b3AtY29sb3I9IiMzMzQxNTUiLz4KICAgICAgPHN0b3Agb2Zmc2V0PSIxMDAlIiBzdG9wLWNvbG9yPSIjMGYxNzJhIi8+CiAgICA8L2xpbmVhckdyYWRpZW50PgogIDwvZGVmcz4KICA8cmVjdCB3aWR0aD0iODAwIiBoZWlnaHQ9IjQ1MCIgZmlsbD0idXJsKCNiZykiLz4KICA8cmVjdCB4PSI2NSIgeT0iNTUiIHdpZHRoPSI2NzAiIGhlaWdodD0iMzQwIiByeD0iMTQiIGZpbGw9IiM0NzU1NjkiLz4KICA8cGF0aCBkPSJNMjk1IDE2NSBRMzY1IDExMCA0MzUgMTY1IFE0MTUgMjE1IDM2NSAyMTUgUTMxNSAyMTUgMjk1IDE2NSBaIiBmaWxsPSIjZmJjZmU4Ii8+CiAgPGNpcmNsZSBjeD0iMzY1IiBjeT0iMjQ1IiByPSIzNCIgZmlsbD0iIzc4MzUwZiIvPgogIDxwYXRoIGQ9Ik0yODUgMzg1IEwzMTAgMjg1IEw0MjAgMjg1IEw0NDUgMzg1IFoiIGZpbGw9IiNmY2U3ZjMiLz4KICA8Y2lyY2xlIGN4PSIzNjUiIGN5PSIzMzUiIHI9IjM0IiBmaWxsPSIjZmJjZmU4IiBzdHJva2U9IiNlYWIzMDgiIHN0cm9rZS13aWR0aD0iNSIvPgogIDxyZWN0IHg9IjE5NSIgeT0iMzQyIiB3aWR0aD0iNDEwIiBoZWlnaHQ9IjQwIiByeD0iMTAiIGZpbGw9IiMwZjE3MmEiIG9wYWNpdHk9IjAuOSIvPgogIDx0ZXh0IHg9IjQwMCIgeT0iMzY3IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmaWxsPSIjZmJjZmU4IiBmb250LWZhbWlseT0ic2Fucy1zZXJpZiIgZm9udC1zaXplPSIxNCIgZm9udC13ZWlnaHQ9ImJvbGQiPkNlbGVicmF0aW9uICZhbXA7IEV2ZW50IEhpZ2hsaWdodCDigKIgUGVhY2ggR2VsZSAmYW1wOyBGYW48L3RleHQ+Cjwvc3ZnPg=="
INTERVIEW_STILL_URI = "data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSI4MDAiIGhlaWdodD0iNDUwIiB2aWV3Qm94PSIwIDAgODAwIDQ1MCI+CiAgPGRlZnM+CiAgICA8bGluZWFyR3JhZGllbnQgaWQ9ImJnIiB4MT0iMCIgeTE9IjAiIHgyPSIxIiB5Mj0iMSI+CiAgICAgIDxzdG9wIG9mZnNldD0iMCUiIHN0b3AtY29sb3I9IiM0NzU1NjkiLz4KICAgICAgPHN0b3Agb2Zmc2V0PSIxMDAlIiBzdG9wLWNvbG9yPSIjMWUyOTNiIi8+CiAgICA8L2xpbmVhckdyYWRpZW50PgogIDwvZGVmcz4KICA8cmVjdCB3aWR0aD0iODAwIiBoZWlnaHQ9IjQ1MCIgZmlsbD0idXJsKCNiZykiLz4KICA8cmVjdCB4PSI2NSIgeT0iNTUiIHdpZHRoPSI2NzAiIGhlaWdodD0iMzQwIiByeD0iMTQiIGZpbGw9IiM2NDc0OGIiLz4KICA8Y2lyY2xlIGN4PSI2NDUiIGN5PSI5NiIgcj0iMjgiIGZpbGw9IiMwZjE3MmEiIHN0cm9rZT0iIzM4YmRmOCIgc3Ryb2tlLXdpZHRoPSIyLjUiLz4KICA8dGV4dCB4PSI2NDUiIHk9IjkzIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmaWxsPSIjZmZmZmZmIiBmb250LWZhbWlseT0ic2Fucy1zZXJpZiIgZm9udC1zaXplPSI4IiBmb250LXdlaWdodD0iYm9sZCI+REFSQU1PTEE8L3RleHQ+CiAgPHRleHQgeD0iNjQ1IiB5PSIxMDQiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZpbGw9IiMzNGQzOTkiIGZvbnQtZmFtaWx5PSJzYW5zLXNlcmlmIiBmb250LXNpemU9IjgiIGZvbnQtd2VpZ2h0PSJib2xkIj5EWU5BU1RZPC90ZXh0PgogIDxjaXJjbGUgY3g9IjM4NSIgY3k9IjE1NSIgcj0iNDIiIGZpbGw9IiMxZTI5M2IiLz4KICA8cGF0aCBkPSJNMjk1IDM5NSBMMzI1IDIyMCBMNDQ1IDIyMCBMNDc1IDM5NSBaIiBmaWxsPSIjMGYxNzJhIi8+CiAgPHJlY3QgeD0iMjAwIiB5PSIyOTUiIHdpZHRoPSI0MDAiIGhlaWdodD0iNjIiIHJ4PSIxMCIgZmlsbD0iIzBmMTcyYSIgb3BhY2l0eT0iMC45MiIvPgogIDx0ZXh0IHg9IjQwMCIgeT0iMzIwIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmaWxsPSIjZmZmZmZmIiBmb250LWZhbWlseT0ic2Fucy1zZXJpZiIgZm9udC1zaXplPSIxNCIgZm9udC13ZWlnaHQ9ImJvbGQiPnRoZXNlIGFyZSB0aGUgdGhpbmdzIHRoYXQ8L3RleHQ+CiAgPHRleHQgeD0iNDAwIiB5PSIzNDMiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZpbGw9IiMzNGQzOTkiIGZvbnQtZmFtaWx5PSJzYW5zLXNlcmlmIiBmb250LXNpemU9IjE0IiBmb250LXdlaWdodD0iYm9sZCI+bWFrZXMgdXMgZ3JvdyBhcyBpbmRpdmlkdWFsczwvdGV4dD4KPC9zdmc+"
SPEAKER_STILL_URI = "data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSI4MDAiIGhlaWdodD0iNDUwIiB2aWV3Qm94PSIwIDAgODAwIDQ1MCI+CiAgPGRlZnM+CiAgICA8bGluZWFyR3JhZGllbnQgaWQ9ImJnIiB4MT0iMCIgeTE9IjAiIHgyPSIxIiB5Mj0iMSI+CiAgICAgIDxzdG9wIG9mZnNldD0iMCUiIHN0b3AtY29sb3I9IiMzMzQxNTUiLz4KICAgICAgPHN0b3Agb2Zmc2V0PSIxMDAlIiBzdG9wLWNvbG9yPSIjMWUyOTNiIi8+CiAgICA8L2xpbmVhckdyYWRpZW50PgogIDwvZGVmcz4KICA8cmVjdCB3aWR0aD0iODAwIiBoZWlnaHQ9IjQ1MCIgZmlsbD0idXJsKCNiZykiLz4KICA8cmVjdCB4PSI2NSIgeT0iNTUiIHdpZHRoPSI2NzAiIGhlaWdodD0iMzQwIiByeD0iMTQiIGZpbGw9IiNmMWY1ZjkiLz4KICA8dGV4dCB4PSI0MTUiIHk9IjE1NSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZmlsbD0iIzk5MWIxYiIgZm9udC1mYW1pbHk9InNhbnMtc2VyaWYiIGZvbnQtc2l6ZT0iNzgiIGZvbnQtd2VpZ2h0PSJib2xkIiBvcGFjaXR5PSIwLjI4Ij5DRjwvdGV4dD4KICA8dGV4dCB4PSIyMzUiIHk9IjIyMCIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZmlsbD0iIzdmMWQxZCIgZm9udC1mYW1pbHk9InNhbnMtc2VyaWYiIGZvbnQtc2l6ZT0iMjIiIGZvbnQtd2VpZ2h0PSJib2xkIj5DQU0uLi48L3RleHQ+CiAgPHRleHQgeD0iNTQ1IiB5PSIyMTAiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZpbGw9IiM3ZjFkMWQiIGZvbnQtZmFtaWx5PSJzYW5zLXNlcmlmIiBmb250LXNpemU9IjE4IiBmb250LXdlaWdodD0iYm9sZCI+Li4uTE9XU0hJUDwvdGV4dD4KICA8Y2lyY2xlIGN4PSIzODUiIGN5PSIxNDgiIHI9IjM0IiBmaWxsPSIjMWUyOTNiIi8+CiAgPHJlY3QgeD0iMzU3IiB5PSIxMzgiIHdpZHRoPSI1NiIgaGVpZ2h0PSIxNiIgcng9IjQiIGZpbGw9IiMwZjE3MmEiLz4KICA8cGF0aCBkPSJNMzE1IDM5NSBMMzM1IDIxNSBMNDM1IDIxNSBMNDU1IDM5NSBaIiBmaWxsPSIjYThhMjllIi8+CiAgPHJlY3QgeD0iNTIwIiB5PSIyNjUiIHdpZHRoPSI5MCIgaGVpZ2h0PSIxMzAiIHJ4PSI4IiBmaWxsPSIjZDk3NzA2Ii8+CiAgPHJlY3QgeD0iMTk1IiB5PSIzNDYiIHdpZHRoPSI0MTAiIGhlaWdodD0iMzgiIHJ4PSIxMCIgZmlsbD0iIzBmMTcyYSIgb3BhY2l0eT0iMC45Ii8+CiAgPHRleHQgeD0iNDAwIiB5PSIzNzEiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZpbGw9IiNmOGZhZmMiIGZvbnQtZmFtaWx5PSJzYW5zLXNlcmlmIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iYm9sZCI+Q2FtcHVzIEZlbGxvd3NoaXAgU3RhZ2UgU3BlYWtpbmcg4oCiIE1pYyAmYW1wOyBQb2RpdW08L3RleHQ+Cjwvc3ZnPg=="

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
    p, span, label, .stMarkdown, div[data-testid="stMarkdownContainer"] {
        color: #1e293b !important;
    }
    .upside-hero {
        background: linear-gradient(135deg, #0f172a 0%, #1e1b4b 55%, #312e81 100%);
        padding: 2rem 2.25rem;
        border-radius: 18px;
        color: #ffffff !important;
        margin-bottom: 1.5rem;
        box-shadow: 0 12px 28px -6px rgba(15, 23, 42, 0.25);
    }
    .upside-hero h1 {
        margin: 0.35rem 0 0.65rem 0;
        font-size: 2.2rem;
        font-weight: 800;
        letter-spacing: -0.02em;
        color: #ffffff !important;
    }
    .upside-hero p {
        margin: 0;
        color: #e0e7ff !important;
        font-size: 1.03rem;
        line-height: 1.6;
    }
    .upside-badge {
        display: inline-block;
        background: rgba(16, 185, 129, 0.22);
        border: 1px solid rgba(52, 211, 153, 0.55);
        color: #34d399 !important;
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
        display: block;
    }
    .card-thumb {
        width: 100%;
        height: 200px;
        object-fit: cover;
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
        color: #1e1b4b !important;
        margin-bottom: 0.5rem;
    }
    .pill-tag-green {
        background: #d1fae5;
        color: #065f46 !important;
    }
    .cta-link {
        display: inline-block;
        margin-top: 0.65rem;
        padding: 0.52rem 0.95rem;
        border-radius: 10px;
        background: #0f172a;
        color: #ffffff !important;
        text-decoration: none;
        font-weight: 700;
        font-size: 0.86rem;
    }
    .cta-link:hover {
        background: #1e293b;
    }
    .cta-whatsapp {
        background: #059669;
    }
    .cta-whatsapp:hover {
        background: #047857;
    }
    .cta-social {
        background: #1e1b4b;
    }
    .cta-social:hover {
        background: #312e81;
    }
    .stTextInput label, .stTextArea label, .stSelectbox label, .stFileUploader label {
        color: #0f172a !important;
        font-weight: 700 !important;
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
            <h1>Clean Pacing, Clear Voice & Visuals That Connect</h1>
            <p>
                <strong>Upside ng</strong> edits stage talks and interviews, event celebrations, school outreach documentaries,
                comedy POV reels, and football/sports clips with smooth transitions, motion effects, colour adjustments,
                sound design, captions, and engaging storytelling.
            </p>
            <div style="margin-top: 1.1rem; font-size: 0.92rem; color: #cbd5e1 !important;">
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
            <span class="pill-tag pill-tag-green">DIRECT BOOKING & SOCIAL CHANNELS</span>
            <h3 style="margin:0.25rem 0 0.75rem 0; font-size:1.3rem; font-weight:800; color:#0f172a;">
                Work With Michael Blessing & Upside ng
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

st.markdown("## 🎞️ Edited Videos & Project Stills")
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
