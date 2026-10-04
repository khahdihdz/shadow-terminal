import random, time
from .player import Player, save, load
from .combat import fight
from . import data
from .ui import *

CASE_CLUES = [
    {
        "id": "signal",
        "title": "MANH MỐI 01 — TÍN HIỆU NIGHT RAVEN",
        "text": [
            "Một tín hiệu ngắn xuất hiện trên terminal lúc 02:17.",
            "Mã nguồn: NR-17 / TẦN SỐ 441.7 / ĐIỂM GIAO: GA NGẦM.",
            "Dữ liệu không chứa danh tính thật; đây là dữ liệu gameplay giả lập.",
            "Suy luận: người gửi muốn ai đó tiếp cận khu ga tàu điện ngầm."
        ],
        "hint": "Hãy kiểm tra Ga tàu điện ngầm trên bản đồ sau khi đọc manh mối này."
    },
    {
        "id": "warehouse",
        "title": "MANH MỐI 02 — LÔ HÀNG KHÔNG NGƯỜI NHẬN",
        "text": [
            "Một phiếu vận chuyển cũ được tìm thấy trong nhà kho.",
            "Lô hàng: SH-204. Tuyến: Nhà kho → Khu công nghiệp.",
            "Người nhận chỉ được ghi là 'RAVEN'. Không có địa chỉ hay thông tin cá nhân.",
            "Suy luận: SHADOW đang chuyển thiết bị giữa hai khu vực."
        ],
        "hint": "Khám phá Nhà kho bỏ hoang và Khu công nghiệp để tìm thêm dấu vết."
    },
    {
        "id": "base",
        "title": "MANH MỐI 03 — DẤU VẾT CĂN CỨ",
        "text": [
            "USB mã hóa chứa một đoạn nhật ký giả lập của SHADOW.",
            "Nội dung: 'NR-17 chỉ là mồi nhử. Điểm cuối nằm dưới khu công nghiệp.'",
            "Một tọa độ gameplay trỏ về Căn cứ bí mật.",
            "Suy luận: Night Raven đang dẫn nhân vật tới trung tâm của vụ án."
        ],
        "hint": "Đến Căn cứ bí mật để đối chiếu dữ kiện và mở khóa phần kết luận."
    }
]

