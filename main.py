import flet as ft


def main(page: ft.Page):
    page.theme_mode = ft.ThemeMode.DARK
    page.title = "flet IA n8n"
    page.window.width = 420
    page.window.height = 740
    page.window.resizable = False
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    

    
    # Comandos / Ações
    def join_chat_click(e):
        if not join_user_name.value:
            join_user_name.error_text = "Nome é obrigatório!"
            join_user_name.update()
        else:
            page.session.set('user_name',join_user_name.value)
            page.dialog.open = False
            new_message.prefix = ft.Text(f"{join_user_name.value}:")
            # new_message.update()
            page.update() 
    def send_message_click(e):
        pass
     
    app_bar = ft.AppBar(
        leading=ft.Icon(ft.Icons.ASSISTANT),
        leading_width=50,
        title = ft.Text("Flet IA com n8n"),
        center_title = True,
        bgcolor = ft.Colors.SURFACE,
    )
    
    join_user_name = ft.TextField(
        label="Digite seu nome",
        autofocus=True,
        on_submit=join_chat_click,
    )
    page.dialog = ft.AlertDialog(
        open=True,
        modal=True,
        title=ft.Text("Bem-Vindo(a)!", size=20, color=ft.Colors.WHITE),
        content=ft.Column([join_user_name], width=300, height=70, tight=True),
        actions=[ft.ElevatedButton(text='Começar',on_click=join_chat_click)],
        actions_alignment=ft.MainAxisAlignment.END,      
    )
    
    chat = ft.ListView(
        expand  = True,
        spacing = 10,
        padding = 20,
        # width = 140,
        auto_scroll= True, 
    )
  
    
    new_message = ft.TextField(
       hint_text = "No que posso ajudar?",
       autofocus=True,
       shift_enter=True,
       min_lines = 1,
       max_lines = 5,
       filled=True,
       bgcolor= "#273c75",
       # border_radius=ft.border_radius.all(20),
       border_radius=10,
       # color=ft.Colors.ON_SURFACE,
       color="#FFFFFF",
       # border_color = ft.Colors.TRANSPARENT,
       border_color="#273c75",
       # focused_border_color="#FFFFFF",
       on_submit=send_message_click,
           
    )
    
 
    container = ft.Container(
        width =page.window.width,
        height =page.window.height,
        expand=True,
        bgcolor="#192a56",
        border_radius=30,
        alignment=ft.Alignment(0,0),
        content=ft.Column(
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=10,
            controls=[
                ft.Container(
                    content=
                        ft.Row(
                          alignment=ft.MainAxisAlignment.CENTER,  
                          vertical_alignment=ft.CrossAxisAlignment.CENTER,
                          spacing=10, 
                          controls=[
                              ft.Text('pyFlet IA com n8n',size=14,color=ft.Colors.WHITE)
                              ]       
                        ),
                        border_radius=5,
                        height=40,
                        margin=ft.margin.only(left=20, top=20, right=20, bottom=0),
                            
                ),
                ft.Container(
                    content=chat,
                    border_radius=10,
                    expand=True,
                    padding=ft.padding.all(10),
                    margin=ft.margin.only(left=20, top=5, right=20, bottom=0),
                    bgcolor="#273c75"
                             
                ),
                ft.Container(
                    margin=ft.margin.only(left=20, top=5, right=20, bottom=20),
                    content=ft.Row(
                          controls=[
                              new_message,
                              ft.IconButton(
                                 icon=ft.Icons.SEND_ROUNDED,
                                 tooltip='Enviar',
                                 icon_color=ft.Colors.WHITE,
                                 on_click=send_message_click,
                                     
                              )
                          ],
                          # alignment=ft.MainAxisAlignment.CENTER,  
                          # vertical_alignment=ft.CrossAxisAlignment.CENTER,
                          # spacing=10, 
                    ),
                   
                    
                   
                ),
               
            ]    
        )
        
    )
    
    def update_size(e):
        container.width = page.window.width
        container.height = page.window.height
        
    page.on_window_resize = update_size
    
    page.add(page.dialog, container)
    page.update()

ft.app(main)