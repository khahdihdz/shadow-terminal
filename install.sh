#!/data/data/com.termux/files/usr/bin/bash
set -e

ROOT="$(cd "$(dirname "$0")" && pwd)"
BIN_DIR="$PREFIX/bin"
CMD="$BIN_DIR/shadow"

echo "== Shadow Terminal: trình cài đặt Termux =="

command -v python3 >/dev/null || {
    echo "Chưa có Python. Hãy chạy: pkg install python"
    exit 1
}

mkdir -p "$BIN_DIR"

cat > "$CMD" <<EOF
#!/data/data/com.termux/files/usr/bin/bash
cd "$ROOT"
exec python3 "$ROOT/main.py" "$@"
EOF

chmod +x "$CMD"

# Dọn launcher cũ nếu đã từng cài vào ~/.local/bin.
rm -f "$HOME/.local/bin/shadow" 2>/dev/null || true

echo
echo "Đã cài command: shadow"
echo "Vị trí: $CMD"

if command -v shadow >/dev/null 2>&1; then
    echo "Kiểm tra: OK"
else
    echo "Cảnh báo: Termux chưa nhận PATH. Hãy mở lại Termux rồi chạy: shadow"
fi

echo
echo "Chạy game bằng:"
echo "  shadow"
