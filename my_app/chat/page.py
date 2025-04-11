import reflex as rx


from my_app import ui

from .form import chat_form
from .state import ChatMessage,ChatState
def message_box(chat_message:ChatMessage):
    print("message box")
    
    return rx.box(rx.text(chat_message.message))

def chat_page():
    
    
    return ui.base_layout(
        rx.vstack(
            rx.hstack(
            rx.heading("Chat Here", size ="5"),
            rx.cond(ChatState.not_found , "Not found","Found"),
            rx.button("+ New Chat", on_click=ChatState.create_new_and_redirect),
            rx.box(
                rx.foreach(
                    ChatState.messages,
                    lambda msg: rx.markdown(
                        msg.message,
                        color=rx.cond(msg.is_bot, "blue", "white"),  # Use rx.cond instead of if-else
                        align=rx.cond(msg.is_bot, "left", "right"),
                        padding="5px",
                        border_radius="5px",
                        background_color=rx.cond(msg.is_bot, "gray", "black"),
                        
                        
                    )),
                    ),
                          
                width = "100%",
                padding = "10px",
                border="1px solid black",
                border_radius = "5px",
                height = "300px",
                overflow_y = "scroll",
            ),

            rx.form(
                rx.input(placeholder = "Your message", name = "message"),
                rx.button("Submit",type="submit"),
                on_submit=ChatState.handle_submit,
            ),
            spacing = "5",
            justify = "center",
            min_height = "85vh",
            
                    
        ),
        rx.logo(),
    )