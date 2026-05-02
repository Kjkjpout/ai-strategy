import streamlit as st
import pandas as pd
from datetime import datetime
from streamlit_gsheets import GSheetsConnection

# --- 1. 介面與完全隱藏設定 ---
st.set_page_config(page_title="ViralAI Pro", layout="centered")
st.markdown("""<style>#MainMenu, footer, header, .stDeployButton {visibility: hidden;}</style>""", unsafe_allow_html=True)

# --- 2. 連結 Google Sheets 資料庫 ---
# 注意：這裡會讀取你在 Streamlit Secrets 設定的網址
conn = st.connection("gsheets", type=GSheetsConnection)
df = conn.read()

# --- 3. 登入邏輯 ---
if 'login_status' not in st.session_state:
    st.session_state.login_status = False

if not st.session_state.login_status:
    st.markdown("## 🔒 會員登入系統")
    input_phone = st.text_input("請輸入註冊電話號碼：")
    
    if st.button("確認進入"):
        # 在表格中搜尋電話
        user_row = df[df['phone'].astype(str) == input_phone]
        
        if not user_row.empty:
            expiry_str = user_row.iloc[0]['expiry_date']
            expiry_date = datetime.strptime(expiry_str, "%Y-%m-%d")
            
            if datetime.now() <= expiry_date:
                st.session_state.login_status = True
                st.session_state.user_phone = input_phone
                st.session_state.expiry = expiry_str
                st.rerun()
            else:
                st.error(f"❌ 您的權限已於 {expiry_str} 到期，請聯繫續約。")
        else:
            st.error("⚠️ 查無此號碼，請聯繫管理員授權。")
    st.stop()

# --- 4. 正式功能介面 ---
st.success(f"✅ 歡迎使用！您的授權至：{st.session_state.expiry}")
st.markdown("<h2>🔥 ViralAI 爆款引擎</h2>", unsafe_allow_html=True)
url = st.text_input("貼上分析連結：")
if st.button("🔍 開始深度分析"):
    st.info("分析中...")
    # (此處放之前的分析邏輯內容)
