import csv
import os
from collections import deque


class DbQueue:
    def __init__(self, max_len=100):
        self.db = deque()
        self.max_len = max_len

    def push(self, text_id):
        if len(self.db) > self.max_len:
            self.db.popleft()
        self.db.append(text_id)

    def find(self, text_id):
        return text_id in self.db

    def save_data(self):
        with open("history_msg_id.csv", "w") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(list(self.db))

    def load_data(self):
        if os.path.exists("history_msg_id.csv"):
            with open("history_msg_id.csv", "r") as csvfile:
                ids = csv.reader(csvfile)
                for text_ids in ids:
                    for text_id in text_ids:
                        self.db.append(text_id)

    def delete_data(self):
        if os.path.exists("history_msg_id.csv"):
            os.remove("history_msg_id.csv")
