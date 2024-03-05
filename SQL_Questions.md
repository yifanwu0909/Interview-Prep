# SQL Questions

- [Explain Normalization?](#explain-normalization)
- [DDL vs DML](#difference-between-ddl-and-dml)
- [ACID Properties](#acid-properties-in-sql)
- [Write a Query to Find all the Duplicates in a Table?](#write-a-query-to-find-all-the-duplicates-in-a-table)
- [Clustered vs non-clustered](#difference-between-a-clustered-and-non-clustered-index)
- [Denormalisation](#explain-denormalisation)
- [Collation](#what-is-collation)
- [inner, outer, and full outer join](#what-is-the-difference-between-inner-outer-and-full-outer-join)
- [Join vs Union?](#explain-the-difference-between-a-join-and-a-union)
- [UNION vs UNION ALL](#explain-the-difference-between-union-and-union-all)
- [Write a Query to Print the Highest Salary from a Table](#write-a-query-to-print-the-highest-salary-from-a-table)
- [Shared vs Inclusive Locks](#what-is-the-difference-between-shared-and-inclusive-locks)
- [Transpose Using SQL](#explain-the-mechanism-of-transpose-using-sql)
- [Working of the B-trees Index](#explain-the-working-of-the-b-trees-index)
- [Effect of Truncate and Delete on an Identity](#explain-the-effect-of-truncate-and-delete-on-an-identity)
- [Cost of Having a Database Index](#explain-the-cost-of-having-a-database-index)
- [Advantages of Having an Index](#what-are-the-advantages-of-having-an-index)
- [Indexing in the Database](#explain-indexing-in-the-database)
- [OLAP and OLTP](#what-is-olap-and-oltp)
- [In What Conditions Does CASE WHEN Apply](#in-what-conditions-does-case-when-apply)
- [Explain the Cases to Use HAVING versus WHERE](#explain-the-cases-to-use-having-versus-where)
- [PL/SQL](#what-is-plsql)
- [ETL in SQL](#what-is-etl-in-sql)
- [Nested Triggers](#what-are-nested-triggers)
- [Commits and Checkpoints](#what-are-commits-and-checkpoints)
- [What is the point of using a foreign key constraint?](#What-is-the-point-of-using-a-foreign-key-constraint)
- [What is the difference between MySQL and PostgreSQL? How about between PL/SQL and SQL?](#What-is-the-difference-between-Mysql-and-Postgresql-How-about-between-pl-sql-and-sql)
- [SQL View?](#What-is-an-sql-View)
- [DDL, DQL, DML, DCL](#DDL-DQL-DML-DCL)
- [What is SQL?](#what-is-sql)
- [Different flavors of SQL?](#what-are-the-different-flavors-of-sql)
- [Primary key](#what-is-a-primary-key)
- [Top RDBMS engines](#what-are-the-top-rdbms-engines)
- [RDBMS vs No-SQL database](#how-is-an-rdbms-different-from-a-no-sql-database)
- [Give examples of commands for each.](#give-examples-of-commands-for-each)
- [Common data types in SQL?](#what-are-the-common-data-types-in-sql)
- [Does an SQLite database support date time objects?](#does-an-sqlite-database-support-date-time-objects)
- [Attribute constraints](#what-are-attribute-constraints-and-explain-them)
- [inner join vs left outer join](#what-is-the-difference-between-inner-join-and-left-outer-join)
- [UNION vs UNION ALL](#what-is-the-difference-between-union-and-union-all)
- [When should one use a CTE over a subquery?](#when-should-one-use-a-cte-over-a-subquery)
- [window functions](#what-are-window-functions)
- [WHERE vs HAVING](#what-is-the-difference-between-where-and-having)
- [COALESCE function](#what-does-the-coalesce-function-do)

## Explain Normalization?
Normalization is a method of organization of the data in the database to minimize redundancy from a set of relations. The concept of Normal forms is used to perform normalization on a relation. 

1NF:- If a relationship has an atomic value it is in 1NF.  
2NF:- For a relation to be in 2NF, it should be in 1NF and all the non-key attributes are fully functionally dependent on the primary key.  
3NF:- For a relation to be in 3NF, it should be in 2NF and additionally no transition dependency exists.  
BCNF:- Boy Codd’s Normal form is a strong representation of 3NF.  

[Back to TOC](#SQL-Questions)


## Difference Between DDL and DML?
- DDL stands for Data Definition language whereas, DML is called Data Manipulation Language.
- DDL creates a schema with some constraints. DML adds, retrieves or updates the data in that schema. 
- DDL defines the column attribute of the table. DML provides the row attribute of the table.
- Examples of DDL commands are created, alter, drop, rename, etc. and those of DML are merged, update, insert, etc. 
- The WHERE clause is not used in DDL but is used in DML.

[Back to TOC](#SQL-Questions)


## ACID Properties in SQL?
- Atomicity - Changes in the data must be like a single operation. 
- Consistency - The data must be consistent before and after the transaction. 
- Isolation - Multiple transactions can be done without any hindrance. 
- Durability - Transaction gets successful in case of system failures.  
 
[Back to TOC](#SQL-Questions)


## Write a Query to Find all the Duplicates in a Table?
- Using the GROUP BY command to group all the rows by target columns. Here target columns are the ones where you can check the duplicates.
- Use the HAVING command and integrate the COUNT function to check if any group has more than one entry.

[Back to TOC](#SQL-Questions)


## Difference Between a Clustered and non-clustered Index?
- A clustered index is used to define the order to sort the index or table just like a dictionary. A non-clustered index collects all the data in one place and records it at a different place.
- The clustered index is faster than the non-clustered index.
- Less memory is used to perform operations on a clustered index as compared to a non-clustered index. 

[Back to TOC](#SQL-Questions)


## Explain Denormalisation?
The database optimization technique in which we add data(redundant)  to the table(s) is called denormalization. The technique is useful as it helps to reduce the costly joins in the database.

OLAP are databases intended for online analytical processing, while OLTP are databases intended for online transaction processing. Denormalize the data when it falls under OLAP operations and normalize when OLTP.

[Back to TOC](#SQL-Questions)


## What is Collation?
In a SQL server, collation provides sorting rules, accent, and case sensitivity properties to the data in the database. It represents each character in the database by defining the bit patterns using collation.

Some of the collation levels are as below:
- Case-sensitive (_CS)
- Accent-sensitive (_AS)
- Kana-sensitive (_KS)
- Width-sensitive (_WS)
- Variation-selector-sensitive (_VSS)a
- Binary (_BIN)
- Binary-code point (_BIN2)

[Back to TOC](#SQL-Questions)


## What is the Difference Between inner, outer, and full outer join?
- In an inner join, the rows that are common in both tables are the outputs. 
- In a full outer join, all the rows in both tables are returned.
- An outer join returns the values from either or both tables. 

[Back to TOC](#SQL-Questions)


## Explain the Difference Between a Join and a Union?
- Join retrieves the matched records from the tables whereas union is used to combine the set of two different SELECT statements.
- Join does not remove duplicate data whereas union removes duplicate data(rows) from selected statements.
  
[Back to TOC](#SQL-Questions)


## Explain the Difference Between UNION AND UNION ALL?
Union keeps unique records whereas Union keeps all records including all the duplicates. Also, the union does a deduplication step before returning the data and the union all prints concatenated results 

[Back to TOC](#SQL-Questions)


## Write a Query to Print the Highest Salary from a Table?
```
SELECT * FROM EMP WHERE salary=(select Max(salary) FROM EMP);
```

[Back to TOC](#SQL-Questions)


## What is the Difference Between Shared and Inclusive Locks?
- In the shared lock, the lock mode is only in read operation but in the inclusive lock, it is in reading and writes operation.
- A shared lock prevents others from updating the data whereas an inclusive lock prevents others from reading or updating the data.
- Any number of transactions can hold a shared lock on a particular item whereas, only one transaction can be held in an exclusive lock.

[Back to TOC](#SQL-Questions)


## Explain the Mechanism of Transpose Using SQL?
- Transpose in SQL is defined as changing a row or column into a particular format to visualize the data from a new perspective. 
- One basic transpose is changing a row to a column or a column to a row. Typical transpose methods are dynamic and joined transposition.
- All of the transpose methods are used for data analysis for a fruitful outcome. 

[Back to TOC](#SQL-Questions)


## Explain the Working of the B-trees Index?
A B-tree is defined as a self-balancing search tree in which all leaves are at the same level. To insert data in a B-tree, it is inserted at the leaf node. 

In the B-trees index, the tree has a key-value pair which is called a payload. This value is referenced to the actual data record.

When we use a B-tree index, the database searches a given key with correspondence to B-tree and gets the index. 

[Back to TOC](#SQL-Questions)


## Explain the Effect of Truncate and Delete on an Identity?
- The DELETE command is used to delete a specific row in the table whereas, TRUNCATE deletes all the data from the rows.
- DELETE is a DML command and slower than the TRUNCATE command which is a DDL command. 
- DELETE command active triggers whereas TRUNCATE does not.  

[Back to TOC](#SQL-Questions)


## Explain the Cost of Having a Database Index?
It eats up your space. The larger your table, the larger will be the index. 

ADD, DELETE or UPDATE of certain rows in the table must be also done to our index.

As a thumb rule, an index must be created on a table if the table in the indexed column will be required frequently.

[Back to TOC](#SQL-Questions)


## What are the Advantages of Having an Index?
- It speeds up the SELECT query.
- Data retrieval becomes quite easy.
- Indexes can be used for sorting.
- It makes a row unique without any duplicates.
- Large string text can be inserted when the index is set to fill-text index.

[Back to TOC](#SQL-Questions)


## Explain Indexing in the Database?
Indexing is a data structure technique to optimize the database performance by reducing disk access during the time a query is being processed.  

Indexing has the following attributes:

- Access Types: Based on the search type
- Access Time: Based on search time
- Insertion Time: Based on quick insertion
- Deletion Time: Based on quick deletion
- Space Overhead: Based on additional overhead space.

[Back to TOC](#SQL-Questions)


## What is OLAP and OLTP?
### Online Analytical Processing (OLAP)
Businesses have to comprehend a set of data that helps finance leaders and business teams to get insights into their users and the performance of multiple related factors.

A business can have various data across the business process and strategies that help teams to analyze the performance at a more granular level.

These data are stored in multiple database systems and thus require consistent, real-time, and more flexible processes that help the team analyze the data and process further for more analysis.

Online Analytical Processing or OLAP contains software tools that are used for analyzing business data and help get insights into the database.

For example, OLAP can be used to build the Spotify song recommendation engine that automatically generates a playlist for users based on their song choices and historical listening data.

### Online Transaction Processing(OLTP)
The transaction is an integral part of every business. A business offering services to its customers receive an amount when the customer uses the services.

An invoice gets immediately generated when users pay for the services of their choice.

The transaction database comes into the picture when we have to store the transaction information of all users.

However, Online Transaction Processing (OLTP) offers transaction-oriented applications that are categorized in a 3-tier architecture.
 
OLTP helps businesses to perform certain activities related to the transaction database.

For example, Transaction through online banking serves the same purpose where OLTP can be used to operate the user transaction information.

[Back to TOC](#SQL-Questions)


## In What Conditions Does CASE WHEN Apply?
SQL is used for querying databases and modifying the values in large datasets. It also provides a way to manipulate data when there are multiple cases. 

For example, a table contains a list of employees(name) along with experience (EXP) and joining date(ac_date). 

Now, if we want to query the data in such a way that if the experience is greater than(>) “4”, then insert “Is a senior” in a new column named “exp_level”, otherwise insert NULL in the column.

You can query the database in such cases using the CASE WHEN statement.

The CASE WHEN statement is similar to the If/else condition in programming languages like C, C++, Python, etc.

The CASE statement is followed by one pair of WHEN and THEN statements. However, you can add nested statements based on your requirements.

Once the CASE statement is completed, it is finished by adding the ending statement that starts with ELSE and END AS.

In the example above, we have employee.database that lists out the employees of a company with attributes such as employee name, joining year, experience, and more. Using the CASE WHEN statement in this example, 

```
SELECT employee_name,
       exp,
       CASE WHEN exp > 4 THEN 'Is a Senior'
            ELSE NULL END AS exp_level
  FROM xyz.marketing_employees
```

[Back to TOC](#SQL-Questions)


## Explain the Cases to Use HAVING versus WHERE?

### HAVING Clause in SQL
SQL offers HAVING clauses to filter a group of data in a database.

For example, company XYZ has a list of employees who have more than 1 year of experience.

The database contains rows and columns including the employee name, joining data, experience, and experience level.

You can retrieve a list of employees who have more than 5 years of experience.

The HAVING clause provides you with a way to control the information and modify the data with a bunch of data.

The syntax of the HAVING clause is the HAVING condition.

In the example, we can retrieve the list of employees having more than 5 years of experience by querying the database as below:

```
SELECT employee_name, exp_level,
FROM EMPLOYEE
GROUP BY experience
HAVING COUNT(experience) > 5;
```

### WHERE Clause in SQL
 
WHERE clause is used when you want to filter the records based on a particular condition.

For example, in an employee table, we can retrieve the list of all employees who have exactly 5 years of experience in a company. The syntax of the WHERE clause is, WHERE condition.

In the example, we can extract the name of employees who have 5 years of experience by querying the database as below:
```
SELECT employee_name, exp_level,
FROM EMPLOYEE
WHERE experience=  5;
```

[Back to TOC](#SQL-Questions)


## What is PL/SQL?
The PL/SQL is a block-structured language that encourages developers to use the power of SQL using procedural statements.

It is a featured procedural language that has embedded the power of decision-making and many more features of POP.

Using a single block command, PL/SQL can run multiple queries with the support of extensive error checking.

PL/SQL is an extension of SQL that is used to create applications. 

[Back to TOC](#SQL-Questions)


## What is ETL in SQL?
ETL stands for ‘Extract, Transform and Load”. It uses the concept of data warehousing to make data visualization and data analysis. In a broader context, it is used for data integration.

Any system where data is taken from one system and stored/copied in another destination system and its data is represented differently is called an ETL process.

[Back to TOC](#SQL-Questions)


## What are Nested Triggers?
SQL offers Data Manipulation Language (DML) and Data Definition Language(DDL) to perform certain operations while querying the database.

When a particular type of operation is performed on the database, it automatically executes some actions on the database as well.

When these types of actions are triggered in the database, they are known as Nested triggers.

SQL categorizes the nested triggers into two main categories- AFTER triggers and INSTEAD OF triggers.

As the name suggests AFTER trigger is executed after a DML or DDL operation is performed on the database. 

However, INSTEAD OF trigger is executed in place of DML and DDL operations.

[Back to TOC](#SQL-Questions)


## What are Commits and Checkpoints?
The commit makes sure the data is consistent and maintained in the updated state after the current transaction ends. A new record is added to the log memory when a commit is used.

In the case of a checkpoint, it is used to write all the changes that are committed to disk up the system change number in the control files and header files. 

[Back to TOC](#SQL-Questions)

## What is the point of using a foreign key constraint?
The foreign key constraint comprises a set of rules, or limits, that will ensure that the values in the child and parent tables match. Technically, this means that the foreign key constraint will maintain the referential integrity within the database.

[Back to TOC](#SQL-Questions)

## What is the difference between Mysql and Postgresql? How about between pl sql and sql?

SQL has a few versions, each carrying specific characteristics.

MySQL and PostgreSQL are just two versions of the Structured Query Language. PostgreSQL supports outer joins, while MySQL doesn’t – you’ll need to use UNION or UNION ALL to emulate an outer join in MySQL. 
 
PL/SQL is not a version of SQL. PL/SQL is a complete procedural programming language and its scope of application is different. It is not strictly related to relational databases.

[Back to TOC](#SQL-Questions)

## What is an Sql View?

A view is a virtual table whose contents are obtained from an existing table or tables, called base tables. The retrieval happens through an SQL statement, incorporated into the view. So, you can think of a view object as a view into the base table. The view itself does not contain any real data; the data is electronically stored in the base table. The view simply shows the data contained in the base table.

[Back to TOC](#SQL-Questions)

## DDL, DQL, DML, DCL

- **Data Definition Language (DDL)**
  - `CREATE`
  - `ALTER`
  - `DROP`
  - `RENAME`
  - `TRUNCATE`
  - `COMMENT`

- **Data Query Language (DQL)**
  - `SELECT`

- **Data Manipulation Language (DML)**
  - `INSERT`
  - `UPDATE`
  - `DELETE`
  - `MERGE`
  - `CALL`
  - `EXPLAIN PLAN`
  - `LOCK TABLE`

- **Data Control Language (DCL)**
  - `GRANT`
  - `REVOKE`

[Back to TOC](#SQL-Questions)


## What is SQL?
SQL, which stands for Structured Query Language, is a standardized programming language used for managing and manipulating relational databases. It enables users to perform various operations on a database, such as querying data, updating records, and defining and modifying the structure of database objects. SQL is widely used because of its ability to efficiently query large data sets across multiple tables and its support for a wide range of database systems, including MySQL, PostgreSQL, SQL Server, Oracle, and SQLite, among others.

Key operations performed using SQL include:

- **Data Querying**: Retrieving data from databases using the `SELECT` statement, often combined with various clauses to filter and sort data.
- **Data Manipulation**: Inserting (`INSERT`), updating (`UPDATE`), and deleting (`DELETE`) records in a database to manage the data.
- **Data Definition**: Creating (`CREATE`), altering (`ALTER`), and dropping (`DROP`) database objects like tables, views, indexes, and stored procedures.
- **Data Control**: Managing access to the database and its objects through permissions using commands like `GRANT` and `REVOKE`.

SQL plays a crucial role in both web and software development that involves the storage, retrieval, and manipulation of data in relational database management systems (RDBMS).

[Back to TOC](#SQL-Questions)


## What are the different flavors of SQL?
SQL, or Structured Query Language, is the standard language for dealing with relational databases. However, various database management systems (DBMS) implement their version of SQL, often adding extensions or modifications to standard SQL to enhance functionality or performance. These variations are sometimes referred to as "flavors" of SQL. Here are some of the most widely used flavors:

1. **MySQL**: One of the most popular open-source relational database management systems. MySQL is widely used in web applications and is a part of the LAMP stack (Linux, Apache, MySQL, PHP/Python/Perl).

2. **PostgreSQL**: An advanced, open-source object-relational database system known for its robustness, scalability, and support for advanced data types and functionalities, such as JSON storage and geographic data (GIS).

3. **SQLite**: A C-language library that implements a small, fast, self-contained, high-reliability, full-featured, SQL database engine. SQLite is the most used database engine in the world, found in various applications, from browsers to mobile apps.

4. **Oracle Database (Oracle DB)**: A multi-model database management system produced and marketed by Oracle Corporation. It is known for its feature-rich, enterprise-scale capabilities, including support for pluggable databases and multi-tenancy.

5. **Microsoft SQL Server (MSSQL)**: A relational database management system developed by Microsoft. It is known for its integration with the .NET framework, offering a range of tools for business intelligence, reporting, and in-depth analytics.

6. **IBM DB2**: A family of data management products, including database servers, developed by IBM. It supports both relational and object-relational models and is known for its performance on large systems.

7. **MariaDB**: A fork of MySQL, created by the original developers of MySQL after concerns over Oracle's acquisition of MySQL. MariaDB is intended to remain free under the GNU GPL and aims to maintain compatibility with MySQL, ensuring a drop-in replacement capability.

8. **SAP HANA**: An in-memory, column-oriented, relational database management system developed and marketed by SAP SE. Its primary function as a database server is to store and retrieve data as requested by the applications, with an emphasis on speed and advanced analytics.

Each of these SQL flavors has its syntax nuances, proprietary functions, and extensions beyond the standard SQL. However, the core of SQL—the SELECT, INSERT, UPDATE, DELETE statements, and the concept of querying with JOINs—remains consistent across these variations, allowing skills in one flavor to be somewhat transferable to another with some learning and adjustments.

[Back to TOC](#SQL-Questions)


## What is a primary key?
A primary key is a fundamental concept in the realm of relational database management systems (RDBMS). It is a column (or a set of columns) in a table that uniquely identifies each row in that table. The primary key serves several important purposes in a database:

1. **Uniqueness**: Ensures that each row in a table can be uniquely identified, meaning no two rows can have the same value(s) in the primary key column(s).
2. **Indexing**: The database automatically creates a unique index for the primary key column(s), which speeds up the retrieval of data based on the primary key.
3. **Referential Integrity**: Primary keys play a crucial role in relationships between tables. A primary key in one table can be referenced by a foreign key in another table, establishing a direct link between the rows of the two tables. This is used to enforce referential integrity within the database.
4. **Simplicity**: Having a single, unique identifier for each row simplifies the process of querying, updating, or deleting specific records in a database.

**Characteristics of a Primary Key:**
- It must contain unique values.
- It cannot contain NULL values.
- A table can have only one primary key, which can consist of single or multiple columns (composite key).

[Back to TOC](#SQL-Questions)


## What are the top RDBMS engines?
As of my last update in 2023, several Relational Database Management System (RDBMS) engines are widely recognized for their performance, features, and scalability. The "top" RDBMS engines can vary based on the criteria used (such as popularity, performance, feature set, etc.), but here's a list of some of the most prominent ones:

1. **Oracle Database**: Oracle DB is known for its robust feature set, scalability, and performance, particularly in enterprise environments. It supports a wide range of data types and has extensive capabilities for data warehousing, online transaction processing (OLTP), and mixed database workloads.

2. **MySQL**: MySQL is one of the most popular open-source RDBMS, widely used for web applications and as part of the LAMP (Linux, Apache, MySQL, PHP/Python/Perl) stack. It's known for its ease of use, reliability, and strong performance for web-based applications.

3. **Microsoft SQL Server**: MSSQL Server is a comprehensive, enterprise-grade database solution developed by Microsoft. It offers extensive tools for data analysis, integration, and reporting. It's used in a wide range of applications, from small websites to large-scale enterprise systems.

4. **PostgreSQL**: PostgreSQL is an advanced, open-source object-relational database system. It is highly extensible and supports advanced data types and functions. It's known for its standards compliance, robustness, and support for complex queries.

5. **IBM Db2**: IBM Db2 is designed for enterprise users and offers high performance and scalability for both OLTP and data warehousing uses. It supports various platforms, including Linux, UNIX, and Windows, as well as cloud environments.

6. **SQLite**: Unlike the other RDBMS engines mentioned, SQLite is a lightweight, file-based database. It's embedded into the end program, offering a simple, disk-based database that doesn't require a separate server process. It's widely used in mobile apps, small to medium-sized websites, and desktop applications.

7. **MariaDB**: MariaDB is a fork of MySQL, created by the original developers of MySQL after concerns over Oracle's acquisition of MySQL. It aims to maintain open-source freedom and compatibility with MySQL, while also introducing new features and improvements.

8. **SAP HANA**: SAP HANA is an in-memory, column-oriented, relational database management system that emphasizes high-speed transactions and real-time analytics. It's part of SAP's strategy to offer a high-performance analytical and transactional processing system.

9. **Amazon Aurora**: Part of Amazon Web Services (AWS), Aurora is a cloud-based RDBMS that is compatible with MySQL and PostgreSQL. It's designed to offer the performance and reliability of high-end commercial databases at a fraction of the cost.

10. **CockroachDB**: Although newer to the scene, CockroachDB is a cloud-native, distributed SQL database designed for horizontal scalability and strong consistency with a focus on global applications.

[Back to TOC](#SQL-Questions)


## How is an RDBMS different from a No-SQL database?
Here's a comparison of RDBMS and NoSQL databases in a tabular format:

| Feature | RDBMS | NoSQL |
|---------|-------|-------|
| **Data Model** | Structured schema with tables, rows, and columns. Data is stored in relations and typically normalized. | Variety of data models (key-value, document, column-family, graph). Schema-less or flexible schema for unstructured or semi-structured data. |
| **Scalability** | Traditionally scaled vertically (more powerful server). Not inherently designed for horizontal scaling. | Designed for horizontal scalability (across many servers). Built to distribute data across multiple machines. |
| **Query Language** | Uses SQL for defining and manipulating data. Supports complex queries including joins and transactions. | No standard query language; uses a variety of query languages or APIs tailored to specific data models. Some support SQL-like querying. |
| **Consistency** | Follows ACID properties (Atomicity, Consistency, Isolation, Durability) for transactions. Ensures data integrity and consistency. | Often follows BASE model (Basically Available, Soft state, Eventual consistency). May sacrifice some consistency for availability and partition tolerance. |
| **Use Cases** | Ideal for applications requiring complex transactions, strong consistency, and a well-defined data structure. Common in banking systems, ERP systems, and applications requiring complex querying. | Suited for applications needing high performance with large volumes of data, scalability, and flexible data models. Used in big data applications, real-time web apps, and systems where data structure can evolve. |

This table summarizes the key differences between RDBMS and NoSQL databases, highlighting their data models, scalability, query languages, consistency models, and typical use cases.

[Back to TOC](#SQL-Questions)


## What do DDL, DCL, and DML stand for?
[Back to TOC](#SQL-Questions)


## Give examples of commands for each.
[Back to TOC](#SQL-Questions)


## What are the common data types in SQL?
[Back to TOC](#SQL-Questions)


## Does an SQLite database support date time objects?
[Back to TOC](#SQL-Questions)


## What are attribute constraints, and explain them?
[Back to TOC](#SQL-Questions)


## What is the difference between inner join and left outer join?
[Back to TOC](#SQL-Questions)


## What is the difference between UNION and UNION ALL?
[Back to TOC](#SQL-Questions)


## When should one use a CTE over a subquery?
[Back to TOC](#SQL-Questions)


## What are window functions?
[Back to TOC](#SQL-Questions)


## What is the difference between WHERE and HAVING?
[Back to TOC](#SQL-Questions)


## What does the COALESCE function do?
[Back to TOC](#SQL-Questions)


