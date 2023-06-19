BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "sefit_afastamento" (
	"id"	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	"data_criacao"	date NOT NULL,
	"data_inicio"	date NOT NULL,
	"data_fim"	date NOT NULL,
	"motivo"	varchar(10) NOT NULL,
	"obs"	text,
	"fk_servidor_id"	integer NOT NULL,
	FOREIGN KEY("fk_servidor_id") REFERENCES "sefit_servidor"("mat") DEFERRABLE INITIALLY DEFERRED
);
INSERT INTO "sefit_afastamento" ("id","data_criacao","data_inicio","data_fim","motivo","obs","fk_servidor_id") VALUES (1,'2023-06-18','2023-06-18','2023-06-23','fl','',3165460),
 (2,'2023-06-18','2023-09-01','2023-10-01','fr','Ferias do Servidor. Todo o mês de setembro de 2023',3165460);
CREATE INDEX IF NOT EXISTS "sefit_afastamento_fk_servidor_id_fc3ec91b" ON "sefit_afastamento" (
	"fk_servidor_id"
);
COMMIT;
