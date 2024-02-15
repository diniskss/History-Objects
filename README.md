<h1><b>Информационная система учета и контроля объектов, представляющих архитектурную и историческую ценность</b></h1>
<i><b>Скрипт по созданию БД:</b></i>
<pre>CREATE TABLE test.Categories (
	Category_name varchar(100) NOT NULL,
	Category_id INT auto_increment primary key NOT NULL
)
ENGINE=InnoDB
DEFAULT CHARSET=utf8mb3
COLLATE=utf8mb3_general_ci
COMMENT='Таблица категорий'
AUTO_INCREMENT=1;

CREATE TABLE test.Object (
	Object_id varchar(100) NULL,
	Category_id varchar(100) NULL,
	Object_age INT NOT NULL,
	Object_location varchar(100) NULL,
	Object_where_it_was_found varchar(100) NULL
)
ENGINE=InnoDB
DEFAULT CHARSET=utf8mb3
COLLATE=utf8mb3_general_ci;

CREATE table test.user (
	user_id int auto_increment primary key NOT NULL,
	login varchar(100) not null,
	password varchar(100) not null
)</pre>
