# from machi_koro import lobby, player

from machi_koro.game import Game

from machi_koro_ai.agent import Agent
from machi_koro_ai.agent_choices import AgentChoices


class MachiKoroAi(object):
    """
    docstring
    """

    def __init__(self) -> None:
        super().__init__()

        # Observer
        # Action
        # Reward
        # Environment State
        # Agent State

        # Agent
        # policy - agents behavior function
        # value function - How good is each state and/or action
        # model - agent's representation of the environment
        # models predicts what the environment will do next

        # Q defines how good is it to take a particular action from a given state
        # V defines how good is it to be in a specific state

        # self.actions = ['buy_landmark', 'buy_establishment', 'nothing']

        agent_choices1 = AgentChoices()
        agent1 = Agent(1, "agent 1", agent_choices1)

        agent_choices2 = AgentChoices()
        agent2 = Agent(2, "agent 2", agent_choices2)

        players = [agent1, agent2]

        game = Game(1, players)
        game.start()

    # def get_legal_actions(self):
    #     ''' Get all leagal actions
    #     Returns:
    #         encoded_action_list (list): return encoded legal action list (from str to int)
    #     '''
    #     encoded_action_list = []
    #     for i in range(len(self.actions)):
    #         encoded_action_list.append(i)
    #     return encoded_action_list


n_games = 10000

if __name__ == "__main__":
    machi_koro_ai = MachiKoroAi()

    agent_choices1 = AgentChoices()
    agent1 = Agent(1, "agent 1", agent_choices1)

    agent_choices2 = AgentChoices()
    agent2 = Agent(2, "agent 2", agent_choices2)

    players = [agent1, agent2]

    for i in range(n_games):

        game = Game(1, players)
        game.start()
