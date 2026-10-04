# Shadow Terminal — Sinh Tồn Bóng Tối

Game RPG/Survival chạy trực tiếp trên **Termux Android**, giao diện Terminal tiếng Việt.

## Lưu dữ liệu

Game lưu save trong thư mục con:

```
~/storage/downloads/ShadowTerminal/
```

Trên Android, thư mục này tương ứng với:

```
Download/ShadowTerminal/
```

Trước lần chạy đầu tiên, nếu Termux chưa được cấp quyền truy cập bộ nhớ, chạy:

```bash
termux-setup-storage
```

Sau đó chấp nhận quyền truy cập.

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

## Tính năng

- RPG theo lượt hoàn toàn offline.
- Khám phá nhiều khu vực.
- Combat theo lượt.
- Kỹ năng và nâng cấp nhân vật.
- Kho đồ và vật phẩm.
- Nhiệm vụ/điều tra.
- Puzzle OSINT mô phỏng bằng dữ liệu hư cấu.
- Sự kiện ngẫu nhiên.
- Save/Load trong thư mục Downloads.
- UI tiếng Việt.
- Tối ưu màn hình điện thoại.

## Điều khiển

```
1-9  Chọn menu
B    Quay lại
```

## OSINT mô phỏng

Các vụ điều tra chỉ là gameplay giả lập. Game không quét IP thật, brute-force tài khoản, lấy mật khẩu, thu thập dữ liệu cá nhân, quét mạng hoặc tấn công hệ thống.

## License

MIT License.

**© 2026 khahdihdz**
