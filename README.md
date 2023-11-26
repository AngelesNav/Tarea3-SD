# Hadoop
Para levantar topologia de contenedores:
```sh
docker compose up --build
```

---
## **Utilizar Hadoop**

**[0]** Se accede al contenedor que contiene el servicio de hadoop:
```sh
docker exec -it hadoop bash
```
**[1]** Se creará un respectivo directorio para gestionar las acciones del usuario hduser (es imporatnte que tenga este nombre para todos los comandos)\
Creación de carpeta para usuario:
```sh
hdfs dfs -mkdir /user
```
Creación de usuario en el directorio:
```sh
hdfs dfs -mkdir /user/hduser
```
Creación de directorio para el procesamiento archivos y/o textos:
```sh
hdfs dfs -mkdir input
```
**[2]** Damos los permisos tantos del usuario y del directorio
```sh
sudo chown -R hduser .
```
**[3]** Cargamos los txt extraidos de wikipedia a hadoop mediante los siguientes comandos, primero accedemos a la carpeta donde estan alojados y se ejecuta hdfs.
```sh
cd examples/
hdfs dfs -put carpeta1/*.txt input
hdfs dfs -put carpeta2/*.txt input
```
Se puede validar que efectivamente se hayan procesado dichos archivos contenidos en los directorios con el siguiente comando:
```sh
hdfs dfs -ls input

```
## Para eliminar todos los archivs .txt ingresados a Hadoop, con el siguiente comando
```sh
hdfs dfs -rm input/*.txt
```
## Cómo probar el código de WordCount simple
Dentro de bash, ejecutar
```sh
bash contador.sh
```
## Cómo probar el código de WordCount Inverted Indexing
Dentro de bash, ejecutar
```sh
----------
```
## Cómo probar el Buscador
Dentro de la carpeta examples, ejecutar
```sh
python3 buscador.py
