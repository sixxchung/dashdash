import sys
import os
sys.path.append(
    os.path.dirname(os.path.abspath(os.path.dirname(os.path.dirname(__file__))))
) 
#from dashPages.basic_cards.basic_cards    import basic_cards_tab
#from dashPages.social_cards.social_cards  import social_cards_tab
#from dashPages.tab_cards.tab_cards        import tab_cards_tab
#from dashPages.basic_boxes.basic_boxes    import tab
#from dashPages.value_boxes.value_boxes    import value_boxes_tab

import dashPages.basic_cards.view   as basic_cards
import dashPages.social_cards.view  as social_cards
import dashPages.tab_cards.view     as tab_cards
import dashPages.basic_boxes.view   as basic_boxes
import dashPages.value_boxes.view   as value_boxes

from dash import Dash, html, dcc
import dash_admin_components as dac

MENU_ITEMS = ("basic_cards", "social_cards", "tab_cards",
              "basic_boxes", "value_boxes", 
              "gallery_1", "gallery_2", "stock")

# =============================================================================
# Dash Admin Components
# =============================================================================

# Body
body = dac.Body(
    dac.TabItems([
        # basic_cards._tab,
        # social_cards_tab,
        # tab_cards_tab,
        # basic_boxes.tab,
        # value_boxes_tab,

        basic_cards.content,
        social_cards.content,
        tab_cards.content,
        basic_boxes.content,
        value_boxes.content,

        dac.TabItem(  
            children = html.P('Gallery 1 (You can add Dash Bootstrap Components!)'),
            id = 'content_gallery_1'
        ),
        dac.TabItem(
            children = html.P('Gallery 2 (You can add Dash Bootstrap Components!)'),
            id='content_gallery_2'
        ),
    ])
)


# Footer
footer = dac.Footer(
	html.A("@DawidKopczyk, Quantee",
            href="https://twitter.com/quanteeai",
            target="_blank",
        ),
	right_text="2019"
)

# =============================================================================
# App Layout
# =============================================================================
#app.layout = dac.Page([navbar, sidebar, body, controlbar, footer])
