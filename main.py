from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

def get_player_info(Id):    
    url = "https://shop2game.com/api/auth/player_id_login"
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Origin": "https://shop2game.com",
        "Referer": "https://shop2game.com/app",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
        "x-datadome-clientid": "10BIK2pOeN3Cw42~fake~key"
    }
    payload = {
        "app_id": 100067,
        "login_id": f"{Id}",
        "app_server_id": 0,
    }
    return requests.post(url, headers=headers, json=payload)

@app.route('/region', methods=['GET'])
def region():
    uid = request.args.get('uid')
    if not uid:
        return jsonify({"message": "Please provide a UID"})
    
    response = get_player_info(uid)
    try:
        if response.status_code == 200:
            data = response.json()
            if not data.get('nickname') and not data.get('region'):
                return jsonify({"message": "UID not found"})
            return jsonify({
                "uid": uid,
                "nickname": data.get('nickname', ''),
                "region": data.get('region', '')
            })
    except:
        pass
    return jsonify({"message": "UID not found"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
