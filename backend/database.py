import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

try:
    client = MongoClient(os.getenv("MONGO_URI"))
    db = client[os.getenv("MONGO_DB")]
    faq_collection = db["faqs"]
    print("✅ 成功連線 MongoDB Atlas")

except Exception as e:
    print("❌ 連線失敗，請檢查 .env 設定")
    faq_collection = None
