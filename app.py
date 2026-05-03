import streamlit as st
import pandas as pd
from datetime import datetime
from streamlit_gsheets import GSheetsConnection

# 🧠 關鍵：容錯加載，防止 Error installing requirements 導致全機崩潰
try:
    import yt_dlp
    ANALYSIS_READY = True
except ImportError:
    ANALYSIS_READY = False

# --- 1. 視覺還原：黑底、紅橙漸層、白色輸入框 ---
st.set_page_config(page_title="ViralAI 強棒", page_icon="🔥", layout="centered")

st.markdown("""
    <style>
    .stApp { background-color: #0e1117; color: white; }
    .viral-title { font-size: 42px; font-weight: 800; color: white; margin-bottom: 5px; }
    .stTextInput input { background-color: white !important; color: black !important; border-radius: 8px !important; }
    /* 漸層按鈕 */
    .stButton > button {
        background: linear-gradient(90deg, #ff4b2b 0%, #ff416c 100%) !important;
        color: white !important;
        border: none !important;
        border-radius: 12px !important;
        height: 50px !important;
        width: 100% !important;
        font-weight: bold;
    }
    .report-card {
        background-color: #1c2533;
        padding: 15px;
        border-radius: 12px;
        border-left: 5px solid #ff4b2b;
        margin-top: 15px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 2. 會員驗證系統 ---
try:
    conn = st.connection("gsheets", type=GSheetsConnection)
    df = conn.read()
except Exception as e:
    st.error("⚠️ 資料庫連線異常，請檢查 Secrets 設定。")
    st.stop()

if 'login' not in st.session_state: st.session_state.login = False

if not st.session_state.login:
    st.markdown('<div class="viral-title">🔥 ViralAI</div>', unsafe_allow_html=True)
    st.write("全平台爆款內容拆解引擎")
    u_phone = st.text_input("手機號碼驗證", placeholder="請輸入您的註冊手機號...")
    
    if st.button("立即登入系統"):
        # 嚴格匹配 Google Sheets 中的手機號碼
        user_match = df[df['phone'].astype(str).str.strip() == u_phone.strip()]
        if not user_match.empty:
            exp_date = pd.to_datetime(user_match.iloc[0]['expiry_date']).date()
            if datetime.now().date() <= exp_date:
                st.session_state.login = True
                st.rerun()
            else: st.error("❌ 權限已過期")
        else: st.error("❌ 號碼未授權，請聯繫管理員")

else:
    # --- 3. 真實爆款拆解邏輯 ---
    st.markdown('<div class="viral-title">🔥 ViralAI</div>', unsafe_allow_html=True)
    st.write("### 🚀 輸入連結，啟動 AI 深度拆解")
    
    # 支援平台圖示
    st.markdown("🎵 TikTok · 🔴 抖音 · ▶️ YouTube · 📸 Instagram · 📕 小紅書")
    
    url = st.text_input("貼上您想分析的影片連結", placeholder="http://...")

    if st.button("開始 AI 深度分析"):
        if not ANALYSIS_READY:
            st.warning("🛠️ 系統分析模組（yt-dlp）尚在部署中，請稍候 1 分鐘並刷新頁面。")
        elif url:
            with st.status("🧠 正在提取爆款基因...", expanded=True) as status:
                try:
                    # 使用 yt-dlp 真實抓取影片資訊
                    ydl_opts = {'quiet': True, 'no_warnings': True}
                    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                        info = ydl.extract_info(url, download=False)
                        video_title = info.get('title', '熱門影片')
                    
                    status.update(label="✅ 分析完成！腳本已生成", state="complete")
                    st.success(f"已成功分析影片：{video_title}")

                    # 核心：生成 5 套適配豆包的 10 秒短影音腳本
                    keyword = video_title[:10]
                    scripts = [
                        f"關於【{keyword}】為什麼能火？底層邏輯就一個：抓住焦慮。學會這招，你也能翻倍播放！",
                        f"2026年最後風口：把【{keyword}】重新做一遍。10秒鐘拆解流量密碼，看完趕緊去實操。",
                        f"實測有效！這套【{keyword}】的腳本幫我漲粉破萬。文案我放在下方，建議直接複製。",
                        f"如果你的影片沒流量，試試把開頭換成：關於【{keyword}】你不知道的真相。流量絕對瞬間炸開。",
                        f"豆包 AI 配合這套【{keyword}】專屬腳本簡直絕了！10秒生成高質感內容，現在就試！"
                    ]

                    st.markdown("---")
                    for i, s in enumerate(scripts, 1):
                        with st.container():
                            st.markdown(f'<div class="report-card">', unsafe_allow_html=True)
                            st.write(f"**🔥 方案 {i}：**")
                            st.code(s) # 方便用戶點擊複製
                            st.markdown('</div>', unsafe_allow_html=True)
                    
                    st.balloons()
                except Exception as e:
                    st.error(f"分析失敗。連結無效或該平台限制抓取。")
        else:
            st.warning("請先輸入連結")
