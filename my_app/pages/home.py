"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config
from my_app import ui , navigation

# def home_page() -> rx.Component:
#     # Welcome Page (Index)
#     return ui.base_layout(
#         # rx.color_mode.button(position="top-right"),
#         rx.vstack(
#             rx.heading("Welcome to Reflex!", size="9"),
#             spacing = "5",
#             justify = "center",
#             min_height = "85vh",
 

#         ),
#         rx.logo(),
#     )
  
    

      
def home_page() -> rx.Component:
    # Welcome Page (Index)
    return ui.base_layout(
        # rx.color_mode.button(position="top-right"),
        rx.vstack(
            rx.heading("Welcome to Reflex!", size="9"),
            rx.text(
                "Get started by editing ",
                rx.code(f"{config.app_name}/{config.app_name}.py"),
                size="5",
            ),
            rx.link(
                rx.button("Check out our docs!"),
                href="https://reflex.dev/docs/getting-started/introduction/",
                is_external=True,
            ),
            rx.box("Go to about",on_click = navigation.state.NavState.to_about_us),
            spacing="5",
            justify="center",
            min_height="85vh",
        ),
        rx.logo(),
    )


app = rx.App()


