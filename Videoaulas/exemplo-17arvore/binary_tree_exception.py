class BinaryTreeException(Exception):
    def __init__(self, mensagem) -> None:
        super().__init__(mensagem)