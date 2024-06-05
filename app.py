from flask import Flask, jsonify, request
import uuid

app = Flask(__name__)

items = ['Apple','Mango','Orange']

@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(items), 200

@app.route('/add-items', methods=['POST'])
def create_item():
    new_item = request.json
    items.append(new_item)
    return jsonify(new_item), 201

@app.route('/get-item/<item_id>', methods=['GET'])
def get_item(item_id):
    item_id=int(item_id)
    if 0 <= item_id < len(items):
        return jsonify(items[item_id]), 200
    else:
        return jsonify({'error': 'Item not found'}), 404

@app.route('/update-item/<item_id>', methods=['PUT'])
def update_item(item_id):
    item_id=int(item_id)
    if 0 <= item_id < len(items):
        items[item_id] = request.json
        return jsonify(items[item_id]), 200
    else:
        return jsonify({'error': 'Item not found'}), 404
    
@app.route('/delete-item/<item_id>', methods=['DELETE'])
def delete_item(item_id):
    item_id=int(item_id)
    if 0 <= item_id < len(items):
        removed_item = items.pop(item_id)
        return jsonify(removed_item), 200
    else:
        return jsonify({'error': 'Item not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
