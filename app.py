import streamlit as st
import google.generativeai as genai
from youtube_transcript_api import YouTubeTranscriptApi

# 設定大氣排版
st.set_page_config(page_title="李大哥 AI 萬能戰略大腦", layout="wide")

# 配置 API (使用最穩定的 001 版本)
genai.configure(api_key="AIzaSyCfISY4wutzf8TG8hQ10SAMJVj9Sidf4vc")
model = genai.GenerativeModel('gemini-1.5-flash-001')

st.title("🚀 李大哥專屬：Hermes 級全平台戰略大腦")
st.markdown("---")

with st.sidebar:
    st.header("⚙️ 模式切換")
    mode = st.radio("選擇功能", ["YouTube 爆紅拆解", "9大商業戰略"])
    st.markdown("---")
    
    if mode == "YouTube 爆紅拆解":
        yt_url = st.text_input("貼上影片連結", placeholder="https://www.youtube.com/watch?v=...")
        st.info("💡 貼上連結後，AI 會自動拆解爆紅原因並寫腳本。")
    else:
        industry = st.selectbox("選擇行業", ["股市分析", "數位行銷", "醫美保養", "房地產", "餐飲加盟"])
        product = st.text_input("輸入產品/標的", placeholder="例如：1618合機技術分析")
    
    generate_btn = st.button("🔥 開始深度分析")

def get_yt_id(url):
    if "v=" in url: return url.split("v=")[1].split("&")[0]
    elif "youtu.be/" in url: return url.split("youtu.be/")[1]
    return None

if generate_btn:
    if mode == "YouTube 爆紅拆解" and yt_url:
        with st.spinner("正在調動感知能力抓取內容..."):
            try:
                video_id = get_yt_id(yt_url)
                transcript_list = YouTubeTranscriptApi.get_transcript(video_id, languages=['zh-TW', 'zh-CN', 'en'])
                full_text = " ".join([i['text'] for i in transcript_list])
                
                prompt = f"""
                你是一位短影音爆紅專家。請根據『五層記憶金字塔』邏輯分析此內容：
                1. 爆紅拆解：為什麼這影片會熱門？(分析情緒、鉤子、痛點)
                2. 核心架構：它如何抓住用戶注意力？
                3. 腳本重製：請幫我寫一個 30 秒的腳本，模仿其爆紅邏輯但要適合李大哥的數位創業背景。
                
                內容原文：{full_text[:3500]}
                """
                res = model.generate_content(prompt)
                st.success("✅ 爆紅密碼拆解完成！")
                st.markdown(res.text)
            except Exception as e:
                st.error(f"此影片可能未開啟字幕或限制抓取。錯誤提示: {e}")

    elif mode == "9大商業戰略" and product:
        with st.spinner("AI 正在計算 9 大戰略畫布..."):
            # 原本的 9 大戰略生成邏輯
            prompt = f"請針對『{industry}』的『{product}』，輸出 9 個維度的戰略，每個維度用 '###' 開頭..."
            res = model.generate_content(prompt)
            parts = res.text.split('###')
            
            # 顯示 3x3 畫布
            col1, col2, col3 = st.columns(3)
            with col1:
                st.info(f"### 1. 使用情境\n{parts[1] if len(parts)>1 else '數據中'}")
                st.info(f"### 2. 根源痛點\n{parts[2] if len(parts)>2 else '數據中'}")
                st.info(f"### 3. 使用頻率\n{parts[3] if len(parts)>3 else '數據中'}")
            with col2:
                st.success(f"### 4. 回訪觸發\n{parts[4] if len(parts)>4 else '數據中'}")
                st.success(f"### 5. 收費觸發\n{parts[5] if len(parts)>5 else '數據中'}")
                st.success(f"### 6. 牽引能力\n{parts[6] if len(parts)>6 else '數據中'}")
            with col3:
                st.warning(f"### 7. 門檻行動\n{parts[7] if len(parts)>7 else '數據中'}")
                st.warning(f"### 8. 依賴風險\n{parts[8] if len(parts)>8 else '數據中'}")
                st.warning(f"### 9. 停止訊號\n{parts[9] if len(parts)>9 else '數據中'}")
