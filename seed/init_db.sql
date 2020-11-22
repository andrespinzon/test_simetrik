CREATE TABLE public.transaction (
	transaction_id varchar NULL,
	transaction_date date NULL,
	transaction_amount int NULL,
	client_id int NULL,
	client_name varchar NULL
);


CREATE TABLE public.file (
	"name" varchar NULL,
	created_at date NULL
);
