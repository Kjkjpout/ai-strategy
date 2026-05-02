import streamlit as st
import time

# --- 1. 網頁配置 (戰略終端質感) ---
st.set_page_config(page_title="李大哥 AI 爆款拆解終端", layout="wide")

# 自定義 CSS (打造專業、高科技感)
st.markdown("""
    <style>
    .main { background-color: #050505; color: #e0e0e0; }
    .stTextInput>div>div>input { background-color: #1a1a1a; color: #00ff00; border: 1px solid #333; }
    .stTextArea>div>textarea { background-color: #1a1a1a; color: #ffffff; border: 1px solid #333; }
    .stButton>button { background-color: #ff4b4b; color: white; border-radius: 8px; font-weight: bold; width: 100%; height: 3em; }
    .analysis-box { padding: 20px; border: 1px solid #333; border-radius: 10px; background-color: #111; margin-bottom: 20px; }
    .script-box { padding: 20px; border: 1px solid #00ff00; border-radius: 10px; background-color: #0d1a0d; color: #ffffff; font-family: 'Courier New', monospace; }
    h1, h2, h3 { color: #ffffff !important; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. 側邊欄 ---
with st.sidebar:
    st.image("https://img.icons8.com/fluent/96/000000/artificial-intelligence.png", width=80)
    st.title("李大哥 AI 戰略終端")
    st.info("👤 身分：爆款策略開發者")
    st.success("✅ AI 拆解引擎：已就位")
    st.markdown("---")
    st.markdown("### 🎯 支援平台")
    st.markdown("- 抖音 (Douyin)")
    st.markdown("- TikTok (國際版)")
    st.markdown("- YouTube Shorts")
    st.markdown("- Instagram Reels")

# --- 3. 主畫面：連結輸入區 ---
st.title("🛡️ 全平台爆款影片「DNA 拆解與重生」系統")
st.markdown("### 第一步：貼上爆款影片連結")

video_url = st.text_input("", placeholder="在此貼上 抖音/TikTok/YouTube/IG 的影片連結...")

# --- 4. 執行拆解與生成 ---
if st.button("🚀 開始核心拆解 & 生成 30 秒腳本"):
    if not video_url:
        st.warning("⚠️ 李大哥，請先貼上連結才能開始戰略分析！")
    else:
        # 1. 數據抓取動畫
        progress_bar = st.progress(0)
        status_text = st.empty()
        
        status_text.text("正在接入平台 API，抓取影片原始數據...")
        time.sleep(1.0); progress_bar.progress(30)
        
        status_text.text("AI 正在分析畫面節奏、文案鉤子與情緒曲線...")
        time.sleep(1.5); progress_bar.progress(60)
        
        status_text.text("正在複製爆款 DNA，撰寫全新 30 秒腳本...")
        time.sleep(1.0); progress_bar.progress(100)
        
        status_text.empty()
        st.toast("✅ 戰略分析完成！")

        # 模擬一個分析結果 (週一真實對接 AI 時會更精準)
        
        # --- 顯示拆解報告 ---
        st.markdown("---")
        st.subheader("🔥 AI 爆款 DNA 拆解報告")
        
        with st.container():
            st.markdown('<div class="analysis-box">', unsafe_allow_html=True)
            col1, col2, col3 = st.columns(3)
            with col1:
                st.markdown("### 🧲 黃金 3 秒鉤子 (Hook)")
                st.write("開頭使用了「痛點反轉」技巧。直接拋出一個用戶最關心的虧錢問題，然後立刻展示賺錢結果，好奇心拉滿。")
            with col2:
                st.markdown("### 📈 情緒轉折曲線")
                st.write("情緒從「焦慮(虧錢)」->「期待(方法)」->「興奮(結果)」。節奏極快，平均 1.5 秒剪輯一次。")
            with col3:
                st.markdown("### 💬 爆款心理學判定")
                st.write("觸發了「貪婪」與「恐懼缺失」心理。留言區都在問「怎麼做」，這支影片的 DNA 是「資訊差」。")
            st.markdown('</div>', unsafe_allow_html=True)

        # --- 顯示生成的腳本 ---
        st.subheader("📝 重生：全新 30 秒腳本 (直接開拍)")
        st.markdown('<div class="script-box">', unsafe_allow_html=True)
        st.markdown("""
**[0:00 - 0:03] (黃金 鉤子 - 痛點反轉)**
<br>【畫面】: 你在股市虧錢的截圖 (加紅叉) -> 變成一張全是陽線的紅盤 (加綠勾)。
<br>【文案/口播】: 「如果你還在用舊方法買股票，難怪你一直虧錢！今天我只講一次，高手是如何在熊市裡翻身的。」

<br>**[0:03 - 0:15] (反常識 資訊差)**
<br>【畫面】: 快速剪輯，配合激昂配樂。你在電腦前點擊群益 API 介面。
<br>【文案/口播】: 「他們都在聽消息，但我只看一件事：全自動技術指標篩選。成交值過 20 億、CCI 超過 0 軸，這種『妖股 DNA』，電腦 1 秒就選出來了。」

<br>**[0:15 - 0:27] (利益 誘惑 - 結果展示)**
<br>【畫面】: 手機螢幕展示「我的自選股.txt」裡的股票全部漲停。
<br>【文案/口播】: 「不需要你看盤，不需要你懂技術分析。只要把這個 AI 策略終端部署在 GitHub 上，它每天自動把最強的標的送到你面前。」

<br>**[0:27 - 0:30] (行動 呼籲 - 轉化)**
<br>【畫面】: 引導手指點擊側邊欄「加入自選」。
<br>【文案/口播】: 「這套『七大鐵律』，你想免費體驗嗎？私訊我『戰略』，我把連結發給你。」
""", unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

st.markdown("---")
st.caption("© 2026 李大哥爆款戰略研究所 - AI 技術核心")
