from sqlalchemy import inspect

from database import Client, Product, Order, OrderItem, Delivery, Sale, Report
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

from config import app, database


class ClientView(ModelView):
    column_list = [c_attr.key for c_attr in inspect(Client).mapper.column_attrs]


def config():
    admin = Admin(app, name="'ООО' Астрохим", template_mode="bootstrap4")
    admin.add_view(ClientView(Client, database.session, "Клиенты"))
    admin.add_view(ModelView(Product, database.session, "Товары"))
    admin.add_view(ModelView(Order, database.session, "Заказы"))
    admin.add_view(ModelView(OrderItem, database.session, "Состав заказа"))
    admin.add_view(ModelView(Delivery, database.session, "Поставки"))
    admin.add_view(ModelView(Sale, database.session, "Продажи"))
    admin.add_view(ModelView(Report, database.session, "Отчеты"))
