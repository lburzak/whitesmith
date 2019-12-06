from dataclasses import dataclass
from enum import Enum
from operator import attrgetter
from typing import Callable, Optional

from readchar import key

from chance import calculate_forging_success_chance
from data.recipes import recipes
from forging import forge, get_effective_difficulty
from inventory import Inventory, InventoryRecord
from list_view import ListView
from metal import Metal
from product import Product
from recipe import Recipe
from view import View, KeyListener


@dataclass
class ForgingChoice:
    recipe: Optional[Recipe]
    metal: Optional[InventoryRecord]


class ForgingStage(Enum):
    CHOOSING_RECIPE = 1
    CHOOSING_METAL = 2
    FORGING = 3


class ForgeView(View, KeyListener):
    loaded_recipes = recipes
    inventory: Inventory
    recipes_list_view = ListView([recipe.product_name.capitalize() for recipe in loaded_recipes])
    metals_list_view = ListView([])
    on_change: Callable
    current_choice = ForgingChoice(None, None)
    current_stage = ForgingStage.CHOOSING_RECIPE
    last_product: Optional[Product] = None

    def __init__(self, on_change: Callable, inventory: Inventory):
        self.inventory = inventory
        self.on_change = on_change

    def can_forge(self) -> bool:
        return self.current_choice.metal and self.current_choice.recipe and self.current_choice.recipe.size <= self.current_choice.metal.count

    def render(self) -> str:
        stage_render = ""
        if self.current_stage == ForgingStage.CHOOSING_RECIPE:
            stage_render = self.render_choosing_recipe()
        elif self.current_stage == ForgingStage.CHOOSING_METAL:
            stage_render = self.render_choosing_metal()
        elif self.current_stage == ForgingStage.FORGING:
            stage_render = self.render_forging()
        return self.render_choice() + "\n\n" + stage_render

    def render_choosing_recipe(self) -> str:
        return "Wybierz przepis: \n\n" + self.recipes_list_view.render()

    def render_choosing_metal(self) -> str:
        records = sorted(list(self.inventory.get_records().values()), key=attrgetter("count"), reverse=True)
        self.metals_list_view.items = ["%dx %s" % (record.count, record.item.name) for record in records]
        return "Wybierz metal: \n\n" + self.metals_list_view.render()

    def render_forging(self):
        level = 10
        difficulty = get_effective_difficulty(self.current_choice.metal.item, self.current_choice.recipe)
        chance = calculate_forging_success_chance(level, difficulty)
        chance_info = "Szansa na sukces: %f" % chance
        product_info = ""
        if self.last_product:
            product_info = "\n\n\tWytworzyłeś: [%s (%d)]!" % (self.last_product.name, self.last_product.rating)
        return chance_info + product_info

    def render_choice(self) -> str:
        r = ""
        m = ""
        w = ""
        o = ""
        if self.current_choice.recipe:
            r = "Przepis: %s" % self.current_choice.recipe.product_name.capitalize()
        if self.current_choice.metal:
            m = " + %s" % self.current_choice.metal.item.name
        if self.current_choice.recipe and self.current_choice.metal:
            w = "\n\tMateriały: %d / %d" % (self.current_choice.metal.count, self.current_choice.recipe.size)
        if self.can_forge():
            o = "  OK!"
        return r + m + w + o

    def handle_confirm(self):
        if self.current_stage == ForgingStage.CHOOSING_RECIPE:
            self.current_choice.recipe = self.loaded_recipes[self.recipes_list_view.pos]
        elif self.current_stage == ForgingStage.CHOOSING_METAL:
            records = sorted(list(self.inventory.get_records().values()), key=attrgetter("count"), reverse=True)
            self.current_choice.metal = records[self.metals_list_view.pos]
        elif self.current_stage == ForgingStage.FORGING:
            self.attempt_forging()

    def attempt_forging(self):
        if self.current_choice.recipe and self.current_choice.metal:
            self.last_product = forge(10, self.current_choice.recipe, self.current_choice.metal.item)

    def handle_up(self):
        if self.current_stage == ForgingStage.CHOOSING_RECIPE:
            self.recipes_list_view.up()
        elif self.current_stage == ForgingStage.CHOOSING_METAL:
            self.metals_list_view.up()

    def handle_down(self):
        if self.current_stage == ForgingStage.CHOOSING_RECIPE:
            self.recipes_list_view.down()
        elif self.current_stage == ForgingStage.CHOOSING_METAL:
            self.metals_list_view.down()

    def next_stage(self):
        if self.current_stage != ForgingStage.FORGING:
            self.current_stage = ForgingStage(self.current_stage.value + 1)

    def prev_stage(self):
        if self.current_stage != ForgingStage.CHOOSING_RECIPE:
            self.current_stage = ForgingStage(self.current_stage.value - 1)

    def on_key(self, k: key):
        if k == key.UP:
            self.handle_up()
        elif k == key.DOWN:
            self.handle_down()
        elif k == key.ENTER:
            self.handle_confirm()
        elif k == key.LEFT:
            self.prev_stage()
        elif k == key.RIGHT:
            self.next_stage()
        self.on_change()
