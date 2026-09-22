# Grade 12 English Learning Platform
## Temporary Suspended
Nền tảng học tiếng Anh lớp 12 theo SPEC-001 Phase 1. Kiến trúc modular monolith:
FastAPI + Jinja2 + HTMX, PostgreSQL (asyncpg), SQLAlchemy Async và Alembic.

---

## 📌 Trạng thái dự án

Hiện tại dự án đang ở giai đoạn **Skeleton nền tảng (Phase 1 Foundation)**, chuẩn bị cho việc phát triển các tính năng MVP.

### ✅ Đã hoàn thành
- **App Factory & Lifespan**: Khởi tạo ứng dụng FastAPI với async lifespan quản lý connection pool (SQLAlchemy async engine + asyncpg).
- **Cấu hình môi trường**: Tự động load cấu hình từ `.env` qua `pydantic-settings` (`Settings`).
- **Health check & Readiness**:
  - `/health`: Liveness probe (trả về trạng thái hoạt động của server).
  - `/ready`: Readiness probe (kiểm tra kết nối thực tế tới PostgreSQL).
- **Giao diện cơ bản**: Tích hợp Jinja2 templates, static assets (CSS) và HTMX fragment sample.
- **Khung Module chuẩn hóa**: Định hình router cho các module: `auth`, `users`, `learning`, `flashcards`, `srs`, `games`, `admin`.
- **Cơ sở dữ liệu**: Docker Compose cho PostgreSQL 16 cùng script khởi tạo ban đầu (`db/init/schemas.sql`, `db/init/seed.sql`).
- **Quản lý gói**: Quản lý dependency và môi trường ảo thông qua **Poetry** (`pyproject.toml`, `poetry.lock`).
- **File thực thi**: Hỗ trợ chạy trực tiếp qua `app/run.py` hoặc lệnh `uvicorn`.

### ⏳ Đang & Chưa triển khai
- Nghiệp vụ xác thực: Đăng ký, đăng nhập, xác thực OTP, quản lý phiên (Session/JWT).
- Nghiệp vụ học tập: CRUD Unit/Lesson, quản lý Deck/Flashcard, thuật toán lặp lại ngắt quãng SRS/FSRS.
- Mini-games: Game engine, sinh đề bài và tính điểm.
- Lưu trữ media (Cloud Storage), Rate Limiting, CSRF Protection.
- Triển khai Cloud (GCP Cloud Run / Cloud SQL).

---

## 📁 Cấu trúc thư mục

```text
grade12-english-learning-platform/
├── app/                        # Mã nguồn ứng dụng chính
│   ├── core/                   # Cấu hình lõi & dependencies dùng chung
│   │   ├── config.py           # Settings & biến môi trường (.env)
│   │   ├── database.py         # Quản lý AsyncSession & kết nối DB
│   │   ├── exceptions.py       # Xử lý custom exceptions
│   │   ├── security.py         # Dependencies bảo mật & quyền truy cập
│   │   └── templates.py        # Cấu hình Jinja2 templates
│   ├── modules/                # Các module nghiệp vụ (Modular Monolith)
│   │   ├── admin/              # Quản trị hệ thống
│   │   ├── auth/               # Xác thực & phân quyền
│   │   ├── flashcards/         # Quản lý từ vựng & flashcards
│   │   ├── games/              # Mini-games & bài tập tương tác
│   │   ├── learning/           # Quản lý bài học theo chương trình SGK
│   │   ├── srs/                # Thuật toán Spaced Repetition System (FSRS)
│   │   └── users/              # Thông tin & hồ sơ người dùng
│   ├── static/                 # Static files (CSS, JS, images, icons)
│   │   └── app.css             # Stylesheet chính
│   ├── templates/              # Giao diện Jinja2 HTML
│   │   ├── user/               # Templates dành cho học sinh/người dùng
│   │   └── admin/              # Templates dành cho quản trị viên
│   ├── main.py                 # FastAPI app factory, lifespan & core endpoints
│   ├── models.py               # Import tập trung tất cả SQLAlchemy ORM models
│   └── run.py                  # Script khởi chạy server local bằng uvicorn
├── db/                         # Cơ sở dữ liệu & scripts
│   └── init/                   # Script khởi tạo ban đầu cho PostgreSQL
│       ├── schemas.sql         # Định nghĩa cấu trúc bảng
│       └── seed.sql            # Dữ liệu mẫu ban đầu
├── docs/                       # Tài liệu kỹ thuật, roadmap & deployment
├── tests/                      # Unit tests & Integration tests
├── .env.example                # File mẫu cấu hình biến môi trường
├── docker-compose.yaml         # Docker Compose (chạy PostgreSQL service)
├── Dockerfile                  # Dockerfile build image cho ứng dụng
├── pyproject.toml              # Khai báo dependencies & cấu hình project (Poetry/Tools)
└── README.md                   # Tài liệu hướng dẫn dự án
```

