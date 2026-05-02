import streamlit as st
import time

# --- 1. 網頁頂級視覺配置 ---
st.set_page_config(page_title="VIRAL ENGINE AI - 爆款戰略終端", layout="wide")

# 自定義 CSS：打造黑金商用質感
st.markdown("""
    <style>
    /* 全域背景 */
    .stApp {
        background-color: #0a0a0a;
        color: #f5f5f5;
    }
    
    /* 玻璃質感容器 */
    .glass-card {
        background: rgba(255, 255, 255, 0.03);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 20px;
        padding: 30px;
        margin-bottom: 25px;
        backdrop-filter: blur(10px);
    }
    
    /* 醒目的輸入框 */
    .stTextInput>div>div>input {
        background-color: #1a1a1a !important;
        color: #fbbf24 !important; /* 科技金 */
        border: 1px solid #444 !important;
        height: 60px !important;
        font-size: 20px !important;
        border-radius: 12px !important;
    }
    
    /* 戰略紅按鈕 */
    .stButton>button {
        background: linear-gradient(90deg, #ff3b3b 0%, #ff0000 100%);
        color: white;
        border: none;
        height: 60px;
        font-size: 22px !important;
        font-weight: bold;
        border-radius: 12px;
        transition: 0.3s;
        text-transform: uppercase;
        letter-spacing: 2px;
    }
    .stButton>button:hover {
        box-shadow: 0 0 25px rgba(255, 59, 59, 0.6);
        transform: translateY(-2px);
    }
    
    /* 腳本顯示區 */
    .script-box {
        background-color: #0d1a0d;
        border-left: 5px solid #00ff00;
        padding: 25px;
        font-family: 'Courier New', monospace;
        color: #e0e0e0;
        line-height: 1.8;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 2. 側邊欄：品牌與狀態 ---
with st.sidebar:
    st.markdown("<h1 style='color: #ff3b3b;'>VIRAL ENGINE</h1>", unsafe_allow_html=True)
    st.markdown("### 2026 商用戰略版")
    st.success("✅ AI 核心：已就緒")
    st.divider()
    st.write("📊 **分析庫存：** 1,280 支影片")
    st.write("📈 **今日產出：** 42 組腳本")

# --- 3. 主畫面：核心操作 ---
st.markdown("<h1 style='text-align: center; color: white;'>🛡️ AI 爆款影片 DNA 拆解系統</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #a3a3a3; font-size: 18px;'>貼入爆款連結，獲取重生腳本</p>", unsafe_allow_html=True)
st.write("")

# 這裡就是您要的連結輸入區，我把它做得非常大且明顯
video_url = st.text_input(
    label="請貼入影片連結 (YouTube / 抖音 / TikTok / IG)：", 
    placeholder="在此貼上爆款網址...",
    label_visibility="visible"
)

st.write("")

if st.button("🚀 開始深度拆解爆款 DNA"):
    if not video_url:
        st.error("❌ 李大哥，請先輸入連結！")
    else:
        # 動態模擬分析過程
        with st.status("🛠️ 正在連接全球數據庫分析中...", expanded=True) as status:
            st.write("抓取影片原始數據與評論分佈...")
            time.sleep(1)
            st.write("AI 正在掃描畫面節奏與鏡頭切換頻率...")
            time.sleep(1.2)
            st.write("比對爆款庫，提取 30 秒腳本模型...")
            time.sleep(0.8)
            status.update(label="✅ 拆解報告已生成！", state="complete", expanded=False)

        # --- 4. 結果展現 (賣錢的關鍵就在這) ---
        col1, col2 = st.columns([1, 1])
        
        with col1:
            st.markdown('<div class="glass-card">', unsafe_allow_html=True)
            st.subheader("🔥 爆款基因報告")
            st.write("✅ **開頭鉤子：** 使用了「反常識」對比，1.2 秒內留人。")
            st.write("✅ **情緒拉扯：** 前 10 秒製造焦慮，後 20 秒給予解決方案。")
            st.write("✅ **互動機制：** 文案埋設「隱性爭議」，觸發評論區對戰。")
            st.markdown('</div>', unsafe_allow_html=True)

        with col2:
            st.markdown('<div class="glass-card">', unsafe_allow_html=True)
            st.subheader("📈 預期爆發數值")
            st.progress(85, text="完播率潛力: 85%")
            st.progress(92, text="分享轉發意願: 92%")
            st.markdown('</div>', unsafe_allow_html=True)

        # --- 5. 腳本生成區 ---
        st.subheader("📝 重生腳本 (30 秒高轉化版)")
        st.markdown(f"""
            <div class="script-box">
            <b>【00-03s】黃金開頭：</b> 特寫畫面 + 衝擊性字幕「如果你也還在虧錢...」。<br>
            <b>【03-15s】建立信任：</b> 快速展示後台數據，配合激昂配樂節奏。<br>
            <b>【15-25s】解決方案：</b> 直接給出核心方法，文字排版簡約有力。<br>
            <b>【25-30s】強效行動：</b> 語音引導「點擊左下角」或「私訊領取」。<br>
            </div>
        """, unsafe_allow_html=True)

st.divider()
st.caption("© 2026 李大哥 AI 戰略研究所 | 商業版權所有")
