# Security-Focused Web App for Object and People Detection


This web application aims to enhance security measures in high-security environments such as airports, government buildings, or other restricted access areas. It utilizes OpenCV, Convolutional Neural Networks (CNNs), and Django to detect and monitor both objects and individuals passing through the premises.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the app.

```bash
pip install tensorflow opencv-python cvlib django
```

## Usage

```bash
# Start the Django server
python manage.py runserver

```
Access the application through a web browser at http://localhost:8000/. The app will start detecting and monitoring objects and people passing through the premises using the connected camera.

## Features
* Object Detection: Utilizes CNNs through the cvlib library to identify various objects present within the camera's view.

* People Detection: Employs OpenCV and cvlib to detect and track individuals moving within the monitored area.

* Real-time Monitoring: Provides real-time monitoring and alerts security personnel in case of any suspicious or unauthorized objects or activities.

* Web Interface: Accessible through a web browser, enabling remote monitoring and administration
## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
