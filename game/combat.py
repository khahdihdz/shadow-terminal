import random
from . import data
from .ui import hp_bar, box, ask, RED, GREEN, YELLOW, RESET

def fight(player):
    enemy=random.choice(data.ENEMIES).copy()
    hp=enemy["hp"]; defended=False
    while hp>0 and player.hp>0:
        box("CHIẾN ĐẤU",[
            f"{enemy['name']}  {hp_bar(hp,enemy['hp'])} {hp}/{enemy['hp']}",
            f"{player.name}     {hp_bar(player.hp,player.max_hp)} {player.hp}/{player.max_hp}",
            "", "[1] Tấn công","[2] Kỹ năng","[3] Vật phẩm","[4] Phòng thủ","[5] Bỏ chạy"])
        choice=ask("Chọn",{"1","2","3","4","5"})
        if choice=="1":
            damage=max(1,player.strength+random.randint(1,8)-enemy["def"])
            if random.random()<0.10+player.luck*0.01: damage*=2; print(YELLOW+"Đòn chí mạng!"+RESET)
            hp-=damage; print(f"{GREEN}Bạn gây {damage} sát thương.{RESET}")
        elif choice=="2":
            if player.energy<20: print(RED+"Không đủ năng lượng."+RESET); continue
            player.energy-=20
            damage=max(8,player.intelligence+random.randint(8,16)-enemy["def"]//2)
            hp-=damage; print(f"{GREEN}Kỹ năng gây {damage} sát thương.{RESET}")
        elif choice=="3":
            if player.inventory.get("medkit",0)>0:
                player.inventory["medkit"]-=1; player.hp=min(player.max_hp,player.hp+35); print(GREEN+"Đã dùng Bộ cứu thương."+RESET)
            else: print(RED+"Bạn không còn Bộ cứu thương."+RESET)
        elif choice=="4":
            defended=True; player.energy=min(player.max_energy,player.energy+10); print("Bạn thủ thế.")
        else:
            if random.random()<0.55: print("Bạn đã rút lui."); return False
            print("Không thể bỏ chạy!")
        if hp>0:
            damage=max(1,enemy["atk"]-player.defense//2+random.randint(-2,4))
            if defended: damage//=2; defended=False
            player.hp=max(0,player.hp-damage); print(f"{RED}{enemy['name']} gây {damage} sát thương.{RESET}")
    if player.hp<=0: return False
    player.gain_xp(enemy["xp"]); player.money+=enemy["money"]
    print(GREEN+f"Bạn đã đánh bại {enemy['name']}! +{enemy['xp']} XP, +{enemy['money']} Xu."+RESET)
    return True
