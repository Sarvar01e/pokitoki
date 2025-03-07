from typing import Optional


class FakeGPT:
    def __init__(self, error: Optional[Exception] = None):
        self.error = error
        self.question = None
        self.history = None

    async def ask(self, question: str, history: list) -> str:
        self.question = question
        self.history = history
        if self.error:
            raise self.error
        return question


class FakeDalle:
    def __init__(self, error: Optional[Exception] = None):
        self.error = error
        self.prompt = None
        self.size = None

    async def imagine(self, prompt: str, size: str) -> str:
        self.prompt = prompt
        self.size = size
        if self.error:
            raise self.error
        return "image"


class FakeBot:
    def __init__(self, username: str) -> None:
        self.username = username
        self.can_read_all_group_messages = True
        self.text = ""

    @property
    def name(self) -> str:
        return f"@{self.username}"

    async def send_chat_action(self, **kwargs) -> None:
        pass

    async def send_message(self, chat_id: int, text: str, **kwargs) -> None:
        self.text = text

    async def send_document(
        self, chat_id: int, document: object, caption: str, filename: str, **kwargs
    ) -> None:
        self.text = f"{caption}: {filename}"

    async def send_photo(self, chat_id: int, photo: str, caption: str = None, **kwargs) -> None:
        self.text = f"{caption}: {photo}"


class FakeApplication:
    def __init__(self, bot: FakeBot) -> None:
        self.chat_data = {}
        self.user_data = {}
        self.bot = bot
