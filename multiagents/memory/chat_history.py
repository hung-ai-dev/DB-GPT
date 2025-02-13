from typing import List
from pydantic import Field
from multiagents.message import Message

from . import memory_registry
from .base import BaseMemory

@memory_registry.register("chat_history")
class ChatHistoryMemory(BaseMemory):
    messages: List[Message] = Field(default=[])

    def add_message(self, messages: List[Message]) -> None:
        for message in messages:
            self.messages.append(message)

    def to_string(self, add_sender_prefix: bool = False) -> str:
        if len(self.messages) == 0:
            return ""
        if add_sender_prefix:
            return "\n".join(
                [
                    f"[{message.sender}]: {str(message.content)}"
                    if message.sender != ""
                    else str(message.content)
                    for message in self.messages
                ]
            )
        else:
            return "\n".join([str(message.content) for message in self.messages])

    def reset(self) -> None:
        self.messages = []
