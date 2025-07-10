## How to run

1. Cài đặt Docker & Docker Compose

2. Chạy lệnh sau trong thư mục này:

   ```bash
   docker-compose up --build
```

3. Gửi request:

   * POST `http://localhost/generate`
   * Body dạng JSON:

     ```json
     {
       "prompt": "a cat sitting on a rocket in space"
     }
     ```

## Kết quả

* Trả về ảnh `.png` do mô hình Stable Diffusion sinh ra.
* Nginx proxy hoạt động ổn định đến FastAPI app.

