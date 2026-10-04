import os, sys, time, shutil, textwrap

RESET="\033[0m"; DIM="\033[2m"; BOLD="\033[1m"
CYAN="\033[96m"; GREEN="\033[92m"; YELLOW="\033[93m"; RED="\033[91m"; MAGENTA="\033[95m"

def clear():
    os.system("clear")

def pause(msg="Nhấn Enter để tiếp tục..."):
    input(f"\n{DIM}{msg}{RESET}")

def terminal_width(default=50):
    """Lấy chiều rộng terminal nhưng luôn giữ box vừa màn hình điện thoại."""
    try:
        columns=shutil.get_terminal_size((default, 24)).columns
    except OSError:
        columns=default
    return max(32, min(columns, 60))

def box(title, lines, width=None):
    """Hiển thị hộp văn bản và tự xuống dòng, tuyệt đối không cắt nội dung."""
    if width is None:
        width=terminal_width()
    width=max(32, width)
    inner=width-4

    print(f"╔{'═'*(width-2)}╗")

    title_text=str(title)
    title_lines=textwrap.wrap(
        title_text,
        width=inner,
        break_long_words=True,
        break_on_hyphens=False
    ) or [""]
    for part in title_lines:
        print(f"║{BOLD}{part:^{width-2}}{RESET}║")

    print(f"╠{'═'*(width-2)}╣")

    for line in lines:
        text=str(line)
        wrapped=textwrap.wrap(
            text,
            width=inner,
            break_long_words=True,
            break_on_hyphens=False
        ) or [""]
        for part in wrapped:
            print(f"║ {part:<{inner}} ║")

    print(f"╚{'═'*(width-2)}╝")

def hp_bar(value, maximum, length=18):
    value=max(0,min(value,maximum)); filled=int(length*value/maximum) if maximum else 0
    return "█"*filled+"░"*(length-filled)

def title():
    width=terminal_width()
    print(CYAN+BOLD+"╔"+"═"*(width-2)+"╗")
    title_lines=["SHADOW TERMINAL","SINH TỒN BÓNG TỐI"]
    for line in title_lines:
        print(f"║{line:^{width-2}}║")
    print("╚"+"═"*(width-2)+"╝"+RESET)

def ask(prompt, choices):
    while True:
        value=input(f"{YELLOW}{prompt}{RESET} ").strip().lower()
        if value in choices: return value
        print(f"{RED}Lựa chọn không hợp lệ.{RESET}")