class Game:
    def __init__(self):
        self.player=None

    def run(self):
        while True:
            clear(); title()
            print("[1] Trò chơi mới")
            print("[2] Tiếp tục")
            print("[3] Tải game")
            print("[4] Hướng dẫn")
            print("[5] Thoát")
            c=ask("Chọn",{"1","2","3","4","5"})
            if c=="1":
                self.new_game()
                self.loop()
            elif c in {"2","3"}:
                self.player=load(1)
                if self.player:
                    self.loop()
                else:
                    print(RED+"Chưa có dữ liệu lưu."+RESET)
                    pause()
            elif c=="4":
                self.help()
            elif c=="5":
                return

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
            print("[7] Điều tra  [8] Cửa hàng [9] Cài đặt [0] Thoát")
            c=ask("Chọn",set("0123456789"))
            if c=="1": self.explore()
            elif c=="2": self.map_menu()
            elif c=="3": self.character()
            elif c=="4": self.inventory()
            elif c=="5": self.quests()
            elif c=="6": save(p); print(GREEN+"Đã lưu game."+RESET); pause()
            elif c=="7": self.investigation()
            elif c=="8": self.shop()
            elif c=="9": self.settings()
            elif c=="0": save(p); return

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
        c=ask("Chọn",{"1","2","3","4","5","6","b"})
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
        status="ĐÃ HOÀN THÀNH" if progress>=4 else f"{min(progress,3)}/3"
        box("NHIỆM VỤ",[
            "VỤ ÁN #001 — Tín hiệu Night Raven",
            "Mục tiêu: thu thập và đối chiếu 3 manh mối.",
            f"Tiến độ: {status}",
            "Phần thưởng: 100 XP + 200 tiền + Danh tiếng +5"
        ])
        print("\nHướng dẫn:")
        print("1. Mở Điều tra để xem hồ sơ và manh mối.")
        print("2. Chọn Tìm manh mối khi vụ án chưa đủ 3 dữ kiện.")
        print("3. Đọc gợi ý của từng manh mối để biết khu vực cần khám phá.")
        print("4. Khi đủ 3 manh mối, chọn Kết luận vụ án.")
        if progress>=3 and progress<4:
            p.gain_xp(100); p.money+=200; p.reputation+=5
            p.quests["case_001"]=4
            print(GREEN+"\nBạn đã phá được vụ án! Phần thưởng đã nhận."+RESET)
        pause()

    def investigation(self):
        p=self.player
        q=p.quests
        progress=q.get("case_001",0)
        clues=q.setdefault("case_001_clues",[])
        clear()
        print(BOLD+CYAN+"╔══════════════════════════════════════════════╗")
        print("║              HỒ SƠ ĐIỀU TRA                 ║")
        print("║              VỤ ÁN #001                     ║")
        print("╚══════════════════════════════════════════════╝"+RESET)
        print("\nMục tiêu: xác định Night Raven là gì và tìm điểm cuối của tín hiệu.")
        print("Trạng thái:", GREEN+"ĐÃ PHÁ ÁN"+RESET if progress>=4 else YELLOW+f"ĐANG ĐIỀU TRA ({len(clues)}/3)"+RESET)
        print("\n[1] Hồ sơ vụ án")
        print("[2] Xem toàn bộ manh mối đã có")
        print("[3] Hướng dẫn điều tra")
        print("[4] Tìm manh mối")
        if len(clues)>=3 and progress<4:
            print("[5] Kết luận vụ án")
        elif progress>=4:
            print("[5] Xem kết luận")
        print("[B] Quay lại")
        choices={"1","2","3","4","b"}
        if len(clues)>=3 or progress>=4: choices.add("5")
        c=ask("Chọn",choices)
        if c=="1":
            clear()
            box("HỒ SƠ VỤ ÁN",[
                "Mã vụ án: CASE-001",
                "Tên: Tín hiệu Night Raven",
                "Đối tượng: tổ chức SHADOW (hư cấu)",
                "Điểm bắt đầu: một tín hiệu lúc 02:17",
                "Nhiệm vụ: tìm nguồn tín hiệu và điểm cuối",
                "Quy tắc: chỉ sử dụng dữ liệu giả lập trong game."
            ])
            print("\nCâu hỏi điều tra:")
            print("• Ai phát tín hiệu?")
            print("• Vì sao tín hiệu dẫn tới ga ngầm?")
            print("• Lô hàng SH-204 đi đâu?")
            print("• Điểm cuối của Night Raven nằm ở đâu?")
            pause()
        elif c=="2":
            clear()
            if not clues:
                print(YELLOW+"Bạn chưa có manh mối nào."+RESET)
            else:
                for index in clues:
                    clue=CASE_CLUES[index]
                    print(BOLD+f"\n{clue['title']}"+RESET)
                    for line in clue["text"]: print("  "+line)
                    print(MAGENTA+"  Gợi ý: "+clue["hint"]+RESET)
            pause()
        elif c=="3":
            clear()
            box("HƯỚNG DẪN ĐIỀU TRA",[
                "BƯỚC 1 — Đọc hồ sơ để biết câu hỏi.",
                "BƯỚC 2 — Tìm manh mối cho tới khi đủ 3/3.",
                "BƯỚC 3 — Đọc kỹ phần Suy luận và Gợi ý.",
                "BƯỚC 4 — Đến khu vực được gợi ý để nhập vai điều tra.",
                "BƯỚC 5 — Khi đủ 3 manh mối, chọn Kết luận vụ án.",
                "BƯỚC 6 — Nhận thưởng và xem kết luận đầy đủ."
            ])
            print("\nKhông cần Internet. Không có quét mạng, mật khẩu thật hay dữ liệu cá nhân.")
            pause()
        elif c=="4":
            missing=[i for i in range(len(CASE_CLUES)) if i not in clues]
            if not missing:
                print(GREEN+"Bạn đã thu thập đủ toàn bộ manh mối."+RESET)
            else:
                index=random.choice(missing)
                clues.append(index)
                q["case_001"]=len(clues)
                clue=CASE_CLUES[index]
                clear()
                print(GREEN+BOLD+"[+] MANH MỐI MỚI ĐƯỢC GHI NHẬN"+RESET)
                print(BOLD+"\n"+clue["title"]+RESET)
                for line in clue["text"]: print(line)
                print(MAGENTA+"\nGợi ý tiếp theo: "+clue["hint"]+RESET)
                save(p)
            pause()
        elif c=="5":
            clear()
            if progress>=4:
                box("KẾT LUẬN ĐÃ XÁC NHẬN",[
                    "Night Raven là tín hiệu mồi nhử do SHADOW dựng lên.",
                    "Lô hàng SH-204 nối Nhà kho với Khu công nghiệp.",
                    "Dữ kiện cuối cùng xác nhận điểm đến là Căn cứ bí mật.",
                    "Vụ án #001 đã được giải."
                ])
            elif len(clues)>=3:
                q["case_001"]=3
                box("KẾT LUẬN VỤ ÁN",[
                    "Tín hiệu Night Raven dẫn dụ người điều tra qua ga ngầm.",
                    "Lô hàng SH-204 chứng minh tuyến Nhà kho → Khu công nghiệp.",
                    "Dấu vết cuối cùng chỉ tới Căn cứ bí mật.",
                    "Kết luận: Night Raven là mồi nhử để che giấu hoạt động của SHADOW."
                ])
                p.gain_xp(100); p.money+=200; p.reputation+=5
                q["case_001"]=4
                print(GREEN+"\nVụ án đã được phá. +100 XP, +200 tiền, +5 danh tiếng."+RESET)
                save(p)
            pause()

    def shop(self):
        p=self.player
        while True:
            clear()
            box("CỬA HÀNG SHADOW",[
                "Tiền hiện có: 💰 "+str(p.money),
                "Mua vật phẩm bằng tiền trong game.",
                "Cửa hàng hoạt động hoàn toàn offline."
            ])
            print("\n[1] Bộ cứu thương  — 60 tiền  | Hồi 35 HP")
            print("[2] Nước tăng lực  — 45 tiền  | Hồi 30 năng lượng")
            print("[3] USB mã hóa     — 120 tiền | Vật phẩm điều tra")
            print("[4] Đồng xu cổ     — 25 tiền  | Bán lại được")
            print("[B] Quay lại")
            c=ask("Chọn",{"1","2","3","4","b"})
            if c=="b": return
            items={"1":("medkit",60),"2":("energy",45),"3":("usb",120),"4":("coin",25)}
            key,price=items[c]
            if p.money<price:
                print(RED+"Không đủ tiền."+RESET)
            else:
                p.money-=price
                p.inventory[key]=p.inventory.get(key,0)+1
                print(GREEN+f"Đã mua {data.ITEMS[key]['name']}."+RESET)
                save(p)
            pause()

    def settings(self):
        clear(); box("CÀI ĐẶT",["Giao diện: Terminal","Ngôn ngữ: Tiếng Việt","Âm thanh: Terminal Bell tùy môi trường"])
        pause()

    def help(self):
        clear()
        print(BOLD+CYAN+"HƯỚNG DẪN CHƠI — SHADOW TERMINAL"+RESET)
        print("\nMỤC TIÊU")
        print("Bạn là Raven, một người sống sót bị kéo vào chuỗi tín hiệu bí ẩn của SHADOW.")
        print("Khám phá thành phố, chiến đấu, nâng cấp nhân vật và điều tra để mở khóa câu chuyện.")
        print("\nBẮT ĐẦU")
        print("1. Chọn Trò chơi mới và đặt tên.")
        print("2. Chọn Khám phá để nhận sự kiện, chiến đấu hoặc tìm tài nguyên.")
        print("3. Dùng Bản đồ để di chuyển giữa 6 khu vực.")
        print("4. Vào Nhân vật để dùng điểm kỹ năng.")
        print("5. Vào Kho đồ để hồi HP/năng lượng hoặc bán đồng xu.")
        print("6. Vào Nhiệm vụ để xem tiến độ.")
        print("7. Vào Điều tra để đọc hồ sơ, thu thập và đối chiếu manh mối.")
        print("\nĐIỀU TRA VỤ ÁN #001")
        print("• Mở [7] Điều tra → [1] Hồ sơ vụ án để đọc toàn bộ mục tiêu.")
        print("• Chọn [4] Tìm manh mối cho tới khi đạt 3/3.")
        print("• Mỗi manh mối có Dữ kiện, Suy luận và Gợi ý.")
        print("• Dùng Gợi ý để biết khu vực cần khám phá tiếp.")
        print("• Đủ 3/3 → chọn [5] Kết luận vụ án.")
        print("• Hoàn thành sẽ nhận 100 XP, 200 tiền và +5 danh tiếng.")
        print("\nCHIẾN ĐẤU")
        print("Tấn công gây sát thương cơ bản; Kỹ năng mạnh hơn nhưng tốn năng lượng.")
        print("Phòng thủ giảm sát thương; Bỏ chạy kết thúc trận nếu thành công.")
        print("\nLƯU GAME")
        print("Game tự lưu sau khám phá/điều tra và có thể lưu thủ công bằng [6].")
        print("Save: ~/storage/downloads/ShadowTerminal/save_1.json")
        print("\nAN TOÀN")
        print("OSINT trong game chỉ là mô phỏng. Không quét mạng thật, không brute-force,")
        print("không lấy mật khẩu, không thu thập PII và không tấn công hệ thống.")
        pause()
