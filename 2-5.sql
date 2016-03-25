SET SERVEROUTPUT ON
DECLARE 
 vtoday DATE := SYSDATE;
 vtomorrow DATE:=SYSDATE+1;

BEGIN

 DBMS_OUTPUT.PUT_LINE(vtoday);
 DBMS_OUTPUT.PUT_LINE(vtomorrow);

:basic_percent:45;
:pf_percent:12;

END; 
/
