"""
Hardware abstraction layer.
- On Raspberry Pi: tries to import RPi.GPIO.
- Else: uses a MockGPIO so code runs on any PC.
"""
from typing import Any

class MockGPIO:
    BCM = "BCM"
    OUT = "OUT"

    def setmode(self, *_: Any, **__: Any): pass
    def setup(self, *_: Any, **__: Any): pass
    def PWM(self, *_: Any, **__: Any):
        class _PWM:
            def start(self, *_: Any): pass
            def ChangeDutyCycle(self, *_: Any): pass
            def stop(self): pass
        return _PWM()
    def cleanup(self): pass

try:
    import RPi.GPIO as _GPIO
    GPIO = _GPIO  # Real hardware
except Exception:
    GPIO = MockGPIO()  # Fallback for dev machines
