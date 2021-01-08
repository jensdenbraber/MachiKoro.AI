from machi_koro.player_choices import PlayerChoices
from machi_koro.game import EstablishmentBase, LandmarkCard


class AgentChoices(PlayerChoices):
    """
    docstring
    """

    def choice_two_dices(self):
        raise NotImplementedError

    def choice_build(self, buyable_establishments: EstablishmentBase, buyable_landmarks: LandmarkCard):
        game = self.player.game
        raise NotImplementedError
