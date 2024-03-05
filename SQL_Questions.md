# SQL Questions

1. [Explain Normalization?](#explain-normalization)
2. [DDL vs DML](#difference-between-ddl-and-dml)
3. [ACID Properties](#acid-properties-in-sql)
4. [Write a Query to Find all the Duplicates in a Table?](#find-duplicates-in-a-table)
5. [Clustered vs non-clustered](#clustered-vs-non-clustered-index)
6. [Denormalisation](#explain-denormalisation)
7. [Collation](#what-is-collation)
8. [inner, outer, and full outer join](#difference-between-joins)
9. [Join vs Union?](#join-vs-union)
10. [UNION vs UNION ALL](#union-vs-union-all)
11. [Write a Query to Print the Highest Salary from a Table](#highest-salary-query)
12. [Shared vs Inclusive Locks](#shared-vs-inclusive-locks)
13. [Transpose Using SQL](#mechanism-of-transpose)
14. [Working of the B-trees Index](#working-of-b-trees-index)
15. [Effect of Truncate and Delete on an Identity](#truncate-vs-delete)
16. [Cost of Having a Database Index](#cost-of-database-index)
17. [Advantages of Having an Index](#advantages-of-having-an-index)
18. [Indexing in the Database](#explain-indexing)
19. [OLAP and OLTP](#olap-and-oltp)
20. [In What Conditions Does CASE WHEN Apply](#case-when-conditions)
21. [Explain the Cases to Use HAVING versus WHERE](#having-vs-where)
22. [PL/SQL](#what-is-plsql)
23. [ETL in SQL](#what-is-etl)
24. [Nested Triggers](#nested-triggers)
25. [Commits and Checkpoints](#commits-and-checkpoints)


## Explain Normalization?
Normalization is a method of organization of the data in the database to minimize redundancy from a set of relations. The concept of Normal forms is used to perform normalization on a relation. 

1NF:- If a relationship has an atomic value it is in 1NF.  
2NF:- For a relation to be in 2NF, it should be in 1NF and all the non-key attributes are fully functionally dependent on the primary key.  
3NF:- For a relation to be in 3NF, it should be in 2NF and additionally no transition dependency exists.  
BCNF:- Boy Codd’s Normal form is a strong representation of 3NF.  

[Back to TOC](#SQL-Questions)


## Explain the Difference Between DDL and DML?
- DDL stands for Data Definition language whereas, DML is called Data Manipulation Language.
- DDL creates a schema with some constraints. DML adds, retrieves or updates the data in that schema. 
- DDL defines the column attribute of the table. DML provides the row attribute of the table.
- Examples of DDL commands are created, alter, drop, rename, etc. and those of DML are merged, update, insert, etc. 
- The WHERE clause is not used in DDL but is used in DML.

[Back to TOC](#SQL-Questions)


## What are ACID Properties in SQL?
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
[Back to TOC](#SQL-Questions)


## Explain the Difference Between a Join and a Union?
[Back to TOC](#SQL-Questions)


## Explain the Difference Between UNION AND UNION ALL?
[Back to TOC](#SQL-Questions)


## Write a Query to Print the Highest Salary from a Table?
[Back to TOC](#SQL-Questions)


## What is the Difference Between Shared and Inclusive Locks?
[Back to TOC](#SQL-Questions)


## Explain the Mechanism of Transpose Using SQL?
[Back to TOC](#SQL-Questions)


## Explain the Working of the B-trees Index?
[Back to TOC](#SQL-Questions)


## Explain the Effect of Truncate and Delete on an Identity?
[Back to TOC](#SQL-Questions)


## Explain the Cost of Having a Database Index?
[Back to TOC](#SQL-Questions)


## What are the Advantages of Having an Index?
[Back to TOC](#SQL-Questions)


## Explain Indexing in the Database?
[Back to TOC](#SQL-Questions)


## What is OLAP and OLTP?
[Back to TOC](#SQL-Questions)


## In What Conditions Does CASE WHEN Apply?
[Back to TOC](#SQL-Questions)


## Explain the Cases to Use HAVING versus WHERE?
[Back to TOC](#SQL-Questions)


## What is PL/SQL?
[Back to TOC](#SQL-Questions)


## What is ETL in SQL?
[Back to TOC](#SQL-Questions)


## What are Nested Triggers?
[Back to TOC](#SQL-Questions)


## What are Commits and Checkpoints?
[Back to TOC](#SQL-Questions)

