CREATE TABLE public.transactions (
	transaction_id varchar NULL,
	transaction_date date NULL,
	transaction_amount int NULL,
	client_id int NULL,
	client_name varchar NULL
);


CREATE TABLE public.files (
	"name" varchar NULL,
	created_at date NULL
);
