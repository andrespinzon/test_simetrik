### SOLUCION
Esta compuesta por una estructura de microservicios.
Dividido en diferentes capas dentro de cada aplicacion:
    
    files
        - managers (Querys)
        - models
        - serializers
        - services
        - test
            - test_services
            - test_managers
        - views
        
Para correr el servidor, se debe ejecutar el siguiente comando: 

    docker-compose up

NOTA: Por favor ejecutar doble vez el comando docker-compose up,  para que el servidor se ejecute 
Correctamente, puesto que la primera vez en correrlo ejecuta la migración 
Lo que hace que el servidor no se pueda conectar a la 
Bane de datos. 
        
Por otra parte se agrego la integracion con MINIO, el cual sirve como servidor de almacenamiento
este permite faciles integraciones con AWS, Google, entre otras. 

Para visualizar los archivos que se almacenan en este servidor nos dirigimos a:

    http://localhost:9000
    
E ingresamos las siguientes credenciales:

    MINIO_ACCESS_KEY=AKIAIOSFODNN7EXAMPLE
    MINIO_SECRET_KEY=wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY

el bucket definido en el servidor es llamado simetrik.

### TEST

![alt text](images_test/unit_test.png)

### ENDPOINTS

Para realizar las pruebas del endpoint de subir el archivo 
se adjunta en el proyecto en la carpeta
    
    seed/transaction_files.csv
    
#### UPLOAD FILE
    curl --location --request POST 'http://localhost:8000/api/files/upload-file/' \
    --form 'file=@"/DEVELOP/PRUEBAS/SIMETRIK/transaction_files.csv"'

    
![alt text](images_test/upload_file.png)

####  GET DETAIL TRANSACTION 

    curl --location --request GET 'http://localhost:8000/api/transactions/52fba4fa-3a01-4961-a809-e343dd4f9599/'
    
![alt text](images_test/get_detail_transaction.png)


#### GET TRANSACTIONS WITH PARAMS 
    
    curl --location --request GET 'http://localhost:8000/api/transactions/?page=1&per_page=2&order_by=transaction_amount&transaction_id=52fba4fa-3a01-4961-a809-e343dd4f9654&transaction_date=2020-06-04&transaction_amount=15000,45000&client_id=1071,1068&client_name=nombre%20cliente5'    
    
![alt text](images_test/get_transactions_with_params.png)
