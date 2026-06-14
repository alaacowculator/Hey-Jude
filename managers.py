
from collections import Counter
from data_manager import load_data, save_data, hash_password
from datetime import datetime

# User Manager
class UserManager:
    def __init__(self, file="users.json"):
        self.file = file
        self.users = load_data(file, {})

    def add_user(self, username, password):
        if not username.strip() or not password:   # guard: no empty users
            return
        self.users = load_data(self.file, {})      # reload fresh
        if username in self.users:
            return                                  # don't overwrite existing user
        self.users[username] = hash_password(password)
        save_data(self.file, self.users)

    def authenticate(self, username, password):
        self.users = load_data(self.file, {})      # always read fresh on login
        return username in self.users and self.users[username] == hash_password(password)


# Mood Manager
class MoodManager:
    def __init__(self, file="moods.json"):
        self.file = file
        self.data = load_data(file, [])

    def add_mood(self, user, mood):
        if not user or not mood:                   # guard: never save empty records
            return
        self.data = load_data(self.file, [])       # reload fresh before appending
        self.data.append({"user": user, "mood": mood, "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")})
        save_data(self.file, self.data)

    def get_user_moods(self, user):
        self.data = load_data(self.file, [])       # always fresh
        return [m for m in self.data if m["user"] == user]

    def get_mood_summary(self, user):
        moods = [m["mood"] for m in self.get_user_moods(user)]
        return Counter(moods)


# Journal Manager
class JournalManager:
    def __init__(self, file="journals.json"):
        self.file = file
        self.data = load_data(file, [])

    def add_entry(self, user, text):
        if not user or not text.strip():           # guard: never save empty records
            return
        self.data = load_data(self.file, [])       # reload fresh before appending
        self.data.append({"user": user, "text": text, "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")})
        save_data(self.file, self.data)

    def get_user_entries(self, user):
        self.data = load_data(self.file, [])       # always fresh
        return [j for j in self.data if j["user"] == user]
