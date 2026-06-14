# 🍏 Hey Jude — Mood Tracker

> *"Love is old, love is new, love is all, love is you"*

A Beatles-themed mental wellness web app — log your moods, write journal entries, and track your emotional patterns over time.

![Python](https://img.shields.io/badge/Python-3.9+-blue?style=flat-square&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red?style=flat-square&logo=streamlit)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)

---

## ✨ Features

- 🔐 **User Authentication** — Secure login & signup with SHA-256 password hashing
- 📝 **Mood Logger** — Log daily moods (Happy, Neutral, Anxious, Sad, Revolutionary)
- 📖 **Journal** — Write and save personal journal entries
- 📜 **History** — View all past mood logs with timestamps
- 📊 **Analytics** — Visual mood frequency bar chart
- 🎨 **Custom UI** — Dark Apple-inspired theme with Abbey Road artwork

---

## 🚀 How to Run

```bash
# 1. Install dependencies
pip install streamlit pandas

# 2. Run the app
streamlit run app.py
```

Open your browser at `http://localhost:8501`

**Demo credentials:**
```
Username: demo
Password: demo
```

---

## 📂 Project Structure

```
hey-jude-mood-tracker/
├── app.py              ← Main Streamlit app + UI + navigation
├── auth.py             ← Login & signup logic
├── managers.py         ← UserManager, MoodManager, JournalManager
├── data_manager.py     ← JSON load/save + password hashing
├── abbey_road.jpg      ← Beatles Abbey Road artwork
├── users.json          ← User credentials (hashed passwords)
├── moods.json          ← Mood log entries
└── journals.json       ← Journal entries
```

---

## 🏗️ Architecture

```
app.py  ──►  AuthManager  ──►  UserManager  ──►  data_manager.py
        ──►  MoodManager   ──►  moods.json
        ──►  JournalManager ──►  journals.json
```

The app follows a **clean separation of concerns**:
- `app.py` handles only UI and navigation
- `managers.py` handles all business logic
- `data_manager.py` handles all file I/O
- `auth.py` handles authentication flow

---

## 🔒 Security

- Passwords are never stored in plain text
- All passwords hashed with **SHA-256** via Python's `hashlib`
- JSON files reload fresh on every operation to prevent stale data

---

## 🛠️ Built With

- [Streamlit](https://streamlit.io/) — Web UI
- [Python](https://python.org/) — Backend logic
- [pandas](https://pandas.pydata.org/) — Data display
- JSON — Lightweight persistent storage

---

> 🎵 Inspired by The Beatles · Built with love · For educational purposes
