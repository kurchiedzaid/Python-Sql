Create or replace trigger get_departments_id_seq_trig 
BEFORE INSERT ON Departments for each row
BEGIN
if (:new.department_id is not null) then
raise_application_error (
-20001, ‘I supply the keys, not you’
);
end if;
select departments_seq.nextval into :new.department_id from dual;
END;
/