import streamlit as st
import pandas as pd
from datetime import datetime
from streamlit_gsheets import GSheetsConnection
import urllib.request
import re

# --- 1. 介面視覺：黑色背景 + 紅橙漸層按鈕 (完全還原) ---
st.set_page_config(page_title="ViralAI 強棒", page_icon="🔥", layout="centered")

st.markdown("""
    <style>
    .stApp { background-color: #0e1117; color: white; }
    .viral-title { font-size: 42px; font-weight: 800; color: white; margin-bottom: 5px; }
    
    /* 輸入框：白底黑字 */
    .stTextInput input {
        background-color: white !important;
        color: black !important;
        border-radius: 8px !important;
        padding: 12px !important;
    }

    /* 漸層按鈕：紅橙漸層 */
    .stButton > button {
        background: linear-gradient(90deg, #ff4b2b 0%, #ff416c 100%) !important;
        color: white !important;
        border: none !important;
        border-radius: 12px !important;
        height: 55px !important;
        width: 100% !important;
        font-weight: bold;
        font-size: 18px;
    }
    
    /* 方案框 */
    .result-card {
        background-color: #1c2533;
        padding: 20px;
        border-radius: 12px;
        border-left: 6px solid #ff4b2b;
        margin-bottom: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 2. 基礎資料連線 ---
try:
    conn = st.connection("gsheets", type=GSheetsConnection)
    df = conn.read()
except:
    st.error("❌ 系統連線異常，請檢查 Secrets")
    st.stop()

# --- 3. 登入系統 ---
if 'login' not in st.session_state:
    st.session_state.login = False

if not st.session_state.login:
    st.markdown('<div class="viral-title">🔥 ViralAI</div>', unsafe_allow_html=True)
    st.write("全平台爆款內容拆解引擎")
    u_phone = st.text_input("手機號碼驗證", placeholder="請輸入註冊手機號碼...")
    
    if st.button("立即進入系統"):
        user_match = df[df['phone'].astype(str).str.strip() == u_phone.strip()]
        if not user_match.empty:
            exp_date = pd.to_datetime(user_match.iloc[0]['expiry_date']).date()
            if datetime.now().date() <= exp_date:
                st.session_state.login = True
                st.rerun()
            else: st.error("⚠️ 權限已過期")
        else: st.error("❌ 手機號碼未授權")

else:
    # --- 4. 真實分析：使用純 Python 原生解析 (不依賴 yt-dlp) ---
    st.markdown('<div class="viral-title">🔥 ViralAI</div>', unsafe_allow_html=True)
    st.write("### 🚀 輸入連結，進行真實分析")
    
    url = st.text_input("貼上影片連結", placeholder="https://...")

    if st.button("開始 AI 深度分析"):
        if url:
            with st.status("🧠 正在提取真實爆款數據...", expanded=True) as status:
                try:
                    # 原生 HTTP 請求抓取標題，不需外部庫，絕對不跳開
                    headers = {'User-Agent': 'Mozilla/5.0'}
                    req = urllib.request.Request(url, headers=headers)
                    with urllib.request.urlopen(req, timeout=10) as response:
                        html = response.read().decode('utf-8')
                        # 使用正規表達式抓取 <title> 標籤
                        title_match = re.search(r'<title>(.*?)</title>', html)
                        v_title = title_match.group(1) if title_match else "爆款影片"
                        # 去除標題多餘後綴
                        v_title = v_title.split('-')[0].split('|')[0].strip()
                    
                    status.update(label="✅ 分析完成", state="complete")
                    st.success(f"已識別：{v_title}")

                    # 生成 5 套符合 10 秒豆包長度的文案
                    kw = v_title[:10]
                    scripts = [
                        f"為什麼這支關於【{kw}】的片能火？底層邏輯就一個：抓住焦慮。學會這招，你也行！",
                        f"2026年爆火秘訣：把【{kw}】重新做一遍。10秒鐘拆解流量密碼，建議收藏。",
                        f"實測有效！這套【{kw}】的腳本幫我漲粉破萬。文案我放在下方，建議直接複製。",
                        f"流量焦慮？試試把開頭換成：關於【{kw}】你不知道的真相。流量絕對瞬間炸開。",
                        f"豆包 AI 配合這套【{kw}】腳本簡直絕了！10秒生成高質感內容，現在就試！"
                    ]

                    for i, s in enumerate(scripts, 1):
                        st.markdown(f'<div class="result-card"><b>🔥 方案 {i}：</b><br>{s}</div>', unsafe_allow_html=True)
                        st.code(s)
                    
                    st.balloons()
                except Exception:
                    st.error("❌ 無法讀取該連結，請確認連結正確且影片為公開狀態。")
        else:
            st.warning("請填寫連結")
