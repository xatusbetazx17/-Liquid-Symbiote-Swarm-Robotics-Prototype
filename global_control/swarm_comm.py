def broadcast_command(agents, command):
    """
    In a real BLE setting, this would send notifications to each Bot.
    Here we just set a flag on each simulated agent.
    """
    for bot in agents:
        if command == "FORM":
            bot.formed = True
