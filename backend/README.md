# 🚗 Smart Parking Backend (FastAPI)

Dự án mô phỏng **hệ thống quản lý bãi đỗ xe thông minh**  
Xây dựng bằng **FastAPI** – tích hợp mô hình AI từ **Roboflow** để nhận diện xe, biển số, và kiểm tra chỗ đỗ.

---

## 🧱 Cấu trúc thư mục

```
fastapi_parking/
│── app/
│   ├── main.py              # file chạy chính (FastAPI entrypoint)
│   ├── routers/
│   │    └── parking.py      # route xử lý logic nhận diện, trạng thái
│   ├── models/              # định nghĩa database (nếu dùng)
│   ├── database.py          # cấu hình database (SQLite, MySQL,...)
│   └── config.py            # cấu hình chung (API key, biến môi trường,...)
│
│── requirements.txt         # danh sách thư viện cần cài
│── README.md
└── .gitignore
```

---

## ⚙️ Cài đặt và chạy thử

### 1️⃣ Tạo và kích hoạt môi trường ảo

```bash
python -m venv venv
```

- **Windows:** `venv\Scripts\activate`
- **Linux/macOS:** `source venv/bin/activate`

---

### 2️⃣ Cài đặt thư viện

```bash
pip install -r requirements.txt
```

Nếu chưa có file `requirements.txt`:
```bash
pip install fastapi uvicorn
pip freeze > requirements.txt
```

---

### 3️⃣ Chạy server FastAPI

```bash
uvicorn app.main:app --reload
```

- Truy cập: http://127.0.0.1:8000  
- Tài liệu API: http://127.0.0.1:8000/docs

---

## 🧪 Kiểm tra nhanh API

### ✅ Kiểm tra backend hoạt động

```bash
GET /
```
**Kết quả:**
```json
{"message": "🚗 Smart Parking Backend is running!"}
```

### ✅ Kiểm tra trạng thái bãi xe

```bash
GET /parking/status
```
**Kết quả mẫu:**
```json
{"parking_status": "available", "slots_free": 12}
```

---

## 🧩 Tích hợp Roboflow API (Tùy chọn)

```bash
pip install roboflow python-multipart
```

Ví dụ trong code:

```python
from roboflow import Roboflow

rf = Roboflow(api_key="YOUR_API_KEY")
project = rf.workspace().project("parking-detection")
model = project.version(1).model
```

---

## 👨‍💻 Tác giả
Smart Parking Simulation  
Phát triển bởi [UET]

