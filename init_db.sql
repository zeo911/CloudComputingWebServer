CREATE TABLE admin (
    user_id VARCHAR(50) PRIMARY KEY,
    name VARCHAR(50),
    password VARCHAR(64),
    contact INT 
);

CREATE TABLE books (
    BOOK_ID VARCHAR(50) PRIMARY KEY,
    CATEGORY VARCHAR(100),
    NAME VARCHAR(64),
    AUTHOR VARCHAR(100),
    COPIES INT
);


CREATE TABLE staffs (
    STAFF_ID VARCHAR(10) PRIMARY KEY,
    name VARCHAR(50),
    password VARCHAR(30),
    contact INT
);

CREATE TABLE CUSTOMERS (
    CID VARCHAR(10) PRIMARY KEY,
    name VARCHAR(80)
);

CREATE TABLE customer_books (
    customer_id INT,
    book_id INT,
    PRIMARY KEY (customer_id, book_id),
    FOREIGN KEY (customer_id) REFERENCES customers(CID),
    FOREIGN KEY (book_id) REFERENCES books(BOOK_ID)
);
