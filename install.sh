#!/data/data/com.termux/files/usr/bin/bash
set -e
ROOT="$(cd "$(dirname "$0")" && pwd)"
echo "== Shadow Terminal: trình cài đặt Termux =="
command -v python3 >/dev/null || { echo "Chưa có Python. Hãy chạy: pkg install python"; exit 1; }
mkdir -p "$HOME/.local/bin"
cat > "$HOME/.local/bin/shadow" <<EOF
#!/data/data/com.termux/files/usr/bin/bash
cd "$ROOT"
exec python3 "$ROOT/main.py" "$@"
EOF
chmod +x "$HOME/.local/bin/shadow"
case ":$PATH:" in *":$HOME/.local/bin:"*) ;; *) echo 'export PATH="$HOME/.local/bin:$PATH"' >> "$HOME/.bashrc"; export PATH="$HOME/.local/bin:$PATH";; esac
echo "Đã cài command: shadow"
echo "Chạy: shadow"
