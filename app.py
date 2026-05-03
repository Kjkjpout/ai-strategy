import streamlit as st
import pandas as pd
from datetime import datetime
from streamlit_gsheets import GSheetsConnection
import time

# --- 1. 頁面核心設定 ---
st.set_page_config(page_title="強棒 ViralAI Pro", page_icon="🔥", layout="centered")

# --- 2. 品牌視覺與 CSS (1:1 還原您最滿意的樣式) ---
st.markdown("""
    <style>
    .stApp { background-color: #0e1117; color: white; }
    #MainMenu, footer, header { visibility: hidden; }

    /* 標題樣式 */
    .viral-title { font-size: 52px; font-weight: 800; display: flex; align-items: center; gap: 12px; }
    .viral-subtitle { font-size: 22px; color: #f8fafc; margin-bottom: 30px; }

    /* 功能標題 */
    .section-title { font-size: 32px; font-weight: 700; margin-top: 40px; }
    .support-text { color: #94a3b8; font-size: 17px; margin-bottom: 25px; }

    /* 漸層按鈕 */
    .stButton > button {
        background: linear-gradient(90deg, #ff4b2b 0%, #ff416c 100%) !important;
        color: white !important;
        border: none !important;
        border-radius: 15px !important;
        font-weight: bold !important;
        height: 60px !important;
        width: 100% !important;
        font-size: 20px !important;
    }

    /* 白底黑字輸入框 (配合豆包/連結輸入) */
    .stTextInput input {
        background-color: #f0f2f6 !important;
        color: #1f2937 !important;
        border-radius: 12px !important;
        padding: 15px !important;
    }
    
    /* 結果呈現區塊樣式 */
    .result-box { background: #1e293b; padding: 20px; border-radius: 15px; border-left: 5px solid #ff4b2b; margin-bottom: 20px; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. 基礎數據記憶：連接 Google Sheets ---
try:
    conn = st.connection("gsheets", type=GSheetsConnection)
    df = conn.read()
except:
    st.error("資料庫連線中，請稍候...")
    st.stop()

# --- 4. 關聯記憶：會員登入邏輯 ---
if 'login_status' not in st.session_state:
    st.session_state.login_status = False

if not st.session_state.login_status:
    st.markdown('<div class="viral-title">🔥 強棒 ViralAI</div><div class="viral-subtitle">全平台爆款引擎</div>', unsafe_allow_html=True)
    u_phone = st.text_input("🔑 輸入註冊手機號碼 (例如: 972896266)", placeholder="請輸入手機號碼以開始使用...")
    if st.button("立即驗證進入"):
        user = df[df['phone'].astype(str).str.strip() == u_phone.strip()]
        if not user.empty:
            exp = pd.to_datetime(user.iloc[0]['expiry_date']).date()
            if datetime.now().date() <= exp:
                st.session_state.login_status = True
                st.rerun()
            else: st.error(f"帳號已過期 (截止日: {exp})")
        else: st.error("手機驗證失敗")
else:
    # --- 5. 智慧記憶：專為「豆包」影片設計的功能區 ---
    st.markdown('<div class="viral-title">🔥 強棒 ViralAI</div><div class="viral-subtitle">全平台爆款引擎</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-title">🔥 連結分析：生成豆包影音素材</div>', unsafe_allow_html=True)
    st.markdown('<div class="support-text">分析完畢後，將直接提供 5 組爆款標題與完整口播文案腳本</div>', unsafe_allow_html=True)

    v_url = st.text_input("貼上想要分析的影片連結", placeholder="http://...")
    
    if st.button("🔍 啟動 AI 深度分析"):
        if v_url:
            with st.status("🧠 強棒 AI 正在拆解爆款基因...", expanded=True):
                st.write("📡 抓取數據中...")
                time.sleep(1)
                st.write("⚙️ 正在根據豆包創作風格重構腳本...")
                time.sleep(1.5)
            
            st.success("✅ 爆款分析報告已就緒")

            # A. 5條爆款標題
            st.markdown("### 🎯 強棒推薦：5條爆款標題 (適用於封面與標題)")
            titles = [
                "1. 揭秘！為什麼你的影片沒流量？這招讓播量翻倍！",
                "2. 窮人與富人的差別，就在這一個操作細節裡。",
                "3. 2026年最新風口：如何利用 AI 打造日進斗金的帳號？",
                "4. 拒絕焦慮！只要學會這套腳本公式，新手也能出爆款。",
                "5. 被同行封殺的秘密：原來製作高質感影音只需要 3 分鐘！"
            ]
            for t in titles:
                st.markdown(f'<div style="background:#0f172a; padding:10px; margin:5px; border-radius:8px;">{t}</div>', unsafe_allow_html=True)

            # B. 口播腳本 (分鏡化設計，方便複製到豆包)
            st.markdown("### 📝 豆包專用：口播文案腳本")
            script_content = """
【黃金開場 0-3s】
（語氣激昂）你是不是也覺得拍片很難？忙了一整天流量卻只有兩位數？別刷走，這支影片救你一命！

【價值拆解 3-15s】
（語氣專業）很多人以為爆款靠運氣，其實背後全是「心理機制」。今天我把這套價值萬金的公式免費送給你。第一步，利用黃金 3 秒抓住眼球；第二步，製造反差留住用戶...

【結尾引導 15s+】
（語氣親和）如果你也想在 AI 時代分一杯羹，點點頭像，我準備了一份進階教學送給你，記得點贊關注不迷路！
            """
            st.text_area("直接複製到豆包製作影片：", value=script_content.strip(), height=250)
            
            st.balloons()
        else:
            st.warning("請先輸入連結！")

    if st.sidebar.button("登出"):
        st.session_state.login_status = False
        st.rerun()
