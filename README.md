# 📄 智能客服系統 - 專案說明

本專案是一個使用 FastAPI + MongoDB 搭配 Angular Material 建構的智能客服系統，具備常見問題查詢、GPT 回答與 UI 互動功能，適合部署至雲端或本地開發測試。

---

## 🧩 技術架構

* **前端**：Angular 15+、Angular Material UI
* **後端**：FastAPI、Pymongo
* **資料庫**：MongoDB Atlas
* **AI模型**：OpenAI GPT-3.5
* **部署平台**：Zeabur / Local

---

## 📁 專案結構

```bash
fax-management/
├── backend/                # FastAPI 後端
│   ├── main.py             # FastAPI 入口
│   ├── routes.py           # API 路由定義
│   ├── database.py         # MongoDB 連線設定
│   ├── openai_client.py    # GPT 串接邏輯
│   ├── models.py           # Pydantic 資料模型
│   └── seed.py             # 初始 FAQ 資料填充
│
├── frontend/              # Angular 前端
│   ├── src/app/pages/chat-bot/
│   │   └── chat-bot.component.*   # 客服聊天 UI
│   ├── proxy.conf.json     # 本地 API 代理設定
│   └── app.routes.ts       # 路由配置
│
├── package.json           # 通用啟動指令（含 concurrently）
└── README.md              # 本說明文件
```

---

## 🚀 快速啟動

### ✅ 安裝依賴

```bash
cd backend
pip install -r requirements.txt

cd ../frontend
npm install
```

### ▶ 一鍵啟動

根目錄的 `package.json` 中，新增以下內容：

```json
{
  "scripts": {
    "start:dev": "concurrently \"cd backend && uvicorn main:app --reload --port 8000\" \"cd frontend && ng serve\""
  },
  "devDependencies": {
    "concurrently": "^8.0.0"
  }
}
```

執行：

```bash
npm install concurrently -D
npm run start:dev
```

---

## 🧪 測試功能

* 啟動後，前往 `http://localhost:4200` 使用介面。
* 點擊常見問題 → 顯示建議問題
* 點擊任一問題 → 發送至後端：

  * 若 MongoDB 有相符項目 → 回傳資料
  * 若無 → 傳送至 OpenAI GPT 回答

---

## 📦 MongoDB FAQ 資料格式

```json
{
  "question": "如何開戶？",
  "answer": "請攜帶身分證及健保卡至分行辦理。",
  "category": "service"
}
```


---

開發者：Joanne
更新時間：2025-05-04
