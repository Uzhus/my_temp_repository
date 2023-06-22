from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import relationship

from config import database


class Client(database.Model):
    __tablename__ = "clients"
    client_id = Column(Integer, primary_key=True)
    client_name = Column(String(255))
    contact_person = Column(String(255))
    contact_email = Column(String(255))
    contact_phone = Column(String(255))
    address = Column(String(255))
    orders = relationship("Order", backref="client")


class Product(database.Model):
    __tablename__ = "products"
    product_id = Column(Integer, primary_key=True)
    product_name = Column(String(255))
    category = Column(String(255))
    description = Column(String(255))
    price = Column(Integer)
    stock_quantity = Column(Integer)
    order_items = relationship("OrderItem", backref="product")
    sales = relationship("Sale", backref="product")
    deliveries = relationship("Delivery", backref="product")


class Order(database.Model):
    __tablename__ = "orders"
    order_id = Column(Integer, primary_key=True)
    client_id = Column(Integer, ForeignKey("clients.client_id"))
    order_date = Column(String(255))
    total_amount = Column(Integer)
    order_items = relationship("OrderItem", backref="order")
    sales = relationship("Sale", backref="order")


class OrderItem(database.Model):
    __tablename__ = "order_items"
    order_id = Column(Integer, ForeignKey("orders.order_id"), primary_key=True)
    product_id = Column(Integer, ForeignKey("products.product_id"), primary_key=True)
    quantity = Column(Integer)


class Delivery(database.Model):
    __tablename__ = "deliveries"
    delivery_id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey("products.product_id"))
    delivery_date = Column(String(255))
    supplier = Column(String(255))
    quantity = Column(Integer)


class Sale(database.Model):
    __tablename__ = "sales"
    sale_id = Column(Integer, primary_key=True)
    order_id = Column(Integer, ForeignKey("orders.order_id"))
    sale_date = Column(String(255))
    product_id = Column(Integer, ForeignKey("products.product_id"))
    quantity = Column(Integer)
    total_amount = Column(Integer)


class Report(database.Model):
    __tablename__ = "reports"
    report_id = Column(Integer, primary_key=True)
    report_date = Column(String(255))
    report_content = Column(String(255))


def save(obj):
    try:
        database.session.add(obj)
        database.session.commit()
    except SQLAlchemyError as e:
        print(e)
        database.session.rollback()


def delete_all(obj_clas):
    database.session.query(obj_clas).delete()
    database.session.commit()


def delete(obj):
    database.session.delete(obj)
    database.session.commit()


def get_all(obj_class):
    return database.session.query(obj_class).all()


def find_by_id(obj_class, obj_id):
    return database.session.query(obj_class).filter(obj_class.id == obj_id).first()
