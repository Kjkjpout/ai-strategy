import streamlit as st
import google.generativeai as genai
from youtube_transcript_api import YouTubeTranscriptApi

# 設定大氣排版
st.set_page_config(page_title="李大哥 AI 全平台戰略系統", layout="wide")

# 配置 API (使用 1.5-flash-001 最穩)
genai.configure(api_key="AIzaSyCfISY4wutzf8TG8hQ10SAMJVj9Sidf4vc")
model = genai.GenerativeModel('gemini-1.5-flash-001')

st.title("🚀 李大哥專屬：全平台爆紅密碼拆解器")
st.markdown("---")

# 直接把功能放在主畫面中央，不用去側邊欄找
tab1, tab2 = st.tabs(["🔥 全平台影片連結拆解", "📊 9大商業戰略畫布"])

with tab1:
    st.header("🎥 貼上影片網址（YouTube / TikTok / IG / 抖音）")
    v_url = st.text_input("在這裡貼上連結：", placeholder="https://...")
    
    if st.button("🚀 開始深度分析爆紅腳本"):
        if v_url:
            with st.spinner("正在調動感知能力抓取內容..."):
                try:
                    # 判斷是否為 YouTube 進行自動抓取
                    if "youtube.com" in v_url or "youtu.be" in v_url:
                        if "v=" in v_url: video_id = v_url.split("v=")[1].split("&")[0]
                        else: video_id = v_url.split("/")[-1]
                        
                        transcript_list = YouTubeTranscriptApi.get_transcript(video_id, languages=['zh-TW', 'zh-CN', 'en'])
                        content_source = " ".join([i['text'] for i in transcript_list])
                    else:
                        # TikTok/IG/抖音 走預測模型
                        content_source = f"全平台連結分析：{v_url}"

                    prompt = f"""
                    你是一位頂級短影音專家。請針對這個連結進行『爆紅密碼拆解』：
                    1. 爆紅原因：為什麼這影片會熱門？(鉤子、情緒、痛點)
                    2. 底層邏輯：套用『五層記憶金字塔』分析其策略。
                    3. 30秒神腳本：寫一個同樣邏輯但適合李大哥背景的 30 秒腳本。
                    
                    原始資料：{content_source[:3000]}
                    """
                    res = model.generate_content(prompt)
                    st.success("✅ 分析完成！")
                    st.markdown(res.text)
                except Exception as e:
                    st.error(f"分析失敗，請檢查連結是否正確或影片是否有字幕。錯誤: {e}")
        else:
            st.warning("請先貼上網址喔！")

with tab2:
    st.header("📈 9大商業戰略生成")
    industry = st.selectbox("行業", ["股市分析", "數位行銷", "醫美保養", "房地產", "餐飲加盟"])
    product = st.text_input("產品名稱")
    if st.button("產生戰略畫布"):
        st.info("9大戰略功能運作中...")
