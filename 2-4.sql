SET SERVEROUTPUT ON
DECLARE 
 vtoday DATE := SYSDATE;
 vtomorrow vtoday%TYPE;

BEGIN
 vtomorrow:=vtoday+1;
 DBMS_OUTPUT.PUT_LINE(vtoday);
 DBMS_OUTPUT.PUT_LINE(vtomorrow);



END; 
/
