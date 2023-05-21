create database email_users;
use email_users;

drop table user_info;
create table user_info(
	user_name char(20),
    user_lastname char(20),
    email char(80)
) comment 'Пользователи';
