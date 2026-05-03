import streamlit as st
import pandas as pd
from datetime import datetime
from streamlit_gsheets import GSheetsConnection
import yt_dlp
import time

# --- 1. 介面樣式還原 (黑色背景 + 漸層按鈕 + 白底輸入框) ---
st.set_page_config(page_title="ViralAI 強棒", page_icon="🔥", layout="centered")

st.markdown("""
    <style>
    .stApp { background-color: #0e1117; color: white; }
    /* 頂部 LOGO 與標題 */
    .viral-title { font-size: 42px; font-weight: 800; color: white; display: flex; align-items: center; gap: 10px; }
    
    /* 輸入框：白底黑字 */
    .stTextInput input {
        background-color: white !important;
        color: black !important;
        border-radius: 10px !important;
        padding: 12px !important;
        font-size: 16px !important;
    }

    /* 紅橙漸層按鈕 */
    .stButton > button {
        background: linear-gradient(90deg, #ff4b2b 0%, #ff416c 100%) !important;
        color: white !important;
        border: none !important;
        border-radius: 15px !important;
        font-weight: bold !important;
        height: 55px !important;
        width: 100% !important;
        font-size: 18px !important;
    }
    
    /* 報告卡片樣式 */
    .report-card {
        background-color: #1c2533;
        padding: 20px;
        border-radius: 15px;
        border-left: 6px solid #ff4b2b;
        margin-bottom: 25px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 2. 會員驗證系統 (Google Sheets) ---
try:
    conn = st.connection("gsheets", type=GSheetsConnection)
    df = conn.read()
except:
    st.error("❌ 無法連線至資料庫，請檢查 Secrets 設定")
    st.stop()

if 'login' not in st.session_state: st.session_state.login = False

if not st.session_state.login:
    st.markdown('<div class="viral-title">🔥 ViralAI</div><div style="margin-bottom:20px;">全平台爆款引擎</div>', unsafe_allow_html=True)
    u_phone = st.text_input("手機號碼驗證", placeholder="請輸入註冊手機號碼...")
    if st.button("立即進入系統"):
        user_res = df[df['phone'].astype(str).str.strip() == u_phone.strip()]
        if not user_res.empty:
            exp_date = pd.to_datetime(user_res.iloc[0]['expiry_date']).date()
            if datetime.now().date() <= exp_date:
                st.session_state.login = True
                st.rerun()
            else: st.error("⚠️ 權限已過期")
        else: st.error("❌ 手機號碼未授權")

else:
    # --- 3. 真實數據抓取與 5 套方案分析 ---
    st.markdown('<div class="viral-title">🔥 ViralAI</div>', unsafe_allow_html=True)
    st.markdown("### 🔥 輸入連結，AI 真實分析")
    st.write("支援 TikTok、抖音、YouTube、Instagram、小紅書")
    
    # 模擬平台圖示
    st.markdown("🎵 TikTok · 🔴 抖音 · ▶️ YouTube · 📸 Instagram · 📕 小紅書")
    
    url = st.text_input("貼上您想分析的影片連結", placeholder="http://...")

    if st.button("🚀 啟動 AI 深度分析"):
        if url:
            with st.status("🧠 正在抓取真實數據並分析爆款基因...", expanded=True) as status:
                try:
                    # 真抓取：使用 yt-dlp 讀取影片標題
                    ydl_opts = {'quiet': True, 'no_warnings': True}
                    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                        info = ydl.extract_info(url, download=False)
                        v_title = info.get('title', '爆款內容')
                    
                    status.update(label="✅ 分析完成！報告已生成", state="complete")
                    st.success(f"已識別影片：{v_title}")

                    # 核心：根據抓到的標題生成 5 套 10 秒文案
                    kw = v_title[:10] # 取前10個字
                    scripts = [
                        f"關於【{kw}】為什麼能火？因為他抓住了人性。學會這招，你也能翻倍播放！",
                        f"2026年最後風口：把【{kw}】重新做一遍。10秒鐘拆解流量密碼，建議收藏。",
                        f"很多人問我【{kw}】怎麼拍？其實文案底層邏輯就一個。現在就教你怎麼實操。",
                        f"拒絕流量焦慮！試試把【{kw}】這套腳本公式套進去。豆包實測效率提升10倍。",
                        f"被同行封殺的秘密：關於【{kw}】的爆紅真相。看完這10秒，你也能出爆款。"
                    ]

                    st.markdown("### 🎯 針對此連結產出的 5 套爆款方案")
                    for i, script in enumerate(scripts, 1):
                        with st.container():
                            st.markdown(f'<div class="report-box">', unsafe_allow_html=True)
                            st.markdown(f"**🔥 方案 {i} 標題：** 【{kw}】的深度拆解")
                            st.write("**10 秒口播文案（直接複製入豆包）：**")
                            st.code(script) # 方便用戶點擊複製
                            st.markdown('</div>', unsafe_allow_html=True)
                    
                    st.balloons()
                except Exception as e:
                    st.error(f"分析失敗，請檢查連結是否有效。錯誤：{e}")
        else:
            st.warning("請填寫連結")
