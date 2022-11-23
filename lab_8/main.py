from admin_user_order_car import *
import jwt
import flask
from werkzeug.security import generate_password_hash, check_password_hash


def control_limits(list_of_elem, given_offset, given_limit):
    given_offset = int(given_offset)
    given_limit = int(given_limit)
    elem_from = given_offset * given_limit
    elem_to = (given_offset + 1) * given_limit
    if elem_from >= len(list_of_elem):
        return {"status": 404, "message": "car is not found"}
    if elem_to > len(list_of_elem):
        elem_to = len(list_of_elem)
    to_return = []
    for x in range(elem_from, elem_to):
        to_return.append((list_of_elem[x]))
    return to_return


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        token = flask.request.args.get('token')
        if not token:
            return flask.jsonify({'message': 'Token is missing!'}), 401
        try:
            data = jwt.decode(token, str(app.config['SECRET_KEY']), algorithms=["HS256"])
            current_user = User.query.filter_by(email=data['email']).first()
        except:
            return flask.jsonify({'message': 'Token is invalid!'}), 401
        return f(current_user, *args, **kwargs)
    return decorated


@app.route('/cars/', methods=['GET'])
def get_all_with_sort_and_search():
    cars = Car.query.all()
    all_requests = Car.query
    count = all_requests.count()
    print(cars)
    if len(cars) > 0:
        if 'sort_by' in request.args and 'sort_type' in request.args:
            fields = cars[0].__dict__
            field = request.args['sort_by']
            if field in fields:
                cars.sort(key=lambda car_: getattr(car_, field))
                if request.args['sort_type'] == "desc":
                    cars.reverse()
        if 's' in request.args:
            find_part = request.args['s']
            found = []
            for car_ in cars:
                if car_.elem_search(find_part):
                    found.append(car_.to_file())
                    count = len(found)
            to_return = found
        else:
            res3 = []
            for i in range(len(cars)):
                res3.append(cars[i].to_file())
            to_return = res3
        if 'limit' in request.args:
            if 'offset' in request.args:
                to_return = control_limits(to_return, request.args['offset'], request.args['limit'])
            else:
                to_return = control_limits(to_return, 0, request.args['limit'])
        return jsonify(to_return, {"count": len(to_return)})

    else:
        return jsonify({"status": 404, "message": "car is not found"}), 404


@app.route('/cars/<given_id>', methods=['GET'])
def get_one_request(given_id):
    cars = Car.query
    element = Car.query.get(given_id)
    if element not in cars:
        return jsonify({"status": 404, "message": "car is not found"}), 404
    return jsonify(element.to_file()), 200


@app.route('/cars', methods=['POST'])
@token_required
def add_request(current_user):
    if not current_user.is_admin:
        return jsonify({'status': 403, "message": "You are not admin!"}), 403
    for elem in Car.query:
        if request.json["ID"] == elem.get_ID:
            return jsonify({'status': 404, "message": "car already exits"}), 404
    data = []
    for key in Car.get_attributes():
        data.append(request.json[key])
    try:
        input_value = Car(*data)
        print(input_value)
    except ValidationError as error:
        return jsonify({"status": 400, "message": str(error)}), 400
    db.session.add(input_value)
    db.session.commit()
    return jsonify({"status": 200, "message": "new car has been successfully added"})


@app.route('/cars/<given_id>', methods=['PUT'])
@token_required
def update_request(current_user, given_id):
    if not current_user.is_admin:
        return jsonify({'status': 403, "message": "You are not admin!"}), 403
    cars = Car.query
    element = Car.query.get(given_id)
    if element not in cars:
        return jsonify({"status": 404, "message": "car is not found"}), 404
    else:
        input_data = []
        for key in Car.get_attributes():
            input_data.append(request.json[key])
        try:
            new_payment = Car(*input_data)
        except ValidationError as error:
            return jsonify({"status": 400, "message": str(error)}), 400
        db.session.delete(element)
        db.session.add(new_payment)
        db.session.commit()
        return jsonify({"status": 200, "message": "car has been successfully updated"})


@app.route('/cars/<given_id>', methods=['DELETE'])
@token_required
def delete_request(current_user, given_id):
    if not current_user.is_admin:
        return jsonify({'status': 403, "message": "You are not admin!"}), 403
    elements = Car.query
    car_to_delete = Car.query.get(given_id)
    if car_to_delete not in elements:
        return jsonify({"status": 404, "message": "car is not found"}), 404
    else:
        db.session.delete(car_to_delete)
        db.session.commit()
        return jsonify({"status": 200, "message": "car has been successfully deleted"})


@app.route('/user/', methods=['GET'])
def get_all_with_sort_and_search1():
    cars = User.query.all()
    all_requests = User.query
    count = all_requests.count()
    print(cars)
    if len(cars) > 0:
        if 'sort_by' in request.args and 'sort_type' in request.args:
            fields = cars[0].__dict__
            field = request.args['sort_by']
            if field in fields:
                cars.sort(key=lambda car_: getattr(car_, field))
                if request.args['sort_type'] == "desc":
                    cars.reverse()
        if 's' in request.args:
            find_part = request.args['s']
            found = []
            for car_ in cars:
                if car_.elem_search(find_part):
                    found.append(car_.to_file())
                    count = len(found)
            to_return = found
        else:
            res3 = []
            for i in range(len(cars)):
                res3.append(cars[i].to_file())
            to_return = res3
        if 'limit' in request.args:
            if 'offset' in request.args:
                to_return = control_limits(to_return, request.args['offset'], request.args['limit'])
            else:
                to_return = control_limits(to_return, 0, request.args['limit'])
        return jsonify(to_return, {"count": len(to_return)})

    else:
        return jsonify({"status": 404, "message": "user is not found"}), 404