---

## 🚀 Hướng dẫn chạy ứng dụng

Ứng dụng hiện hỗ trợ chạy **Server trên máy local** (với Poetry) kết hợp **PostgreSQL trên Docker**.

### 1. Yêu cầu hệ thống
- **Python**: `>= 3.11`
- **Poetry**: Đã cài đặt trên máy
- **Docker / Docker Desktop**: Đang chạy

---

### 2. Cài đặt môi trường & Dependencies

Cài đặt các thư viện cần thiết bằng Poetry:

```powershell
poetry install
```

---

### 3. Cấu hình biến môi trường

Tạo file `.env` từ `.env.example`:

- **Windows PowerShell:**
  ```powershell
  Copy-Item .env.example .env
  ```
- **macOS / Linux:**
  ```bash
  cp .env.example .env
  ```

Nội dung cấu hình mặc định cho môi trường local:
```env
APP_ENV=local
DATABASE_URL=postgresql+asyncpg://english:english_local@localhost:5432/english
DB_POOL_SIZE=5
DB_MAX_OVERFLOW=2
POSTGRES_USER=english
POSTGRES_PASSWORD=english_local
POSTGRES_DB=english
```

---

### 4. Khởi động Cơ sở dữ liệu (PostgreSQL)

Chạy container PostgreSQL nền thông qua Docker Compose:

```powershell
docker compose up -d db
```

---

### 5. Khởi chạy Web Application

Bạn có thể chạy ứng dụng bằng một trong hai cách:

#### Cách 1: Sử dụng lệnh `uvicorn` qua Poetry (Khuyến nghị)
```powershell
poetry run uvicorn app.main:app --host 127.0.0.1 --port 8000 --reload
```

#### Cách 2: Chạy thông qua file `app/run.py`
```powershell
poetry run python app/run.py
```

---

### 6. Truy cập ứng dụng

Sau khi khởi chạy thành công, truy cập các đường dẫn sau trên trình duyệt:
- 🌐 **Trang chủ**: [http://127.0.0.1:8000](http://127.0.0.1:8000)
- 📖 **API Docs (Swagger UI)**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- ❤️ **Health Check**: [http://127.0.0.1:8000/health](http://127.0.0.1:8000/health)
- 🔍 **DB Readiness**: [http://127.0.0.1:8000/ready](http://127.0.0.1:8000/ready)

---

### 7. Dừng hệ thống

- Để dừng tiến trình Web server: Nhấn `Ctrl + C` tại terminal đang chạy server.
- Để dừng container PostgreSQL:
  ```powershell
  docker compose down
  ```
  *(Dữ liệu trong database sẽ được lưu lại trong Docker volume `postgres_data`).*
- Để dừng và xóa toàn bộ dữ liệu database:
  ```powershell
  docker compose down -v
  ```

---

## 🧪 Kiểm tra & Đảm bảo chất lượng mã nguồn

Chạy kiểm tra linting, typing và unit tests:

```powershell
# Kiểm tra định dạng & linting
poetry run ruff check .
poetry run ruff format --check .

# Kiểm tra kiểu dữ liệu (Type check)
poetry run mypy app

# Chạy Unit tests
poetry run pytest -q
```

---

## 🛠 Quy ước phát triển

1. Tạo nhánh theo định dạng `feat/<tên-tính-năng>` hoặc `fix/<tên-lỗi>`.
2. Router chỉ tiếp nhận request; Service xử lý business/transaction; Repository/Query thực thi truy vấn DB.
3. Tuyệt đối không commit secrets, thông tin nhạy cảm hoặc tài liệu có bản quyền vào repository.
4. Xem thêm chi tiết tại [Kế hoạch phát triển](docs/roadmap.md) và [Hướng dẫn triển khai](docs/deployment.md).

