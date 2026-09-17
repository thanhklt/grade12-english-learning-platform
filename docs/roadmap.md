# Phase 1 roadmap

1. Foundation: skeleton hiện tại; xác nhận CI và chạy local trên máy các thành viên.
2. Auth: Argon2 password hash; email/username canonicalization; OTP hash 6 chữ số,
   TTL 10 phút, tối đa 5 lần thử, resend 60 giây; DB-backed session với token hash.
   Chưa verify thì chưa tạo session. Reset password revoke toàn bộ session cũ.
3. Learning/Admin: Unit → Lesson → Content, publish ở cấp Unit, audit,
   Cloud Storage image/audio. Enforce ADMIN trên backend.
4. Flashcards: private deck/card, ownership trên mọi query, CSV import/export
   không mang theo tiến độ SRS.
5. SRS: tích hợp FSRS; due trước new; mặc định 20 new/day/deck;
   progress + immutable history trong cùng transaction; idempotency và lock.
6. Games: bốn strategies; fixed Unit game và game từ deck đã kiểm tra quyền;
   backend giữ đáp án và chấm điểm.
7. GCP: staging/production tách biệt; deploy thủ công trước khi thiết lập CD.
8. Stabilization: integration/security/load tests với workload thực tế.

Mục tiêu của SPEC: 1.000 concurrent users, 200 RPS normal, 500 RPS burst,
p95 API <500 ms và 5xx <1%. Skeleton chưa chứng minh các mục tiêu này.

Admin dependency hiện fail closed. Khi triển khai auth, đọc session từ DB,
kiểm tra expiry/revoked/user ACTIVE/email verified và role ADMIN.
Thêm CSRF cho request thay đổi trạng thái; cookie HttpOnly/Secure/SameSite.
Không biến role header hoặc UUID thành cơ chế phân quyền.
