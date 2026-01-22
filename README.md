# Function Plot API

A simple FastAPI backend for generating and visualizing mathematical and signal-based functions using Matplotlib.

The API allows creating multiple signals on a single plot with customizable parameters such as amplitude, frequency, phase, noise, and line style.

---

## Features

- Supported signals: sin, cos, square, triangle, sawtooth
- Multiple plots on one figure
- Per-signal configuration (amplitude, frequency, phase, noise, style)
- Global plot options (grid, normalization, labels)
- PNG image returned by the API
- Optional saving of the plot to a file

---

## Tech Stack

- Python
- FastAPI
- Matplotlib
- NumPy
- SciPy

---

## Running the project

```bash
pip install -r requirements.txt
uvicorn main:app --reload
