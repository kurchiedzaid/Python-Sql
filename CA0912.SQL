CREATE TABLE table_analysis
(
ename varchar2(20),
years number(2),
sal number(8,2)
);
/

SET SERVEROUTPUT ON
DECLARE
	empname employees.first_name%TYPE;
	salary employees.salary%TYPE;
	hireDate employees.hire_date%TYPE;
BEGIN
SELECT first_name,salary,hire_date
INTO table_analysis
FROM employees
WHERE salary <3500 AND hire_date > '01-FEB-2009';
	LOOP
		DBMS_OUTPUT.PUT_LINE(empname || ' ' || salary || ' ' || hireDate);
		EXCEPTION
	IF salary <3500  AND HIRE_DATE<'01-FEB-2009'THEN
      DBMS_OUTPUT.PUT_LINE(' due for raise');
      WHEN OTHERS THEN
    DBMS_OUTPUT.PUT_LINE('not due for raise');
    END;
  END LOOP;
END;
/