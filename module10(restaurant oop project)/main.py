from menu import Pizza, Burger, Menu, Drinks
from restaurant import Restaurant
from users import *
from order import *

def main():
    print("Main function")
    menu = Menu()
    pizza_1 = Pizza('pizza_1 Pizza', 700, 'large', ['top1', 'top2', 'top3'])
    pizza_2 = Pizza('pizza_2 Pizza', 600, 'large', ['top4'])
    pizza_3 = Pizza('pizza_3 Pizza', 400, 'small', ['top5', 'top6'])

    menu.add_menu_item('pizza', pizza_1)
    menu.add_menu_item('pizza', pizza_3)
    menu.add_menu_item('pizza', pizza_2)

    burger1 = Burger('Naga Burger', 400, 'chikcen', ['bread', 'chilli'])
    burger2 = Burger('Naga2 Burger', 300, 'chikcen2', ['bread2', 'chilli2'])
    burger3 = Burger('Naga3 Burger', 900, 'chikcen3', ['bread3', 'chilli3'])

    menu.add_menu_item('burger', burger1)
    menu.add_menu_item('burger', burger2)
    menu.add_menu_item('burger', burger3)

    drink1 = Drinks('coke', 90, True)
    drink2 = Drinks('coke1', 90, False)
    drink3 = Drinks('coke3', 90, True)

    menu.add_menu_item('drinks', drink1)
    menu.add_menu_item('drinks', drink2)
    menu.add_menu_item('drinks', drink3)

    # ===================show menu==========================
    menu.show_menu()

    restaurant = Restaurant('SAI BABA', 2000, menu)

    manager = Manager('mr. xyz', '03781', 'wwjkj@gmail.com', 'somewhere', 15000, '4 12, 2011', 'manager')
    restaurant.add_employee('manager', manager)

    chef = Chef('Mr. xyz', '009183834', 'sss@gmail.com', 'auweru', 800, '12, 4, 2005', 'Chef', '222')
    restaurant.add_employee('chef', chef)

    server = Server('server', 89920101, 'qwjee@gmail.com', 'mars', 2200, '20198', 'server')
    restaurant.add_employee('server', server)

    # ==================show employee===============
    restaurant.show_employee()

    # customer1 placing order
    customer1 = Customer('sakib', 382109, '@gmail.com', 'iueroqwi', 100000)
    order1 = Order(customer1, [pizza_1, pizza_3, burger2, burger1])
    customer1.place_order(order1)
    restaurant.add_order(order1)
    restaurant.receive_payment(order1, 120000, customer1)
    print('revenue and balance: ', restaurant.revenue, restaurant.balance)

    # customer2 placing order
    customer2 = Customer('Rakib', 382109, '@gmail.com', 'iueroqwi', 100000)
    order2 = Order(customer2, [pizza_3, drink1, pizza_1, burger2])
    customer2.place_order(order2)
    restaurant.add_order(order2)
    restaurant.receive_payment(order2, 120000, customer2)
    print('revenue and balance: ', restaurant.revenue, restaurant.balance)

    # pay rent
    restaurant.pay_expense(restaurant.rent, '1 month rent')
    print('revenue and balance: ', restaurant.revenue, restaurant.balance)

    # pay salary
    restaurant.pay_salary(chef)
    print('revenue and balance: ', restaurant.revenue, restaurant.balance)


# call the main method
if __name__ == '__main__':
    main()
