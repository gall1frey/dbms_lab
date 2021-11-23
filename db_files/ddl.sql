drop database hoteldb;
create database hoteldb;

\c hoteldb

create table HOTEL(
HOTEL_NAME varchar(30) NOT NULL,
HOTEL_PNUMBER numeric(10,0),
HOTEL_EMAIL varchar(50) NOT NULL,
HOTEL_ID numeric(10,0) NOT NULL UNIQUE,
PRIMARY KEY(HOTEL_ID)
);

create table CUSTOMER(
C_ID numeric(10,0) NOT NULL UNIQUE,
C_FNAME varchar(30) NOT NULL,
C_LNAME varchar(30) NOT NULL,
C_PHNO numeric(10,0) NOT NULL,
C_EMAIL varchar(50) NOT NULL,
C_DOB date NOT NULL,
C_NUM_PEOPLE numeric(10,0),
C_ROOM numeric(10,0),
C_CHECKED_IN boolean NOT NULL DEFAULT TRUE,
PRIMARY KEY(C_ID)
);

create table EMPLOYEE(
E_ID numeric(10,0) NOT NULL UNIQUE,
E_FNAME varchar(30) NOT NULL,
E_LNAME varchar(30) NOT NULL,
E_PHNO numeric(10,0) NOT NULL,
E_DOB date NOT NULL,
E_SALARY numeric(10,0) NOT NULL,
E_ACC_NUM numeric(10,0) NOT NULL,
E_DEPT_ID numeric(10,0) NOT NULL,
E_MGR_ID numeric(10,0) NOT NULL,
PRIMARY KEY(E_ID)
);

create table DEPARTMENT(
D_DESCRIPTION varchar(100),
D_NAME varchar(20) NOT NULL,
D_ID numeric(10,0) NOT NULL UNIQUE,
D_MANAGER_ID numeric(10,0) NOT NULL,
PRIMARY KEY(D_ID)
);

create table SERVICES(S_ID numeric(10,0) NOT NULL UNIQUE,
S_DESCRIPTION varchar(100),
S_CHARGES numeric(10,0) NOT NULL,
S_NAME varchar(30) NOT NULL,
DEPT_ID numeric(10,0) NOT NULL,
PRIMARY KEY(S_ID),
FOREIGN KEY (DEPT_ID) REFERENCES DEPARTMENT(D_ID)
);

create table ROOMS(
R_ID numeric(10,0) NOT NULL UNIQUE,
R_FLOORNO numeric(10,0) NOT NULL,
R_NOBEDS numeric(10,0) NOT NULL,
R_DESCRIPTION varchar(50),
R_CHARGES numeric(10,0),
PRIMARY KEY(R_ID)
);

create table BILL(
B_INFO varchar(100),
B_AMT numeric(10,0),
B_ID numeric(10,0) NOT NULL,
B_PAYMODE varchar(30),
B_DATE date NOT NULL,
CUST_ID numeric(10,0) NOT NULL,
PRIMARY KEY(B_ID),
FOREIGN KEY(CUST_ID) REFERENCES CUSTOMER(C_ID)
);

alter table EMPLOYEE add constraint FKEY_DNO FOREIGN KEY (E_DEPT_ID) REFERENCES DEPARTMENT(D_ID);
--alter table EMPLOYEE add constraint MGR_FKEY FOREIGN KEY (E_MGR_ID) REFERENCES EMPLOYEE(E_ID);
