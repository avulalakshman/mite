
create table internship(id integer primary key, name text not null, company text, i_year integer, status integer);

create table student(regno integer primary key, name text not null,sem integer, placed integer);

create table registration(regno integer references student(regno), i_id integer references internship(id), status integer);


insert into internship values(1001,"UI","Spaneos","2018",1);
insert into internship values(1002,"Data Analytics","Spaneos","2019",1);
insert into internship values(1003,"Machine Learning","Delithe","2019",1);
insert into internship values(1004,"Ethical Hacking","Spaneos","2020",1);
insert into internship values(1005,"IOT","Spaneos","2018",1);


insert into student(regno,name,sem,placed) values(16001,"Abhijith",7,0);
insert into student(regno,name,sem,placed) values(16002,"Adithya",7,0);
insert into student(regno,name,sem,placed) values(16015,"Joy",7,0);
insert into student(regno,name,sem,placed) values(16020,"Sandhya",7,0);
insert into student(regno,name,sem,placed) values(16024,"Niranjan",7,0);
insert into student(regno,name,sem,placed) values(16029,"Prashil",7,0);
insert into student(regno,name,sem,placed) values(16030,"Praneeth",7,0);
insert into student(regno,name,sem,placed) values(16034,"Rakshitha",7,0);
insert into student(regno,name,sem,placed) values(16035,"Rashmi",7,0);
insert into student(regno,name,sem,placed) values(16043,"Bhatta",7,0);
insert into student(regno,name,sem,placed) values(16057,"Vignesh",7,0);
insert into student(regno,name,sem,placed) values(16058,"Vikhyath",7,0);

insert into registration(rengno, i_id,status) values(16001,1001,0);
insert into registration(rengno, i_id,status) values(16002,1002,1);
insert into registration(rengno, i_id,status) values(16001,1002,0);
insert into registration(rengno, i_id,status) values(16002,1001,1);
insert into registration(rengno, i_id,status) values(16001,1003,0);
insert into registration(rengno, i_id,status) values(16002,1004,1);
insert into registration(rengno, i_id,status) values(16015,1003,1);
insert into registration(rengno, i_id,status) values(16020,1004,1);
insert into registration(rengno, i_id,status) values(16024,1005,0);
insert into registration(rengno, i_id,status) values(16029,1001,0);
insert into registration(rengno, i_id,status) values(16030,1002,1);
insert into registration(rengno, i_id,status) values(16034,1003,1);
insert into registration(rengno, i_id,status) values(16035,1004,1);
insert into registration(rengno, i_id,status) values(16043,1005,0);
insert into registration(rengno, i_id,status) values(16057,1001,0);
insert into registration(rengno, i_id,status) values(16058,1002,1);