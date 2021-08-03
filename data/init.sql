CREATE DATABASE IF NOT EXISTS store;

CREATE TABLE IF NOT EXISTS store.products (
product_id int NOT NULL AUTO_INCREMENT,
product_name varchar(22) NOT NULL,
product_price float NOT NULL,
PRIMARY KEY (product_id)
);

CREATE TABLE IF NOT EXISTS store.couriers (
courier_id int NOT NULL AUTO_INCREMENT,
courier_name varchar(22) NOT NULL,
courier_phone varchar(11) NOT NULL,
PRIMARY KEY (courier_id)
);

CREATE TABLE IF NOT EXISTS store.orders (
order_id int NOT NULL AUTO_INCREMENT,
customer_name varchar(22) NOT NULL,
customer_surname varchar(22) NOT NULL,
customer_address varchar(100) NOT NULL,
courier_id int NOT NULL,
order_status varchar(10),
PRIMARY KEY (order_id),
FOREIGN KEY (courier_id) REFERENCES couriers (courier_id)
);