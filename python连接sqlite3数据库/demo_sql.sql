--������sql  
create table demo (id INT not null, name varchar(20));

--�����sql
insert into demo (id, name) values (1, 'richard');
insert into demo (id, name) values (2, 'bluce');
insert into demo (id, name) values (3, 'grace');
insert into demo (id, name) values (4, 'jhon');
insert into demo (id, name) values (5, 'nio');

--��ѯ��sql
select * from demo;
select * from demo where name = 'nio';
select name from demo where id=1;

