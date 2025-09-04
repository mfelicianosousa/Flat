"""Este módulo implementa as classes de mensagem para um chat em Flet."""
import flet as ft


class Message:
    """Representa uma única mensagem com autor, texto e tipo de usuário."""
    def __init__(self, user_name: str, text: str, user_type: str):
        self.user_name = user_name
        self.text = text
        self.user_type = user_type

class ChatMessage(ft.Row):
    """Um widget que exibe uma mensagem de chat formatada com um avatar."""
    def __init__(self, message: Message):
        # É fundamental chamar o construtor da classe pai (ft.Row)
        super().__init__()

        # Atributos da Row
        self.alignment = ft.MainAxisAlignment.START
        self.vertical_alignment = ft.CrossAxisAlignment.START
        self.spacing = 5

        # Define o conteúdo do avatar com base no tipo de usuário
        if message.user_type == "ia":
            avatar_content = ft.Icon(ft.Icons.ASSISTANT, color=ft.Colors.WHITE)
        else:
            avatar_content = ft.Text(
                self.__get_initials(message.user_name),
                color=ft.Colors.WHITE
            )

        # Define a lista de controles que compõem a linha da mensagem
        self.controls = [
            ft.CircleAvatar(
                content=avatar_content,
                color=ft.Colors.WHITE,
                bgcolor=self.__get_avatar_color(message.user_name),
            ),
            ft.Column(
                [
                    ft.Text(
                        message.user_name,
                        size=12,
                        weight="bold",
                        color=ft.Colors.WHITE
                    ),
                    ft.Markdown(
                        message.text,
                        selectable=True,
                        extension_set="gitHubWeb",
                        code_theme="atom-one-dark",
                        width=350
                    )
                ],
                tight=True,
                spacing=5,
            )
        ]

    def __get_initials(self, user_name: str):
        """Pega as iniciais do nome de usuário para o avatar."""
        if not user_name:
            return "?"
        
        parts = user_name.split()
        if len(parts) == 1:
            return parts[0][0].upper() + parts[0][1].upper()
        else:
            return parts[0][0].upper() + parts[1][0].upper()

    def __get_avatar_color(self, user_name: str):
        """Gera uma cor consistente para o avatar do usuário."""
        color_lookup = [
            ft.Colors.AMBER, ft.Colors.BLUE, ft.Colors.BROWN,
            ft.Colors.CYAN, ft.Colors.GREEN, ft.Colors.INDIGO,
            ft.Colors.LIME, ft.Colors.ORANGE, ft.Colors.PINK,
            ft.Colors.RED, ft.Colors.TEAL, ft.Colors.YELLOW,
        ]
        user_hash = hash(user_name)
        index = user_hash % len(color_lookup)
        return color_lookup[index]