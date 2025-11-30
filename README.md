# Sweet Shop Billing System (Python + MySQL)

A simple Shop Management and Billing System built using Python and MySQL. This project allows users to select products, calculate total price, 
choose payment methods, and store orders in a database.

## Features

* Menu display for sweet shop products
* Quantity input with validation
* Price calculation
* Order cancel or confirm option
* Payment method selection (Cash, Card, UPI)
* Stores order details in MySQL database
* Uses Python OOP concepts

## Folder Structure

```
project-folder/
│
├── main.py
├── README.md
└── requirements.txt
```

## Technologies Used

* Python 3
* MySQL
* mysql-connector-python
* Object-Oriented Programming

## Database Table

The project automatically creates an `orders` table with the following columns:

| Column         | Type                |
| -------------- | ------------------- |
| id             | INT, Auto Increment |
| product_name   | VARCHAR(255)        |
| quantity       | INT                 |
| price_per_item | FLOAT               |
| total_price    | FLOAT               |
| payment_method | VARCHAR(50)         |

## How to Run

### Install dependencies

```
pip install mysql-connector-python
```

### Update database credentials

Inside the script:

```
host="localhost"
user="root"
password="yourpassword"
database="shop_management"
```

### Run the script

```
python main.py
```

## Contributions

Contributions and suggestions are welcome.

## License

This project is open-source and free to use.
