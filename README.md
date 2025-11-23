# Sensor Simulation Project
A Python-based sensor simulator with a FastAPI backend, SQLite data storage and pytest automation.

## Features
Sensor model with temperature & state handling
- Input validation and safety limit enforcement
- Lightweight SQLite database wrapper
- FastAPI application exposing sensor instance
- Fully unit-tested with pytest (9/9 passing)

## Installation
```bash
git clone https://github.com/Dklish/sensor-sim.git
cd sensor-sim/sensor_sim_python
```
## Create Virtual Enviorment 
```bash 
python -m venv .venv
source .venv/bin/activate        # macOS/Linux
.venv\Scripts\activate           # Windows
```
## Install Dependencies 
```bash 
pip install -r requirements.txt
```

## Run Fast API App 
```bash 
uvicorn app.main:first_app --reload
```

## Run Tests
```bash 
python -m pytest
```
## Requirements
- Python 3.11+
- FastAPI
- pytest
- SQLite

**Author:** Diego Klish
