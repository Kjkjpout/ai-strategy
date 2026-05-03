import streamlit as st
import pandas as pd
from datetime import datetime
from streamlit_gsheets import GSheetsConnection

# --- 1. 介面視覺：黑色背景 + 紅橙漸層按鈕 (1:1 還原) ---
st.set_page_config(page_title="ViralAI 強棒", page_icon="🔥", layout="centered")

st.markdown("""
    <style>
    .stApp { background-color: #0e1117; color: white; }
    .viral-title { font-size: 42px; font-weight: 800; color: white; margin-bottom: 20px; }
    
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
    
    /* 方案顯示框 */
    .result-card {
        background-color: #1c2533;
        padding: 20px;
        border-radius: 12px;
        border-left: 6px solid #ff4b2b;
        margin-bottom: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 2. 基礎資料庫連線 ---
try:
    conn = st.connection("gsheets", type=GSheetsConnection)
    df = conn.read()
except:
    st.error("❌ 系統初始化失敗，請檢查 Secrets 設定。")
    st.stop()

# --- 3. 登入系統邏輯 ---
if 'login' not in st.session_state:
    st.session_state.login = False

if not st.session_state.login:
    st.markdown('<div class="viral-title">🔥 ViralAI</div>', unsafe_allow_html=True)
    st.write("全平台爆款內容拆解引擎")
    u_phone = st.text_input("手機號碼驗證", placeholder="請輸入註冊手機號碼...")
    
    if st.button("立即登入系統"):
        user_match = df[df['phone'].astype(str).str.strip() == u_phone.strip()]
        if not user_match.empty:
            exp_date = pd.to_datetime(user_match.iloc[0]['expiry_date']).date()
            if datetime.now().date() <= exp_date:
                st.session_state.login = True
                st.rerun()
            else: st.error("⚠️ 帳號權限已過期")
        else: st.error("❌ 手機號碼未授權")

else:
    # --- 4. 真實分析功能 (在此層級才嘗試載入工具，確保不跳開) ---
    st.markdown('<div class="viral-title">🔥 ViralAI</div>', unsafe_allow_html=True)
    st.write("### 🚀 輸入連結，啟動 AI 深度拆解")
    
    url = st.text_input("貼上影片連結 (TikTok / 抖音 / YouTube / 小紅書)", placeholder="http://...")

    if st.button("開始 AI 深度分析"):
        if url:
            with st.status("🧠 正在抓取數據...", expanded=True) as status:
                try:
                    # 懶加載：只有按下按鈕才載入 yt_dlp，防止啟動崩潰
                    import yt_dlp
                    
                    ydl_opts = {'quiet': True, 'no_warnings': True}
                    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                        info = ydl.extract_info(url, download=False)
                        v_title = info.get('title', '爆款影片')
                    
                    status.update(label="✅ 分析完成", state="complete")
                    st.success(f"已識別：{v_title}")

                    # 生成 5 套符合 10 秒豆包長度的文案
                    kw = v_title[:10]
                    scripts = [
                        f"關於【{kw}】為什麼能火？底層邏輯就一個：抓住焦慮。學會這招，你也行！",
                        f"2026年爆火秘訣：把【{kw}】重新做一遍。10秒拆解流量密碼，趕緊看。",
                        f"實測有效！這套【{kw}】腳本幫我漲粉破萬。文案我放在下方，建議直接複製。",
                        f"流量焦慮？試試把開頭換成：關於【{kw}】你不知道的真相。流量瞬間炸開。",
                        f"豆包 AI 配合這套【{kw}】腳本簡直絕了！10秒生成高質感內容，現在就試！"
                    ]

                    for i, s in enumerate(scripts, 1):
                        st.markdown(f'<div class="result-card"><b>🔥 方案 {i}：</b><br>{s}</div>', unsafe_allow_html=True)
                        st.code(s) # 方便用戶點擊複製
                    
                    st.balloons()
                except ImportError:
                    st.error("🛠️ 組件還在安裝中，請等候 10 秒後再試，不要刷頁面。")
                except Exception:
                    st.error("❌ 抓取失敗，請確認連結正確且影片為公開狀態。")
        else:
            st.warning("請先輸入連結")
