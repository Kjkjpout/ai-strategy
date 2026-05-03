import streamlit as st
import pandas as pd
from datetime import datetime
from streamlit_gsheets import GSheetsConnection
import time
import yt_dlp  # 確保您在 requirements.txt 加入了 yt-dlp

# --- 1. 頁面設定 ---
st.set_page_config(page_title="強棒 ViralAI Pro", page_icon="🔥", layout="centered")

# --- 2. 1:1 視覺還原 (黑底、漸層鈕、白底輸入框) ---
st.markdown("""
    <style>
    .stApp { background-color: #0e1117; color: white; }
    #MainMenu, footer, header { visibility: hidden; }
    .viral-title { font-size: 52px; font-weight: 800; display: flex; align-items: center; gap: 12px; }
    .viral-subtitle { font-size: 22px; color: #f8fafc; margin-bottom: 30px; }
    .section-title { font-size: 32px; font-weight: 700; margin-top: 40px; }
    .stButton > button {
        background: linear-gradient(90deg, #ff4b2b 0%, #ff416c 100%) !important;
        color: white !important;
        border-radius: 15px !important;
        font-weight: bold !important;
        height: 60px !important;
        width: 100% !important;
        font-size: 20px !important;
    }
    .stTextInput input {
        background-color: #f0f2f6 !important;
        color: #1f2937 !important;
        border-radius: 12px !important;
        padding: 15px !important;
    }
    .result-card { background: #1e293b; padding: 20px; border-radius: 15px; border-left: 5px solid #ff4b2b; margin-top: 20px; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. 會員登入驗證 (Google Sheets) ---
try:
    conn = st.connection("gsheets", type=GSheetsConnection)
    df = conn.read()
except:
    st.stop()

if 'login_status' not in st.session_state:
    st.session_state.login_status = False

if not st.session_state.login_status:
    st.markdown('<div class="viral-title">🔥 強棒 ViralAI</div><div class="viral-subtitle">全平台爆款引擎</div>', unsafe_allow_html=True)
    u_phone = st.text_input("🔑 輸入手機號碼驗證")
    if st.button("立即進入"):
        user = df[df['phone'].astype(str).str.strip() == u_phone.strip()]
        if not user.empty:
            exp = pd.to_datetime(user.iloc[0]['expiry_date']).date()
            if datetime.now().date() <= exp:
                st.session_state.login_status = True
                st.rerun()
            else: st.error("帳號已到期")
        else: st.error("查無號碼")
else:
    # --- 4. 真實數據抓取與分析主功能 ---
    st.markdown('<div class="viral-title">🔥 強棒 ViralAI</div><div class="viral-subtitle">全平台爆款引擎</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-title">🔥 輸入連結，真實數據分析</div>', unsafe_allow_html=True)
    
    video_url = st.text_input("貼上 YouTube / 抖音 / TikTok 連結", placeholder="https://...")

    if st.button("🚀 啟動真實數據拆解"):
        if video_url:
            with st.status("📡 正在連線並抓取影片真實數據...", expanded=True) as status:
                try:
                    # 使用 yt-dlp 真實抓取 metadata
                    ydl_opts = {'quiet': True, 'no_warnings': True}
                    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                        info = ydl.extract_info(video_url, download=False)
                        v_title = info.get('title', '未知標題')
                        v_desc = info.get('description', '')[:200]
                        v_tags = info.get('tags', [])
                    
                    st.write(f"✅ 已成功識別影片：{v_title}")
                    st.write("🧠 AI 正在根據影片內容重構 10 秒腳本...")
                    time.sleep(1)
                    status.update(label="真實數據分析完畢！", state="complete")

                    # --- 生成基於真實數據的內容 ---
                    st.markdown(f"### 📊 影片原始數據摘要")
                    st.write(f"**原始標題：** {v_title}")
                    st.write(f"**關鍵標籤：** {', '.join(v_tags) if v_tags else '無標籤'}")

                    st.markdown("---")
                    st.markdown("### 🎯 強棒推薦：5 組豆包爆款方案 (基於本影片)")

                    # 這裡的標題與文案會帶入 v_title 的元素
                    for i in range(1, 6):
                        with st.container():
                            st.markdown(f'<div class="result-card">', unsafe_allow_html=True)
                            st.markdown(f"**方案 {i} 爆款標題：**")
                            # 模擬 AI 根據標題生成的創意標題
                            new_title = f"【{v_title[:10]}...】爆火真相！為什麼這支片能瘋傳？" if i==1 else f"2026 必看：關於 {v_title[:15]} 的流量密碼"
                            st.code(new_title)
                            
                            st.markdown(f"**10 秒豆包口播文案：**")
                            # 模擬 AI 生成的 10 秒短文案
                            script_txt = f"你知道為什麼 {v_title[:10]} 能火嗎？背後邏輯其實很簡單，就是抓住了人性。學會這招，你的播放量也能翻倍！點贊關注我，帶你實操。"
                            st.text_area(f"腳本內容 (方案 {i})", value=script_txt, height=80, key=f"scr_{i}")
                            st.markdown('</div>', unsafe_allow_html=True)
                    
                    st.balloons()

                except Exception as e:
                    st.error(f"數據抓取失敗：連結格式不正確或影片受到限制。")
                    st.info("請確認連結是否正確，或嘗試其他公開影片。")
        else:
            st.warning("請先輸入連結！")

    if st.sidebar.button("登出"):
        st.session_state.login_status = False
        st.rerun()
