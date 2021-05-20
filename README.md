# Sitema de recomendación de películas

## Pre-requisitos
aws cli  
python 3  
virtualenv
## Instalar dependencias
python3 -m pip install --user -U -r requirements.txt

## Montaje de infraestructura
1. creacion de key par (pares de claves) para EC2 en aws console.
2. Asignar permisos : sudo chmod 0400 </path/to/my-key-pair.pem> (linux, revisar si es necesario en windows)
3. Despliegue de servicios: utiliza los archivios movie-rs.yml para configuración de servicios a utilizar 
 y movie-rs-param-dev.json contiene los pararametros, del directorio cloudformation, se ejecuta: 
 
    python3 ./scripts/create_cfn_stack.py --environment dev --ec2-key-name movie-rs-keypar

4. Cargar datos a S3 : se debe poner la carpeta con los datos en el directorio raw data, ejecutar  
    
    python3 ./scripts/upload_apps_to_s3.py
    
5. Cargar scripts a S3 :  
    
    python3 ./scripts/upload_csv_files_to_s3.py

6. Crear catálogo de datos GLUE:  
  python3 ./scripts/crawl_raw_data.py --crawler-name movie-sr-raw



  
## comandos útiles
+ listar buckets del proyecto  
aws s3api list-buckets | jq -r '.Buckets[] | select(.Name | startswith("movie-sr-")).Name'
+ Consultar tablas en catálogo de datos  
 aws glue get-tables --database movie_sr | jq -r '.TableList[] | select(.Name | startswith("raw_")).Name'
 
+ Revisar parámetros almencados en SSM:   
aws ssm get-parameters-by-path --path '/movie_sr' | jq -r ".Parameters[] | {Name: .Name, Value: .Value}"



creaer acceso ssh ec2 para ip porpia export EMR_MASTER_SG_ID=$(aws ec2 describe-security-groups | \
    jq -r '.SecurityGroups[] | select(.GroupName=="ElasticMapReduce-master").GroupId')aws ec2 authorize-security-group-ingress \
    --group-id ${EMR_MASTER_SG_ID} \
    --protocol tcp \
    --port 22 \
    --cidr $(curl ipinfo.io/ip)/32

## Referencia
[Running PySpark Applications on Amazon EMR: Methods for Interacting with PySpark on Amazon Elastic MapReduce](https://garystafford.medium.com/running-pyspark-applications-on-amazon-emr-e536b7a865ca)


conexion al cluster
ssh -i ~/movie-key-ec2.pem -ND 8157 hadoop@ec2-54-164-202-23.compute-1.amazonaws.com
python3 ./scripts/submit_spark_ssh.py --ec2-key-path /home/david/Descargas/movie-key-ec2.pem
