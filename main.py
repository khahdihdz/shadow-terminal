#!/usr/bin/env python3
from game.engine import Game

if __name__ == "__main__":
    try:
        Game().run()
    except KeyboardInterrupt:
        print("\n\nĐã thoát Shadow Terminal. Dữ liệu đã được giữ an toàn.")
