from mesa import Model
from mesa.time import RandomActivation
from mesa.space import ContinuousSpace
from .agent import SymBotAgent

class SymBotModel(Model):
    def __init__(self, N=100, width=100, height=100):
        super().__init__()
        self.num_agents = N
        self.space = ContinuousSpace(width, height, True)
        self.schedule = RandomActivation(self)
        for i in range(self.num_agents):
            agent = SymBotAgent(i, self)
            self.schedule.add(agent)
            x = self.random.uniform(0, width)
            y = self.random.uniform(0, height)
            self.space.place_agent(agent, (x, y))

    def step(self):
        self.schedule.step()
