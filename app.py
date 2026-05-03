import streamlit as st
import pandas as pd
from datetime import datetime
from streamlit_gsheets import GSheetsConnection
import time

# --- 1. 系統核心設定 ---
st.set_page_config(page_title="HookFlow PRO", page_icon="🌊", layout="centered")

# --- 2. 商業級 CSS 美工設計 ---
st.markdown("""
    <style>
    .stApp { background: linear-gradient(160deg, #020617 0%, #0f172a 100%); color: #f8fafc; }
    .main-title { font-size: 45px; font-weight: 800; background: -webkit-linear-gradient(#fff, #94a3b8); -webkit-background-clip: text; -webkit-text-fill-color: transparent; text-align: center; }
    .login-box { background: rgba(255, 255, 255, 0.05); border: 1px solid rgba(255, 255, 255, 0.1); border-radius: 20px; padding: 30px; margin-top: 20px; }
    .stButton > button { background: linear-gradient(90deg, #f97316 0%, #ef4444 100%) !important; color: white !important; border: none !important; border-radius: 12px !important; width: 100% !important; font-weight: bold !important; height: 50px !important; }
    .stTextInput input { background-color: rgba(255, 255, 255, 0.05) !important; color: white !important; border-radius: 10px !important; border: 1px solid rgba(255, 255, 255, 0.2) !important; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. 資料庫連接 (Google Sheets) ---
try:
    conn = st.connection("gsheets", type=GSheetsConnection)
    # 讀取客戶資料表
    df = conn.read()
except Exception as e:
    st.error("資料庫連線失敗，請檢查 Streamlit Secrets 設定。")
    st.stop()

# --- 4. 登入邏輯變數初始化 ---
if 'login_status' not in st.session_state:
    st.session_state.login_status = False
    st.session_state.user_phone = ""

# --- 5. 介面流程：登入頁 vs 功能頁 ---

if not st.session_state.login_status:
    # 【登入頁面】
    st.markdown('<h1 class="main-title">🌊 HookFlow <span style="color:#ef4444;">PRO</span></h1>', unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #94a3b8;'>請輸入註冊手機號碼以開始使用</p>", unsafe_allow_html=True)
    
    with st.container():
        st.markdown('<div class="login-box">', unsafe_allow_html=True)
        input_phone = st.text_input("📱 手機號碼", placeholder="請輸入您的手機號碼...")
        
        if st.button("🔑 立即驗證登入"):
            # 驗證邏輯
            user_data = df[df['phone'].astype(str) == input_phone]
            
            if not user_data.empty:
                expiry_str = user_data.iloc[0]['expiry_date']
                expiry_date = pd.to_datetime(expiry_str).date()
                today = datetime.now().date()
                
                if today <= expiry_date:
                    st.session_state.login_status = True
                    st.session_state.user_phone = input_phone
                    st.success(f"登入成功！歡迎回來，您的服務有效期至：{expiry_date}")
                    time.sleep(1)
                    st.rerun()
                else:
                    st.error(f"您的帳號已於 {expiry_date} 過期，請聯繫管理員續費。")
            else:
                st.error("找不到此手機號碼，請確認是否已註冊。")
        st.markdown('</div>', unsafe_allow_html=True)

else:
    # 【功能頁面 - 已登入】
    st.sidebar.markdown(f"👤 已登入: **{st.session_state.user_phone}**")
    if st.sidebar.button("登出系統"):
        st.session_state.login_status = False
        st.rerun()

    st.markdown('<h1 class="main-title">🌊 HookFlow <span style="color:#ef4444;">PRO</span></h1>', unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #94a3b8;'>AI 驅動的全平台爆款內容拆解引擎</p>", unsafe_allow_html=True)
    st.write("---")

    # 平台選擇
    cols = st.columns(5)
    platforms = ["TikTok", "抖音", "YouTube", "IG", "小紅書"]
    for i, p in enumerate(platforms):
        with cols[i]: st.button(p)

    st.write("")
    url = st.text_input("🔗 貼上您想分析的影片連結", placeholder="https://...")

    if st.button("🚀 啟動 AI 深度分析"):
        if url:
            with st.status("正在召喚專家團進行拆解...", expanded=True) as status:
                st.write("🔍 掃描演算法權重...")
                time.sleep(1)
                st.write("🎬 拆解黃金 3 秒鉤子...")
                time.sleep(1)
                status.update(label="報告已生成！", state="complete", expanded=False)

            st.success("✅ 爆款拆解報告已就緒")
            
            # 報告內容卡片
            c1, c2 = st.columns(2)
            with c1:
                st.info("📊 **演算法洞察**\n\n該影片觸發了搜尋權重池，建議模仿其前3秒的視覺衝擊。")
            with c2:
                st.warning("🎯 **爆款標題建議**\n\n1. AI 變現全攻略\n2. 效率翻倍的秘密\n3. 漲粉十萬的真相")
                
            st.text_area("📝 推薦腳本案 (可複製到豆包)", "【視覺】快速閃過畫面\n【旁白】如果你還在為了流量發愁...\n【結尾】立即點擊...")
            st.balloons()
        else:
            st.error("請提供有效連結！")
