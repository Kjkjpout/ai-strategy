import streamlit as st
import google.generativeai as genai
from youtube_transcript_api import YouTubeTranscriptApi

# 1. 專業商用頁面配置
st.set_page_config(page_title="李大哥 AI 全平台商用戰略系統", layout="wide")

# 2. 核心 AI 引擎配置 (修正 404 型號報錯)
# 這裡使用最穩定的 'gemini-1.5-flash' 名稱
genai.configure(api_key="AIzaSyCfISY4wutzf8TG8hQ10SAMJVj9Sidf4vc")
model = genai.GenerativeModel('gemini-1.5-flash')

# 3. 側邊欄：商業控制台
with st.sidebar:
    st.header("💼 商業專案設定")
    industry = st.selectbox("選擇目標行業", ["股市分析", "數位行銷", "醫美保養", "房地產", "餐飲加盟"])
    product = st.text_input("輸入產品/標的名稱", placeholder="例如：4906正文")
    st.markdown("---")
    strategy_btn = st.button("🔥 生成最強 9 大戰略畫布")

# 4. 主畫面：功能分頁
st.title("🚀 李大哥專屬：Hermes 全平台商用戰略系統")
tab1, tab2 = st.tabs(["🎥 影音連結拆解 (感知模式)", "📊 商業戰略結果 (決策模式)"])

# --- 功能一：全平台影音感知拆解 ---
with tab1:
    st.header("🎥 全平台爆紅密碼分析")
    st.write("支援 YouTube, TikTok, IG, 抖音等連結，分析爆紅邏輯並產出 30 秒腳本。")
    v_url = st.text_input("貼上連結進行採集：", placeholder="https://...", key="v_url")
    
    if st.button("🚀 開始全網感知拆解", key="run_video"):
        if v_url:
            with st.spinner("AI 正在解析全網流量密碼..."):
                try:
                    # YouTube 自動採集邏輯
                    if "youtube.com" in v_url or "youtu.be" in v_url:
                        if "v=" in v_url: video_id = v_url.split("v=")[1].split("&")[0]
                        else: video_id = v_url.split("/")[-1]
                        transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=['zh-TW', 'zh-CN', 'en'])
                        content = " ".join([t['text'] for t in transcript])
                    else:
                        content = f"此為全平台連結分析：{v_url}"

                    prompt = f"請分析此影片的爆紅原因並寫一個30秒腳本：{content[:3000]}"
                    res = model.generate_content(prompt)
                    st.success("✅ 分析完成！")
                    st.markdown(res.text)
                except Exception as e:
                    st.error(f"分析異常，請確認連結與字幕權限。錯誤：{e}")

# --- 功能二：9大商業戰略畫布 ---
with tab2:
    if strategy_btn:
        if product:
            st.header(f"📈 {product} 的 9 大商業戰略結果")
            with st.spinner("AI 決策模型計算中..."):
                try:
                    # 修正 Prompt 邏輯
                    prompt = f"針對行業『{industry}』的『{product}』，輸出 9 個維度的商業戰略，每項用 '###' 開頭。"
                    res = model.generate_content(prompt)
                    
                    # 畫布展示
                    st.success("✅ 戰略生成完成！")
                    st.markdown(res.text)
                except Exception as e:
                    st.error(f"戰略生成失敗：{e}")
    else:
        st.info("👈 請在左側輸入產品名稱並按下按鈕。")
