

import os
import sys

from dash import html, dcc
import dash_admin_components as dac

sys.path.append(
    os.path.dirname(os.path.abspath(
        os.path.dirname(os.path.dirname(__file__))))
)

import dashPages.stock.view as stock
import dashPages.gallery_2.view as gallery_2
import dashPages.gallery_1.view as gallery_1
import dashPages.value_boxes.view as value_boxes
import dashPages.basic_boxes.view as basic_boxes
import dashPages.tab_cards.view as tab_cards
import dashPages.social_cards.view as social_cards
import dashPages.basic_cards.view as basic_cards

MENU_ITEMS = ("basic_cards", "social_cards", "tab_cards",
              "basic_boxes", "value_boxes",
              "gallery_1", "gallery_2", "stock")

# =============================================================================
# Dash Admin Components
# =============================================================================

# Body
body = dac.Body(
    dac.TabItems([
        basic_cards.content,
        social_cards.content,
        tab_cards.content,
        basic_boxes.content,
        value_boxes.content,

        gallery_1.content,
        gallery_2.content,
        stock.content,

        # eval(f"myitems"),
        # exec(f"myitems"),

        dac.TabItem(id='content_gallery_01',
                    children=html.P('Gallery 1 (You can add Dash Bootstrap Components!)')),
        dac.TabItem(id='content_gallery_02',
                    children=html.P('Gallery 2 (You can add Dash Bootstrap Components!)')),
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

# Navbar
top_right_ui = dac.NavbarDropdown(
    badge_label="!",
    badge_color="danger",
    src="https://quantee.ai",
        header_text="2 Items",
    children=[
        dac.NavbarDropdownItem(
            children="message 1",
            date="today"
        ),
        dac.NavbarDropdownItem(
            children="message 2",
            date="yesterday"
        ),
    ]
)

navbar = dac.Navbar(
    color="white",
    text="I can write text in the navbar!",
    children=top_right_ui
)


# Sidebar
subitems = [
    dac.SidebarMenuSubItem(id='tab_gallery_1',
                           label='Gallery 1',
                           icon='arrow-circle-right',
                           badge_label='Soon',
                           badge_color='success'),
    dac.SidebarMenuSubItem(id='tab_gallery_2',
                           label='Gallery 2',
                           icon='arrow-circle-right',
                           badge_label='Soon',
                           badge_color='success')
]

sidebar = dac.Sidebar(
    dac.SidebarMenu(
        children=[
            dac.SidebarHeader(
                children="Cards"),  # ------------------------------
            dac.SidebarMenuItem(id='tab_cards',
                                label='Basic cards', icon='box'),
            dac.SidebarMenuItem(id='tab_social_cards',
                                label='Social cards', icon='id-card'),
            dac.SidebarMenuItem(id='tab_tab_cards',
                                label='Tab cards', icon='image'),
            dac.SidebarHeader(
                children="Boxes"),  # ------------------------------
            dac.SidebarMenuItem(id='tab_basic_boxes',
                                label='Basic boxes', icon='desktop'),
            dac.SidebarMenuItem(id='tab_value_boxes',
                                label='Value/Info boxes', icon='suitcase'),
            dac.SidebarHeader(
                children="Gallery"),  # ----------------------------
            dac.SidebarMenuItem(
                label='Galleries', icon='cubes',
                children=subitems),
        ]
    ),
    title='Dash Admin',
    skin="light",
    color="primary",
    brand_color="primary",
    url="https://quantee.ai",
    src="https://adminlte.io/themes/AdminLTE/dist/img/user2-160x160.jpg",
    elevation=3,
    opacity=0.8
)


# Controlbar
controlbar = dac.Controlbar(
    children=[
        html.Br(),
        html.P("Slide to change graph in Basic Boxes"),
        dcc.Slider(id='controlbar-slider',
                   min=10,
                   max=50,
                   step=1,
                   value=20
                   )
    ],
    title="My right sidebar",
    skin="light"
)


# =============================================================================
# App Layout
# =============================================================================
#app.layout = dac.Page([navbar, sidebar, body, controlbar, footer])
