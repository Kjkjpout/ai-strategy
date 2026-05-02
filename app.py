import streamlit as st
import time

# --- 極致 UI 設置 (複刻 ViralAI 截圖風格) ---
st.set_page_config(page_title="ViralAI - 爆款腳本引擎", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #0E0B16; }
    h1, h2, h3, p, span, label { color: #FFFFFF !important; }
    
    /* 複刻紅橙漸變按鈕 */
    div.stButton > button {
        background: linear-gradient(90deg, #FF2E63, #FF6A3D) !important;
        color: white !important;
        border: none !important;
        border-radius: 12px !important;
        padding: 12px 0px !important;
        font-size: 18px !important;
        font-weight: bold !important;
        width: 100%;
    }

    /* 平台選擇標籤 */
    .platform-row { display: flex; gap: 10px; margin-bottom: 20px; }
    .platform-tag {
        background: #1C1C26;
        border: 1px solid #333;
        color: #888 !important;
        padding: 8px 16px;
        border-radius: 10px;
        font-size: 14px;
    }
    .platform-tag-active {
        background: rgba(255, 46, 99, 0.15);
        border: 1.5px solid #FF2E63;
        color: #FF2E63 !important;
        font-weight: bold;
    }

    /* 方案卡片 */
    .viral-card {
        background: #161622;
        border: 1px solid #2A2A3A;
        border-radius: 20px;
        padding: 25px;
        margin-bottom: 30px;
    }

    /* 逐字稿文案框 */
    .script-text-box {
        background: #000000;
        border-left: 4px solid #FF2E63;
        padding: 20px;
        color: #FFFFFF !important;
        font-size: 20px !important;
        line-height: 1.6;
        white-space: pre-wrap;
        margin: 15px 0;
    }
    
    .title-orange { color: #FF6A3D !important; font-size: 24px; font-weight: 800; }
    </style>
    """, unsafe_allow_html=True)

# --- 標題區 ---
st.markdown("<h1 style='font-size: 2.2rem;'>🔥 ViralAI</h1>", unsafe_allow_html=True)
st.markdown("<p style='color:#888 !important;'>全平台爆款引擎 · 深度文案生成</p>", unsafe_allow_html=True)

st.write("")
st.markdown("### 🔥 輸入帳號/連結，生成逐字腳本")

# 模擬平台切換
st.markdown("""
    <div class="platform-row">
        <div class="platform-tag platform-tag-active">🎵 TikTok</div>
        <div class="platform-tag">🔴 抖音</div>
        <div class="platform-tag">▶️ YouTube</div>
        <div class="platform-tag">📸 Instagram</div>
        <div class="platform-tag">📕 小紅書</div>
    </div>
    """, unsafe_allow_html=True)

url = st.text_input("貼入連結或帳號名稱", placeholder="https://...", label_visibility="collapsed")

# --- 模擬爆款腳本數據庫 (真正的口播文案) ---
scripts_repo = [
    {
        "title": "方案 1：【焦慮反擊類】500播放的真相",
        "hook": "你以為內容不好？錯！是你第一秒就在趕人！",
        "copywriting": "「為什麼你的影片總是卡在500播放？(停頓)\n不是你拍得爛，而是你根本不懂大數據的『開頭生存法則』！\n大多數人第一秒就在自我介紹，或者是講廢話，(快節奏)\n記住，現在的人耐心只有3秒。\n你想突破播放量，必須把這套爆款基因植入你的腳本。\n點擊左下角，我幫你分析好的模板，直接照著唸就能火！」"
    },
    {
        "title": "方案 2：【利益誘惑類】AI 幫你賺錢",
        "hook": "不用露臉、不用拍攝，這支影片是 AI 30 秒做出來的！",
        "copywriting": "「聽好了，2026年如果你還在苦哈哈地剪片，你真的會被淘汰！(展示手機)\n你看這支影片，(指螢幕) 從文案到配音到畫面，全部是 AI 一鍵生成的。\n我只用了不到30秒，效果比你剪3個小時還要好！\n想知道我是怎麼做到的嗎？\n關注我，回覆『AI』，我把這套全自動變現流程發給你！」"
    },
    {
        "title": "方案 3：【數據揭秘類】百萬大號的暗器",
        "hook": "那些大網紅不肯說的秘密，其實就在這套數據裡！",
        "copywriting": "「你真的以為那些百萬大號是靠運氣火的嗎？(搖頭)\n別傻了，他們背後都有強大的數據監控工具！\n他們知道幾點發、用什麼鉤子、哪句話能讓你留下來。(加速)\n今天我把這套專業級的分析報告直接公開，\n想看你帳號爆款基因的，點讚這部影片，首頁連結見！」"
    },
    {
        "title": "方案 4：【邏輯拆解類】爆款萬能公式",
        "hook": "所有熱門影片，前 3 秒都逃不過這套邏輯！",
        "copywriting": "「短影音爆紅真的有公式！(敲黑板)\n公式就是：負面鉤子 + 價值觀點 + 行動導流。\n第一句先嚇唬他，第二段給出解決方案，最後讓他不得不關注你。\n這套邏輯在 TikTok、抖音、YT 全部通用！\n如果你還不會寫腳本，收藏這部影片，下次發片對照一遍。」"
    },
    {
        "title": "方案 5：【效率革命類】解放雙手",
        "hook": "別再手剪了！我用 AI 搞定了一週的內容！",
        "copywriting": "「你還在逐幀剪輯、對音軌嗎？(驚訝)\n太慢了！現在大玩家都在用 AI 自動化生產內容了。\n我這一週發了50支影片，全部是 AI 幫我完成的，播放量反而更高！\n想跟我一樣解放雙手的，點擊下方連結，\n直接開啟你的 AI 內容工廠試用名額！」"
    }
]

if st.button("🔍 開始 AI 深度分析與生成"):
    if url:
        with st.status("🛸 正在解析全平台數據... 生成 30s 逐字口播稿", expanded=True):
            time.sleep(1.5)
            
        st.markdown("## 📊 分析完成！為您生成 5 套口播腳本")
        
        for i, s in enumerate(scripts_repo):
            st.markdown(f"""
            <div class="viral-card">
                <div class="title-orange">{s['title']}</div>
                <div style="margin: 15px 0;">
                    <span style="background:#FF2E63; padding:4px 10px; border-radius:5px; font-weight:bold;">🔥 爆款鉤子</span>
                    <p style="font-size:22px; font-weight:bold; margin-top:10px;">{s['hook']}</p>
                </div>
                <div style="color: #00F2EA; font-weight: bold;">🎙️ 30 秒口播逐字文案（可直接拍片）：</div>
                <div class="script-text-box">{s['copywriting']}</div>
            </div>
            """, unsafe_allow_html=True)
            
            st.button(f"🎬 方案 {i+1} 一鍵生成影片預覽", key=f"gen_{i}")
    else:
        st.warning("請輸入有效連結")
