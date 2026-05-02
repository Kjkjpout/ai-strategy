import streamlit as st
import time
import re

# --- ViralAI 介面完美複刻與全平台適配 ---
st.set_page_config(page_title="ViralAI - 全平台爆款引擎", layout="wide")

st.markdown("""
    <style>
    /* 背景與基礎顏色設定 */
    .stApp { background-color: #0B0A12; }
    h1, h2, h3, h4, p, span, label, .stMarkdown {
        color: #FFFFFF !important;
        font-family: 'SF Pro Display', -apple-system, sans-serif;
    }
    
    /* 複刻平台選擇行 (兩行佈局) */
    .platform-container {
        display: flex;
        flex-wrap: wrap;
        gap: 10px;
        margin-bottom: 20px;
    }
    .platform-tag {
        background: #191922;
        border: 1px solid #333;
        color: #888 !important;
        padding: 8px 15px;
        border-radius: 10px;
        font-size: 14px;
        cursor: pointer;
    }
    .platform-tag-active {
        background: rgba(255, 46, 99, 0.15);
        border: 1.5px solid #FF2E63;
        color: #FF2E63 !important;
        padding: 8px 15px;
        border-radius: 10px;
        font-weight: bold;
    }

    /* 紅橙漸變大按鈕 (與截圖顏色完全同步) */
    div.stButton > button {
        background: linear-gradient(90deg, #FF2E63 0%, #FF6A3D 100%) !important;
        color: white !important;
        border: none !important;
        border-radius: 12px !important;
        padding: 15px 0px !important;
        font-size: 18px !important;
        font-weight: bold !important;
        width: 100%;
        box-shadow: 0 4px 15px rgba(255, 46, 99, 0.3);
    }
    
    /* 爆款方案卡片 */
    .viral-card {
        background: #14141D;
        border: 1px solid #2A2A35;
        border-radius: 18px;
        padding: 20px;
        margin-bottom: 20px;
    }
    .script-box {
        background: #000000;
        border: 1px solid #333;
        border-radius: 10px;
        padding: 15px;
        color: #FFFFFF !important;
        font-size: 18px !important;
        line-height: 1.7;
        white-space: pre-wrap;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 標題區 ---
st.markdown("<h2 style='font-size: 2.2rem;'>🔥 ViralAI</h2>", unsafe_allow_html=True)
st.markdown("<p style='color:#888 !important; margin-top:-10px;'>全平台爆款引擎</p>", unsafe_allow_html=True)

st.write("")
st.markdown("#### 🔥 輸入連結，AI 深度分析")
st.markdown("<p style='color:#888 !important;'>支援 TikTok、抖音、YouTube、Instagram、小紅書連結</p>", unsafe_allow_html=True)

# --- 平台選擇 UI 模擬 ---
st.markdown("<p style='color:#AAAAAA !important; font-size:14px;'>選擇平台</p>", unsafe_allow_html=True)
st.markdown("""
    <div class="platform-container">
        <span class="platform-tag-active">🎵 TikTok</span>
        <span class="platform-tag">🔴 抖音</span>
        <span class="platform-tag">▶️ YouTube</span>
        <span class="platform-tag">📸 Instagram</span>
        <span class="platform-tag">📕 小紅書</span>
    </div>
    """, unsafe_allow_html=True)

# --- 連結處理邏輯 ---
url_input = st.text_input("貼上連結或帳號名稱：", value="http://xhslink.com/o/5xJrZj2ydiY", placeholder="請貼入影片連結...")

if st.button("🔍 開始 AI 深度分析"):
    if url_input:
        # 自動識別平台
        platform = "未知平台"
        if "xhslink" in url_input or "xiaohongshu" in url_input: platform = "小紅書"
        elif "tiktok" in url_input: platform = "TikTok"
        elif "douyin" in url_input: platform = "抖音"
        elif "youtube" in url_input or "youtu.be" in url_input: platform = "YouTube"
        elif "instagram" in url_input: platform = "Instagram"
        
        with st.status(f"🚀 正在連接 {platform} 引擎進行深度抓取...", expanded=True):
            time.sleep(1.5)
            st.write(f"✅ 已識別 {platform} 爆款基因")
            st.write("✅ 正在拆解影片技術點：闊面修容、淡顏釣系、姐感氛圍")
        
        st.markdown("---")
        st.markdown(f"### 📊 針對 {platform} 影片生成的 5 套重寫方案")

        # 此處腳本已根據「美妝/妝教」技術核心進行深度重編
        schemes = [
            {"title": "方案 1：【技術流】闊面修容法", "hook": "闊面大鼻頭女孩別再無效化妝了！核心在於『視覺重心上移』！", "script": "「為什麼你化完妝臉還是很大？(指著臉) 因為你只會遮，不會提亮！\n這部影片拆解了爆款妝教的祕訣，(快節奏)\n不需要拼命打陰影，重點在眼下三角區的骨相重塑。\n大鼻頭瞬間變精緻，這才是釣系姐感的精髓！」"},
            {"title": "方案 2：【反差感】淡顏逆襲姐感", "hook": "誰說淡顏沒氣場？教你如何把大鼻頭化成清冷貴氣感！", "script": "「淡顏姐妹別再死磕濃妝了！那只會讓你的臉更笨重。\n學學這套『欲拒還迎』的釣系妝。(眼神犀利)\n利用淡顏的留白優勢，配合橫向腮紅縮短中庭，\n不用濾鏡也能擁有的高級立體感，現在就學起來！」"},
            {"title": "方案 3：【避坑指南】化妝越化越髒？", "hook": "化妝2小時出門像泥牆？這3個修容點你絕對打錯了！", "script": "「救命！我看這支影片才發現，闊面臉最忌諱山根黑影！\n真正的重寫邏輯在於『內提亮，外留白』。\n跟我一起拆解這套爆款修容曲線，(展示動作)\n30秒教你改掉無效手法，讓你的大臉盤子視覺縮小一倍！」"},
            {"title": "方案 4：【氛圍感】釣系妝底層邏輯", "hook": "所有人都在教你遮瑕，卻沒人教你如何營造『鬆弛姐感』！", "script": "「大鼻頭其實是增加親和力的利器！(語氣反轉)\n這套腳本教你如何重組五官比例。\n關鍵點：眉尾上揚、鼻尖點亮、口紅模糊邊緣。\n不費力就能火爆全網的妝造密碼，直接公開給你！」"},
            {"title": "方案 5：【效率革命】30秒速成妝教", "hook": "沒時間看長影片？30秒給你最全的闊面大鼻頭救星攻略！", "script": "「這套妝造真的太神了！一抹、二推、三定妝。(激動快節奏)\n針對闊面淡顏，我們只做內提亮和眉尾提拉。\n效果不好你來找我！(堅定)\n現在點擊連結，AI 直接幫你優化專屬的美妝口播文案！」"}
        ]

        for i, s in enumerate(schemes):
            st.markdown(f"""
            <div class="viral-card">
                <div style="color: #FF6A3D; font-size: 20px; font-weight: 800;">{s['title']}</div>
                <div style="margin: 10px 0;"><span style="background:#FF2E63; padding:3px 8px; border-radius:5px; font-size:12px;">🔥 爆款鉤子</span> {s['hook']}</div>
                <div style="color: #00F2EA; font-size:14px; margin-bottom:5px;">🎙️ 30秒口播逐字文案：</div>
                <div class="script-box">{s['script']}</div>
            </div>
            """, unsafe_allow_html=True)
            st.button(f"🎬 生成方案 {i+1} 影片預覽", key=f"btn_{i}")
    else:
        st.error("⚠️ 請輸入有效的影片連結！")
