import random

class DistanceSensor:
    """Mock sensor example. Replace with real HC-SR04 or LiDAR reading."""
    def read_cm(self) -> float:
        # demo: 20–120 cm arası rastgele değer
        return round(random.uniform(20.0, 120.0), 1)
