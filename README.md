# BLDC Motor Steering Panel

This project is a Flask application that serves as a steering panel for a Brushless DC (BLDC) motor. It allows users to set the speed of the motor, read the current speed from a microcontroller via Wi-Fi, and control the motor with stop and go buttons.

## Project Structure

```
bldc_steering_panel
├── app
│   ├── __init__.py
│   ├── routes.py
│   ├── static
│   │   ├── css
│   │   │   └── styles.css
│   └── templates
│       └── index.html
├── requirements.txt
├── run.py
└── README.md
```

## Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd bldc_steering_panel
   ```

2. **Create a virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application:**
   ```bash
   python run.py
   ```

5. **Access the steering panel:**
   Open your web browser and navigate to `http://127.0.0.1:5000`.

## Usage

- **Set Speed:** Enter a desired speed value in the input field and click the "Set Speed" button to update the motor speed.
- **Current Speed:** The current speed of the motor will be displayed on the interface.
- **Control Buttons:** Use the "Go" button to start the motor and the "Stop" button to halt its operation.

## Dependencies

- Flask
- Any additional libraries required for Wi-Fi communication with the microcontroller (to be specified in `requirements.txt`).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.