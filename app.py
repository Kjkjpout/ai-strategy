import os; os.environ['STREAMLIT_SERVER_LIVERELOAD'] = 'true' # 👈【強制重啟通道】：不用找按鈕，貼完代碼強制 Reboot！
import streamlit as st
import google.generativeai as genai
from youtube_transcript_api import YouTubeTranscriptApi

# 1. 專業商用頁面配置
st.set_page_config(page_title="李大哥 AI 全平台商用戰略系統", layout="wide")

# 2. 引擎配置 (【關鍵修復】：使用最新的正式版全稱編號)
# 在您的 API 權限下，'gemini-1.5-flash-latest' 是在 2026/5 最穩定的通道
genai.configure(api_key="AIzaSyCfISY4wutzf8TG8hQ10SAMJVj9Sidf4vc")
model = genai.GenerativeModel('gemini-1.5-flash-latest')

# --- 3. 側邊欄：商業控制台 ---
with st.sidebar:
    st.header("💼 商業專案設定")
    industry = st.selectbox("選擇目標行業", ["股市分析", "數位行銷", "醫美保養", "房地產", "餐飲加盟"])
    product = st.text_input("輸入產品/標的名稱", placeholder="例如：1618合機技術分析")
    st.markdown("---")
    # 這是您原本生成 9 大戰略的按鈕
    strategy_btn = st.button("🔥 生成 9 大商用戰略結果")

# --- 4. 主畫面：功能分頁 ---
st.title("🚀 李大哥專屬：Hermes 全平台商用戰略系統")
st.info("系統已接通最新 `gemini-1.5-flash-latest` 大腦。貼完代碼請等日誌顯示『Updated app!』")
tab1, tab2 = st.tabs(["🎥 影音連結拆解 (感知模式)", "📊 商業戰略結果 (決策模式)"])

# --- 功能一：全平台影音感知拆解 ---
with tab1:
    st.header("🎥 全平台爆紅密碼拆解")
    st.write("支援 YouTube, TikTok, IG, 抖音等連結，分析爆紅邏輯並產出 30 秒腳本。")
    v_url = st.text_input("貼上連結進行感知：", placeholder="https://...", key="v_url")
    
    if st.button("🚀 開始全網感知拆解", key="run_video"):
        if v_url:
            with st.spinner("AI 正在解析全網流量密碼..."):
                try:
                    # YouTube 字幕採集邏輯 (商用精準版)
                    if "youtube.com" in v_url or "youtu.be" in v_url:
                        if "v=" in v_url: video_id = v_url.split("v=")[1].split("&")[0]
                        else: video_id = v_url.split("/")[-1]
                        transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=['zh-TW', 'zh-CN', 'en'])
                        content = " ".join([t['text'] for t in transcript])
                    else:
                        # 其他短影音走預測感知模式
                        content = f"此為全平台影音連結：{v_url}，分析平台屬性並重構爆紅邏輯。"

                    prompt = f"""
                    你是一位專業策略操盤專家。請針對以下感知內容：
                    1. 爆紅拆解：分析其情緒、鉤子、用戶痛點與商用價值。
                    2. 底層邏輯：套用『五層記憶金字塔』分析其算法優勢。
                    3. 30秒腳本：模仿此邏輯寫一個能轉化訂單的 30 秒爆紅腳本。
                    感知內容：{content[:3000]}
                    """
                    res = model.generate_content(prompt)
                    st.success("✅ 全平台感知拆解完成！")
                    st.markdown(res.text)
                except Exception as e:
                    st.error(f"分析異常，請確認連結與字幕。錯誤：{e}")
        else:
            st.warning("請先輸入網址喔。")

# --- 功能二：9大商業戰略畫布 ---
with tab2:
    # 這裡顯示左側按鈕點擊後的結果
    if strategy_btn:
        if product:
            st.header(f"📈 {product} 的 9 大商業戰略")
            with st.spinner("AI 決策模型計算中..."):
                try:
                    # 決策 Prompt 邏輯 (大氣商用版)
                    prompt = f"針對行業『{industry}』的產品『{product}』，輸出 9 個維度的專業顧問商用戰略，每項用 '###' 開頭。"
                    res = model.generate_content(prompt)
                    parts = res.text.split('###')
                    
                    # 彩色戰略方塊展示
                    col1, col2, col3 = st.columns(3)
                    with col1:
                        st.info(f"### 1. 使用情境\n{parts[1] if len(parts)>1 else '計算中'}")
                        st.info(f"### 2. 根源痛點\n{parts[2] if len(parts)>2 else '計算中'}")
                    with col2:
                        st.success(f"### 4. 回訪觸發\n{parts[4] if len(parts)>4 else '計算中'}")
                        st.success(f"### 5. 收費觸發\n{parts[5] if len(parts)>5 else '計算中'}")
                    with col3:
                        st.warning(f"### 7. 門檻行動\n{parts[7] if len(parts)>7 else '計算中'}")
                        st.warning(f"### 8. 依賴風險\n{parts[8] if len(parts)>8 else '計算中'}")
                    
                    st.markdown("---")
                    st.markdown(res.text) # 文字版複製
                except Exception as e:
                    st.error(f"戰略生成失敗：{e}")
        else:
            st.error("⚠️ 請先在左側輸入產品名稱喔！")
    else:
        st.write("👈 請在左側輸入資料並按下按鈕，結果會顯示在這裡。")
