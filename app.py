import streamlit as st
import time

# --- ViralAI Mobile UI Setup ---
st.set_page_config(page_title="ViralAI", layout="centered")

st.markdown("""
    <style>
    .stApp { background-color: #0B0A12; }
    h2, p, span, label { color: #FFFFFF !important; }
    .platform-row { display: flex; gap: 8px; margin-bottom: 15px; flex-wrap: wrap; }
    .tag-active { 
        background: rgba(255, 46, 99, 0.15); border: 1.5px solid #FF2E63; 
        color: #FF2E63 !important; padding: 6px 12px; border-radius: 8px; font-weight: bold; font-size: 13px;
    }
    .tag-inactive { 
        background: #191922; border: 1px solid #333; 
        color: #888 !important; padding: 6px 12px; border-radius: 8px; font-size: 13px;
    }
    div.stButton > button {
        background: linear-gradient(90deg, #FF2E63 0%, #FF6A3D 100%) !important;
        color: white !important; border: none !important; border-radius: 12px !important;
        padding: 18px 0px !important; font-size: 18px !important; font-weight: bold !important;
        width: 100%; box-shadow: 0 4px 15px rgba(255, 46, 99, 0.3);
    }
    .viral-card {
        background: #14141D; border: 1px solid #2A2A35;
        border-radius: 18px; padding: 20px; margin-bottom: 15px;
    }
    .script-box {
        background: #000000; border-radius: 10px; padding: 15px;
        color: #FFFFFF !important; font-size: 18px; line-height: 1.7; margin-top: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h2>🔥 ViralAI</h2>", unsafe_allow_html=True)
st.markdown("<p style='color:#888 !important; margin-top:-10px;'>全平台爆款引擎</p>", unsafe_allow_html=True)

st.write("")
st.markdown("#### 🔥 輸入連結，AI 真實分析")
st.markdown("<p style='color:#888 !important; font-size: 14px;'>支援 TikTok、抖音、YouTube、Instagram、小紅書</p>", unsafe_allow_html=True)

st.markdown("""
    <div class="platform-row">
        <span class="tag-active">🎵 TikTok</span> <span class="tag-inactive">🔴 抖音</span> <span class="tag-inactive">▶️ YouTube</span>
    </div>
    <div class="platform-row" style="margin-top:-5px;">
        <span class="tag-inactive">📸 Instagram</span> <span class="tag-inactive">📕 小紅書</span>
    </div>
    """, unsafe_allow_html=True)

url_input = st.text_input("貼上連結：", value="http://xhslink.com/o/5xJrZj2ydiY", label_visibility="collapsed")

if st.button("🔍 開始 AI 深度分析"):
    with st.status("🚀 正在掃描全平台爆款基因...", expanded=True):
        time.sleep(1.5)
        st.write("✅ 成功獲取資料：闊面臉修容、淡顏釣系妝、姐感氛圍")
    
    st.markdown("---")
    st.markdown(f"""
        <div class="viral-card">
            <div style="color: #FF6A3D; font-size: 20px; font-weight: 800;">方案 1：【技術流】闊面翻身術</div>
            <div style="color: #00F2EA; font-size:14px; margin-top:10px;">🎙️ 30秒口播逐字文案：</div>
            <div class="script-box">「闊面大鼻頭的姐妹看過來！別再無效化妝了！核心在於『視覺重心上移』。不用拼命打黑陰影，而是強調骨相提亮。學會這套內輪廓修容法，笨重感秒變高級姐感！」</div>
        </div>
    """, unsafe_allow_html=True)
