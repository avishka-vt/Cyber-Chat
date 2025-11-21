from flask import Flask, request, jsonify
from flask_cors import CORS
from conversation_manager import conversation_manager
from config import config
import os

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})


@app.route('/api/health', methods=['GET'])
def health():
    return jsonify({'status': 'healthy', 'service': 'cybersecurity_chatbot'}), 200


@app.route('/api/countries', methods=['GET'])
def get_countries():
    countries = conversation_manager.get_country_options()
    return jsonify({'countries': countries}), 200


@app.route('/api/session/create', methods=['POST'])
def create_session():
    try:
        data = request.get_json() or {}
        user_id = data.get('user_id')
        country_code = data.get('country_code', 'NYC')

        valid_countries = ['NYC', 'GERMANY', 'SOUTH_KOREA']
        if country_code not in valid_countries:
            return jsonify({'error': 'Invalid country code', 'valid_countries': valid_countries}), 400

        session_id = conversation_manager.create_session(user_id, country_code)

        return jsonify({
            'session_id': session_id,
            'user_id': conversation_manager.active_sessions[session_id]['user_id'],
            'country_code': country_code,
            'message': 'Welcome! I am your cybersecurity compliance advisor. How can I assist you today?'
        }), 201

    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/chat', methods=['POST'])
def chat():
    try:
        data = request.get_json()

        if not data or 'session_id' not in data or 'message' not in data:
            return jsonify({'error': 'Missing session_id or message'}), 400

        session_id = data.get('session_id')
        user_message = data.get('message', '').strip()

        if not user_message:
            return jsonify({'error': 'Message cannot be empty'}), 400

        result = conversation_manager.handle_user_input(session_id, user_message)

        if 'error' in result:
            return jsonify(result), 400

        return jsonify(result), 200

    except Exception as e:
        return jsonify({'error': str(e), 'success': False}), 500


@app.route('/api/session/<session_id>/switch-country', methods=['POST'])
def switch_country(session_id):
    try:
        data = request.get_json()

        if not data or 'country_code' not in data:
            return jsonify({'error': 'Missing country_code'}), 400

        new_country = data.get('country_code')
        valid_countries = ['NYC', 'GERMANY', 'SOUTH_KOREA']

        if new_country not in valid_countries:
            return jsonify({'error': 'Invalid country code', 'valid_countries': valid_countries}), 400

        success = conversation_manager.switch_country(session_id, new_country)

        if not success:
            return jsonify({'error': 'Invalid session'}), 404

        return jsonify({
            'success': True,
            'message': f'Switched to {new_country} cybersecurity compliance advisor',
            'country_code': new_country
        }), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/session/<session_id>/info', methods=['GET'])
def get_session_info(session_id):
    try:
        info = conversation_manager.get_session_info(session_id)

        if 'error' in info:
            return jsonify(info), 404

        return jsonify(info), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/session/<session_id>/end', methods=['POST'])
def end_session(session_id):
    try:
        success = conversation_manager.end_session(session_id)

        if not success:
            return jsonify({'error': 'Failed to end session'}), 400

        return jsonify({'success': True, 'message': 'Session ended'}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Endpoint not found'}), 404


@app.errorhandler(500)
def internal_error(error):
    return jsonify({'error': 'Internal server error'}), 500


if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=config.PORT,
        debug=config.FLASK_DEBUG
    )
