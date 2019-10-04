DROP TABLE IF EXISTS user_info;
DROP TABLE IF EXISTS company;
DROP TABLE IF EXISTS stock_price;
DROP TABLE IF EXISTS assets;

CREATE TABLE user_info (
	user_ID INT PRIMARY KEY NOT NULL,
	username TEXT NOT NULL,
	password TEXT NOT NULL,
	difficulty INT NOT NULL,
	day_of_progress INT NOT NULL
);


CREATE TABLE company (
	company_ID INT PRIMARY KEY NOT NULL,
	company_name TEXT NOT NULL
);


CREATE TABLE stock_price (
	dayNo INT NOT NULL,
	company_ID INT,
	price INT NOT NULL,
	FOREIGN KEY (company_ID) REFERENCES company(company_ID),
	PRIMARY KEY (company_ID, dayNo)

);

CREATE TABLE assets (
	user_ID INT,
	company_ID INT,
	amount INT,
	FOREIGN KEY (company_ID) REFERENCES company(company_ID),
	FOREIGN KEY (user_ID) REFERENCES user_info(user_ID),
	PRIMARY KEY (company_ID, user_ID)

);