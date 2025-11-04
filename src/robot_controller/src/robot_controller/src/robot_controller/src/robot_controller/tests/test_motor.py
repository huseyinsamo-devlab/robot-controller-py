from robot_controller.motor import Motor

def test_can_set_speed(monkeypatch):
    m = Motor(pwm_pin=18)
    m.set_speed(50)
    m.stop()
    m.close()
