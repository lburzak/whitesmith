from player import Player


class TopBarView:
    temporary_message = ""
    player: Player

    def __init__(self, player: Player):
        self.player = player

    def on_xp_gain(self, skill: str, amount: int, to_next: int):
        self.temporary_message = "%s XP +%d (%d do nast. poziomu)" % (skill, amount, to_next)

    def on_level_up(self, skill: str, prev_lvl: int, curr_lvl: int):
        self.temporary_message = "%s LEVEL UP! (%d => %d)" % (skill, prev_lvl, curr_lvl)

    def render(self, current_route: str) -> str:
        return "< %s >\t%d$\tKowalstwo: %d (%d/%d XP)\t\tGórnictwo: %d (%d/%d XP)" % (
            current_route,
            self.player.money,
            self.player.forging_gauge.level,
            self.player.forging_gauge.xp,
            self.player.forging_gauge.get_xp_needed(),
            self.player.mining_gauge.level,
            self.player.mining_gauge.xp,
            self.player.mining_gauge.get_xp_needed()
        )
