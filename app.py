import streamlit as st
import time

# --- 核心配置與 UI 注入 ---
st.set_page_config(page_title="AI Viral Master Pro", layout="wide")

# 強化的視覺 CSS：確保文字全白、高對比、科技感
st.markdown("""
    <style>
    .stApp { background-color: #0B0E14; }
    /* 卡片容器 */
    .viral-card {
        background: rgba(255, 255, 255, 0.05);
        border: 2px solid #00F2EA;
        border-radius: 15px;
        padding: 25px;
        margin-bottom: 20px;
    }
    /* 強制白色文字 */
    .white-text { color: #FFFFFF !important; font-size: 18px; line-height: 1.6; }
    .neon-text { color: #00F2EA !important; font-weight: bold; font-size: 20px; }
    .hook-label { 
        background-color: #FF2E63; 
        color: white !important; 
        padding: 5px 15px; 
        border-radius: 50px; 
        font-weight: bold;
        display: inline-block;
        margin-bottom: 10px;
    }
    /* 標題加強 */
    .section-header { color: #FFFFFF !important; border-left: 5px solid #00F2EA; padding-left: 15px; margin: 30px 0 20px 0; }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1 style='color:#00F2EA;'>⚡ AI Viral Master Pro</h1>", unsafe_allow_html=True)

url = st.text_input("", placeholder="請貼入影片連結...", label_visibility="collapsed")

if st.button("🚀 開始分析並生成 5 套爆款方案", use_container_width=True):
    with st.spinner("正在提取數據並撰寫 30 秒腳本..."):
        time.sleep(1)

        st.markdown("<h2 class='section-header'>🎬 5 套爆款標題與 30 秒詳細腳本</h2>", unsafe_allow_html=True)

        # 這裡就是你要的：清晰的標題、30秒腳本、純白文字
        scripts_data = [
            {
                "title": "標題：為什麼你的流量總是卡在 500？",
                "hook": "你以為是內容不好？錯！是因為你沒過大數據的門檻！",
                "script": "00-05s：[視覺] 快速切換多張低點讚截圖，配沉重BGM。\n05-20s：[教學] 展示 AI 分析後的後台曲線，解釋『完播率』公式。\n20-30s：[行動] 點擊下方，我把這套 AI 爆款模板發給你。"
            },
            {
                "title": "標題：普通人翻身的最後一個紅利窗口",
                "hook": "2026年，不會用 AI 生產內容的人將被徹底淘汰！",
                "script": "00-05s：[視覺] 科技感隧道轉場，配節奏感極強的 Bass 音。\n05-20s：[內容] 展示 AI 10 秒產出 5 支影片的全過程，震撼視覺。\n20-30s：[行動] 關注我，帶你掌握全自動化內容工廠。"
            },
            {
                "title": "標題：別再自己剪片了！AI 幫你做！",
                "hook": "我用 30 秒做完了你 3 小時的工作量，而且更火！",
                "script": "00-05s：[視覺] 分屏對比：左邊手忙腳亂，右邊一鍵生成。\n05-20s：[核心] 快速演示 APP 功能介面，標注關鍵分析點。\n20-30s：[行動] 私訊『AI』，領取工具內測名額。"
            },
            {
                "title": "標題：短影音爆紅的『底層公式』曝光",
                "hook": "所有熱門影片都逃不過這 3 秒的邏輯控制！",
                "script": "00-05s：[視覺] 特寫爆款標題，配合碎裂特效。\n05-20s：[知識] 拆解 Hook -> Story -> CTA 的黃金比例結構。\n20-30s：[行動] 點贊收藏，下一支影片你就照著這個拍！"
            },
            {
                "title": "標題：揭秘！那些百萬大號不肯說的秘密",
                "hook": "他們不是運氣好，而是用了這套數據分析工具！",
                "script": "00-05s：[視覺] 滿螢幕的點讚和評論動畫，氛圍感拉滿。\n05-20s：[揭秘] 展示競爭對手帳號的深度分析數據報告。\n20-30s：[行動] 想看更多數據？主頁連結見。"
            }
        ]

        for i, item in enumerate(scripts_data):
            st.markdown(f"""
            <div class="viral-card">
                <div class="neon-text">方案 {i+1}：{item['title']}</div>
                <hr style="border: 0.5px solid rgba(255,255,255,0.1)">
                <div class="hook-label">黃金 3 秒鉤子</div>
                <div class="white-text" style="font-weight: bold; margin-bottom: 15px;">{item['hook']}</div>
                <div style="color: #00F2EA; font-size: 14px; margin-bottom: 5px;">📜 30 秒詳細執行腳本：</div>
                <div class="white-text" style="background: rgba(0,0,0,0.3); padding: 15px; border-radius: 8px; white-space: pre-wrap;">{item['script']}</div>
            </div>
            """, unsafe_allow_html=True)
            
            # 每一個方案下方預留生成按鈕
            if st.button(f"🛠️ 點擊生成方案 {i+1} 的 AI 影片", key=f"gen_{i}"):
                st.write("⏳ 正在調用 API 接口... 請稍候")
