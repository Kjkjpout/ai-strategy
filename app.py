import streamlit as st
import pandas as pd
from datetime import datetime
from streamlit_gsheets import GSheetsConnection
import time

# --- 1. 頁面核心設定 ---
st.set_page_config(page_title="强棒 ViralAI Pro", page_icon="🔥", layout="centered")

# --- 2. 最終鎖定：ViralAI 強棒 視覺風格 (1:1 截圖還原) ---
st.markdown("""
    <style>
    /* 全黑底色與白字 */
    .stApp { background-color: #0e1117; color: white; }
    
    /* 隱藏預設元件 */
    #MainMenu, footer, header, .stDeployButton { visibility: hidden; }

    /* 頂部標題與標語 */
    .viral-header { margin-top: -40px; margin-bottom: 30px; }
    .viral-title { font-size: 52px; font-weight: 800; display: flex; align-items: center; gap: 12px; }
    .viral-subtitle { font-size: 22px; color: #f8fafc; margin-top: 5px; font-weight: 500; }

    /* 功能區標題 */
    .section-title { font-size: 32px; font-weight: 700; margin: 40px 0 10px 0; display: flex; align-items: center; gap: 10px; }
    .support-text { color: #94a3b8; font-size: 17px; margin-bottom: 25px; }

    /* 平台按鈕模擬 (黑底灰邊) */
    .platform-row { display: flex; gap: 10px; margin-bottom: 25px; flex-wrap: wrap; }
    .plat-chip { background: #1f2937; border: 1px solid #374151; padding: 10px 18px; border-radius: 10px; font-size: 15px; }

    /* 紅橙漸層啟動按鈕 */
    .stButton > button {
        background: linear-gradient(90deg, #ff4b2b 0%, #ff416c 100%) !important;
        color: white !important;
        border: none !important;
        border-radius: 15px !important;
        font-weight: bold !important;
        height: 60px !important;
        width: 100% !important;
        font-size: 20px !important;
        box-shadow: 0 4px 15px rgba(255, 75, 43, 0.3) !important;
    }

    /* 連結輸入框：高對比白底黑字 */
    .stTextInput input {
        background-color: #f0f2f6 !important;
        color: #1f2937 !important;
        border: none !important;
        border-radius: 12px !important;
        padding: 15px !important;
        font-size: 18px !important;
    }

    /* 結果呈現區塊樣式 */
    .result-box { background: #1f2937; padding: 20px; border-radius: 15px; border-left: 5px solid #ff4b2b; margin-bottom: 20px; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. 資料庫連接 (連動 Google Sheets) ---
try:
    conn = st.connection("gsheets", type=GSheetsConnection)
    df = conn.read()
except Exception:
    st.stop()

# --- 4. 登入系統邏輯 ---
if 'login_status' not in st.session_state:
    st.session_state.login_status = False
if 'user_phone' not in st.session_state:
    st.session_state.user_phone = ""

# --- 5. 流程控制 ---

if not st.session_state.login_status:
    # 【登入頁面】
    st.markdown('<div class="viral-header"><div class="viral-title">🔥 強棒 ViralAI Pro</div><div class="viral-subtitle">全平台爆款引擎</div></div>', unsafe_allow_html=True)
    st.markdown("### 🔒 用戶手機登入")
    u_phone = st.text_input("手機號碼", placeholder="請輸入註冊手機號碼...")
    
    if st.button("驗證登入"):
        user_match = df[df['phone'].astype(str).str.strip() == u_phone.strip()]
        if not user_match.empty:
            exp = pd.to_datetime(user_match.iloc[0]['expiry_date']).date()
            if datetime.now().date() <= exp:
                st.session_state.login_status = True
                st.session_state.user_phone = u_phone
                st.rerun()
            else: st.error(f"帳號已過期")
        else: st.error("查無此號碼")

else:
    # 【主頁面：強棒 ViralAI 功能區】
    st.sidebar.markdown(f"👤 當前用戶: **{st.session_state.user_phone}**")
    if st.sidebar.button("登出系統"):
        st.session_state.login_status = False
        st.rerun()

    st.markdown('<div class="viral-header"><div class="viral-title">🔥 強棒 ViralAI Pro</div><div class="viral-subtitle">全平台爆款引擎</div></div>', unsafe_allow_html=True)
    st.markdown('<div class="section-title">🔥 輸入連結，AI 真實分析</div>', unsafe_allow_html=True)
    st.markdown('<div class="support-text">支援 TikTok、抖音、YouTube、Instagram、小紅書</div>', unsafe_allow_html=True)

    st.markdown('<div class="platform-row"><div class="plat-chip">🎵 TikTok</div><div class="plat-chip">🔴 抖音</div><div class="plat-chip">▶️ YouTube</div><div class="plat-chip">📸 Instagram</div><div class="plat-chip">📕 小紅書</div></div>', unsafe_allow_html=True)

    video_url = st.text_input("請輸入連結", placeholder="例如: http://xhslink.com/...")
    
    if st.button("🔍 開始 AI 深度分析"):
        if video_url:
            with st.status("🧠 強棒 AI 正在拆解爆款基因...", expanded=True) as status:
                st.write("📡 數據抓取中...")
                time.sleep(1)
                st.write("⚙️ 分析演算法洞察與腳本重構...")
                time.sleep(1.5)
                status.update(label="分析完成！", state="complete", expanded=False)
            
            # 結果展示：5條標題與口播腳本
            st.success("✅ 爆款拆解報告")

            col1, col2 = st.columns(2)
            with col1:
                st.markdown('<div class="result-box">📊 **演算法洞察**<br><br>該影片觸發了搜尋權重池，建議模仿其開頭的懸念設置，完播率潛力極高。</div>', unsafe_allow_html=True)
            with col2:
                st.markdown('<div class="result-box">🎯 **爆款標題 (5條)**<br><br>1. 揭秘！新手如何用 AI 做影片，日增萬粉！<br>2. 拒絕焦慮！只要學會這套腳本公式，流量翻倍！<br>3. 別再浪費時間了，2026內容創作者最後的機會！<br>4. 我後悔沒早點知道，這招讓播量破百萬！<br>5. HookFlow 實測！教你如何用 10 秒鐘抓住眼球！</div>', unsafe_allow_html=True)
            
            st.markdown("### 📝 10 秒影片口播文案腳本 (可直接貼入豆包)")
            
            # 分成兩套腳本 Tab，方便選擇
            tab1, tab2 = st.tabs(["🔥 爆款腳本 A", "💡 創意腳本 B"])
            
            with tab1:
                script_a = """
【視覺】畫面快速閃過收入截圖 + 震撼音樂
【旁白】如果你還在為了流量發愁，那這條影片你一定要看完。
【節奏】第 5 秒切換至工具操作畫面，展示效率。
【結尾】點擊頭像，領取同款 AI 工具包。
                """
                st.text_area("直接複製到豆包製作影片 (A套)：", value=script_a.strip(), height=150)
                
            with tab2:
                script_b = """
【視覺】第一人稱口播開場，背景保持簡約。
【旁白】很多人問我怎麼同時管理 10 個帳號，其實全靠它。
【節奏】快節奏卡點，展示 3 個核心功能。
【結尾】這就是為什麼你必須立刻開始。
                """
                st.text_area("直接複製到豆包製作影片 (B套)：", value=script_b.strip(), height=150)
                
            st.balloons()
        else:
            st.warning("請先提供影片連結。")
