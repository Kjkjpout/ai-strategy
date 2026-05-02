import streamlit as st
import google.generativeai as genai
from youtube_transcript_api import YouTubeTranscriptApi

# 設定大氣排版
st.set_page_config(page_title="李大哥 AI 全平台戰略系統", layout="wide")

# 配置 API
genai.configure(api_key="AIzaSyCfISY4wutzf8TG8hQ10SAMJVj9Sidf4vc")
model = genai.GenerativeModel('gemini-1.5-flash-001')

# --- 1. 左邊側邊欄 (恢復您原本的功能) ---
with st.sidebar:
    st.header("📋 項目設定")
    industry = st.selectbox("選擇行業", ["股市分析", "數位行銷", "醫美保養", "房地產", "餐飲加盟"])
    product = st.text_input("輸入產品/標的", placeholder="例如：1618合機技術分析")
    st.markdown("---")
    strategy_btn = st.button("🔥 生成 9 大戰略畫布")

# --- 2. 中間主畫面 (全平台貼網址功能) ---
st.title("🚀 李大哥專屬：全平台爆紅密碼拆解器")
st.markdown("---")

# 主畫面的標籤頁
tab1, tab2 = st.tabs(["🎥 影音連結拆解 (YT/抖音/IG)", "📊 商業戰略結果"])

with tab1:
    st.header("貼上影片網址")
    v_url = st.text_input("在這裡貼上連結：", placeholder="https://...")
    
    if st.button("🚀 開始深度分析爆紅腳本"):
        if v_url:
            with st.spinner("正在調動感知能力抓取內容..."):
                try:
                    # YouTube 自動抓取邏輯
                    if "youtube.com" in v_url or "youtu.be" in v_url:
                        if "v=" in v_url: video_id = v_url.split("v=")[1].split("&")[0]
                        else: video_id = v_url.split("/")[-1]
                        transcript_list = YouTubeTranscriptApi.get_transcript(video_id, languages=['zh-TW', 'zh-CN', 'en'])
                        content_source = " ".join([i['text'] for i in transcript_list])
                    else:
                        content_source = f"平台連結分析：{v_url}"

                    prompt = f"分析此內容爆紅邏輯並寫一個30秒神腳本：{content_source[:3000]}"
                    res = model.generate_content(prompt)
                    st.success("✅ 分析完成！")
                    st.markdown(res.text)
                except Exception as e:
                    st.error(f"分析失敗: {e}")
        else:
            st.warning("請先貼上網址喔！")

with tab2:
    if strategy_btn and product:
        st.header(f"📈 {product} 的 9 大商業戰略")
        # 這裡會跑原本的戰略生成代碼
        res = model.generate_content(f"針對『{industry}』的『{product}』產生9個維度戰略...")
        st.markdown(res.text)
    else:
        st.info("請在左側輸入資料並點擊『生成 9 大戰略畫布』")
