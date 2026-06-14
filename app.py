import streamlit as st
import pandas as pd
from managers import UserManager, MoodManager, JournalManager
from auth import AuthManager


st.set_page_config(page_title="Hey Jude", page_icon="🍏", layout="wide")


user_manager = UserManager()
mood_manager = MoodManager()
journal_manager = JournalManager()
auth_manager = AuthManager(user_manager)

# 3. ALAA NANA
def apply_custom_ui():
    st.markdown("""
        <style>
        .stApp { background-color: #1a1a1a; }
        .apple-logo { display: flex; justify-content: center; font-size: 45px; margin-top: -60px; }
        
        
        .quote-style {
            color: #56B85C;
            font-size: 20px;
            text-align: center;
            font-style: italic;
            margin-bottom: 25px;
            font-family: 'Georgia', serif;
        }

        /*Dashboard buttons in the form of rectangles*/
        .mega-button div.stButton > button {
            background-color: #262626 !important; 
            color: #56B85C !important;
            border: 2px solid #56B85C !important; 
            border-radius: 10px !important;
            width: 100% !important; 
            height: 80px !important; 
            font-size: 22px !important;
            font-weight: bold !important;
            margin-bottom: 10px !important;
        }
        
        /* الأزرار العادية (Login/Signup) */
        div.stButton > button {
            background-color: black !important; color: #56B85C !important;
            border: 1px solid #56B85C !important; border-radius: 10px !important;
            width: 100% !important; font-weight: bold !important;
        }

        h1 { color: #56B85C !important; font-size: 28px !important; }
        h2 { color: white !important; font-size: 22px !important; text-align: center; margin-bottom: 5px !important; }
        label { color: #56B85C !important; }
        header {visibility: hidden;} footer {visibility: hidden;}
        </style>
    """, unsafe_allow_html=True)

def show_abbey_road():
    img_name = "abbey_road.jpg"
    try:
        st.image(img_name, use_container_width=True)
    except:
        st.error("Image file not found.")

# --- pages --

class MoodLogPage:
    def display(self):
        apply_custom_ui()
        st.markdown("<h1>How are you feeling?</h1>", unsafe_allow_html=True)
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            moods = ["Happy", "Neutral", "Anxious", "Sad", "Revolutionary"]
            mood = st.selectbox("Select your mood:", moods)
            if st.button("Save Mood"):
                mood_manager.add_mood(st.session_state.username, mood)
                st.success("Mood saved! Let it be.")
            if st.button("← Back"):
                st.session_state.page = "Dashboard"; st.rerun()

class JournalPage:
    def display(self):
        apply_custom_ui()
        st.markdown("<h1>Write Your Thoughts</h1>", unsafe_allow_html=True)
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            content = st.text_area("What's on your mind?", height=200)
            if st.button("Save Entry"):
                if content.strip():
                    journal_manager.add_entry(st.session_state.username, content.strip())
                    st.success("Journal saved!")
                else: st.warning("Please write something.")
            if st.button("← Back"):
                st.session_state.page = "Dashboard"; st.rerun()

class HistoryPage:
    def display(self):
        apply_custom_ui()
        st.markdown("<h1>Your Journey</h1>", unsafe_allow_html=True)
        moods = mood_manager.get_user_moods(st.session_state.username)
        if moods:
            st.table(pd.DataFrame(moods)[['time', 'mood']])
        else: st.info("No records yet.")
        if st.button("← Back"):
            st.session_state.page = "Dashboard"; st.rerun()

class AnalyticsPage:
    def display(self):
        apply_custom_ui()
        st.markdown("<h1>Mood Insights</h1>", unsafe_allow_html=True)
        count = mood_manager.get_mood_summary(st.session_state.username)
        if count:
            df = pd.DataFrame(list(count.items()), columns=['Mood', 'Count'])
            st.bar_chart(df.set_index('Mood'))
        else: st.info("No analytics yet.")
        if st.button("← Back"):
            st.session_state.page = "Dashboard"; st.rerun()

# --- App Controller --- (ALAA NANA)
class App:
    def __init__(self):
        st.session_state.setdefault("logged_in", False)
        st.session_state.setdefault("page", "Login")
        st.session_state.setdefault("username", "")
        self.pages = {
            "MoodLog": MoodLogPage(),
            "Journal": JournalPage(),
            "ViewLogs": HistoryPage(),
            "Analytics": AnalyticsPage()
        }
#ALAA NANA
    def run(self):
        apply_custom_ui()
        if not st.session_state.logged_in:
            left_col, right_col = st.columns([1, 2])
            with left_col:
                st.markdown("<div class='apple-logo'>🍏</div>", unsafe_allow_html=True)
                st.markdown("<h1>Hey Jude</h1>", unsafe_allow_html=True)
                tab1, tab2 = st.tabs(["Sign In", "Sign Up"])
                with tab1:
                    u = st.text_input("Username", key="li_u")
                    p = st.text_input("Password", type="password", key="li_p")
                    if st.button("Login"):
                        if not u.strip() or not p:
                            st.error("Please enter both username and password.")
                        elif auth_manager.login(u.strip(), p):
                            st.session_state.logged_in = True
                            st.session_state.username = u.strip()
                            st.session_state.page = "Dashboard"; st.rerun()
                        else:
                            st.error("Invalid credentials")
                with tab2:
                    new_u = st.text_input("New Username", key="su_u")
                    new_p = st.text_input("New Password", type="password", key="su_p")
                    if st.button("Create Account"):
                        if not new_u.strip() or not new_p:
                            st.error("Username and password cannot be empty.")
                        else:
                            user_manager.add_user(new_u.strip(), new_p)
                            st.success("Account created! Please Sign In.")
            with right_col:
                show_abbey_road()

        elif st.session_state.page == "Dashboard":
           
            st.markdown(f"<h2>Welcome, {st.session_state.username}</h2>", unsafe_allow_html=True)
            
           
            st.markdown("<div class='quote-style'>Love is old, love is new, love is all, love is you</div>", unsafe_allow_html=True)
            
            # أزرار الداشبورد (المستطيلات العريضة)
            st.markdown('<div class="mega-button">', unsafe_allow_html=True)
            if st.button("📝 LOG MOOD"): st.session_state.page = "MoodLog"; st.rerun()
            if st.button("📖 JOURNAL"): st.session_state.page = "Journal"; st.rerun()
            if st.button("📜 HISTORY"): st.session_state.page = "ViewLogs"; st.rerun()
            if st.button("📊 ANALYTICS"): st.session_state.page = "Analytics"; st.rerun()
            st.markdown('</div>', unsafe_allow_html=True)
            
            if st.button("Logout"):
                st.session_state.logged_in = False
                st.session_state.page = "Login"; st.rerun()
            
            show_abbey_road()
        else:
            self.pages[st.session_state.page].display()#  Navigation Flow

if __name__ == "__main__":
    App().run()