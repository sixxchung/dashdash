import dash_bootstrap_components as dbc
from dash import dcc, html
import dash_admin_components as dac

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

navbar = dac.Navbar(color="white",
                    text="I can write text in the navbar!",
                    children=top_right_ui)


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
        [
            dac.SidebarHeader(children="Cards"),
            dac.SidebarMenuItem(
                id='tab_cards', label='Basic cards', icon='box'),
            dac.SidebarMenuItem(id='tab_social_cards',
                                label='Social cards', icon='id-card'),
            dac.SidebarMenuItem(id='tab_tab_cards',
                                label='Tab cards', icon='image'),
            dac.SidebarHeader(children="Boxes"),
            dac.SidebarMenuItem(id='tab_basic_boxes',
                                label='Basic boxes', icon='desktop'),
            dac.SidebarMenuItem(id='tab_value_boxes',
                                label='Value/Info boxes', icon='suitcase'),
            dac.SidebarHeader(children="Gallery"),
            dac.SidebarMenuItem(label='Galleries',
                                icon='cubes', children=subitems),
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
    [
        html.Br(),
        html.P("Slide to change graph in Basic Boxes"),
        dcc.Slider(
            id='controlbar-slider',
            min=10,
            max=50,
            step=1,
            value=20
        )
    ],
    title="My right sidebar",
    skin="light"
)
