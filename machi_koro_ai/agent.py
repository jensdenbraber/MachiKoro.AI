from machi_koro.player import Player
from machi_koro_ai.agent_choices import AgentChoices


class Agent(Player):
    """
    Ai agent class
    """

    def __init__(self, player_id: int, name: str, player_choices: AgentChoices):
        super().__init__(player_id, name, player_choices)
