SQL CLASS

What is Data:
It is the Collection of raw facts or observations

dal      120
sugar    50
salt     30


What is Information
It is the Collection of Processed data

Maths 90
Science 75
Social 60

Total 225/300

What is Data Base?
It is a Container  which is stores the organized data electronic device is called as data base

Types of Data
1.Structed Data
2.Un Structed Data
3.Semi-Structed Data

What is Structed Data?
Structed data is northing but the data is in the form of rows and columns or in the form of tables

What is Un Structed Data?
The data is in the form of Audios, Videos, Images, Text is called as Un Structed data.

What is semi-Structed Data?
The Data can handle both Structed and unstructed data
Ex:JSON,HTML


What is Organizing?
The data which stores in an organized or in a planned way is called as Organizing

What is DBMS:
Data Base Management System: It is a software is used manage the database, create table to the database , insert data in to the table, update the data , delete the data and retrieve the data.

What is Software?
The Program which follows a set of instructions to do a specific task is called as software

Type of DBMS:
1.Hierirical DBMS
2.Networking DBMS
3.Relational DBMS
4.Non Relational DBMS

What is RDBMS?
The data which stores in a structed way and establishes the relations between the tables.
EX: MYSQL, SQLLITE, POSTGRE SQL, ORACLE.

What is NRDBMS:
The database which stores in the unstructed and semi structed data in it is called Non Relational DBMS
EX: Cassandra, NOSQL and MongoDB.

What is MYSQL?
It is a software tool to manage the Relational database management System.

What is SQL?
It is a Programming language which handles


__________________________________________________________________18/07/2026 Day2____________________________________________________________


MySQL:

It is a software deals with rdbms with sql.

DataTypes:
We are using 3 types of Data types in MySQL
1.Numeric
2.String
3.Date and Time

Numeric Data Type:
It is used to store the numeric values in it. we are using 5 types of numeric Data types

1.TINYINT : Signed value -128 to 127  Unsigned value 0 to 255
ex: Age and Semesters

Smallint : It stores the value in between -32768 to +32767 usingned value is 65535
ex: Marks

Mediumint: It is store the value in between -8.3million to +8.3million byte size is 3 bytes.
Ex: population in a city or town

Int: We can store upto -2.1 billion to +2.1 billion unsigned value is 0 to 4.2 billion byte size is 4

int
population in a city or town +2.1 billions unsigned value is 0 to 4.2 billion byte size is 4
ex : prodectid, employeeid

bigint: we can store upto -9.2 quintillion to +9.2 unsigned values is o to 18.4 quintillion byte size 8

Float: we can used to store the decimal approximate values in 0 to 7
ex: temperature, scientific calculations.

Double: approximate range upto 15-16
ex: engineering calculations

Decimal: we can store the values using precision and scale decimal(p,s)
ex:salary

Sring datatypes
it is a group or combination of characters is called as strings

1.Char()

char(10)\
'chandu'
'chandu___
it is fixed length faster then varchar
ex: phone number , adhaar number,pancard number
it is stored in the from of

varchar()
varchar(120)
'uma'
o/p:'uma'
it stores only variables length memory efficient
ex. names, gmails.

3.Text(): it used to store the paragraphs.
ex. summaries , feed backs , gossips.
 
4. Data & Time : it is used to store the date in the from of data and time.

1. Data :it is used to store only date.
ex:date of birth and joining time

2.time: it is used to store both date and time . ex Train bookings, and all other bookings


3. time stamp: it is used to store the time with milliseconds
ex: running race, login, and logouts


__________________________________________________________________20/07/2026_____________________________________________________________________
DAY-3 COMMANDS:

1.DDL Data Definition Language: It is the define the structed of database
          It is used to define or create , update , rename , and delete the database or tables is called as DDl.
Types of DDl:
Create:To create the databases and tables,

   Syntax: create database databasename;   #for creating database
           Create table tablename;         # for table creation

Alter: It is used to add, update , rename, and delete the column in table.
   Syntax:
        add a column:
          1. alter table tablename add column columnname datatype;

        modify a column in data type:
          2. alter table tablename modify column columnname datatype;

        rename:
          3.alter table tablname rename column columanname to columnname1;

        drop:
          4. alter table tablename drop column columanname;

       Truncate; The Structre is constant but the data should be deleted;
          Syntax:
              truncate table tablename



________________________________________________________________________________22/07/2026_________________________________________________________________

2.DML Data Manipulation language : It is a used to modify the data
    Types in DML are Insert, Update and Delete

	1.Insert: It is insert the values to the table.
	Syntax: Insert into tablename values(Column values);

	2.Update: To update the data
        Syntax: Update  table tablename  set column = value    NOTE SET SQL_SAFE_UPDATES=0;
	"Apply condation" :update tablename set columnname =value  where column=value
	We use where clause for to change the value in that particular row with primary key column value.
	
	3.Delete: TO delete
	Syntax: Delete from tablename
	



3.DQL

4.DCL

5.DDL









 