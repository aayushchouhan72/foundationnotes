Bhai! Let's create a complete Employee Management Database for SQL JOIN practice. It will contain 5 tables with matching records, unmatched records, NULL values, and multiple relationships.

You can practise INNER JOIN, LEFT JOIN, RIGHT JOIN, FULL OUTER JOIN simulation, CROSS JOIN and SELF JOIN.

# 1. Create database

```
CREATE DATABASE join_practice;

USE join_practice;
```

# 2. Create tables

Table 1: departments

```
CREATE TABLE departments (
    dep_id INT PRIMARY KEY,
    dep_name VARCHAR(50),
    location VARCHAR(50)
);
```

Table 2: employees

```
CREATE TABLE employees (
    emp_id INT PRIMARY KEY,
    emp_name VARCHAR(50),
    salary DECIMAL(10,2),
    dep_id INT,
    manager_id INT,
    FOREIGN KEY (dep_id) REFERENCES departments(dep_id)
);
```

Table 3: projects

```
CREATE TABLE projects (
    project_id INT PRIMARY KEY,
    project_name VARCHAR(50),
    budget DECIMAL(12,2)
);
```

Table 4: employee_projects

```
CREATE TABLE employee_projects (
    emp_id INT,
    project_id INT,
    assigned_date DATE,
    PRIMARY KEY (emp_id, project_id),
    FOREIGN KEY (emp_id) REFERENCES employees(emp_id),
    FOREIGN KEY (project_id) REFERENCES projects(project_id)
);
```

Table 5: locations

```
CREATE TABLE locations (
    location_id INT PRIMARY KEY,
    city VARCHAR(50)
);
```

# 3. Insert data

Departments

```
INSERT INTO departments VALUES
(1, 'HR', 'Indore'),
(2, 'IT', 'Bhopal'),
(3, 'Backend', 'Pune'),
(4, 'Frontend', 'Delhi'),
(5, 'Marketing', 'Mumbai'),
(6, 'Sales', 'Jaipur'),
(7, 'Finance', 'Indore');
```

Employees

```
INSERT INTO employees VALUES
(101, 'Aayush', 35000, 2, 105),
(102, 'Komal', 40000, 1, 105),
(103, 'Abhinav', 45000, 3, 106),
(104, 'Krishna', 30000, 4, 106),
(105, 'Rahul', 60000, 2, NULL),
(106, 'Priya', 55000, 3, NULL),
(107, 'Ajay', 32000, 5, 105),
(108, 'Khushi', 28000, NULL, 105),
(109, 'Sneha', 42000, 1, 106),
(110, 'Mohit', 38000, NULL, NULL);
```

Projects

```
INSERT INTO projects VALUES
(201, 'Website Development', 150000),
(202, 'Mobile Application', 200000),
(203, 'AI Chatbot', 300000),
(204, 'E-Commerce', 250000),
(205, 'Payroll System', 100000),
(206, 'CRM Software', 180000);
```

Employee Projects

```
INSERT INTO employee_projects VALUES
(101, 201, '2026-01-10'),
(101, 203, '2026-01-15'),
(102, 205, '2026-01-12'),
(103, 201, '2026-01-20'),
(103, 203, '2026-02-01'),
(104, 202, '2026-02-05'),
(105, 204, '2026-02-10'),
(106, 203, '2026-02-12'),
(107, 206, '2026-02-15'),
(109, 205, '2026-02-20');
```

Locations

```
INSERT INTO locations VALUES
(1, 'Indore'),
(2, 'Bhopal'),
(3, 'Pune'),
(4, 'Delhi'),
(5, 'Mumbai'),
(6, 'Jaipur'),
(7, 'Chennai');
```

# 4. Understand the relationships

## Database relationship diagram

departments

PK: dep_id

One-to-many

employees

PK: emp_id · FK: dep_id · Self FK: manager_id

Many-to-many through bridge table

employee_projects

Composite PK: emp_id + project_id

projects

PK: project_id

# 5. Your JOIN practice questions

Practice checklist

0/25 completed

Level 1 – INNER JOIN

1\. Display employee names with their department names.

2\. Display employee names, salaries and department locations.

3\. Find employees working in the IT department.

4\. Display employees earning more than ₹40,000 with their department names.

5\. Display employee names with their assigned project names.

Level 2 – LEFT & RIGHT JOIN

1\. Display all employees with department names, including employees without departments.

2\. Display all departments with their employees, including empty departments.

3\. Find departments that have no employees.

4\. Find employees who are not assigned to any project.

5\. Display all projects, including projects without assigned employees.

Level 3 – FULL OUTER JOIN

1\. Display all employees and departments, including unmatched records.

2\. Find employees without departments and departments without employees.

3\. Generate a complete employee-project report, including unmatched records.

Level 4 – SELF JOIN

1\. Display employee names with their manager names.

2\. Find employees who have the same manager.

3\. Find employees earning more than their managers.

4\. Display managers who manage more than one employee.

Level 5 – Multiple JOINs

1\. Display employee name, department name and project name.

2\. Display all employees, their departments, projects and project budgets.

3\. Find employees working on more than one project.

4\. Find projects having no employees assigned.

Level 6 – JOIN + GROUP BY

1\. Count employees in each department.

2\. Find average salary in each department.

3\. Find departments with more than two employees.

4\. Find total project budget assigned to each employee.

5\. Find the department with the highest average salary.

# 6. Important verification commands

```
SHOW TABLES;

DESC employees;

SELECT * FROM departments;
SELECT * FROM employees;
SELECT * FROM projects;
SELECT * FROM employee_projects;
SELECT * FROM locations;
```

One important thing: I intentionally included departments without employees, employees without departments, managers with multiple employees, and projects without assignments.

This gives you realistic JOIN practice without needing to create new data every time.

My suggestion: Start with Level 1 and solve all five questions yourself. Send me your SQL queries, and I'll check them one by one without directly giving away the answers. 💪
