import streamlit as st
import time

# 頁面配置
st.set_page_config(page_title="ViralAI - 爆款引擎", layout="wide")

# --- 核心 CSS：完全複刻截圖中的深色質感與漸變按鈕 ---
st.markdown("""
    <style>
    /* 總背景：深紫黑 */
    .stApp {
        background-color: #0E0B16;
    }
    
    /* 標題與文字強制白色 */
    h1, h2, h3, p, span, label {
        color: #FFFFFF !important;
        font-family: 'Inter', -apple-system, sans-serif;
    }

    /* 模擬截圖中的平台選擇按鈕 (選中狀態) */
    .platform-btn-active {
        background: rgba(255, 46, 99, 0.15);
        border: 1.5px solid #FF2E63;
        color: #FF2E63 !important;
        padding: 10px 20px;
        border-radius: 12px;
        font-weight: bold;
        display: inline-block;
        margin-right: 10px;
    }

    /* 模擬截圖中的平台選擇按鈕 (未選中) */
    .platform-btn {
        background: #1C1C26;
        border: 1px solid #333;
        color: #888 !important;
        padding: 10px 20px;
        border-radius: 12px;
        display: inline-block;
        margin-right: 10px;
    }

    /* 爆款方案卡片：深色微透感 */
    .viral-card {
        background: #161622;
        border: 1px solid #2A2A3A;
        border-radius: 20px;
        padding: 25px;
        margin-bottom: 25px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.3);
    }

    /* 關鍵字與標籤樣式 */
    .tag-hook {
        background: linear-gradient(90deg, #FF2E63, #FF5F6D);
        color: white !important;
        padding: 4px 12px;
        border-radius: 8px;
        font-size: 14px;
        font-weight: bold;
    }

    /* 腳本文案框：全黑背景 */
    .script-box {
        background: #000000;
        border: 1px solid #333;
        border-radius: 12px;
        padding: 20px;
        color: #FFFFFF !important;
        font-size: 18px;
        line-height: 1.8;
        white-space: pre-wrap;
    }

    /* 核心漸變大按鈕：紅橙色 */
    div.stButton > button {
        background: linear-gradient(90deg, #FF2E63, #FF6A3D) !important;
        color: white !important;
        border: none !important;
        border-radius: 15px !important;
        padding: 15px 0px !important;
        font-size: 20px !important;
        font-weight: bold !important;
        width: 100%;
        transition: 0.3s;
    }
    div.stButton > button:hover {
        transform: scale(1.02);
        box-shadow: 0 0 20px rgba(255, 46, 99, 0.4);
    }
    
    /* 輸入框樣式 */
    div[data-baseweb="input"] {
        background-color: #1C1C26 !important;
        border-radius: 15px !important;
        border: 1px solid #333 !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 介面佈局 ---

st.markdown("<h1 style='font-size: 2.5rem;'>🔥 ViralAI</h1>", unsafe_allow_html=True)
st.markdown("<p style='color:#888 !important;'>全平台爆款引擎 - 真實 AI 深度分析</p>", unsafe_allow_html=True)

st.markdown("### 🔥 輸入帳號，AI 真實分析")
st.markdown("<p style='color:#888 !important;'>貼上任何平台的帳號連結或名稱，立即分析爆款策略</p>", unsafe_allow_html=True)

# 平台選擇模擬 (純視覺)
st.markdown("""
    <div>
        <span class="platform-btn-active">🎵 TikTok</span>
        <span class="platform-btn">🔴 抖音</span>
        <span class="platform-btn">▶️ YouTube</span>
        <span class="platform-btn">📸 Instagram</span>
        <span class="platform-btn">📕 小紅書</span>
    </div>
    """, unsafe_allow_html=True)

st.write("") # 間距

# 帳號連結輸入
url = st.text_input("帳號連結或名稱", placeholder="例：@username、https://www.tiktok.co...", label_visibility="collapsed")

# 大按鈕
if st.button("🔍 開始 AI 深度分析"):
    if url:
        with st.spinner("🚀 正在抓取數據庫，解析爆款基因..."):
            time.sleep(1.5)
            
            st.markdown("---")
            st.markdown("## 📊 AI 定製生成的 5 套爆款方案")
            
            # 定義 5 組資料 (包含 30s 腳本)
            scripts = [
                {"title": "方案 1：反直覺流量爆發", "hook": "為什麼你發片沒人看？因為你第一秒就在趕人！", "script": "0-5s: 展示低流量截圖，配負面音樂。\n5-20s: 拆解『完播率門檻』邏輯圖表。\n20-30s: 私訊領取 AI 爆款模板。"},
                {"title": "方案 2：AI 工具翻身術", "hook": "不用露臉、不用拍攝，這支影片是 AI 做出來的！", "script": "0-5s: 手機快速操作畫面，快節奏節奏感。\n5-20s: 演示 AI 10秒自動渲染素材過程。\n20-30s: 關注我，掌握全自動化產出。"},
                {"title": "方案 3：數據降維打擊", "hook": "百萬大號的秘密，是用了這套分析工具！", "script": "0-5s: 滿屏點讚評論動畫效果。\n5-20s: 深度對比競爭對手鉤子公式。\n20-30s: 點讚收藏下一支照著拍。"},
                {"title": "方案 4：熱門底層公式", "hook": "所有熱門影片前3秒都逃不過這套邏輯！", "script": "0-5s: 特寫爆款標題碎裂特效。\n5-20s: 拆解 Hook-Story-CTA 黃金比例。\n20-30s: 內測連結就在主頁。"},
                {"title": "方案 5：效率剪輯革命", "hook": "我用 AI 做完一周內容，你還在手動對位？", "script": "0-5s: 左邊人工 vs 右邊 AI 速度對比。\n5-20s: 展示自動配音與運鏡同步完成。\n20-30s: 立即點擊下方領取試用。"}
            ]

            for i, s in enumerate(scripts):
                st.markdown(f"""
                <div class="viral-card">
                    <div style="font-size: 24px; color: #FF6A3D !important; font-weight: 800; margin-bottom:15px;">{s['title']}</div>
                    <div class="tag-hook">黃金 3 秒鉤子</div>
                    <p style="font-size: 22px; font-weight: bold; margin: 15px 0;">{s['hook']}</p>
                    <div style="color: #FF2E63; font-weight: bold; margin-bottom: 10px;">📋 30 秒執行腳本文案：</div>
                    <div class="script-box">{s['script']}</div>
                </div>
                """, unsafe_allow_html=True)
                
                # 每個方案獨立的生成按鈕
                st.button(f"🎬 生成方案 {i+1} 預覽影片", key=f"btn_{i}")
    else:
        st.warning("請先輸入帳號或連結")
