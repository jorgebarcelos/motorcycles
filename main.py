import mysql.connector
from flask import Flask, make_response, jsonify, request

motorcycles_db = mysql.connector.connect(
    host='localhost',
    user='MyUser',
    password='123456',
    database='motorcycles'
)

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False


@app.route('/motorcycles', methods=['GET'])
def get_motorcycles():
    """Get all motorcycles from local database"""
    motorcycles_cursor = motorcycles_db.cursor()
    motorcycles_cursor.execute('SELECT * FROM bikes')
    all_bikes = motorcycles_cursor.fetchall()
    bikes_list = list()
    for bike in all_bikes:
        bikes_list.append(
            {
                'id': bike[0],
                'brand': bike[1],
                'model': bike[2],
                'model_year': bike[3]
            }
        )
    return make_response(jsonify(message='Motorcycles:', data=bikes_list))


@app.route('/motorcycles', methods=['POST'])
def create_motorcycle():
    """Create a new motorcycle in DB"""
    bike = request.json
    motorcycles_cursor = motorcycles_db.cursor()
    bike_sql = f"INSERT INTO bikes (brand, model, model_year) VALUES ('{bike['brand']}', '{bike['model']}', '{bike['model_year']}')"
    motorcycles_cursor.execute(bike_sql)
    motorcycles_db.commit()

    return make_response(jsonify(message='Success to add motorcycle in database :', data=bike))


app.run(debug=True)