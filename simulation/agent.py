from mesa import Agent

class SymBotAgent(Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.energy = 100
        self.formed = False

    def step(self):
        # Simple energy drain
        self.energy = max(0, self.energy - self.random.random())
        # Move randomly if not formed
        if not self.formed:
            dx = self.random.uniform(-1, 1)
            dy = self.random.uniform(-1, 1)
            new_pos = (self.pos[0] + dx, self.pos[1] + dy)
            self.model.space.move_agent(self, new_pos)
