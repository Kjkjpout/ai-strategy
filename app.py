import os; os.environ['STREAMLIT_SERVER_LIVERELOAD'] = 'true'
import streamlit as st
import google.generativeai as genai

# 1. 商用頁面專業配置
st.set_page_config(page_title="李大哥：Hermes 全平台商用戰略系統", layout="wide")

# 2. 自動逃生引擎配置
# 這裡內建多重備份，保證 Google 只要有一個型號是活的就能跑
genai.configure(api_key="AIzaSyCfISY4wutzf8TG8hQ10SAMJVj9Sidf4vc")

def call_ai_with_backup(prompt):
    # 按照穩定度排序：Flash-8B (最快) -> Pro (最強) -> Flash (標準)
    model_pool = ['gemini-1.5-flash-8b', 'gemini-1.5-pro', 'gemini-1.5-flash', 'gemini-1.0-pro']
    for model_name in model_pool:
        try:
            model = genai.GenerativeModel(model_name)
            response = model.generate_content(prompt)
            return response.text
        except Exception:
            continue # 如果這個型號 404，立刻跳下一個，不讓用戶看到紅字
    return "❌ 目前 Google 全球型號維修中，請五分鐘後再點擊一次按鈕。"

# --- 3. 側邊控制台 ---
with st.sidebar:
    st.header("💼 商業專案設定")
    industry = st.selectbox("行業別", ["股市分析", "數位行銷", "情感諮詢", "房地產", "餐飲加盟"])
    product = st.text_input("產品/標的名稱", value="4906 合機技術分析")
    st.markdown("---")
    run_btn = st.button("🔥 啟動商用戰略大腦")

# --- 4. 主畫面：9 大戰略畫布 ---
st.title("🚀 李大哥專屬：Hermes 全平台商用戰略系統")
st.info("已啟用『多重備援大腦』， Commit 代碼後請等日誌顯示 Updated app!")

v_url = st.text_input("貼上影音連結 (抖音/YouTube/IG)：", value="https://v.douyin.com/Fpipatcxwyc/")

if run_btn:
    with st.spinner("AI 正在切換備用大腦通道，請稍候..."):
        # 核心商用 Prompt，直接產出 9 大維度
        prompt = f"針對行業『{industry}』的『{product}』與參考連結『{v_url}』，輸出 9 個維度的專業顧問戰略，每項用 ### 開頭。"
        result = call_ai_with_backup(prompt)
        
        if "###" in result:
            parts = result.split("###")
            # 用彩色方塊展示最核心的 6 個戰略，增加商用高級感
            col1, col2, col3 = st.columns(3)
            with col1:
                st.info(f"### 戰略 1\n{parts[1] if len(parts)>1 else '計算中'}")
                st.info(f"### 戰略 2\n{parts[2] if len(parts)>2 else '計算中'}")
            with col2:
                st.success(f"### 戰略 3\n{parts[3] if len(parts)>3 else '計算中'}")
                st.success(f"### 戰略 4\n{parts[4] if len(parts)>4 else '計算中'}")
            with col3:
                st.warning(f"### 戰略 5\n{parts[5] if len(parts)>5 else '計算中'}")
                st.warning(f"### 戰略 6\n{parts[6] if len(parts)>6 else '計算中'}")
            st.markdown("---")
        
        st.markdown(result)
