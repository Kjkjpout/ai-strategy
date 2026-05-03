import streamlit as st
import pandas as pd

# --- 1. 視覺渲染 (與你的截圖 1:1 匹配) ---
st.set_page_config(page_title="ViralAI", page_icon="🔥")

st.markdown("""
    <style>
    .stApp { background-color: #0e1117; color: white; }
    .viral-title { font-size: 45px; font-weight: 800; color: white; }
    .stTextInput input { background-color: white !important; color: black !important; border-radius: 12px !important; }
    .stButton > button {
        background: linear-gradient(90deg, #ff4b2b 0%, #ff416c 100%) !important;
        color: white !important;
        border: none !important;
        border-radius: 15px !important;
        height: 60px !important;
        width: 100% !important;
        font-weight: bold;
        font-size: 22px !important;
    }
    .card { background-color: #1c2533; padding: 25px; border-radius: 15px; border-left: 8px solid #ff4b2b; margin-top: 25px; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. 登入狀態管理 ---
if 'login' not in st.session_state:
    st.session_state.login = False

# --- 3. 登入介面 ---
if not st.session_state.login:
    st.markdown('<div class="viral-title">🔥 ViralAI</div>', unsafe_allow_html=True)
    st.write("全平台爆款內容拆解引擎")
    u_phone = st.text_input("🔑 手機號碼驗證", placeholder="請輸入註冊手機號碼...")
    
    if st.button("立即進入系統"):
        # 這裡不使用 st.connection，改用最原始、最不會跳開的 CSV 讀取法
        try:
            # 請將下方的 URL 替換成你的 Google Sheet "發布到網路" 的 CSV 連結
            # 這是最穩定的連線方式，不會因為 Secrets 讀取不到而跳開
            SHEET_URL = st.secrets["connections"]["gsheets"]["url"].replace('/edit?usp=sharing', '/export?format=csv')
            df = pd.read_csv(SHEET_URL)
            
            # 清理資料確保比對正確
            df['phone'] = df['phone'].astype(str).str.strip()
            
            if u_phone.strip() in df['phone'].values:
                # 簡單權限檢查
                st.session_state.login = True
                st.rerun()
            else:
                st.error("❌ 手機號碼未授權")
        except Exception as e:
            st.error("系統連線中，請再按一次登入")

else:
    # --- 4. 爆款分析主介面 ---
    st.markdown('<div class="viral-title">🔥 ViralAI</div>', unsafe_allow_html=True)
    st.write("### 🚀 輸入影片連結，AI 現場分析")
    
    url = st.text_input("在此貼上連結 (TikTok/YouTube/抖音)", placeholder="https://...")

    if st.button("啟動 AI 深度拆解"):
        if url:
            with st.spinner("🧠 正在提取爆款基因..."):
                try:
                    # 使用 Python 內置工具，不需安裝任何額外套件
                    import urllib.request
                    headers = {'User-Agent': 'Mozilla/5.0'}
                    req = urllib.request.Request(url, headers=headers)
                    with urllib.request.urlopen(req, timeout=5) as response:
                        content = response.read().decode('utf-8')
                        # 暴力抓標題
                        title = content.split('<title>')[1].split('</title>')[0]
                        v_title = title.split('-')[0].split('|')[0].strip()
                    
                    st.success(f"✅ 已分析影片：{v_title}")
                    
                    # 生成 5 套文案
                    kw = v_title[:8]
                    scripts = [
                        f"為什麼【{kw}】能火？底層邏輯就一個：抓住焦慮。學會這招，你也行！",
                        f"2026年爆火秘訣：把【{kw}】重新做一遍。10秒拆解流量密碼。",
                        f"實測有效！這套【{kw}】腳本幫我漲粉破萬。文案在下方，直接複製。",
                        f"沒流量？試試把開頭換成：關於【{kw}】你不知道的真相。流量瞬間炸開。",
                        f"豆包 AI 配合這套【{kw}】腳本簡解絕了！10秒生成高質感內容，現在就試！"
                    ]

                    for i, s in enumerate(scripts, 1):
                        st.markdown(f'<div class="card"><b>🔥 方案 {i}：</b><br>{s}</div>', unsafe_allow_html=True)
                        st.code(s)
                    st.balloons()
                except:
                    st.error("❌ 讀取連結失敗，請確認連結正確且影片為公開。")
        else:
            st.warning("請先輸入連結")
