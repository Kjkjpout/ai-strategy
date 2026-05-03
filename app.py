import streamlit as st
import pandas as pd
from datetime import datetime

# --- 1. 極速視覺渲染 (啟動時不執行任何運算) ---
st.set_page_config(page_title="ViralAI", page_icon="🔥")

st.markdown("""
    <style>
    .stApp { background-color: #0e1117; color: white; }
    .viral-title { font-size: 42px; font-weight: bold; color: white; }
    .stTextInput input { background-color: white !important; color: black !important; border-radius: 10px !important; }
    .stButton > button {
        background: linear-gradient(90deg, #ff4b2b 0%, #ff416c 100%) !important;
        color: white !important;
        border-radius: 12px !important;
        height: 60px !important; width: 100% !important;
        font-weight: bold; font-size: 20px !important;
    }
    .card { background-color: #1c2533; padding: 20px; border-radius: 15px; border-left: 6px solid #ff4b2b; margin-top: 20px; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. 狀態管理 ---
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

# --- 3. 登入介面 ---
if not st.session_state.logged_in:
    st.markdown('<div class="viral-title">🔥 ViralAI</div>', unsafe_allow_html=True)
    st.write("全平台爆款內容拆解引擎")
    u_phone = st.text_input("🔑 手機號碼驗證", placeholder="輸入註冊手機號碼...")
    
    if st.button("立即進入系統"):
        # 只有按下去這一刻才開始加載連線，防止啟動跳開
        try:
            from streamlit_gsheets import GSheetsConnection
            conn = st.connection("gsheets", type=GSheetsConnection)
            df = conn.read()
            
            user_data = df[df['phone'].astype(str).str.strip() == u_phone.strip()]
            if not user_data.empty:
                exp_date = pd.to_datetime(user_data.iloc[0]['expiry_date']).date()
                if datetime.now().date() <= exp_date:
                    st.session_state.logged_in = True
                    st.rerun()
                else: st.error("⚠️ 帳號已過期")
            else: st.error("❌ 號碼未授權")
        except Exception as e:
            st.error("連線超時，請再試一次")

else:
    # --- 4. 分析主功能 ---
    st.markdown('<div class="viral-title">🔥 ViralAI</div>', unsafe_allow_html=True)
    st.write("### 🚀 輸入連結，進行真實分析")
    
    url = st.text_input("貼上影片連結 (TikTok / 抖音 / YouTube)", placeholder="https://...")

    if st.button("啟動 AI 深度拆解"):
        if url:
            with st.spinner("🧠 正在抓取數據..."):
                try:
                    # 使用原生 urllib 抓取，不載入重型庫
                    import urllib.request
                    headers = {'User-Agent': 'Mozilla/5.0'}
                    req = urllib.request.Request(url, headers=headers)
                    with urllib.request.urlopen(req, timeout=5) as response:
                        html = response.read().decode('utf-8')
                        start = html.find('<title>') + 7
                        end = html.find('</title>', start)
                        v_title = html[start:end].split('-')[0].split('|')[0].strip()
                    
                    st.success(f"✅ 已識別影片：{v_title}")
                    
                    kw = v_title[:8]
                    scripts = [
                        f"關於【{kw}】為什麼能火？底層邏輯就一個：抓住人性。學會這招，你也行！",
                        f"2026年爆火秘訣：把【{kw}】重新做一遍。10秒拆解流量密碼，建議收藏。",
                        f"實測有效！這套【{kw}】的腳本幫我漲粉破萬。文案在下方，直接複製。",
                        f"流量焦慮？試試把開頭換成：關於【{kw}】你不知道的真相。流量瞬間炸開。",
                        f"豆包 AI 配合這套【{kw}】腳本簡解絕了！10秒生成高質感內容，現在就試！"
                    ]

                    for i, s in enumerate(scripts, 1):
                        st.markdown(f'<div class="card"><b>方案 {i}：</b><br>{s}</div>', unsafe_allow_html=True)
                        st.code(s)
                    st.balloons()
                except:
                    st.error("❌ 讀取連結失敗，請確認連結正確。")
        else:
            st.warning("請輸入連結")

    if st.sidebar.button("登出"):
        st.session_state.logged_in = False
        st.rerun()
