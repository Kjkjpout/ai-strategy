import os; os.environ['STREAMLIT_SERVER_LIVERELOAD'] = 'true'
import streamlit as st
import google.generativeai as genai
from youtube_transcript_api import YouTubeTranscriptApi

# 1. 頁面基礎設定
st.set_page_config(page_title="李大哥商用戰略大腦", layout="wide")

# 2. 核心引擎 (鎖定最穩定的通用名稱)
# 這次直接用 'gemini-1.5-flash'，不帶後綴，保證 Google 伺服器認得出！
genai.configure(api_key="AIzaSyCfISY4wutzf8TG8hQ10SAMJVj9Sidf4vc")
model = genai.GenerativeModel('gemini-1.5-flash')

# --- 3. 側邊控制欄 ---
with st.sidebar:
    st.header("💼 專案設定")
    industry = st.selectbox("行業別", ["股市分析", "數位行銷", "情感諮詢", "一般商業"])
    product = st.text_input("產品名稱", value="4906 合機技術分析")
    st.markdown("---")
    strategy_btn = st.button("🔥 啟動商用戰略分析")

# --- 4. 主功能區 ---
st.title("🚀 李大哥專屬：全平台商用戰略系統")
tab1, tab2 = st.tabs(["🎥 影音拆解", "📊 戰略結果"])

with tab1:
    v_url = st.text_input("貼上連結：", value="https://v.douyin.com/Fpipatcxwyc/")
    if st.button("🚀 開始感知分析"):
        with st.spinner("AI 正在連接大腦..."):
            try:
                # 簡單的情感分析 Prompt，保證快速輸出
                prompt = f"分析此連結的爆紅邏輯與 30 秒腳本：{v_url}"
                res = model.generate_content(prompt)
                st.success("✅ 分析完成")
                st.markdown(res.text)
            except Exception as e:
                st.error(f"系統暫時斷線，請稍後重試。錯誤：{e}")

with tab2:
    if strategy_btn:
        with st.spinner("生成 9 大戰略中..."):
            try:
                prompt = f"針對『{product}』，以專業顧問角度輸出 9 個維度的商用戰略。"
                res = model.generate_content(prompt)
                st.markdown(res.text)
            except Exception as e:
                st.error(f"生成失敗：{e}")
