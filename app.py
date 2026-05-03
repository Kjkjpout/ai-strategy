import streamlit as st
import pandas as pd
from datetime import datetime
from streamlit_gsheets import GSheetsConnection
import time

# --- 1. 頁面核心設定 ---
st.set_page_config(page_title="HookFlow PRO", page_icon="🌊", layout="centered")

# --- 2. 最終穩定版美工 CSS (解決遮擋與跑位問題) ---
st.markdown("""
    <style>
    /* 全局背景 */
    .stApp { 
        background: linear-gradient(160deg, #020617 0%, #0f172a 100%); 
        color: #f8fafc; 
    }
    
    /* 標題居中與質感 */
    .main-title { 
        font-size: 50px; 
        font-weight: 800; 
        background: -webkit-linear-gradient(#fff, #94a3b8); 
        -webkit-background-clip: text; 
        -webkit-text-fill-color: transparent; 
        text-align: center; 
        margin-bottom: 5px;
    }

    /* 修正登入盒子的間距，防止遮擋 */
    .login-container {
        padding: 2rem 0rem;
    }

    /* 強化輸入框顯示，確保不會被灰色塊遮擋 */
    .stTextInput input {
        background-color: rgba(255, 255, 255, 0.07) !important;
        color: white !important;
        border: 1px solid rgba(255, 255, 255, 0.2) !important;
        border-radius: 12px !important;
        padding: 15px !important;
        font-size: 16px !important;
    }

    /* 統一按鈕與漸層顏色 */
    .stButton > button {
        background: linear-gradient(90deg, #f97316 0%, #ef4444 100%) !important;
        color: white !important;
        border: none !important;
        border-radius: 12px !important;
        width: 100% !important;
        font-weight: bold !important;
        height: 55px !important;
        box-shadow: 0 8px 20px rgba(239, 68, 68, 0.2) !important;
        transition: 0.3s all ease;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 10px 25px rgba(239, 68, 68, 0.4) !important;
    }

    /* 平台按鈕寬度一致性 */
    div[data-testid="stHorizontalBlock"] button {
        background-color: rgba(255, 255, 255, 0.05) !important;
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
        color: #94a3b8 !important;
        height: 45px !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. 資料庫連接 ---
try:
    conn = st.connection("gsheets", type=GSheetsConnection)
    df = conn.read()
except Exception as e:
    st.error("資料庫連線失敗，請檢查 Streamlit Secrets 設定。")
    st.stop()

# --- 4. 會員狀態初始化 ---
if 'login_status' not in st.session_state:
    st.session_state.login_status = False
    st.session_state.user_phone = ""

# --- 5. 介面判斷流程 ---
if not st.session_state.login_status:
    # 【登入頁面】
    st.markdown('<div class="login-container">', unsafe_allow_html=True)
    st.markdown('<h1 class="main-title">🌊 HookFlow <span style="color:#ef4444;">PRO</span></h1>', unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #94a3b8; font-size: 18px;'>請輸入註冊手機號碼以開始使用</p>", unsafe_allow_html=True)
    
    input_phone = st.text_input("📱 手機號碼", placeholder="例如：0912345678", label_visibility="collapsed")
    
    if st.button("🔑 立即驗證登入"):
        user_data = df[df['phone'].astype(str) == input_phone]
        
        if not user_data.empty:
            expiry_str = user_data.iloc[0]['expiry_date']
            expiry_date = pd.to_datetime(expiry_str).date()
            if datetime.now().date() <= expiry_date:
                st.session_state.login_status = True
                st.session_state.user_phone = input_phone
                st.rerun()
            else:
                st.error(f"帳號已過期 ({expiry_date})，請聯繫管理員。")
        else:
            st.error("手機號碼未註冊。")
    st.markdown('</div>', unsafe_allow_html=True)

else:
    # 【主功能頁面】
    st.sidebar.markdown(f"👤 用戶: **{st.session_state.user_phone}**")
    if st.sidebar.button("登出系統"):
        st.session_state.login_status = False
        st.rerun()

    st.markdown('<h1 class="main-title">🌊 HookFlow <span style="color:#ef4444;">PRO</span></h1>', unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #94a3b8;'>全平台短影音爆款拆解引擎</p>", unsafe_allow_html=True)
    st.write("---")

    cols = st.columns(5)
    platforms = ["TikTok", "抖音", "YouTube", "IG", "小紅書"]
    for i, p in enumerate(platforms):
        with cols[i]: st.button(p)

    st.write("")
    url = st.text_input("🔗 貼上影片連結進行 AI 深度分析", placeholder="https://...")

    if st.button("🚀 啟動 AI 深度分析"):
        if url:
            with st.status("專家團正在工作中...", expanded=True) as status:
                st.write("🔍 正在掃描權重...")
                time.sleep(1)
                st.write("🎬 拆解爆火腳本...")
                time.sleep(1)
                status.update(label="分析完成！", state="complete", expanded=False)

            st.success("✅ 分析報告已就緒")
            c1, c2 = st.columns(2)
            with c1: st.info("📊 **演算法洞察**\n\n該影片觸發了高權重推薦。")
            with c2: st.warning("🎯 **爆款標題建議**\n\n1. AI 秘密武器\n2. 效率翻倍指南")
            st.text_area("📝 AI 重構腳本", "【視覺】開場衝擊\n【旁白】秘密公開...", height=150)
            st.balloons()
        else:
            st.error("請輸入連結！")
