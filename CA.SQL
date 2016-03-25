SET SERVEROUTPUT ON
DECLARE
	empname employees.first_name%TYPE;
	salary employees.salary%TYPE;
	hireDate employees.hire_date%TYPE;

CURSOR emp_cursor IS SELECT first_name, salary, hire_date FROM employees
WHERE salary > 15000 AND hire_date > '01-FEB-1988';
 
BEGIN
	OPEN emp_cursor;
	LOOP
		FETCH emp_cursor INTO empname, salary, hireDate;
		EXIT WHEN emp_cursor%NOTFOUND;
		DBMS_OUTPUT.PUT_LINE(first_name || ' ' || salary || ' ' || hire_date);
		EXCEPTION
      WHEN NO_DATA_FOUND THEN
      DBMS_OUTPUT.PUT_LINE('ERROR');
      WHEN OTHERS THEN
    DBMS_OUTPUT.PUT_LINE('OTHER');
    END;
  END LOOP;
  CLOSE emp_cursor;
END;
/