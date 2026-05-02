import streamlit as st
import time

# 頁面配置
st.set_page_config(page_title="AI Viral Master Pro", layout="wide")

# CSS 注入：強制文字全白，解決你看不到字的問題
st.markdown("""
    <style>
    .stApp { background-color: #0B0E14; }
    /* 所有標籤與標題強制白色 */
    h1, h2, h3, p, label, .stMarkdown { color: #FFFFFF !important; }
    /* 卡片設計 */
    .viral-card {
        background: rgba(255, 255, 255, 0.07);
        border: 1px solid #00F2EA;
        border-radius: 12px;
        padding: 20px;
        margin-bottom: 20px;
    }
    .hook-box {
        background-color: #FF2E63;
        color: white !important;
        padding: 5px 12px;
        border-radius: 6px;
        font-weight: bold;
        display: inline-block;
        margin-bottom: 10px;
    }
    /* 修復按鈕文字顏色 */
    .stButton>button {
        color: #000000 !important;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1 style='color:#00F2EA;'>⚡ AI Viral Master Pro</h1>", unsafe_allow_html=True)

# 使用 Session State 確保按鈕觸發後內容不會消失
if 'processed' not in st.session_state:
    st.session_state.processed = False

# 輸入框
url = st.text_input("請在此貼入影片連結：", placeholder="https://...", key="input_url")

# 按鈕邏輯
if st.button("🚀 開始分析並生成 5 套爆款方案", use_container_width=True):
    if url:
        st.session_state.processed = True
    else:
        st.error("請先輸入連結！")

# 如果狀態為 True，顯示內容
if st.session_state.processed:
    with st.spinner("正在提取數據並撰寫 30 秒腳本..."):
        time.sleep(1) # 模擬運算

        st.markdown("## 🎬 5 套爆款標題與 30 秒詳細腳本")

        # 腳本資料
        scripts = [
            {
                "title": "標題：為什麼你的流量總是卡在 500？",
                "hook": "你以為是內容不好？錯！是因為你沒過大數據的門檻！",
                "content": "0-5s: 快速切換低流量截圖 + 懸疑音樂\n5-20s: 拆解爆款完播率公式\n20-30s: 引導領取 AI 模板"
            },
            {
                "title": "標題：2026年 AI 全自動化變現路徑曝光",
                "hook": "不用露臉、不用拍攝，這支影片是 AI 幫我做的。",
                "content": "0-5s: 展示手機一鍵生成影片的震撼畫面\n5-20s: 快速演示 APP 操作介面\n20-30s: 私訊『AI』領取內測"
            },
            {
                "title": "標題：百萬大號不肯說的秘密",
                "hook": "他們不是運氣好，而是用了這套數據工具！",
                "content": "0-5s: 展示滿屏點讚與評論動畫\n5-20s: 展示競爭對手帳號數據報告\n20-30s: 點贊關注看更多"
            },
            {
                "title": "標題：短影音爆紅的『底層公式』",
                "hook": "所有熱門影片都逃不過這 3 秒的邏輯控制！",
                "script": "0-5s: 特寫爆款標題碎裂特效\n5-20s: 拆解 Hook-Story-CTA 結構\n20-30s: 收藏這部影片照著拍"
            },
            {
                "title": "標題：別再浪費時間手剪影片了",
                "hook": "我用 30 秒做完了你 3 小時的工作量！",
                "content": "0-5s: 對比手忙腳亂 vs AI 一鍵生成\n5-20s: 快速展示自動配音與轉場\n20-30s: 點擊首頁連結體驗"
            }
        ]

        # 循環生成 5 個卡片
        for i, s in enumerate(scripts):
            st.markdown(f"""
            <div class="viral-card">
                <h3 style="color:#00F2EA; margin-top:0;">{s['title']}</h3>
                <div class="hook-box">核心鉤子 (Hook)</div>
                <p style="font-size:20px; font-weight:bold;">{s['hook']}</p>
                <div style="color:#00F2EA; margin-bottom:5px;">📋 30 秒腳本內容：</div>
                <div style="background:rgba(0,0,0,0.5); padding:15px; border-radius:8px; white-space:pre-wrap; border:1px solid #333;">
{s.get('content', s.get('script'))}
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            # 生成影片按鈕
            if st.button(f"🛠️ 生成方案 {i+1} 的 AI 影片預覽", key=f"btn_{i}"):
                st.info(f"正在連線至影片生成引擎，準備處理方案 {i+1}...")
