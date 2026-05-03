import streamlit as st
import pandas as pd
from datetime import datetime
from streamlit_gsheets import GSheetsConnection
import urllib.request

# --- 視覺：黑金爆款還原 ---
st.set_page_config(page_title="ViralAI", page_icon="🔥")

st.markdown("""
    <style>
    .stApp { background-color: #0e1117; color: white; }
    .stTextInput input { background-color: white !important; color: black !important; border-radius: 10px !important; }
    .stButton > button {
        background: linear-gradient(90deg, #ff4b2b 0%, #ff416c 100%) !important;
        color: white !important;
        border-radius: 12px !important;
        height: 55px !important; width: 100% !important;
        font-weight: bold; font-size: 18px !important;
    }
    .card { background-color: #1c2533; padding: 20px; border-radius: 15px; border-left: 6px solid #ff4b2b; margin-top: 20px; }
    </style>
    """, unsafe_allow_html=True)

# --- 1. 登入系統 ---
if 'login' not in st.session_state: st.session_state.login = False

if not st.session_state.login:
    st.markdown('<h1 style="color:white;">🔥 ViralAI</h1>', unsafe_allow_html=True)
    st.write("全平台爆款內容拆解引擎")
    u_phone = st.text_input("手機號碼驗證", placeholder="輸入手機號碼...")
    
    if st.button("立即登入"):
        try:
            conn = st.connection("gsheets", type=GSheetsConnection)
            df = conn.read()
            user = df[df['phone'].astype(str).str.strip() == u_phone.strip()]
            if not user.empty:
                st.session_state.login = True
                st.rerun()
            else: st.error("❌ 號碼未授權")
        except: st.error("系統連線中，請再點一次")

else:
    # --- 2. 主功能：純原生解析 (不再依賴 yt-dlp) ---
    st.markdown('<h1 style="color:white;">🚀 AI 爆款分析</h1>', unsafe_allow_html=True)
    url = st.text_input("貼上連結 (TikTok/YouTube/抖音)", placeholder="https://...")

    if st.button("啟動 AI 深度拆解"):
        if url:
            with st.spinner("🧠 正在提取數據..."):
                try:
                    # 使用最簡單的 urllib 抓標題，絕不崩潰
                    headers = {'User-Agent': 'Mozilla/5.0'}
                    req = urllib.request.Request(url, headers=headers)
                    with urllib.request.urlopen(req, timeout=5) as resp:
                        html = resp.read().decode('utf-8', errors='ignore')
                        # 找標題
                        v_title = html.split('<title>')[1].split('</title>')[0]
                        v_title = v_title.split('-')[0].split('|')[0].strip()
                    
                    st.success(f"✅ 已識別影片：{v_title}")
                    
                    # 生成文案
                    kw = v_title[:8]
                    scripts = [
                        f"關於【{kw}】為什麼能火？邏輯就一個：抓住焦慮。學會這招，你也行！",
                        f"2026年爆火秘訣：把【{kw}】重新做一遍。10秒拆解流量密碼。",
                        f"實測有效！這套【{kw}】腳本幫我漲粉破萬。文案在下方，直接複製。"
                    ]

                    for i, s in enumerate(scripts, 1):
                        st.markdown(f'<div class="card"><b>方案 {i}：</b><br>{s}</div>', unsafe_allow_html=True)
                        st.code(s)
                    st.balloons()
                except:
                    st.error("❌ 連結讀取失敗，請確認連結正確。")
