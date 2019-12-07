from presentation.forge_view import ForgeView
from presentation.market_view import MarketView
from presentation.menu_view import MenuView
from presentation.mine_view import MineView
from presentation.top_bar_view import TopBarView
from presentation.views_root import ViewsRoot
from presentation.inventory_view import InventoryView
from inventory import Inventory
from market import Market
from mining import Mine
from player import Player
from resources import generate_resources

resources = generate_resources()
mine = Mine(resources)
inv = Inventory()
market = Market()
player = Player(inv, 0)

viewsRoot = ViewsRoot()
viewsRoot.top_bar_view = TopBarView(player)

routes = {
    "Magazyn": InventoryView(viewsRoot.change_handler, player.inventory),
    "Kopalnia": MineView(viewsRoot.change_handler, mine, player),
    "Kuźnia": ForgeView(viewsRoot.change_handler, player, resources),
    "Bazar": MarketView(viewsRoot.change_handler, player, market),
}
routes["Menu"] = MenuView(viewsRoot.change_handler, viewsRoot.open_route, list(routes.keys()))

viewsRoot.set_routes(routes)
viewsRoot.start("Menu")
