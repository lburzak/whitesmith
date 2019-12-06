from dataclasses import dataclass


@dataclass
class LevelGauge:
    level: int
    xp: int

    def level_up(self, xp_carryover: int):
        self.level += 1
        self.xp = xp_carryover

    def grant_xp(self, amount: int):
        xp_needed = self.get_xp_needed()
        if self.xp + amount >= xp_needed:
            self.level_up(self.xp + amount - xp_needed)
        else:
            self.xp += amount

    def get_xp_needed(self) -> int:
        pass


class ForgingGauge(LevelGauge):
    def get_xp_needed(self) -> int:
        return self.level * 100


class MiningGauge(LevelGauge):
    def get_xp_needed(self) -> int:
        return self.level * 50
