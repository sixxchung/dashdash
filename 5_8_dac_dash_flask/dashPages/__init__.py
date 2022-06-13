MENU_ITEMS = ("basic_cards", "social_cards", "tab_cards",
              "basic_boxes", "value_boxes",
              "gallery_1", "gallery_2")

import importlib
def load_module(module_nm):
    rlt = importlib.import_module(f"from . import {module_nm}")
    return rlt
#from . import tab_cards
for m in MENU_ITEMS:
    locals()[m] = load_module(m)