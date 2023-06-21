from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from validation import *

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:MARIK2016@localhost/Collections_Cars'
db = SQLAlchemy(app)


class Car(db.Model):
    __tablename__ = "Cars"
    ID = db.Column(db.Integer, primary_key=True)
    brand = db.Column(db.String(50))
    model = db.Column(db.String(30))
    registration_number = db.Column(db.String(8))
    last_repaired_at = db.Column(db.String(15))
    bought_at = db.Column(db.String(15))
    car_mileage = db.Column(db.Integer)

    def __init__(self, ID=0, brand='b', model='b', registration_number='BC1111KA', last_repaired_at='2022-10-10',
                 bought_at='2021-10-10', car_mileage=2):
        self.set_ID(ID)
        self.set_brand(brand)
        self.set_model(model)
        self.set_registration_number(registration_number)
        self.set_last_repaired_at(last_repaired_at)
        self.set_bought_at(bought_at)
        self.set_car_mileage(car_mileage)

    def to_file(self):
        return {
            "ID": str(self.get_ID),
            "brand": str(self.get_brand),
            "model": str(self.get_model),
            "registration_number": str(self.get_registration_number),
            "last_repaired_at": self.get_last_repaired_at,
            "bought_at": self.get_bought_at,
            "car_mileage": str(self.get_car_mileage)
        }

    def search(self, value):
        for element in self.__dict__.values():
            if value in str(element):
                return True
        return False

    def __str__(self):
        return f"{self.ID}, {self.brand}, {self.model}, {self.registration_number}, " + \
               f"{self.last_repaired_at}, {self.bought_at}, {self.car_mileage}"

    @check_if_numeric
    def set_ID(self, ID):
        self.ID = ID

    @check_brand
    def set_brand(self, brand):
        self.brand = brand

    @check_model
    def set_model(self, model):
        self.model = model

    @check_registration_number
    def set_registration_number(self, registration_number):
        self.registration_number = registration_number

    @validation_date
    def set_last_repaired_at(self, last_repaired_at):
        self.last_repaired_at = last_repaired_at

    @validation_date_after
    @validation_date
    def set_bought_at(self, bought_at):
        self.bought_at = bought_at

    @check_if_numeric
    def set_car_mileage(self, car_mileage):
        self.car_mileage = car_mileage

    @property
    def get_ID(self):
        return self.ID

    @property
    def get_brand(self):
        return self.brand

    @property
    def get_model(self):
        return self.model

    @property
    def get_registration_number(self):
        return self.registration_number

    @property
    def get_last_repaired_at(self):
        return self.last_repaired_at

    @property
    def get_bought_at(self):
        return self.bought_at

    @property
    def get_car_mileage(self):
        return self.car_mileage

    @staticmethod
    def get_attributes():
        attributes = []
        for attr, values in vars(Car).items():
            if not attr.startswith("_") and not attr.startswith("set") and not attr.startswith(
                    "get") and not attr.startswith("elem") and not attr.startswith("__") and not attr.startswith("to"):
                attributes.append(attr)
        return attributes


@app.route('/test', methods=['GET'])
def test():
    return {
        'test': 'test1'
    }


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
                if car_.search(find_part):
                    found.append(car_.to_file())
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
        return jsonify(to_return, {"count": count})

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
def add_request():
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
def update_request(given_id):
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
def delete_request(given_id):
    elements = Car.query
    car_to_delete = Car.query.get(given_id)
    if car_to_delete not in elements:
        return jsonify({"status": 404, "message": "car is not found"}), 404
    else:
        db.session.delete(car_to_delete)
        db.session.commit()
        return jsonify({"status": 200, "message": "car has been successfully deleted"})


if __name__ == "__main__":
    app.run(debug=True)