
# Proyecto en Django para test CHR

Como se pidio en la documentacion enviada para el test, en este proyecto genere dos aplicaciones muy sencillas, una llamada BikesAPI para obtener la informacion de la api entregada "http://api.citybik.es/v2/networks/bikesantiago" y almacenarla en una base de datos PostgreSQL mediante un modelo.

Por otro lado, la aplicacion ServiceEnvironmentAPI que contiene el script que se ejecuta al iniciar el proyecto para realizar una extraccion de datos de la pagina entregada 
"https://seia.sea.gob.cl/busqueda/buscarProyectoAction.php?" de la cual se obtienen todos los datos de la tabla de cada pagina existente mediante BeautifulSoup4 y se almacenan en la base de datos PostgreSQL mediante un modelo ademas de generar un archivo Json en la raiz del proyecto.






## Deployment

Para ejecutar este proyecto, primero es necesario instalar las librerias utilizadas, para ello ubicandonos en la raiz del proyecto y ejecutando el siguiente comando en la consola.

```bash
  pip install -r requirements.txt
```

Antes de iniciar el proyecto Django, debemos configurar la conexion a nuestra respectiva base de datos, en este caso como utilizaremos PostgreSQL debemos usar esta configuracion en settings.py 
```bash
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': '*Nombre de la base de datos*',
            'USER': '*usuario*',
            'PASSWORD': '*contrasena*',
            'HOST': '*direccion ip del host, en mi caso utilice localhost*',
            'PORT': '*puerto en el que esta disponible*',
        }
    }
```
Ya configurada la conexion, realizamos los siguientes comandos para actualizar la base de datos
```bash
    py manage.py makemigrations 
    py manage.py migrate
```
Con esto crearemos las tablas en la base de datos, ahora para realizar el web scrapping, el script se ejecuta utilizando el siguiente comando (Puede tardar de 10 a 20 minutos dependiendo del rendimiento del CPU)
```bash
    py manage.py scrap 
```
Una vez realizado se creara el archivo JSON en la raiz del proyecto y tambien se actualizara la base de datos con los datos del scrapping.

Antes de levantar el proyecto, debemos crear un superusuario para acceder a la vista de administrador, por lo que es necesario ejecutar el siguiente comando y seguir las instrucciones
```bash
    py manage.py createsuperuser
```

Ahora para obtener la informacion de la API de bikeSantiago, es necesario iniciar el proyecto Django y acceder a una vista (ya que se pidio explicitamente que fuera una funcion y no un script)
```bash
    py manage.py runserver
```
Y acceder a la ruta dependiendo del puerto en que levante el proyecto (Esto puede tardar varios minutos por lo que quedara cargando la vista y mostrara un mensaje al finalizar)
```bash
    127.0.0.1:8000/bikes
```
Una vez cargada la vista, en la base de datos se almacenan todos los datos de todos los objetos obtenidos por la API, los cuales se pueden ver por la vista del panel de admin de Django, podemos acceder por la siguiente ruta
```bash
    http://127.0.0.1:8000/admin/
```
Nos pedira nuestras credenciales de administrador que creamos previamente y podremos acceder a todos los registros.

## Authors

- [@AnticuchoNotCucho](https://www.github.com/Anticuchonotcucho)

