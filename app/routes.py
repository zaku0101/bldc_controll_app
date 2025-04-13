from flask import Blueprint, render_template, request, jsonify
import requests

bp = Blueprint('main', __name__)

# Replace with the actual IP address of your microcontroller
MICROCONTROLLER_IP = 'http://192.168.1.100'

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/set_speed', methods=['POST'])
def set_speed():
    speed = request.form.get('speed')
    response = requests.post(f'{MICROCONTROLLER_IP}/set_speed', json={'speed': speed})
    return jsonify(response.json())

@bp.route('/get_speed', methods=['GET'])
def get_speed():
    response = requests.get(f'{MICROCONTROLLER_IP}/get_speed')
    return jsonify(response.json())

@bp.route('/stop', methods=['POST'])
def stop_motor():
    response = requests.post(f'{MICROCONTROLLER_IP}/stop')
    return jsonify(response.json())

@bp.route('/go', methods=['POST'])
def go_motor():
    response = requests.post(f'{MICROCONTROLLER_IP}/go')
    return jsonify(response.json())