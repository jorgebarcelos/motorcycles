/*sudo docker run -d -p 3306:3306 -e MYSQL_ROOT_PASSWORD=123456 -e MYSQL_DATABASE=motorcycles -e MYSQL_USER=MyUser -e MYSQL_PASSWORD=123456 motorcycles.db
6cc03780a66034f585a6e2af7c7841f4e6c38bc4919471a00755ab3986308061*/


USE motorcycles;
 
 CREATE TABLE bikes(
 	id integer not null auto_increment,
 	brand varchar(100),
 	model varchar(100),
 	model_year integer,
 	PRIMARY KEY (id)
 );

SET character_set_client = utf8;
SET character_set_connection = utf8;
SET character_set_results = utf8;
SET collation_connection = utf8_general_ci;

INSERT INTO bikes (brand, model, model_year) VALUES ("Harley Davidson", "Forty Eight", 2022);
