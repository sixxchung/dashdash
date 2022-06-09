from dash import Dash, html, dcc
import dash_admin_components as dac


import sys
import os
sys.path.append(
    os.path.dirname(os.path.abspath(os.path.dirname(os.path.dirname(__file__))))
) 

from app.cards        import cards_tab
from app.social_cards import social_cards_tab
from app.tab_cards    import tab_cards_tab
from app.basic_boxes  import basic_boxes_tab
from app.value_boxes  import value_boxes_tab


# =============================================================================
# Dash Admin Components
# =============================================================================

# Body
body = dac.Body(
    dac.TabItems([
        cards_tab,
        social_cards_tab,
        tab_cards_tab,
        basic_boxes_tab,
        value_boxes_tab,
        dac.TabItem(html.P('Gallery 1 (You can add Dash Bootstrap Components!)'),
                    id='content_gallery_1'),
        dac.TabItem(html.P('Gallery 2 (You can add Dash Bootstrap Components!)'),
                    id='content_gallery_2'),
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
