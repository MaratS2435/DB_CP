CREATE TABLE "users" (
  "user_id" SERIAL PRIMARY KEY,
  "password" TEXT NOT NULL,
  "name" VARCHAR(255) NOT NULL,
  "age" int,
  "status" VARCHAR(255) NOT NULL,
  "role" VARCHAR(255),
  "hotel_id" INT,
  "affilation_id" INT
);

COMMENT ON TABLE "users" IS 'Все пользователи';

COMMENT ON COLUMN "users"."user_id" IS 'Идентификатор пользователя';

COMMENT ON COLUMN "users"."password" IS 'Зашифрованный пароль пользователя';

COMMENT ON COLUMN "users"."name" IS 'Имя пользователя';

COMMENT ON COLUMN "users"."age" IS 'Возраст пользователя';

COMMENT ON COLUMN "users"."status" IS 'Статус пользователя: жив, мертв, отошел от дел';

COMMENT ON COLUMN "users"."role" IS 'Роль в мире убийц';

COMMENT ON COLUMN "users"."hotel_id" IS 'Идентификатор ближайшего отеля';

COMMENT ON COLUMN "users"."affilation_id" IS 'Идентификатор организации, в которой состоит';

CREATE TABLE "rules" (
  "rule_id" serial PRIMARY KEY,
  "description" TEXT NOT NULL
);

COMMENT ON TABLE "rules" IS 'Все правила';

COMMENT ON COLUMN "rules"."rule_id" IS 'Идентификатор правила';

COMMENT ON COLUMN "rules"."description" IS 'Описание правила';

CREATE TABLE "affilations" (
  "affilation_id" serial PRIMARY KEY,
  "name" VARCHAR(255) NOT NULL,
  "head_id" INT
);

COMMENT ON TABLE "affilations" IS 'Все организации';

COMMENT ON COLUMN "affilations"."affilation_id" IS 'Идентификатор организации';

COMMENT ON COLUMN "affilations"."name" IS 'Название организации';

COMMENT ON COLUMN "affilations"."head_id" IS 'Идентификатор руководителя';

CREATE TABLE "hotels" (
  "hotel_id" serial PRIMARY KEY,
  "place" VARCHAR(255) NOT NULL,
  "manager" int
);

COMMENT ON TABLE "hotels" IS 'Все отели';

COMMENT ON COLUMN "hotels"."hotel_id" IS 'Идентификатор отеля';

COMMENT ON COLUMN "hotels"."place" IS 'Местоположение отеля';

COMMENT ON COLUMN "hotels"."manager" IS 'Идентификатор руководителя отеля';

CREATE TABLE "contracts" (
  "contract_id" serial PRIMARY KEY,
  "task" TEXT NOT NULL,
  "task_id" INT,
  "client_id" INT,
  "reward" numeric(15,2) NOT NULL
);

COMMENT ON TABLE "contracts" IS 'Все контракты';

COMMENT ON COLUMN "contracts"."task" IS 'Пояснение задания';

COMMENT ON COLUMN "contracts"."task_id" IS 'Идентификатор цели, если есть в базе данных';

COMMENT ON COLUMN "contracts"."client_id" IS 'Идентификатор заказчика';

COMMENT ON COLUMN "contracts"."reward" IS 'Награда в долларах';

CREATE TABLE contracts_executers (
  "contract_id" INT NOT NULL,
  "executer_id" INT NOT NULL
);

COMMENT ON TABLE "contracts_executers" IS 'Все исполнители контрактов';

COMMENT ON COLUMN "contracts_executers"."contract_id" IS 'Идентификатор контракта';

COMMENT ON COLUMN "contracts_executers"."executer_id" IS 'Идентификатор исполнителя';

CREATE TABLE "excommunicados" (
  "user_id" INT NOT NULL,
  "rule_id" INT NOT NULL,
  "reward" numeric(15,2) NOT NULL,
  "begining" timestamp
);

COMMENT ON TABLE "excommunicados" IS 'История исключений';

COMMENT ON COLUMN "excommunicados"."user_id" IS 'Идентификатор наказуемого';

COMMENT ON COLUMN "excommunicados"."rule_id" IS 'Идентификатор нарушенного правила';

COMMENT ON COLUMN "excommunicados"."reward" IS 'Награда в долларах';

COMMENT ON COLUMN "excommunicados"."begining" IS 'Время начала исключения';

ALTER TABLE "users" ADD FOREIGN KEY ("hotel_id") REFERENCES "hotels" ("hotel_id");

ALTER TABLE "users" ADD FOREIGN KEY ("affilation_id") REFERENCES "affilations" ("affilation_id");

ALTER TABLE "affilations" ADD FOREIGN KEY ("head_id") REFERENCES "users" ("user_id");

ALTER TABLE "hotels" ADD FOREIGN KEY ("manager") REFERENCES "users" ("user_id");

ALTER TABLE "contracts" ADD FOREIGN KEY ("task_id") REFERENCES "users" ("user_id");

ALTER TABLE "contracts" ADD FOREIGN KEY ("client_id") REFERENCES "users" ("user_id");

ALTER TABLE "excommunicados" ADD FOREIGN KEY ("user_id") REFERENCES "users" ("user_id");

ALTER TABLE "excommunicados" ADD FOREIGN KEY ("rule_id") REFERENCES "rules" ("rule_id");

ALTER TABLE "contracts_executers" ADD FOREIGN KEY ("contract_id") REFERENCES "contracts" ("contract_id");

ALTER TABLE "contracts_executers" ADD FOREIGN KEY ("executer_id") REFERENCES "users" ("user_id");