# Shadow Terminal — Sinh Tồn Bóng Tối

Game RPG/Survival chạy trực tiếp trên **Termux Android**, giao diện Terminal tiếng Việt.

## Landing Page

Trang giới thiệu game được triển khai bằng GitHub Pages:

**https://khahdihdz.github.io/shadow-terminal/**

Landing page tự động deploy lại mỗi khi có commit lên nhánh `main`. Trang cũng hiển thị commit mới nhất của repository.

## Tính năng

- RPG sinh tồn theo lượt hoàn toàn offline.
- Khám phá 6 khu vực.
- Combat theo lượt.
- Kỹ năng và nâng cấp nhân vật.
- Kho đồ và vật phẩm.
- Nhiệm vụ và điều tra có hồ sơ, manh mối, gợi ý và kết luận.
- Puzzle OSINT mô phỏng bằng dữ liệu hư cấu.
- Sự kiện ngẫu nhiên.
- Save/Load trong thư mục Downloads.
- UI tiếng Việt.
- Tự động triển khai landing page bằng GitHub Actions.

## Lưu dữ liệu

Game lưu save trong:

```
~/storage/downloads/ShadowTerminal/
```

Trên Android:

```
Download/ShadowTerminal/
```

Trước lần chạy đầu tiên, nếu Termux chưa được cấp quyền truy cập bộ nhớ:

```bash
termux-setup-storage
```

Nếu đường dẫn Downloads của Termux chưa tồn tại, game tự động thử `~/downloads/ShadowTerminal/`.

## Cài đặt

```bash
pkg update
pkg install python git
termux-setup-storage

git clone https://github.com/khahdihdz/shadow-terminal.git
cd shadow-terminal
bash install.sh
shadow
```

Hoặc:

```bash
python3 main.py
```

## Điều tra

Vào **[7] Điều tra** trong game để:

1. Đọc toàn bộ hồ sơ vụ án.
2. Xem các câu hỏi điều tra.
3. Đọc từng manh mối đầy đủ.
4. Xem suy luận và gợi ý.
5. Thu thập đủ 3 manh mối.
6. Kết luận vụ án và nhận phần thưởng.

## OSINT mô phỏng

Các vụ điều tra chỉ là gameplay giả lập. Game không quét IP thật, brute-force tài khoản, lấy mật khẩu, thu thập dữ liệu cá nhân, quét mạng hoặc tấn công hệ thống.

## License

MIT License.

**© 2026 khahdihdz**
