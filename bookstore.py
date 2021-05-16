import unittest
import requests
import re
import getpass
import os
import selenium
from selenium import webdriver
from selenium.webdriver.support.select import Select
from time import sleep


basket_items = [ 'Harry Potter', '21 lessons for 21st Century', 'Crime and Punishment', 'Python for Data Analysis' ]
basket_author = ['J.K.Rowling', 'Yuval Noah Harari', 'Fiodor Dostojewski', 'Wes McKinney' ]
basket_ilosc = [2, 1, 1, 1]
basket_price_item = [30, 40, 30, 40]
price_dictionary = {'Harry Potter': 30, '21 lessons for 21st Century': 40, 'Crime and Punishment': 30, 'Python for Data Analysis': 40}

#Print table with products
print("Welcome to our bookstore!\nCheck our best deals:")
szer = 60
print("-" * szer)
print("| Price($)|     Author       |        Title             |")
print("*" * szer)
print("| {:7.2f} | {:18s} | {:27s} |" .format(basket_price_item[0], basket_author[0], basket_items[0]))
print("| {:7.2f} | {:18s} | {:27s} |" .format(basket_price_item[1], basket_author[1], basket_items[1]))
print("| {:7.2f} | {:18s} | {:27s} |" .format(basket_price_item[2], basket_author[2], basket_items[2]))
print("| {:7.2f} | {:18s} | {:27s} |" .format(basket_price_item[3], basket_author[3], basket_items[3]))
print("-" * szer)

#Book choice
print("Which book would you like to add to your basket?")
input_title = input("Please write the title ")
if input_title in basket_items:
    print("How many copies of {0} would you like to add to your basket?" .format(input_title))
    input_quantity = int(input("Please write the quantity "))
    print("You’ve added {0} copy/copies of {1} to your basket!" .format(input_quantity, input_title))
else:
    print("Such book is not available. You will be redirected to another bookstore.")

    driver = webdriver.Firefox()
    driver.get("http://www.empik.com")

    search_input = driver.find_element_by_xpath('//*[@id="bq"]')
    search_input.send_keys(input_title)
    close_button = driver.find_element_by_xpath('/html/body/main/footer/div[5]/div[2]/div[1]/button')
    close_button.click()
    search_category = driver.find_element_by_xpath('//*[@id="searchSet"]/div[2]/button')
    search_category.click()
    search_category_book = driver.find_element_by_xpath('//*[@id="searchSet"]/div[2]/div/label[14]')
    search_category_book.click()
    search_btn = driver.find_element_by_xpath('//*[@id="searchSet"]/button')
    search_btn.click()
    driver.implicitly_wait(60)
    first_product = driver.find_element_by_class_name('ta-product-title')
    print("You chose a book called: ")
    print(first_product.get_attribute("innerText"))
    driver.quit()

    #Assertion
    class TestIfinStore(unittest.TestCase):
        def test_in_store(self):
            self.assertIn(input_title, first_product, msg="Correct search result")
    if __name__ == '__main__':
        unittest.main()
    exit()

print("Would you like to add another book to your basket?")


customer_input = input("yes or no? ")
if customer_input == "no":
    print("Thank you for shopping with us!")
    if input_title in price_dictionary:
        print("Total price for {} copy/copies of {} is".format(input_quantity, input_title), price_dictionary[input_title] * input_quantity)

elif customer_input == "yes":
    print("Please write the title of book you would like to buy ")
    input_title_two = input()
    print("How many copies of {0} would you like to add to your basket?" .format(input_title_two))
    input_quantity_two = int(input("Please write the quantity "))
    print("You’ve added {0} copy/copies of {1} to your basket!" .format(input_quantity_two, input_title_two))
    if input_title_two in price_dictionary:
        success_msg = print("Total price for {} copy/copies of {} is".format(input_quantity_two, input_title_two), price_dictionary[input_title_two] * input_quantity_two)
    if input_title in price_dictionary:
        success_msg2 = print("Total price for {} copy/copies of {} is".format(input_quantity, input_title), price_dictionary[input_title] * input_quantity)

    #test adding book to basket
    class TestAddBook(unittest.TestCase):
        def test_add_book_success(self):
            self.assertIn(input_title, success_msg2)

    #test book not in bookstore
    class TestAddWrongBook(unittest.TestCase):
        def test_add_book_success(self):
            self.assertIn(input_title, basket_items, msg="Book in store!")

    #test title is not None
    class TestTitle(unittest.TestCase):
        def test_title_not_none(self):
            assert input_title is not None

    #test quantity
    class TestQuantity(unittest.TestCase):
        def test_quantity_success(self):
            self.assertGreaterEqual(input_quantity, 1)

#Registration - API call
print("Please create an account to purchase.")
input_email = input("Please input email ")
input_password = getpass.getpass('Please input password')

score = 0
while True:
    if (len(input_password)<8):
        score = -1
        break
    elif not re.search("[a-z]", input_password):
        score = -1
        break
    elif not re.search("[A-Z]", input_password):
        score = -1
        break
    elif not re.search("[0-9]", input_password):
        score = -1
        break
    elif not re.search("[_@$]", input_password):
        score = -1
        break
    else:
        score = 0
        print("Password approved")
        break

param_email = {"email": input_email}
param_pass = {"password": input_password}
response = requests.post("https://reqres.in/api/users/2", param_email, param_pass)
print(response)
assert response.status_code == 201


if score ==-1:
    print("Your password is too weak")
    input_password = getpass.getpass('Please input password')

print("You signed up successfully. Now you'll have to sign in. ")

input_name = input("What's your name?")

    #Login - API call
input_email_signin = input("Please input email ")
input_password_signin = getpass.getpass('Please input password')


param_email_signin = {"email": input_email_signin}
param_pass_signin = {"password": input_password_signin}
response = requests.post("https://reqres.in/api/login", param_email_signin, param_pass_signin)
print(response)
    #assert response.status_code == 421

    #test if sign up and sign in match
class TestCredentials(unittest.TestCase):
    def test_credentials(self):
        self.assertEqual(input_email, input_email_signin)
        self.assertEqual(input_password, input_password_signin)

    #test if email contains @
class TestEmailFormat(unittest.TestCase):
    def test_email_format(self):
        self.assertIn("@", input_email)

    #checkout
print("{0} redeem your gift card" .format(input_name))
valid_gift_cards = ['bookdiscount1', 'booksdiscount2', 'bookdiscount3', 'bookdisocunt4']
gift_card = input("Please input your gift card ")

if gift_card in valid_gift_cards:
    print("Gift card added successfully!")
else:
    print("Such gift card does not exist")

    #test if gift card message displayed
class TestGiftCard(unittest.TestCase):
    def test_gift_card(self):
        self.assertIn(gift_card, valid_gift_cards)

if __name__ == '__main__':
    unittest.main()
