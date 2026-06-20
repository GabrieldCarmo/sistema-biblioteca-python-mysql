CREATE DATABASE IF NOT EXISTS dbbiblioteca;

USE dbbiblioteca;

CREATE TABLE livro(
	id_livro TINYINT PRIMARY KEY AUTO_INCREMENT,
    titulo VARCHAR(60) NOT NULL,
    autor VARCHAR(60) NOT NULL,
    ano_publicacao YEAR NOT NULL
);

select * from livro;