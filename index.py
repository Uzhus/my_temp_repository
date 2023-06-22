from flask import render_template

import admin
from config import app, database
from database import Client, Product, Order, OrderItem, Delivery, Sale, Report, get_all


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


@app.get("/logout")
def logout():
    return show_login_form()


@app.get("/login")
def show_login_form(message=None):
    return render_template("login.html", house_list=get_all(House), message=message, roles=Role.get_roles())


def test_data():
    # Создание объектов клиентов
    client1 = Client(client_name="АвтоДилер1", contact_person="Иванов Иван", contact_email="ivanov@example.com",
                     contact_phone="123456789", address="Москва")
    client2 = Client(client_name="АвтоДилер2", contact_person="Петров Петр", contact_email="petrov@example.com",
                     contact_phone="987654321", address="Санкт-Петербург")
    client3 = Client(client_name="АвтоДилер3", contact_person="Сидоров Сидор", contact_email="sidorov@example.com",
                     contact_phone="567891234", address="Екатеринбург")

    # Создание объектов товаров
    product1 = Product(product_name="Моторное масло", category="Химия", description="Синтетическое моторное масло",
                       price=1000, stock_quantity=50)
    product2 = Product(product_name="Автомобильные шины", category="Шины", description="Летние автомобильные шины",
                       price=2000, stock_quantity=100)
    product3 = Product(product_name="Антифриз", category="Химия", description="Готовый к использованию антифриз",
                       price=500, stock_quantity=30)

    # Создание объектов заказов
    order1 = Order(client=client1, order_date="2023-06-01", total_amount=3000)
    order2 = Order(client=client2, order_date="2023-06-02", total_amount=4000)
    order3 = Order(client=client3, order_date="2023-06-03", total_amount=1500)

    # Создание объектов состава заказов
    order_item1 = OrderItem(order=order1, product=product1, quantity=2)
    order_item2 = OrderItem(order=order2, product=product2, quantity=3)
    order_item3 = OrderItem(order=order3, product=product3, quantity=1)

    # Создание объектов поставок
    delivery1 = Delivery(product=product1, delivery_date="2023-06-04", supplier="Поставщик1", quantity=10)
    delivery2 = Delivery(product=product2, delivery_date="2023-06-05", supplier="Поставщик2", quantity=20)
    delivery3 = Delivery(product=product3, delivery_date="2023-06-06", supplier="Поставщик3", quantity=5)

    # Создание объектов продаж
    sale1 = Sale(order=order1, sale_date="2023-06-05", product=product1, quantity=2, total_amount=2000)
    sale2 = Sale(order=order2, sale_date="2023-06-06", product=product2, quantity=1, total_amount=2000)
    sale3 = Sale(order=order3, sale_date="2023-06-07", product=product3, quantity=1, total_amount=500)

    # Создание объектов отчетов
    report1 = Report(report_date="2023-06-10", report_content="Отчет 1")
    report2 = Report(report_date="2023-06-11", report_content="Отчет 2")
    report3 = Report(report_date="2023-06-12", report_content="Отчет 3")

    # Сохранение объектов в базе данных
    database.session.add_all(
        [client1, client2, client3, product1, product2, product3, order1, order2, order3, order_item1, order_item2,
         order_item3, delivery1, delivery2, delivery3, sale1, sale2, sale3, report1, report2, report3])
    database.session.commit()


if __name__ == "__main__":
    app.app_context().push()
    database.create_all()
    # test_data()
    admin.config()
    app.run()
