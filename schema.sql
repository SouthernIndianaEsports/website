CREATE DATABASE IF NOT EXISTS siea;
USE siea;

CREATE TABLE IF NOT EXISTS events (
	   id int(11) NOT NULL AUTO_INCREMENT,
	   name varchar(50) NOT NULL,
	   date date NOT NULL,
	   time timestamp NOT NULL,
	   location varchar(20) NOT NULL,
	   description varchar(500) NOT NULL,
	   flier text NOT NULL,
	   PRIMARY KEY (id)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
