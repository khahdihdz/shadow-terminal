# Shadow Terminal — Sinh Tồn Bóng Tối

Game RPG/Survival chạy trực tiếp trên **Termux Android**, giao diện Terminal tiếng Việt.

## Tính năng

- 🎮 RPG theo lượt hoàn toàn offline.
- 🗺️ Khám phá nhiều khu vực.
- ⚔️ Combat theo lượt.
- 🧠 Kỹ năng và nâng cấp nhân vật.
- 🎒 Kho đồ và vật phẩm.
- 📜 Nhiệm vụ chính/điều tra.
- 🔎 Puzzle OSINT mô phỏng bằng dữ liệu hư cấu.
- 🎲 Sự kiện ngẫu nhiên.
- 🏆 Thành tựu và nhiều hướng phát triển.
- 💾 Save/Load tại `~/.shadow_terminal/`.
- 📱 Tối ưu cho màn hình điện thoại.
- 🇻🇳 UI tiếng Việt.
- 🚫 Không quét mạng, không thu thập dữ liệu thật.

## Cài trên Termux

Cài Python:

```bash
pkg update
pkg install python git
```

Clone repository:

```bash
git clone https://github.com/khahdihdz/shadow-terminal.git
cd shadow-terminal
```

Cài command:

```bash
bash install.sh
```

Chạy game:

```bash
shadow
```

Hoặc chạy trực tiếp:

```bash
python3 main.py
```

## Điều khiển

```
1-9  Chọn menu
B    Quay lại
I    Kho đồ (trong các màn hình hỗ trợ)
M    Bản đồ
C    Nhân vật
S    Lưu game
L    Tải game
```

Menu trong game hiển thị lựa chọn trực tiếp để thao tác thuận tiện trên bàn phím cảm ứng.

## Lưu game

Save mặc định:

```
~/.shadow_terminal/save_1.json
```

Game tự lưu sau các mốc quan trọng và có tùy chọn lưu thủ công.

## OSINT mô phỏng

Các vụ điều tra chỉ là gameplay giả lập. Game **không**:

- quét IP thật;
- brute-force tài khoản;
- lấy mật khẩu;
- thu thập PII;
- quét mạng;
- tấn công hệ thống;
- gửi dữ liệu ra ngoài.

## Cấu trúc

```
shadow-terminal/
├── main.py
├── install.sh
├── requirements.txt
├── README.md
├── LICENSE
├── game/
│   ├── combat.py
│   ├── data.py
│   ├── engine.py
│   ├── player.py
│   └── ui.py
└── .github/
    └── workflows/
```

## Giấy phép

MIT License.

**© 2026 khahdihdz**
