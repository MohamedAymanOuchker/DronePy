# DronePy

A Python project for controlling a DJI Tello drone with features including keyboard control, computer vision, and autonomous flight capabilities.

## Features

- **Keyboard Control**: Real-time drone control using keyboard input
- **Computer Vision**: Face tracking, line following, and color detection
- **Autonomous Flight**: Basic movements and surveillance capabilities
- **Mapping**: Create maps using drone data
- **Image Processing**: Stream and process video from the drone's camera

## Requirements

- Python 3.7+
- DJI Tello drone
- WiFi connection to the drone

## Getting Started

1. Clone or download this repository.
2. (Optional) Create and activate a virtual environment.
3. Install dependencies:

    ```sh
    pip install -r requirements.txt
    ```

## Usage

### Keyboard Control

```sh
python KeyboardController.py
```
- Use arrow keys for movement (left/right/forward/backward)
- Use `w`/`s` for up/down, `a`/`d` for yaw (rotate)
- Press `e` to take off, `q` to land

### Computer Vision Features

```sh
python FaceTracking.py
```
- Tracks faces in real-time using the drone's camera
- Requires `Resources/haarcascade_frontalface_default.xml`

```sh
python LineFollower.py
```
- Autonomous line following capability

```sh
python ColorPicker.py
```
- Color detection and tracking

### Surveillance and Mapping

```sh
python Surveillance.py
```
- Automated surveillance mode

```sh
python Mapping.py
```
- Create maps using drone data

### Basic Features

```sh
python ImageCapture.py
```
- Stream and display video from the drone's camera

```sh
python BasicMovements.py
```
- Run a simple movement sequence

## Project Structure

- `KeyboardController.py` — Main keyboard control script
- `KeyPressModule.py` — Keyboard input handler
- `FaceTracking.py` — Face detection and tracking
- `LineFollower.py` — Line following implementation
- `ColorPicker.py` — Color detection and tracking
- `Surveillance.py` — Surveillance mode implementation
- `Mapping.py` — Mapping functionality
- `ImageCapture.py` — Video streaming from the drone
- `BasicMovements.py` — Example of scripted movement
- `requirements.txt` — Python dependencies
- `Resources/` — Resources for computer vision (e.g., face cascade XML, sample images)

## Dependencies

- djitellopy >=2.4
- pygame >=2.0
- opencv-python >=4.5

## Notes

- Ensure your computer is connected to the Tello drone's WiFi before running any scripts.
- Tested on Windows with Python 3.10.
- Some features may require good lighting conditions for optimal performance.
- Keep the drone's battery level in mind during extended operations.

## Troubleshooting

- If you encounter issues with video streaming, ensure your firewall allows UDP traffic.
- For face tracking, make sure `Resources/haarcascade_frontalface_default.xml` is present.
- If you have dependency issues, try upgrading pip: `python -m pip install --upgrade pip`.
