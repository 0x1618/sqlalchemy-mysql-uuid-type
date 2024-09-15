from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'
          ] = 'mysql://root:password@localhost/sqlalchemy-mysql-uuid-type'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app=app)

from uuid import uuid4

from mysql_uuid_column import UUIDColumn


class Item(db.Model):
    __tablename__ = 'items'

    uuid = db.Column(UUIDColumn(), primary_key=True)
    name = db.Column(db.String(64), nullable=False)


with app.app_context():
    db.create_all()


@app.route('/create-item')
def create_item_route():
    item_name = request.args.get('name')

    if not item_name:
        return 'Add name query parameter to url.', 400

    item = Item(uuid=uuid4(), name=item_name)

    db.session.add(item)
    db.session.commit()

    item_data = {'uuid': item.uuid, 'name': item.name}

    return item_data, 201


if __name__ == "__main__":
    app.run(debug=True)
