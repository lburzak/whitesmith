import colorama

from presentation.keys_info import ROUTES_KEYS_INFO


class ControlsBar:
    def render(self, current_route: str) -> str:
        info_list: [str] = ["{%s}: %s" % (key, hint) for (key, hint) in ROUTES_KEYS_INFO[current_route].items()]
        return colorama.Fore.YELLOW + " | ".join(info_list) + colorama.Style.RESET_ALL
