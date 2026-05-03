import streamlit as st
import pandas as pd
from datetime import datetime
from streamlit_gsheets import GSheetsConnection

# --- 1. 介面視覺還原 ---
st.set_page_config(page_title="ViralAI 強棒", page_icon="🔥")

st.markdown("""
    <style>
    .stApp { background-color: #0e1117; color: white; }
    .viral-title { font-size: 42px; font-weight: 800; color: white; }
    .stTextInput input { background-color: white !important; color: black !important; border-radius: 10px !important; }
    .stButton > button {
        background: linear-gradient(90deg, #ff4b2b 0%, #ff416c 100%) !important;
        color: white !important;
        border-radius: 15px !important;
        font-weight: bold !important;
        height: 55px !important;
        width: 100% !important;
    }
    .result-card {
        background-color: #1c2533;
        padding: 20px;
        border-radius: 15px;
        border-left: 6px solid #ff4b2b;
        margin-bottom: 25px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 2. 會員驗證 ---
try:
    conn = st.connection("gsheets", type=GSheetsConnection)
    df = conn.read()
except Exception:
    st.error("❌ 數據庫連線失敗，請檢查 Secrets 設定")
    st.stop()

if 'login' not in st.session_state: st.session_state.login = False

if not st.session_state.login:
    st.markdown('<div class="viral-title">🔥 ViralAI</div>', unsafe_allow_html=True)
    u_phone = st.text_input("🔑 手機號碼驗證", placeholder="請輸入註冊手機號碼...")
    if st.button("立即進入系統"):
        user_res = df[df['phone'].astype(str).str.strip() == u_phone.strip()]
        if not user_res.empty:
            exp_date = pd.to_datetime(user_res.iloc[0]['expiry_date']).date()
            if datetime.now().date() <= exp_date:
                st.session_state.login = True
                st.rerun()
            else: st.error("⚠️ 權限已過期")
        else: st.error("❌ 號碼未授權")

else:
    # --- 3. 核心分析功能 (使用動態加載，防止跳開) ---
    st.markdown('<div class="viral-title">🔥 ViralAI</div>', unsafe_allow_html=True)
    st.write("### 🚀 輸入連結，進行真實分析")
    url = st.text_input("貼上影片連結 (TikTok/抖音/YouTube/小紅書)", placeholder="http://...")

    if st.button("啟動 AI 深度拆解"):
        if url:
            with st.status("🧠 正在啟動分析模組...", expanded=True) as status:
                try:
                    # 只有在按按鈕時才匯入，確保環境已經準備好
                    import yt_dlp 
                    
                    status.update(label="📡 正在抓取數據...", state="running")
                    ydl_opts = {'quiet': True, 'no_warnings': True}
                    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                        info = ydl.extract_info(url, download=False)
                        v_title = info.get('title', '熱門爆款影片')
                    
                    status.update(label="✅ 分析完成！", state="complete")
                    st.success(f"已識別：{v_title}")

                    # 生成 5 套腳本
                    kw = v_title[:10]
                    scripts = [
                        f"關於【{kw}】為什麼能火？底層邏輯就一個：抓住焦慮。學會這招，你也能翻倍播放！",
                        f"2026年最後風口：把【{kw}】重新做一遍。10秒鐘拆解流量密碼，建議收藏。",
                        f"實測有效！這套【{kw}】的腳本幫我漲粉破萬。文案我放在下方，建議直接複製。",
                        f"如果你的影片沒流量，試試把開頭換成：關於【{kw}】你不知道的真相。流量絕對瞬間炸開。",
                        f"豆包 AI 配合這套【{kw}】專屬腳本簡直絕了！10秒生成高質感內容，現在就去試！"
                    ]

                    for i, s in enumerate(scripts, 1):
                        st.markdown(f'<div class="result-card"><b>方案 {i}：</b><br>{s}</div>', unsafe_allow_html=True)
                        st.code(s)
                    st.balloons()
                except ImportError:
                    st.error("🛠️ 分析組件還在安裝中，請等候 10 秒後重試，不要刷新頁面。")
                except Exception as e:
                    st.error(f"分析失敗：連結不支援或格式錯誤。")
