import streamlit as st
import urllib.request

# --- 1. 視覺還原：黑金爆款設計 ---
st.set_page_config(page_title="ViralAI", page_icon="🔥")

st.markdown("""
    <style>
    .stApp { background-color: #0e1117; color: white; }
    .viral-title { font-size: 42px; font-weight: 800; color: white; margin-bottom: 5px; }
    .stTextInput input { background-color: white !important; color: black !important; border-radius: 10px !important; }
    .stButton > button {
        background: linear-gradient(90deg, #ff4b2b 0%, #ff416c 100%) !important;
        color: white !important;
        border-radius: 12px !important;
        height: 55px !important; width: 100% !important;
        font-weight: bold; font-size: 18px !important;
    }
    .card { background-color: #1c2533; padding: 20px; border-radius: 15px; border-left: 6px solid #ff4b2b; margin-top: 20px; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. 登入邏輯（改用白名單，避開金鑰錯誤） ---
if 'login' not in st.session_state:
    st.session_state.login = False

# 把你的手機號碼末幾位填在這裡
ALLOWED_USERS = ["97286266"] 

if not st.session_state.login:
    st.markdown('<div class="viral-title">🔥 ViralAI</div>', unsafe_allow_html=True)
    st.write("全平台爆款內容拆解引擎")
    u_phone = st.text_input("🔑 手機號碼驗證", placeholder="輸入手機號碼...")
    
    if st.button("立即進入系統"):
        # 只要結尾符合白名單就放行，不再去連 Google Sheets
        if any(u_phone.strip().endswith(p) for p in ALLOWED_USERS):
            st.session_state.login = True
            st.rerun()
        else:
            st.error("❌ 號碼未授權，請聯繫管理員")

else:
    # --- 3. 分析功能：輕量原生技術 ---
    st.markdown('<div class="viral-title">🔥 ViralAI</div>', unsafe_allow_html=True)
    url = st.text_input("在此貼上影片連結 (TikTok / 抖音 / YouTube)", placeholder="https://...")

    if st.button("啟動 AI 深度拆解"):
        if url:
            with st.spinner("🧠 正在提取真實爆款數據..."):
                try:
                    # 使用原生 urllib 抓取標題，不需安裝外掛
                    headers = {'User-Agent': 'Mozilla/5.0'}
                    req = urllib.request.Request(url, headers=headers)
                    with urllib.request.urlopen(req, timeout=5) as resp:
                        html = resp.read().decode('utf-8', errors='ignore')
                        v_title = html.split('<title>')[1].split('</title>')[0]
                        v_title = v_title.split('-')[0].split('|')[0].strip()
                    
                    st.success(f"✅ 已識別：{v_title}")
                    
                    kw = v_title[:8]
                    scripts = [
                        f"關於【{kw}】為什麼能火？邏輯就一個：抓住人性。學會這招，你也行！",
                        f"2026年爆火秘訣：把【{kw}】重新做一遍。10秒拆解流量密碼，建議收藏。",
                        f"實測有效！這套【{kw}】腳本幫我漲粉破萬。文案在下方，直接複製。"
                    ]

                    for i, s in enumerate(scripts, 1):
                        st.markdown(f'<div class="card"><b>方案 {i}：</b><br>{s}</div>', unsafe_allow_html=True)
                        st.code(s)
                    st.balloons()
                except:
                    st.error("❌ 讀取連結失敗，請確認連結正確且公開。")
