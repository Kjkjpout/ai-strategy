import streamlit as st
import google.generativeai as genai

# 設定頁面外殼，要賣好價錢，排版一定要大氣
st.set_page_config(page_title="李大哥 AI 商業戰略分析系統", layout="wide")

# 這裡建議以後把 API Key 隱藏，目前先放這讓您測試
genai.configure(api_key="AIzaSyCfISY4wutzf8TG8hQ10SAMJVj9Sidf4vc")
model = genai.GenerativeModel('gemini-1.5-flash')

st.title("🚀 李大哥專屬：AI 商業深度戰略生成器")
st.markdown("---")

# 左側輸入區
with st.sidebar:
    st.header("📋 項目設定")
    industry = st.selectbox("選擇行業", ["股市分析", "數位行銷", "醫美保養", "房地產", "餐飲加盟"])
    product = st.text_input("輸入產品/標的", placeholder="例如：1618合機技術分析")
    generate_btn = st.button("🔥 生成 9 大戰略畫布")

# 核心邏輯：嚴格遵守 9 個標籤輸出
def get_9_tags_strategy(ind, prod):
    prompt = f"你是一位頂級戰略顧問。請針對『{ind}』行業的『{prod}』，精準輸出以下 9 個維度的策略：1.使用情境、2.根源痛點、3.使用頻率、4.回訪觸發、5.收費觸發、6.牽引能力、7.門檻行動、8.依賴風險、9.停止訊號。語氣要像台灣專業顧問。"
    response = model.generate_content(prompt)
    return response.text

# 顯示 3x3 網頁佈局
if generate_btn and product:
    with st.spinner("AI 正在深度思考戰略..."):
        res = get_9_tags_strategy(industry, product)
        st.success("✅ 戰略分析已完成！")
        
        # 這裡會呈現漂亮的分欄
        col1, col2, col3 = st.columns(3)
        with col1:
            st.info("### 1. 使用情境")
            st.info("### 2. 根源痛點")
            st.info("### 3. 使用頻率")
        with col2:
            st.success("### 4. 回訪觸發")
            st.success("### 5. 收費觸發")
            st.success("### 6. 牽引能力")
        with col3:
            st.warning("### 7. 門檻行動")
            st.warning("### 8. 依賴風險")
            st.warning("### 9. 停止訊號")
        
        st.markdown("---")
        st.subheader("📝 完整策略報告內容")
        st.write(res)