@app.route('/user/<given_id>', methods=['GET'])
def get_one_request1(given_id):
    cars = User.query
    element = User.query.get(given_id)
    if element not in cars:
        return jsonify({"status": 404, "message": "user is not found"}), 404
    return jsonify(element.to_file()), 200


@app.route('/register', methods=['POST'])
def add_request3():
    for elem in User.query:
        if request.json["ID"] == elem.get_ID:
            return jsonify({'status': 404, "message": "user already exits"}), 404
    data = flask.request.get_json()
    hashed_password = generate_password_hash(data["password"], method="sha256")
    try:
        db.session.add(User(data["ID"], data["first_name"], data["last_name"], data["email"], hashed_password))
        db.session.commit()
    except ValidationError as error:
        return jsonify({"status": 400, "message": str(error)}), 400
    return jsonify({"status": 200, "message": "new user has been successfully registered"})


@app.route('/login', methods=['POST'])
def add_request1():
    data = flask.request.get_json()
    if not data or not data["email"] or not data["password"]:
        return jsonify({"status": 420, "message": "One of the field is empty"}), 420
    user = User.query.filter_by(email=data["email"]).first()
    if not user:
        return jsonify({"status": 404, "message": "User do not exist"}), 404
    if check_password_hash(user.get_password, data["password"]):
        token = jwt.encode({"exp": (dt.datetime.utcnow() + dt.timedelta(minutes=15)), "email": user.get_email},
                           app.config['SECRET_KEY'], algorithm="HS256")
        return flask.jsonify({"email": user.email, "token": token})
    return jsonify({"status": 400, "message": "Invalid password"}), 400


@app.route('/orders', methods=['PUT'])
def update_request2():
    data = flask.request.get_json()
    try:
        to_buy = Order.query.filter_by(model=data["model"]).all()
        to_sell = Car.query.filter_by(model=data["model"]).all()
        if len(to_buy) == 0:
            return jsonify({"status": 404, "message": "model do not exist!"}), 404
        elif to_buy[0].amount == 0:
            return jsonify({"status": 400, "message": "Lack of models!"}), 400
        elif data["amount"] > str(to_buy[0].amount):
            return jsonify({"status": 404, "message": "bigger amount!"}), 404
        to_buy[0].amount -= int(data["amount"])
        db.session.commit()
        return jsonify({"status": 200, "message": "You bought a new car", "Your Car": to_sell[0].to_file()}), 200
    except IndexError:
        return jsonify({"status": 404, "message": "model do not exist!"}), 404



@app.route('/orders/', methods=['GET'])
def get_all_with_sort_and_search2():
    cars = Order.query.all()
    all_requests = Order.query
    count = all_requests.count()
    print(cars)
    if len(cars) > 0:
        if 'sort_by' in request.args and 'sort_type' in request.args:
            fields = cars[0].__dict__
            field = request.args['sort_by']
            if field in fields:
                cars.sort(key=lambda car_: getattr(car_, field))
                if request.args['sort_type'] == "desc":
                    cars.reverse()
        if 's' in request.args:
            find_part = request.args['s']
            found = []
            for car_ in cars:
                if car_.elem_search(find_part):
                    found.append(car_.to_file())
                    count = len(found)
            to_return = found
        else:
            res3 = []
            for i in range(len(cars)):
                res3.append(cars[i].to_file())
            to_return = res3
        if 'limit' in request.args:
            if 'offset' in request.args:
                to_return = control_limits(to_return, request.args['offset'], request.args['limit'])
            else:
                to_return = control_limits(to_return, 0, request.args['limit'])
        return jsonify(to_return, {"count": len(to_return)})

    else:
        return jsonify({"status": 404, "message": "order is not found"}), 404


@app.route('/orders/<given_id>', methods=['GET'])
def get_one_request2(given_id):
    cars = Order.query
    element = Order.query.get(given_id)
    if element not in cars:
        return jsonify({"status": 404, "message": "order is not found"}), 404
    return jsonify(element.to_file()), 200


@app.route('/orders', methods=['POST'])
@token_required
def add_request2(current_user):
    if not current_user.is_admin:
        return jsonify({'status': 403, "message": "You are not admin!"}), 403
    for elem in Order.query:
        if request.json["item_ID"] == elem.get_item_ID:
            return jsonify({'status': 404, "message": "order already exits"}), 404
    data = []
    for key in Order.get_attributes():
        data.append(request.json[key])
    try:
        input_value = Order(*data)
        print(input_value)
    except ValidationError as error:
        return jsonify({"status": 400, "message": str(error)}), 400
    db.session.add(input_value)
    db.session.commit()
    return jsonify({"status": 200, "message": "new order has been successfully added"})


if __name__ == "__main__":
    app.run(debug=True)
