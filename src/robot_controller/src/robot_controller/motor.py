from .hw import GPIO

class Motor:
    def __init__(self, pwm_pin: int, freq_hz: int = 1000):
        self._gpio = GPIO
        self._gpio.setmode(GPIO.BCM)
        self._gpio.setup(pwm_pin, GPIO.OUT)
        self._pwm = self._gpio.PWM(pwm_pin, freq_hz)
        self._pwm.start(0)  # start with 0% duty

    def set_speed(self, duty_percent: float):
        """0–100 arası hız yüzdesi."""
        duty = max(0.0, min(100.0, duty_percent))
        self._pwm.ChangeDutyCycle(duty)

    def stop(self):
        self._pwm.ChangeDutyCycle(0)

    def close(self):
        try:
            self._pwm.stop()
            self._gpio.cleanup()
        except Exception:
            pass
