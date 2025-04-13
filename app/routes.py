from flask import Blueprint, render_template, request, jsonify
import requests

bp = Blueprint('main', __name__)

# Replace with the actual IP address of your microcontroller
MICROCONTROLLER_IP = 'http://192.168.4.1'

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/set_speed', methods=['POST'])
def set_speed():
    speed = request.form.get('speed')
    if not speed or not speed.isdigit():
        return jsonify({'error': 'Invalid speed value'}), 400

    try:
        response = requests.post(
            f'{MICROCONTROLLER_IP}/speed_value',
            json={'speed': int(speed)},
            headers={'Content-Type': 'application/json'}
        )
        response.raise_for_status()

        # Handle plain string response
        if response.headers.get('Content-Type') == 'text/plain' or response.text:
            return jsonify({'message': response.text.strip()}), 200

        # Attempt to parse JSON if the response is JSON
        return jsonify(response.json())
    except requests.exceptions.RequestException as e:
        return jsonify({'error': f'Failed to set speed: {str(e)}'}), 500
    except ValueError as e:
        # Handle JSON parsing errors
        return jsonify({'error': f'Invalid response from microcontroller: {str(e)}'}), 500

@bp.route('/get_speed', methods=['GET'])
def get_speed():
    try:
        # Send a GET request to the microcontroller
        response = requests.get(f'{MICROCONTROLLER_IP}/measured_speed_value')
        response.raise_for_status()

        # Parse the JSON response from the microcontroller
        data = response.json()

        # Ensure the expected key exists in the response
        if "measured_speed" in data:
            return jsonify({'speed': data["measured_speed"]}), 200
        else:
            return jsonify({'error': 'Invalid response format from microcontroller'}), 500
    except requests.exceptions.RequestException as e:
        return jsonify({'error': f'Failed to get speed: {str(e)}'}), 500
    except ValueError as e:
        # Handle JSON parsing errors
        return jsonify({'error': f'Invalid JSON response from microcontroller: {str(e)}'}), 500
    

@bp.route('/stop', methods=['POST'])
def stop_motor():
    try:
        response = requests.post(f'{MICROCONTROLLER_IP}/stop')
        response.raise_for_status()

        # Handle plain string response
        if response.headers.get('Content-Type') == 'text/plain' or response.text:
            return jsonify({'message': response.text.strip()}), 200

        # Attempt to parse JSON if the response is JSON
        return jsonify(response.json())
    except requests.exceptions.RequestException as e:
        return jsonify({'error': f'Failed to stop motor: {str(e)}'}), 500
    except ValueError as e:
        # Handle JSON parsing errors
        return jsonify({'error': f'Invalid response from microcontroller: {str(e)}'}), 500

@bp.route('/go', methods=['POST'])
def go_motor():
    try:
        response = requests.post(f'{MICROCONTROLLER_IP}/go')
        response.raise_for_status()

        # Handle plain string response
        if response.headers.get('Content-Type') == 'text/plain' or response.text:
            return jsonify({'message': response.text.strip()}), 200

        # Attempt to parse JSON if the response is JSON
        return jsonify(response.json())
    except requests.exceptions.RequestException as e:
        return jsonify({'error': f'Failed to start motor: {str(e)}'}), 500
    except ValueError as e:
        # Handle JSON parsing errors
        return jsonify({'error': f'Invalid response from microcontroller: {str(e)}'}), 500