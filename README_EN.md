# YOLO Object Detection Application

English | [Türkçe](README.md)

This is a Python application that performs real-time object detection using the YOLO (You Only Look Once) model. It can detect humans, vehicles, and animals.

## Features

- Real-time object detection
- Webcam and video file support
- FPS (Frame Per Second) display
- Detected object count tracking
- Screenshot capture
- Video recording
- Adjustable detection sensitivity

## Requirements

```bash
pip install -r requirements.txt
```

## Installation

1. Clone the project:
```bash
git clone https://github.com/Semihkulekcioglu/person_animal_car_detection_system.git
cd person_animal_car_detection_system
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

3. Run the program:
```bash
python object_detection_yolo.py
```

## Usage

The program uses webcam by default when started. To use a video file, set the `source` variable in `object_detection_yolo.py` to the path of your video file.

### Controls

- 'q': Exit program
- 's': Take screenshot
- '+': Increase confidence threshold
- '-': Decrease confidence threshold

## Directory Structure

```
.
├── object_detection_yolo.py    # Main program
├── best.pt                     # YOLO model file
├── requirements.txt            # Required packages
├── README.md                   # Turkish documentation
├── README_EN.md               # English documentation
└── detections/                 # Output directory
    ├── screenshots/            # Screenshots
    └── videos/                # Video recordings
```

## Contributing

1. Fork this repository
2. Create a new branch (`git checkout -b feature/newFeature`)
3. Commit your changes (`git commit -am 'New feature: Description'`)
4. Push your branch (`git push origin feature/newFeature`)
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.