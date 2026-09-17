# GCP deployment preparation

Chưa có tài nguyên GCP được tạo hay site được deploy bởi skeleton này.

- Cloud Run chạy Docker image, lắng nghe biến PORT; cấu hình APP_ENV=staging/production.
- DATABASE_URL là secret bắt buộc, cung cấp bằng Secret Manager.
- Kết nối Cloud SQL qua cơ chế GCP hỗ trợ; không mở database public không bảo vệ.
- Cloud Storage lưu media; service account chỉ nhận quyền cần thiết.
- Tách project/resource DB, bucket, secrets giữa staging và production.
- Chạy Alembic bằng job riêng trước rollout; cân nhắc migration backward-compatible.
- Liveness dùng /health; /ready kiểm tra DB, không xác nhận schema đã migrate.
- Baseline theo SPEC: 1 vCPU, 1 GiB, concurrency 20, min 1, max 20.
- Pool mỗi instance: 5 + 2 overflow; tối đa lý thuyết 140 application connections.
- Cần kiểm thử và điều chỉnh theo DB sizing; đây không phải cam kết hiệu năng.
- HTMX hiện được tải từ CDN với version cố định. Vendor bản đã kiểm tra cùng
  license vào static trước khi muốn vận hành không phụ thuộc CDN.
- Hoàn thiện auth, CSRF, rate limiting, backup, monitoring và test trước production.
- CI chỉ kiểm tra/build, không tự động deploy. Dùng Workload Identity Federation
  khi bổ sung CD; tránh service-account key lưu dài hạn trong GitHub.
