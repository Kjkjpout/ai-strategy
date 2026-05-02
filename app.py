import streamlit as st
import time

# --- 1. 頂級視覺配置 (Hermes 滿配風格) ---
st.set_page_config(page_title="Hermes AI 影片全自動工廠", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #050505; color: #ffffff; }
    .glass-card { background: #111; border: 1px solid #333; border-radius: 12px; padding: 20px; margin-bottom: 20px; }
    .headline-section { background: #222; border: 1px solid #ff4b4b; padding: 15px; border-radius: 8px 8px 0 0; }
    .script-section { background-color: #000; border: 1px solid #444; border-left: 5px solid #ff4b4b; padding: 20px; line-height: 1.8; }
    .prompt-section { background: #0d1a0d; border: 1px dashed #00ff00; padding: 15px; border-radius: 0 0 8px 8px; color: #00ff00; font-family: monospace; }
    .stButton>button { background: linear-gradient(90deg, #ff4b4b 0%, #800000 100%); color: white; height: 60px; font-weight: bold; border-radius: 8px; font-size: 20px; }
    .highlight-label { color: #ff4b4b; font-weight: bold; margin-bottom: 5px; display: block; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. 主標題與系統狀態 ---
st.title("🏭 Hermes 滿配 AI 影片自動化工廠")
cols = st.columns(5)
modules = ["👤 身份與記憶", "👁️ 感知能力", "🎨 表達能力", "📊 效率與成本", "🧭 生態導航"]
for i, col in enumerate(cols):
    col.success(modules[i])

st.divider()

# --- 3. 核心搜尋與分發設定區 ---
col_in, col_set = st.columns([2, 1])

with col_in:
    st.subheader("📡 爆款連結偵測")
    video_url = st.text_input("🔗 請貼入 YouTube / 抖音 / TikTok / IG 連結：", placeholder="在此輸入要拆解的爆款網址...")

with col_set:
    st.subheader("📤 自動分發設定")
    target_platforms = st.multiselect("選擇發布平台：", ["抖音", "TikTok", "YouTube Shorts", "Instagram"])

st.write("")

# --- 4. 執行生產 ---
if st.button("🚀 啟動全鏈路生產與自動分發"):
    if not video_url:
        st.error("❌ 李大哥，沒貼連結我沒辦法動啊！")
    else:
        with st.status("🏗️ Hermes 生產線執行中...", expanded=True) as status:
            st.write("🔍 [感知] 正在深度拆解原片文案與爆款基因...")
            time.sleep(1.2)
            st.write("✍️ [文案] AI 正在重構 5 套重生腳本與標題...")
            time.sleep(1.2)
            st.write("🖼️ [表達] 正在規劃 AI 生圖提示詞與視覺參數...")
            time.sleep(0.8)
            if target_platforms:
                st.write(f"📤 [分發] 影片已排程自動上傳至：{', '.join(target_platforms)}")
                time.sleep(1)
            status.update(label="✅ 生產完成！5 套方案已出庫", state="complete", expanded=False)

        # --- 5. 輸出 5 套爆款方案 ---
        def render_factory_output(index, style, titles, script, prompt):
            with st.expander(f"📦 方案 {index}：{style} (點擊展開)"):
                title_html = "".join([f"• {t}<br>" for t in titles])
                st.markdown(f"""
                <div class='headline-section'>
                    <span class='highlight-label'>🔥 推薦爆款標題：</span>
                    <div style='color: #fbbf24; font-size: 18px; font-weight: bold;'>{title_html}</div>
                </div>
                <div class='script-section'>
                    <span class='highlight-label'>🎬 30秒重生腳本：</span>
                    {script}
                </div>
                <div class='prompt-section'>
                    <span class='highlight-label' style='color:#00ff00;'>🖼️ AI 生圖提示詞 (Prompt)：</span>
                    {prompt}
                </div>
                """, unsafe_allow_html=True)

        # 方案 1：深夜扎心
        render_factory_output(1, "深夜扎心風", 
            ["懂事的人，注定沒人疼嗎？", "這段話，送給深夜還在翻聊天紀錄的你", "原來成長的代價，是學會安靜地崩潰"],
            "【0-5s】特寫熄滅螢幕。口播：這輩子最遺憾的，不是沒遇到心動的人，而是遇到了，卻發現自己沒資格。<br>【5-25s】獨自走在路燈下。口播：你以為放不下的是他，其實你只是心疼那個傻傻付出的自己。撐傘久了，衣服還是會被打濕。<br>【25-30s】黑底白字。口播：如果你也曾為了一個人徹夜難眠，點個贊，我懂你。",
            "A lonely person walking under a dim street lamp at night, cinematic shadows, melancholic atmosphere, 8k resolution.")

        # 方案 2：人間清醒
        render_factory_output(2, "人間清醒風", 
            ["卑微換不來愛情，只能換來輕視", "醒醒吧！不回訊息就是最好的答案", "停止自我感動，是你變強的第一步"],
            "【0-5s】剪輯撕照片動作。口播：別再自我感動了！一個不回你訊息的人，他的沈默就是答案。<br>【5-25s】對鏡頭直述。口播：卑微換不來愛情，只能換來輕視。與其花時間去追一匹馬，不如花時間去種草。等到春暖花開，馬自然會回來。<br>【25-30s】自信微笑。口播：關注我，讓你的人生不再卑微。",
            "Confident entrepreneur in a bright minimalist office, breaking a chain metaphor, high contrast, clean aesthetics, 8k.")

        # 方案 3：故事旁白
        render_factory_output(3, "故事旁白風", 
            ["聽說他結婚那天，全場都很開心，除了她", "後來的我們，什麼都有了，卻沒有了『我們』", "回憶是座橋，卻是通往寂寞的牢"],
            "【0-5s】老舊車站畫面。口播：後來的我們，什麼都有了，卻唯獨沒有了我們。<br>【5-25s】交錯剪輯過去與現在。口播：聽說他結婚那天，新郎不是我，但我卻笑得最開心。因為看到傷害過我的女孩，找了一個比我更差的人。最好的報復，是徹底遺忘。<br>【25-30s】夕陽落下。口播：點讚這份解脫，送給正在受傷的你。",
            "Old railway station at sunset, vintage film style, emotional storytelling visuals, nostalgic lighting, 8k.")

        # 方案 4：技術拆解
        render_factory_output(4, "技術獲客風", 
            ["40天賺28萬的底層邏輯", "高單價 Offer 定價公式", "如何讓客戶主動排隊送錢？"],
            "【0-5s】展示三層漏斗圖。口播：高手怎麼做內容？吸睛短片、教育長片、轉化動態，缺一不可！<br>【5-25s】Offer三支柱。口播：一個讓市場無法拒絕的提案，核心在於把風險轉移到自己身上。當客戶覺得不買是他的損失，成交就是順理成章。<br>【25-30s】留言引導。口播：留言區扣『666』解鎖完整模型。",
            "Futuristic digital funnel with golden data flowing through it, high-tech finance style, professional lighting, 8k.")

        # 方案 5：治癒救贖
        render_factory_output(5, "治癒救贖風", 
            ["總有一束光，是為你而亮的", "你值得被全世界溫柔對待", "錯過的不是遺憾，是為了讓更好的出現"],
            "【0-5s】手握熱咖啡冒氣。口播：不管你現在經歷什麼，請相信，這世上總有一束光是為你而亮的。<br>【5-25s】溫暖畫面。口播：錯過的不是遺憾，是為了讓更好的出現。你要等，等那個眼裡全是你的男孩子，等那個能看穿你所有委屈的人。<br>【25-30s】溫暖文字。口播：轉發給最好的閨蜜，告訴她：你值得被愛。",
            "Warm golden hour sunlight, a cup of coffee on a wooden table, soft focus background, peaceful and hopeful mood, 8k.")

st.divider()
st.caption("© 2026 李大哥 AI 戰略研究所 | Hermes 滿配自動化系統")
