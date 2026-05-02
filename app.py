import streamlit as st
import google.generativeai as genai

# 設定大氣排版
st.set_page_config(page_title="李大哥 AI 商業戰略分析系統", layout="wide")

# 配置 API (已修正型號為 latest 版本)
genai.configure(api_key="AIzaSyCfISY4wutzf8TG8hQ10SAMJVj9Sidf4vc")
model = genai.GenerativeModel('gemini-1.5-flash-latest')

st.title("🚀 李大哥專屬：Hermes 級 AI 戰略大腦")
st.markdown("---")

with st.sidebar:
    st.header("📋 項目設定")
    industry = st.selectbox("選擇行業", ["股市分析", "數位行銷", "醫美保養", "房地產", "餐飲加盟"])
    product = st.text_input("輸入產品/標的", placeholder="例如：1618合機技術分析")
    generate_btn = st.button("🔥 生成 9 大戰略畫布")

def get_9_tags_strategy(ind, prod):
    # 融入五層記憶金字塔與 Hermes 配置的深度 Prompt
    prompt = f"""
    你是一位頂級 AI 生態系統戰略顧問。請針對『{ind}』行業的『{prod}』，以打造『滿配 Hermes』級別 AI Agent 與『五層記憶金字塔』的高度，精準輸出 9 個維度的策略。
    請嚴格按照以下格式輸出，每個維度用 '###' 開頭：
    
    ### 1.使用情境：
    ### 2.根源痛點：
    ### 3.使用頻率：
    ### 4.回訪觸發：
    ### 5.收費觸發：
    ### 6.牽引能力：
    ### 7.門檻行動：
    ### 8.依賴風險：
    ### 9.停止訊號：
    """
    response = model.generate_content(prompt)
    return response.text

if generate_btn and product:
    with st.spinner("AI 正在調動五層記憶金字塔進行深度思考..."):
        try:
            res = get_9_tags_strategy(industry, product)
            parts = res.split('###')
            
            st.success("✅ 戰略分析已完成！")
            
            # 顯示 3x3 專業畫布
            col1, col2, col3 = st.columns(3)
            with col1:
                st.info(f"### 1. 使用情境\n{parts[1] if len(parts)>1 else '數據處理中'}")
                st.info(f"### 2. 根源痛點\n{parts[2] if len(parts)>2 else '數據處理中'}")
                st.info(f"### 3. 使用頻率\n{parts[3] if len(parts)>3 else '數據處理中'}")
            with col2:
                st.success(f"### 4. 回訪觸發\n{parts[4] if len(parts)>4 else '數據處理中'}")
                st.success(f"### 5. 收費觸發\n{parts[5] if len(parts)>5 else '數據處理中'}")
                st.success(f"### 6. 牽引能力\n{parts[6] if len(parts)>6 else '數據處理中'}")
            with col3:
                st.warning(f"### 7. 門檻行動\n{parts[7] if len(parts)>7 else '數據處理中'}")
                st.warning(f"### 8. 依賴風險\n{parts[8] if len(parts)>8 else '數據處理中'}")
                st.warning(f"### 9. 停止訊號\n{parts[9] if len(parts)>9 else '數據處理中'}")
        except Exception as e:
            st.error(f"系統連接中，請稍後再試一次生成。錯誤代碼: {e}")
