
create table TEMP(
temp_id NUMBER(6) not null,
message VARCHAR(35),
date_written DATE,


CREATE SEQUENCE tempseq_Trigger
  MINVALUE 1
  MAXVALUE 999999999999999999999999999
  START WITH 1
  INCREMENT BY 1
  CACHE 20;  1



 create or replace trigger tempseq_Trigger
   before insert
     on TEMP
   for each row
 begin
    select temp_seq.nextval
     into :new.temp_id
    from dual;
   end;
 /

DECLARE
  v_date_writtin DATE:=SYSDATE;
  v_message_writtin VARCHAR2(35):='This is my PL/SQL program';		
BEGIN
INSERT INTO TEMP (message,date_written) values (v_message_writtin,v_date_writtin);
END;
/
