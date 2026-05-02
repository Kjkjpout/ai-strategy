import streamlit as st
import google.generativeai as genai
from youtube_transcript_api import YouTubeTranscriptApi

# 設定大氣排版
st.set_page_config(page_title="李大哥 AI 全平台戰略系統", layout="wide")

# 配置 API
genai.configure(api_key="AIzaSyCfISY4wutzf8TG8hQ10SAMJVj9Sidf4vc")
model = genai.GenerativeModel('gemini-1.5-flash-001')

st.title("🚀 李大哥專屬：全平台（TikTok/IG/YT/抖音）爆紅密碼拆解器")
st.markdown("---")

with st.sidebar:
    st.header("⚙️ 模式切換")
    mode = st.radio("選擇功能", ["全平台影片拆解", "9大商業戰略"])
    st.markdown("---")
    
    if mode == "全平台影片拆解":
        platform = st.selectbox("選擇平台", ["YouTube", "TikTok", "Instagram", "抖音", "其他短影音"])
        v_url = st.text_input("貼上影片連結", placeholder="請在此貼上網址...")
        st.info("💡 提示：YouTube 可自動抓取；其餘平台 AI 將針對該標題與內容進行爆紅邏輯重構。")
    else:
        industry = st.selectbox("選擇行業", ["股市分析", "數位行銷", "醫美保養", "房地產", "餐飲加盟"])
        product = st.text_input("輸入產品/標的")
    
    generate_btn = st.button("🔥 開始深度分析")

def get_yt_id(url):
    if "v=" in url: return url.split("v=")[1].split("&")[0]
    elif "youtu.be/" in url: return url.split("youtu.be/")[1]
    return None

if generate_btn:
    if mode == "全平台影片拆解" and v_url:
        with st.spinner(f"正在對調動『五層記憶金字塔』分析 {platform} 內容..."):
            try:
                # YouTube 專用抓取邏輯
                if platform == "YouTube":
                    video_id = get_yt_id(v_url)
                    transcript_list = YouTubeTranscriptApi.get_transcript(video_id, languages=['zh-TW', 'zh-CN', 'en'])
                    content_source = " ".join([i['text'] for i in transcript_list])
                else:
                    # 其他平台使用爆紅趨勢預測邏輯
                    content_source = f"平台：{platform}，連結：{v_url}"

                prompt = f"""
                你是一位全球頂級短影音專家。請針對這個來自 {platform} 的內容進行『爆紅密碼拆解』：
                1. 爆紅拆解：分析此平台的算法偏好，這影片為何會爆？(鉤子、情緒、痛點)
                2. 爆紅模型：套用『智慧記憶金字塔』，總結其成功的底層邏輯。
                3. 30秒神腳本：請幫李大哥寫一個同樣會爆的 30 秒腳本，要包含：[黃金3秒開頭]、[中間反轉]、[結尾行動指令]。
                
                參考來源：{content_source}
                """
                res = model.generate_content(prompt)
                st.success(f"✅ {platform} 爆紅分析完成！")
                st.markdown(res.text)
                
            except Exception as e:
                st.error(f"分析失敗。若是 YouTube 請確認字幕；其餘平台請確保連結正確。錯誤: {e}")

    elif mode == "9大商業戰略" and product:
        # 原本的 9 大戰略顯示邏輯 (略)
        st.info("9大戰略生成中...")
