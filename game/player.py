from dataclasses import dataclass, field
from pathlib import Path
import json

# Android/Termux: lưu dữ liệu trong thư mục con của Downloads để người dùng
# dễ sao lưu/chuyển dữ liệu. Có fallback về HOME nếu Downloads chưa tồn tại.
DOWNLOADS=Path.home()/"storage"/"downloads"
if not DOWNLOADS.exists():
    DOWNLOADS=Path.home()/"downloads"
SAVE_DIR=DOWNLOADS/"ShadowTerminal"

@dataclass
class Player:
    name:str="Raven"; level:int=1; xp:int=0; hp:int=100; max_hp:int=100
    energy:int=100; max_energy:int=100; money:int=250
    strength:int=10; defense:int=5; intelligence:int=10; luck:int=5; reputation:int=0
    skill_points:int=0
    inventory:dict=field(default_factory=lambda:{"medkit":2,"energy":1,"usb":0,"coin":3})
    quests:dict=field(default_factory=lambda:{"case_001":0})
    achievements:list=field(default_factory=list)
    location:int=0

    def gain_xp(self, amount):
        self.xp+=amount
        needed=100*self.level
        while self.xp>=needed:
            self.xp-=needed; self.level+=1; self.skill_points+=1
            self.max_hp+=10; self.max_energy+=5; self.hp=self.max_hp; self.energy=self.max_energy
            needed=100*self.level

    def to_dict(self): return self.__dict__

    @classmethod
    def from_dict(cls,d): return cls(**d)

def save(player, slot=1):
    SAVE_DIR.mkdir(parents=True,exist_ok=True)
    path=SAVE_DIR/f"save_{slot}.json"
    path.write_text(json.dumps(player.to_dict(),ensure_ascii=False,indent=2),encoding="utf-8")
    return path

def load(slot=1):
    path=SAVE_DIR/f"save_{slot}.json"
    if not path.exists(): return None
    return Player.from_dict(json.loads(path.read_text(encoding="utf-8")))
