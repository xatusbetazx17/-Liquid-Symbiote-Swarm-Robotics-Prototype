from simulation.model import SymBotModel
from global_control.swarm_comm import broadcast_command

def main():
    # Initialize and run the simulation
    model = SymBotModel(N=200, width=100, height=100)
    for _ in range(100):
        model.step()

    # Issue formation command to all agents
    broadcast_command(model.schedule.agents, "FORM")
    print("Formation command issued to all agents.")

if __name__ == "__main__":
    main()
