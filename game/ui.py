import os, sys, time

RESET="\033[0m"; DIM="\033[2m"; BOLD="\033[1m"
CYAN="\033[96m"; GREEN="\033[92m"; YELLOW="\033[93m"; RED="\033[91m"; MAGENTA="\033[95m"

def clear():
    os.system("clear")

def pause(msg="Nhấn Enter để tiếp tục..."):
    input(f"\n{DIM}{msg}{RESET}")

def box(title, lines, width=42):
    print(f"╔{'═'*(width-2)}╗")
    print(f"║{BOLD}{title[:width-2]:^{width-2}}{RESET}║")
    print(f"╠{'═'*(width-2)}╣")
    for line in lines:
        text=str(line)
        if len(text)>width-4: text=text[:width-5]+"…"
        print(f"║ {text:<{width-3}}║")
    print(f"╚{'═'*(width-2)}╝")

def hp_bar(value, maximum, length=18):
    value=max(0,min(value,maximum)); filled=int(length*value/maximum) if maximum else 0
    return "█"*filled+"░"*(length-filled)

def title():
    print(CYAN+BOLD+r"""
╔══════════════════════════════════════════════╗
║          SHADOW TERMINAL                    ║
║          SINH TỒN BÓNG TỐI                  ║
╚══════════════════════════════════════════════╝
"""+RESET)

def ask(prompt, choices):
    while True:
        value=input(f"{YELLOW}{prompt}{RESET} ").strip().lower()
        if value in choices: return value
        print(f"{RED}Lựa chọn không hợp lệ.{RESET}")
