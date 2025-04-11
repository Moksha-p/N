"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx


from my_app import ui 

def about_us_page() -> rx.Component:
    # Welcome Page (Index)
    return ui.base_layout(
        # rx.color_mode.button(position="top-right"),
        rx.vstack(
            rx.heading("Welcome to Reflex!", size="9"),
            spacing = "5",
            justify = "center",
            min_height = "85vh",
 

        ),
        rx.logo(),
    )
  
    


app = rx.App()


