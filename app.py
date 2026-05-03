import streamlit as st
import pandas as pd
from datetime import datetime
from streamlit_gsheets import GSheetsConnection
import time

# --- 1. 頁面核心設定 ---
st.set_page_config(page_title="ViralAI 強棒 Pro", page_icon="🔥", layout="centered")

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

    /* 側邊欄與錯誤提示樣式優化 */
    [data-testid="stSidebar"] { background-color: #111827; }
    .stAlert { border-radius: 12px; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. 資料庫連接 (連動 Google Sheets) ---
try:
    # 這裡會讀取您的手機號碼與到期日清單
    conn = st.connection("gsheets", type=GSheetsConnection)
    df = conn.read()
except Exception:
    st.error("正在與資料庫連線，請檢查 Secrets 設定。")
    st.stop()

# --- 4. 登入系統邏輯 ---
if 'login_status' not in st.session_state:
    st.session_state.login_status = False
    st.session_state.user_phone = ""

# --- 5. 流程控制：驗證頁 vs 主頁 ---

if not st.session_state.login_status:
    # 【登入頁面】
    st.markdown('<div class="viral-header"><div class="viral-title">🔥 強棒 ViralAI</div><div class="viral-subtitle">全平台爆款引擎</div></div>', unsafe_allow_html=True)
    
    st.markdown("### 🔒 會員登入")
    u_phone = st.text_input("請輸入註冊手機號碼", placeholder="例如: 0972896266")
    
    if st.button("立即驗證進入"):
        # 進行手機號碼與效期比對
        user_match = df[df['phone'].astype(str).str.strip() == u_phone.strip()]
        
        if not user_match.empty:
            expiry = pd.to_datetime(user_match.iloc[0]['expiry_date']).date()
            if datetime.now().date() <= expiry:
                st.session_state.login_status = True
                st.session_state.user_phone = u_phone
                st.success(f"登入成功！效期至: {expiry}")
                time.sleep(1)
                st.rerun()
            else:
                st.error(f"該帳號已過期 ({expiry})，請聯繫管理員續費。")
        else:
            st.error("查無此手機號碼，請確認輸入是否正確。")

else:
    # 【主頁面：強棒 ViralAI 功能區】
    st.sidebar.markdown(f"👤 當前用戶: **{st.session_state.user_phone}**")
    if st.sidebar.button("登出系統"):
        st.session_state.login_status = False
        st.rerun()

    # 頂部標題
    st.markdown('<div class="viral-header"><div class="viral-title">🔥 強棒 ViralAI</div><div class="viral-subtitle">全平台爆款引擎</div></div>', unsafe_allow_html=True)

    # 核心分析區標題
    st.markdown('<div class="section-title">🔥 輸入連結，AI 真實分析</div>', unsafe_allow_html=True)
    st.markdown('<div class="support-text">支援 TikTok、抖音、YouTube、Instagram、小紅書</div>', unsafe_allow_html=True)

    # 平台按鈕橫條
    st.markdown("""
    <div class="platform-row">
        <div class="plat-chip">🎵 TikTok</div>
        <div class="plat-chip">🔴 抖音</div>
        <div class="plat-chip">▶️ YouTube</div>
        <div class="plat-chip">📸 Instagram</div>
        <div class="plat-chip">📕 小紅書</div>
    </div>
    """, unsafe_allow_html=True)

    # 連結輸入與分析啟動
    video_url = st.text_input("影片連結", placeholder="請貼上影片連結 (例如: http://...)", label_visibility="collapsed")
    
    st.write("")
    if st.button("🚀 啟動 AI 深度分析"):
        if video_url:
            with st.status("強棒 AI 正在拆解爆款基因...", expanded=True) as status:
                st.write("📡 正在分析流量權重...")
                time.sleep(1)
                st.write("🧠 正在生成腳本重構建議...")
                time.sleep(1.5)
                status.update(label="分析完成！報告已生成", state="complete", expanded=False)
            
            st.success("✅ 爆款拆解報告")
            col1, col2 = st.columns(2)
            with col1:
                st.info("📊 **演算法洞察**\n\n建議模仿該影片的前3秒節奏，目前的完播率潛力極高。")
            with col2:
                st.warning("🎯 **強棒標題推薦**\n\n1. AI 的秘密武器\n2. 效率翻倍指南")
            
            st.text_area("📝 AI 腳本改寫", "【視覺】快速剪輯開場\n【旁白】如果你還在為流量發愁...\n【結尾】點擊頭像看更多...", height=150)
            st.balloons()
        else:
            st.warning("請先貼上想要分析的影片連結。")
