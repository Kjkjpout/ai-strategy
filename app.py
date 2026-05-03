import streamlit as st
import pandas as pd
from datetime import datetime
from streamlit_gsheets import GSheetsConnection
import urllib.request

# --- 1. 視覺還原：黑金爆款設計 (對標你的截圖) ---
st.set_page_config(page_title="ViralAI", page_icon="🔥")

st.markdown("""
    <style>
    .stApp { background-color: #0e1117; color: white; }
    .viral-title { font-size: 42px; font-weight: 800; color: white; margin-bottom: 5px; }
    .stTextInput input { background-color: white !important; color: black !important; border-radius: 10px !important; }
    .stButton > button {
        background: linear-gradient(90deg, #ff4b2b 0%, #ff416c 100%) !important;
        color: white !important;
        border-radius: 15px !important;
        height: 60px !important; width: 100% !important;
        font-weight: bold; font-size: 20px !important;
    }
    .result-card { background-color: #1c2533; padding: 20px; border-radius: 15px; border-left: 6px solid #ff4b2b; margin-bottom: 20px; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. 登入系統邏輯 ---
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    st.markdown('<div class="viral-title">🔥 ViralAI</div>', unsafe_allow_html=True)
    st.write("全平台爆款內容拆解引擎")
    u_phone = st.text_input("🔑 手機號碼驗證", placeholder="請輸入註冊手機號碼...")
    
    if st.button("立即進入系統"):
        try:
            conn = st.connection("gsheets", type=GSheetsConnection)
            df = conn.read()
            # 匹配你的 Google Sheet 資料 (手機號末三位為 266 那筆)
            user_data = df[df['phone'].astype(str).str.strip() == u_phone.strip()]
            if not user_data.empty:
                st.session_state.logged_in = True
                st.rerun()
            else:
                st.error("❌ 號碼未授權，請聯繫管理員")
        except:
            st.error("系統初始化中，請稍候再點擊一次")

else:
    # --- 3. 爆款分析主功能 (純原生技術，絕不跳開) ---
    st.markdown('<div class="viral-title">🔥 ViralAI</div>', unsafe_allow_html=True)
    url = st.text_input("貼上影片連結 (TikTok/YouTube/抖音)", placeholder="https://...")

    if st.button("啟動 AI 深度拆解"):
        if url:
            with st.status("🧠 正在提取爆款數據...", expanded=True) as status:
                try:
                    # 使用 Python 內建工具抓取，不依賴 yt-dlp，不會跳開
                    headers = {'User-Agent': 'Mozilla/5.0'}
                    req = urllib.request.Request(url, headers=headers)
                    with urllib.request.urlopen(req, timeout=5) as response:
                        page = response.read().decode('utf-8', errors='ignore')
                        # 暴力截取標題
                        v_title = page.split('<title>')[1].split('</title>')[0]
                        v_title = v_title.split('-')[0].split('|')[0].strip()
                    
                    status.update(label="✅ 分析完成", state="complete")
                    st.success(f"已識別影片：{v_title}")

                    # 生成 5 套爆款文案
                    kw = v_title[:8]
                    scripts = [
                        f"關於【{kw}】為什麼能火？底層邏輯就一個：抓住人性。學會這招，你也行！",
                        f"2026年爆火秘訣：把【{kw}】重新做一遍。10秒拆解流量密碼，建議收藏。",
                        f"實測有效！這套【{kw}】的腳本幫我漲粉破萬。文案在下方，直接複製。",
                        f"流量焦慮？試試把開頭換成：關於【{kw}】你不知道的真相。流量瞬間炸開。",
                        f"豆包 AI 配合這套【{kw}】腳本簡解絕了！10秒生成高質感內容，現在就試！"
                    ]

                    for i, s in enumerate(scripts, 1):
                        st.markdown(f'<div class="result-card"><b>🔥 方案 {i}：</b><br>{s}</div>', unsafe_allow_html=True)
                        st.code(s)
                    st.balloons()
                except:
                    st.error("❌ 讀取連結失敗，請確認連結正確。")
        else:
            st.warning("請先輸入連結")
