class BiometricsMonitor:
    """
    Simulated vital signs monitor.
    """
    def __init__(self):
        self.heart_rate = 72
        self.oxygen     = 98

    def get_vitals(self):
        return {
            "heart_rate": self.heart_rate,
            "oxygen": self.oxygen
        }
