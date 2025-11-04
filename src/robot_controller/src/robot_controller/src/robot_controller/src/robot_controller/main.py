"""
CLI + minimal HTTP control for the motor & sensor.
Run:
  python -m robot_controller.main --speed 40
Or HTTP server:
  python -m robot_controller.main --serve
Then visit: http://127.0.0.1:5000
"""
import argparse
from flask import Flask, jsonify, request
from .motor import Motor
from .sensors import DistanceSensor

app = Flask(__name__)
_motor = None
_sensor = DistanceSensor()

@app.get("/status")
def status():
    return jsonify({"ok": True})

@app.post("/motor")
def motor_api():
    """
    curl -X POST http://127.0.0.1:5000/motor -H "Content-Type: application/json" -d "{\"speed\":60}"
    """
    data = request.get_json(silent=True) or {}
    speed = float(data.get("speed", 0))
    global _motor
    if _motor is None:
        _motor = Motor(pwm_pin=18)
    _motor.set_speed(speed)
    return jsonify({"speed": speed})

@app.get("/distance")
def distance():
    return jsonify({"distance_cm": _sensor.read_cm()})

def run_cli(speed: float | None):
    global _motor
    _motor = Motor(pwm_pin=18)
    if speed is not None:
        _motor.set_speed(speed)
        print(f"Motor speed set to {speed}% (CTRL+C to stop).")
    try:
        while True:
            pass
    except KeyboardInterrupt:
        _motor.close()
        print("\nStopped.")

def run_server():
    app.run(host="127.0.0.1", port=5000, debug=False)

def main():
    parser = argparse.ArgumentParser(description="Robot Controller")
    parser.add_argument("--speed", type=float, help="Set motor speed (0-100)")
    parser.add_argument("--serve", action="store_true", help="Run HTTP server")
    args = parser.parse_args()

    if args.serve:
        run_server()
    else:
        run_cli(args.speed if args.speed is not None else 0.0)

if __name__ == "__main__":
    main()
