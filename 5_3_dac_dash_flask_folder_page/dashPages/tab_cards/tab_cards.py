from dash import html
import dash_admin_components as dac


tab_cards_tab = dac.TabItem(id='content_tab_cards',

                            children=[

                                html.Div(
                                    [

                                        dac.TabBox(
                                            [
                                                dac.TabBoxHeader(
                                                    dac.TabBoxMenu(
                                                        [
                                                            dac.TabBoxMenuItem(tab_id='tab_box_1_tab1',
                                                                               label='Tab 1'),
                                                            dac.TabBoxMenuItem(tab_id='tab_box_1_tab2',
                                                                               label='Tab 2'),
                                                            dac.TabBoxMenuItem(tab_id='tab_box_1_tab3',
                                                                               label='Tab 3')
                                                        ],
                                                        id='tab_box_1_menu'
                                                    ),
                                                    collapsible=False,
                                                    closable=True,
                                                    title="A card with tabs"
                                                ),
                                                dac.TabBoxBody(
                                                    id='tab_box_1'
                                                )
                                            ],
                                            width=6,
                                            elevation=2
                                        ),

                                        dac.TabBox(
                                            [
                                                dac.TabBoxHeader(
                                                    dac.TabBoxMenu(
                                                        [
                                                            dac.TabBoxMenuItem(tab_id='tab_box_2_tab1',
                                                                               label='Tab 1',
                                                                               color='dark'),
                                                            dac.TabBoxMenuItem(tab_id='tab_box_2_tab2',
                                                                               label='Tab 2',
                                                                               color='danger'),
                                                            dac.TabBoxMenuItem(tab_id='tab_box_2_tab3',
                                                                               label='Tab 3',
                                                                               color='primary')
                                                        ],
                                                        id='tab_box_2_menu'
                                                    ),
                                                    closable=True,
                                                    title="A card with colorful tabs"
                                                ),
                                                dac.TabBoxBody(
                                                    id='tab_box_2'
                                                )
                                            ],
                                            color='warning',
                                            width=6,
                                            elevation=2
                                        )
                                    ],
                                    className='row'
                                )

                            ]
                            )
