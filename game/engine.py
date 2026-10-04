import random, time
from .player import Player, save, load
from .combat import fight
from . import data
from .ui import *

class Game:
    def __init__(self):
        self.player=None

    def run(self):
        while True:
            clear(); title()
            print("[1] Trò chơi mới\n[2] Tiếp tục\n[3] Tải game\n[4] Hướng dẫn\n[5] Thoát")
            c=ask("Chọn",{"1","2","3","4","5"})
            if c=="1": self.new_game(); self.loop()
            elif c in {"2","3"}:
                self.player=load(1)
                if self.player: self.loop()
                else: print(RED+"Chưa có dữ liệu lưu."+RESET); pause()
            elif c=="4": self.help()
            else: return

    def new_game(self):
        clear(); title()
        name=input("Tên nhân vật [Raven]: ").strip() or "Raven"
        self.player=Player(name=name)
        save(self.player)
        print(GREEN+"Đã tạo nhân vật."+RESET); pause()

    def loop(self):
        while self.player and self.player.hp>0:
            clear(); title()
            p=self.player
            print(f"{BOLD}{p.name}{RESET} | Cấp {p.level} | HP {p.hp}/{p.max_hp} | NL {p.energy}/{p.max_energy} | 💰 {p.money}")
            print(f"XP {p.xp}/{100*p.level} | Danh tiếng {p.reputation}\n")
            print("[1] Khám phá  [2] Bản đồ  [3] Nhân vật")
            print("[4] Kho đồ    [5] Nhiệm vụ [6] Lưu game")
            print("[7] Điều tra  [8] Cài đặt [9] Thoát")
            c=ask("Chọn",set("123456789"))
            if c=="1": self.explore()
            elif c=="2": self.map_menu()
            elif c=="3": self.character()
            elif c=="4": self.inventory()
            elif c=="5": self.quests()
            elif c=="6": save(p); print(GREEN+"Đã lưu game."+RESET); pause()
            elif c=="7": self.investigation()
            elif c=="8": self.settings()
            else: save(p); return

    def explore(self):
        if random.random()<0.45:
            fight(self.player)
        else:
            events=[
                "Bạn tìm thấy một đồng xu cổ.",
                "Bạn phát hiện một manh mối bị giấu trong terminal.",
                "Bạn giúp một NPC và nhận được 40 tiền.",
                "Một tín hiệu bí ẩn làm tăng danh tiếng của bạn."
            ]
            event=random.choice(events); print(MAGENTA+"\n[!] "+event+RESET)
            if "đồng xu" in event: self.player.inventory["coin"]=self.player.inventory.get("coin",0)+1
            elif "40 tiền" in event: self.player.money+=40
            else: self.player.reputation+=1
        if self.player.hp<=0:
            clear(); box("GAME OVER",["Bóng tối đã nuốt chửng bạn.","Hãy thử lại từ save gần nhất."]); pause()
        else:
            save(self.player); pause()

    def map_menu(self):
        clear(); box("BẢN ĐỒ",[f"[{i+1}] {n}" for i,(n,_) in enumerate(data.LOCATIONS)]+["","[B] Quay lại"])
        c=ask("Chọn",set("123456")+"b")
        if c!="b":
            self.player.location=int(c)-1
            print(f"Bạn đến {data.LOCATIONS[self.player.location][0]}.")
            print(data.LOCATIONS[self.player.location][1]); self.player.energy=max(0,self.player.energy-5); pause()

    def character(self):
        p=self.player
        clear(); box("NHÂN VẬT",[
            f"Tên: {p.name}",f"Cấp độ: {p.level}",f"Kinh nghiệm: {p.xp}/{100*p.level}",
            f"HP: {p.hp}/{p.max_hp}",f"Năng lượng: {p.energy}/{p.max_energy}",
            f"Tiền: {p.money}",f"Sức mạnh: {p.strength}",f"Phòng thủ: {p.defense}",
            f"Trí tuệ: {p.intelligence}",f"May mắn: {p.luck}",f"Danh tiếng: {p.reputation}",
            f"Điểm kỹ năng: {p.skill_points}"])
        if p.skill_points:
            print("\n[1] +Sức mạnh  [2] +Phòng thủ  [3] +Trí tuệ  [4] +May mắn")
            c=ask("Nâng cấp hoặc B để bỏ qua",{"1","2","3","4","b"})
            if c!="b":
                attrs={"1":"strength","2":"defense","3":"intelligence","4":"luck"}
                setattr(p,attrs[c],getattr(p,attrs[c])+1); p.skill_points-=1
        pause()

    def inventory(self):
        p=self.player; clear()
        box("KHO ĐỒ",[f"{data.ITEMS[k]['name']}: x{v}" for k,v in p.inventory.items()])
        print("\n[1] Dùng Bộ cứu thương  [2] Dùng Nước tăng lực  [3] Bán đồng xu  [B] Quay lại")
        c=ask("Chọn",{"1","2","3","b"})
        if c=="1" and p.inventory.get("medkit",0)>0:
            p.inventory["medkit"]-=1; p.hp=min(p.max_hp,p.hp+35)
        elif c=="2" and p.inventory.get("energy",0)>0:
            p.inventory["energy"]-=1; p.energy=min(p.max_energy,p.energy+30)
        elif c=="3" and p.inventory.get("coin",0)>0:
            p.inventory["coin"]-=1; p.money+=25
        pause()

    def quests(self):
        p=self.player; clear()
        progress=p.quests.get("case_001",0)
        box("NHIỆM VỤ",[
            "VỤ ÁN #001 — Tín hiệu Night Raven",
            "Tìm 3 mảnh manh mối trong quá trình khám phá.",
            f"Tiến độ: {progress}/3","Phần thưởng: 100 XP + 200 tiền"
        ])
        if progress>=3:
            print(GREEN+"Bạn đã phá được vụ án. Danh tiếng +5."+RESET); p.reputation+=5
            p.quests["case_001"]=4
        pause()

    def investigation(self):
        p=self.player; progress=p.quests.get("case_001",0)
        clear()
        box("ĐIỀU TRA — VỤ ÁN #001",[
            "Mục tiêu: Night Raven","[✓] Dữ liệu hoàn toàn hư cấu",
            f"Manh mối đã tìm thấy: {min(progress,3)}/3",
            "Mỗi lần khám phá có cơ hội tìm thêm manh mối."
        ])
        if progress<3 and random.random()<0.75:
            p.quests["case_001"]=progress+1
            print(GREEN+"Bạn tìm thấy một manh mối mới!"+RESET)
        else: print("Chưa có manh mối mới.")
        pause()

    def settings(self):
        clear(); box("CÀI ĐẶT",["Giao diện: Terminal","Ngôn ngữ: Tiếng Việt","Âm thanh: Terminal Bell tùy môi trường"])
        pause()

    def help(self):
        clear(); box("HƯỚNG DẪN",[
            "Khám phá để gặp sự kiện và kẻ địch.",
            "Nâng cấp nhân vật bằng điểm kỹ năng.",
            "Thu thập manh mối để phá vụ án.",
            "Lưu game thường xuyên.",
            "Mọi dữ liệu điều tra đều là dữ liệu giả lập.",
            "Game không quét mạng hay thu thập dữ liệu thật."
        ])
        pause()
