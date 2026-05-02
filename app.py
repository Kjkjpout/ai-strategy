import streamlit as st
import google.generativeai as genai
from youtube_transcript_api import YouTubeTranscriptApi

# 1. 頁面基本配置 (讓畫面寬一點，好操作)
st.set_page_config(page_title="李大哥 AI 全平台戰略系統", layout="wide")

# 2. API 配置 (修正 404 報錯問題)
genai.configure(api_key="AIzaSyCfISY4wutzf8TG8hQ10SAMJVj9Sidf4vc")
model = genai.GenerativeModel('gemini-1.5-flash-001')

# --- 3. 【左側選單】恢復原本的功能 ---
with st.sidebar:
    st.header("📋 項目設定")
    industry = st.selectbox("選擇行業", ["股市分析", "數位行銷", "醫美保養", "房地產", "餐飲加盟"])
    product = st.text_input("輸入產品/標的 (必填)", placeholder="例如：1618合機技術分析")
    st.markdown("---")
    # 這是您原本生成 9 大戰略的按鈕
    strategy_btn = st.button("🔥 生成 9 大戰略畫布")

# --- 4. 【中間主畫面】貼連結的功能 ---
st.title("🚀 李大哥專屬：全平台爆紅密碼拆解器")
st.info("左側可以選股市分析，中間可以貼影片連結，兩不耽誤！")

# 使用標籤頁來區分「影片分析」和「戰略結果」
tab1, tab2 = st.tabs(["🎥 影音連結拆解 (YT/抖音/IG)", "📊 商業戰略結果回報"])

with tab1:
    st.header("貼上影片網址")
    v_url = st.text_input("在這裡貼上連結：", placeholder="https://...", key="v_url_input")
    
    if st.button("🚀 開始深度分析爆紅腳本", key="analyze_btn"):
        if v_url:
            with st.spinner("正在抓取內容中..."):
                try:
                    # YouTube 抓取邏輯
                    if "youtube.com" in v_url or "youtu.be" in v_url:
                        if "v=" in v_url: video_id = v_url.split("v=")[1].split("&")[0]
                        else: video_id = v_url.split("/")[-1]
                        transcript_list = YouTubeTranscriptApi.get_transcript(video_id, languages=['zh-TW', 'zh-CN', 'en'])
                        content_source = " ".join([i['text'] for i in transcript_list])
                    else:
                        content_source = f"全平台連結分析請求：{v_url}"

                    prompt = f"""
                    你是一位專業策略顧問。請針對以下內容分析其『爆紅邏輯』並為李大哥寫一個30秒的腳本：
                    內容來源：{content_source[:3000]}
                    """
                    res = model.generate_content(prompt)
                    st.success("✅ 分析完成！")
                    st.markdown(res.text)
                except Exception as e:
                    st.error(f"分析失敗，請確認連結是否正確。錯誤訊息: {e}")
        else:
            st.warning("請先輸入連結喔！")

with tab2:
    # 這裡顯示左側按鈕點擊後的結果
    if strategy_btn:
        if product:
            st.header(f"📈 {product} 的 9 大商業戰略結果")
            with st.spinner("戰略生成中..."):
                try:
                    res = model.generate_content(f"針對『{industry}』的產品『{product}』，以專業顧問角度產生9個維度的商業戰略...")
                    st.markdown(res.text)
                except Exception as e:
                    st.error(f"生成失敗: {e}")
        else:
            st.error("⚠️ 請先在左側輸入『產品/標的』名稱再點擊按鈕！")
    else:
        st.write("👈 請在左側輸入資料並按下按鈕，結果會顯示在這裡。")
