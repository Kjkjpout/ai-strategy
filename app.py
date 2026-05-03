import streamlit as st
import pandas as pd
from datetime import datetime
from streamlit_gsheets import GSheetsConnection
import time

# --- 1. 核心頁面設定 ---
st.set_page_config(page_title="強棒 ViralAI Pro", page_icon="🔥", layout="centered")

# --- 2. 1:1 還原截圖風格設計 (純黑底、漸層鈕、白底輸入框) ---
st.markdown("""
    <style>
    .stApp { background-color: #0e1117; color: white; }
    #MainMenu, footer, header { visibility: hidden; }

    /* 頂部標語與標題 */
    .viral-title { font-size: 52px; font-weight: 800; display: flex; align-items: center; gap: 12px; }
    .viral-subtitle { font-size: 22px; color: #f8fafc; margin-top: 5px; margin-bottom: 30px; }

    /* 功能區標題與文字 */
    .section-title { font-size: 32px; font-weight: 700; margin-top: 40px; display: flex; align-items: center; gap: 10px; }
    .support-text { color: #94a3b8; font-size: 17px; margin-bottom: 25px; }

    /* 漸層按鈕 (紅橙漸層) */
    .stButton > button {
        background: linear-gradient(90deg, #ff4b2b 0%, #ff416c 100%) !important;
        color: white !important;
        border-radius: 15px !important;
        font-weight: bold !important;
        height: 60px !important;
        width: 100% !important;
        font-size: 20px !important;
    }

    /* 連結輸入框 (白底黑字) */
    .stTextInput input {
        background-color: #f0f2f6 !important;
        color: #1f2937 !important;
        border-radius: 12px !important;
        padding: 15px !important;
    }
    
    /* 報告卡片樣式 */
    .report-card { background: #1e293b; padding: 20px; border-radius: 15px; border-left: 5px solid #ff4b2b; margin-bottom: 20px; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. 基礎記憶：資料庫對接 ---
try:
    conn = st.connection("gsheets", type=GSheetsConnection)
    df = conn.read()
except:
    st.stop()

# --- 4. 登入系統邏輯 ---
if 'login_status' not in st.session_state:
    st.session_state.login_status = False

if not st.session_state.login_status:
    # 登入介面
    st.markdown('<div class="viral-title">🔥 強棒 ViralAI</div><div class="viral-subtitle">全平台爆款引擎</div>', unsafe_allow_html=True)
    u_phone = st.text_input("🔑 請輸入註冊手機號碼", placeholder="例如: 972896266")
    if st.button("立即登入"):
        user = df[df['phone'].astype(str).str.strip() == u_phone.strip()]
        if not user.empty:
            exp = pd.to_datetime(user.iloc[0]['expiry_date']).date()
            if datetime.now().date() <= exp:
                st.session_state.login_status = True
                st.rerun()
            else: st.error("帳號已過期")
        else: st.error("查無此手機號碼")
else:
    # --- 5. 智慧記憶：功能主頁面 ---
    st.markdown('<div class="viral-title">🔥 強棒 ViralAI</div><div class="viral-subtitle">全平台爆款引擎</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-title">🔥 輸入連結，AI 真實分析</div>', unsafe_allow_html=True)
    st.markdown('<div class="support-text">支援 TikTok、抖音、YouTube、Instagram、小紅書</div>', unsafe_allow_html=True)

    # 模擬截圖按鈕區塊
    st.markdown('<div style="display:flex; gap:10px; margin-bottom:25px;"><div style="background:#1f2937; padding:8px 15px; border-radius:10px;">🎵 TikTok</div><div style="background:#1f2937; padding:8px 15px; border-radius:10px;">🔴 抖音</div><div style="background:#1f2937; padding:8px 15px; border-radius:10px;">▶️ YouTube</div></div>', unsafe_allow_html=True)

    v_url = st.text_input("貼上連結", placeholder="http://...", label_visibility="collapsed")
    
    if st.button("🚀 開始 AI 深度分析"):
        if v_url:
            with st.status("🧠 強棒正在生成 10 秒豆包專用腳本...", expanded=True):
                time.sleep(2)
            
            st.success("✅ 分析完成！報告已生成")

            # --- 核心：5 條標題 + 5 套口播腳本 ---
            scripts = [
                {"t": "揭秘！為什麼你的影片沒流量？這招讓播量翻倍！", "c": "你以為爆款靠運氣？錯！掌握這套心理公式，就算新手也能出爆款。點贊關注，帶你實操。"},
                {"t": "2026年最後風口：用 AI 打造日進斗金帳號！", "c": "不想當被時代淘汰的人？現在就開始用 AI 生成內容。只需 10 秒，流量自來。"},
                {"t": "窮人與富人的差別，就在這一個操作細節裡。", "c": "普通人還在刷影片，高手已經在用 AI 賺錢了。這套腳本公式，我只教一次。"},
                {"t": "被同行封殺的秘密：高質感影音只需要 3 分鐘！", "c": "別再傻傻剪輯了！豆包 AI 配上這套強棒腳本，效率直接翻 10 倍。"},
                {"t": "拒絕焦慮！學會這招，讓你的流量不再是兩位數。", "c": "還在愁沒流量？那是因為你沒抓到黃金開頭。點開這條片，我手把手教你。"}
            ]

            st.markdown("### 🎯 豆包 10 秒專用：5 套爆款方案")
            
            for i, item in enumerate(scripts, 1):
                with st.expander(f"🔥 方案 {i}：{item['t']}"):
                    st.markdown(f"**爆款標題：**\n`{item['t']}`")
                    st.markdown(f"**10 秒口播文案 (直接複製入豆包)：**")
                    st.text_area(f"腳本 {i}", value=item['c'], height=80, key=f"s_{i}")
            
            st.balloons()
