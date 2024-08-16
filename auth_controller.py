from flask import Flask, request, jsonify
from auth_service import login
from decorators import role_required

app = Flask(__name__)

@app.route('/login', methods=['POST'])
def login_route():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    
    if not username or not password:
        return jsonify({"message": "Username and password are required"}), 400
    
    response = login(username, password)
    return jsonify(response)

@app.route('/admin-data', methods=['POST'])
@role_required('admin')
def admin_data():
    
    return jsonify({"message": "Access granted to admin data"})

@app.route('/user-data', methods=['POST'])
@role_required('user')
def user_data():
   
    return jsonify({"message": "Access granted to user data"})

if __name__ == '__main__':
    app.run(debug=True)
