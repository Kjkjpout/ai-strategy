import streamlit as st
import time

# --- 視覺配置 (對應滿配視覺感) ---
st.set_page_config(page_title="Hermes 滿配 AI 影片自動化工廠", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #050505; color: #ffffff; }
    .stButton>button { 
        background: #ff4b4b; color: white; width: 100%; border-radius: 8px; 
        height: 3.5em; font-size: 18px; font-weight: bold; border: none;
    }
    .stTextInput>div>div>input { background-color: #111; color: #ffffff; border: 1px solid #444; }
    </style>
    """, unsafe_allow_html=True)

# --- 1. 使用情境與標題 (戰略九宮格 Step 1) ---
st.title("🛡️ Hermes 滿配 AI 影片自動化工廠")
st.caption("基於九大核心戰略規劃架構 (Define User Context & Strategy)")

# --- 2. 門檻行動：輸入與按鈕 (戰略九宮格 Step 7) ---
# 確保輸入框與按鈕在同一區塊，方便操作
with st.container():
    st.markdown("### **1. 使用情境 (Define User Context)**")
    video_url = st.text_input("🔗 貼上爆款種子連結，讓 AI 解析其背後戰略：", placeholder="https://youtu.be/...")
    
    # 搜尋按鈕直接放在輸入框下方
    if st.button("🚀 啟動全鏈路生產與自動分發"):
        if not video_url:
            st.error("李大哥，請先填入連結才能啟動搜尋！")
        else:
            with st.status("🏗️ 戰略引擎啟動中...", expanded=True) as status:
                st.write("🔍 正在執行 Step 2: 根源痛點拆解...")
                time.sleep(0.5)
                st.write("🧠 正在執行 Step 4: 回訪觸發邏輯分析...")
                time.sleep(0.5)
                st.write("🎨 正在執行 Step 7: 門檻內容生成...")
                time.sleep(0.5)
                status.update(label="✅ 戰略重生腳本已就位", state="complete")

            # --- 3. 重生方案輸出 (對應 Step 8: 建立依賴) ---
            st.markdown("---")
            st.subheader("🎬 重生腳本 (30秒高轉化版)")
            st.code(f"已成功分析連結：{video_url}\n\n【0-5s】開頭鉤子：反常識對比\n【5-25s】情緒拉扯：由焦慮引向解決方案\n【25-30s】強效行動：點擊左下角獲取系統", language="text")

# --- 4. 配置模組預覽 (對應 Hermes 五大模組) ---
col1, col2, col3, col4 = st.columns(4)
with col1: st.info("👤 身份與記憶")
with col2: st.info("👁️ 感知能力")
with col3: st.info("🗣️ 表達能力")
with col4: st.info("📊 效率與成本")

st.divider()
st.caption("© 2026 李大哥 AI 戰略研究所 | 商業版權所有")
