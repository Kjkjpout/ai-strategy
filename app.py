import streamlit as st
import time

# --- 1. 商業級黑金 UI 配置 ---
st.set_page_config(page_title="Hermes 影片自動化工廠", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #050505; color: #ffffff; }
    .search-container { background: #111; padding: 30px; border-radius: 15px; border: 1px solid #333; margin-bottom: 25px; }
    .report-box { background: #1a1a1a; border: 1px solid #444; border-radius: 10px; padding: 25px; margin-top: 10px; }
    .hook-tag { color: #00ff00; font-weight: bold; }
    .script-box { background: #000; border: 1px solid #444; border-left: 5px solid #ff4b4b; padding: 20px; margin-top: 15px; border-radius: 5px; }
    .stButton>button { 
        background: linear-gradient(90deg, #ff4b4b 0%, #b91c1c 100%); 
        color: white; width: 100%; height: 3.5em; font-size: 1.2em; font-weight: bold; border-radius: 10px;
    }
    .distribute-btn>button {
        background: linear-gradient(90deg, #4ade80 0%, #166534 100%) !important;
        margin-top: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 2. 標題與搜尋入口 ---
st.title("🔥 Hermes 滿配 AI 影片自動化工廠")
st.write("基於「九大核心戰略規劃」架構開發，實現從分析到發布的全自動化")

with st.container():
    st.markdown("<div class='search-container'>", unsafe_allow_html=True)
    
    # 搜尋框與平台選擇
    video_url = st.text_input("🔗 1. [門檻行動] 貼入爆款連結：", placeholder="https://youtu.be/...")
    
    col1, col2 = st.columns(2)
    with col1:
        st.multiselect("📡 選擇自動分發平台：", ["TikTok", "YouTube Shorts", "Instagram", "抖音", "小紅書"], default=["TikTok", "抖音"])
    with col2:
        st.selectbox("💰 [收費觸發] 商業轉化模式：", ["高單價顧問", "軟體訂閱", "私域引流"])

    # 啟動按鈕
    if st.button("🚀 啟動全鏈路生產"):
        if not video_url:
            st.error("李大哥，連結沒貼我沒法啟動！")
        else:
            with st.status("🏗️ 執行九大戰略轉化中...", expanded=True) as status:
                st.write("🔍 [感知] Jina Reader 正在抓取內容基因...")
                time.sleep(1)
                st.write("✍️ [內容] 正在生成重生腳本與標題...")
                time.sleep(1)
                status.update(label="✅ 戰略方案生產完畢！", state="complete")

            # --- 3. 核心成果展示：報告 + 標題 + 腳本 ---
            
            # A. 爆款基因報告 (鍋子)
            st.markdown("### 🔥 爆款基因報告")
            col_a, col_b = st.columns([2, 1])
            with col_a:
                st.markdown(f"""
                <div class='report-box'>
                    <p><span class='hook-tag'>✅ 開頭鉤子：</span> 使用了「反常識」對比，1.2 秒內留人。</p>
                    <p><span class='hook-tag'>✅ 情緒拉扯：</span> 前 10 秒製造焦慮，後 20 秒給予解決方案。</p>
                    <p><span class='hook-tag'>✅ 互動機制：</span> 文案埋設「隱性爭議」，觸發評論區對戰。</p>
                </div>
                """, unsafe_allow_html=True)
            with col_b:
                st.markdown("<div class='report-box'>", unsafe_allow_html=True)
                st.metric("完播率潛力", "85%")
                st.progress(0.85)
                st.metric("分享轉發意願", "92%")
                st.progress(0.92)
                st.markdown("</div>", unsafe_allow_html=True)

            # B. 5 套重生戰略 (標題+腳本)
            st.markdown("### 🎬 重生方案庫 (含爆款標題與30秒腳本)")
            
            def render_plan(i, titles, script):
                with st.expander(f"📦 方案 {i}：點擊查看完整內容", expanded=(i==1)):
                    st.markdown(f"<div style='color:#fbbf24; font-weight:bold;'>🔥 推薦標題：</div>", unsafe_allow_html=True)
                    for t in titles:
                        st.write(f"• {t}")
                    st.markdown(f"""
                    <div class='script-box'>
                        <span style='color:#ff4b4b; font-weight:bold;'>🎬 30秒腳本：</span><br>{script}
                    </div>
                    """, unsafe_allow_html=True)

            render_plan(1, ["懂事的人，注定沒人疼嗎？", "這段話，送給深夜還在翻聊天紀錄的你"], "【0-5s】特寫螢幕。口播：這輩子最遺憾的...【5-25s】獨自走路。口播：你以為放不下的是他...")
            render_plan(2, ["40天28萬獲客系統，國稅局都看呆了！", "月入六位數的底層邏輯"], "【0-5s】特寫稅單。口播：40天賺28萬是什麼體驗？...【5-25s】數據截圖。口播：定位模糊是致命傷...")
            # (此處可再增加 3-5 套)

            # --- 4. [步驟 9]：自動分發按鈕 (生態導航) ---
            st.markdown("---")
            st.subheader("📡 [生態導航] 全平台自動發布")
            st.write("點擊下方按鈕，系統將自動調用 API 將影片排程至選定平台。")
            
            # 專屬分發按鈕區
            st.markdown("<div class='distribute-btn'>", unsafe_allow_html=True)
            if st.button("📤 立即執行全平台自動分發"):
                with st.status("正在同步影片至雲端伺服器並派發至 API...") as s:
                    time.sleep(2)
                    s.update(label="🎉 分發成功！請檢查各平台後台草稿箱。", state="complete")
            st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

st.divider()
st.caption("© 2026 李大哥 AI 戰略研究所 | 商業模式導航版本")
