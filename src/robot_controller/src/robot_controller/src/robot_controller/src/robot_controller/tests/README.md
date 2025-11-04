# robot-controller-py

Minimal Python robot control stack with:
- Motor PWM control (Raspberry Pi or PC via mock)
- Distance sensor example (mock)
- Optional HTTP API (Flask) for simple remote control

## Features
- Works on Raspberry Pi **and** regular PCs (mock HAL)
- CLI usage or HTTP server mode
- Clean `src/` layout, ready for extension

## Quick Start

```bash
# Create and activate venv (Windows PowerShell)
py -m venv .venv
. .venv/Scripts/Activate.ps1

# macOS/Linux:
# python3 -m venv .venv
# source .venv/bin/activate

pip install -r requirements.txt

# Run CLI (sets speed to 40%)
python -m robot_controller.main --speed 40

# Run HTTP server
python -m robot_controller.main --serve
# Then open http://127.0.0.1:5000
