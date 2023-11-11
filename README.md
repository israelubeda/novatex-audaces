# Creacion de productos ODOO utilizando API 

_Creacion de productos utilizando el protocolo XMLRPC en odoo _

## Comenzando 🚀

_Estas instrucciones te permitirán obtener la creacion de un Producto en odoo v.16 pero puede ser utilizado para cualquier version de odoo ,utilizando Python 3._



### Pre-requisitos 📋

_Para el ejemplo se utilizara python 3.X y las librerias **xmlrpc** y **ssl**_

```
Python
xmlrpc
ssl

```

### Instalación 🔧

_Instalacion de Librerias_

```
pip install xmlrpc
pip install ssl

```
_en el archivo [crearProducto.py](crearProducto.py) modificar las variables de url,db,username y password ,con los datos que seran entregados, en caso de no tenerlos se pueden obtener en el perfil de cada usario, creando los permisos para la **API**_

```
url = "https://tu-instancia-odoo.com"
db = "tu_base_de_datos"
username = "tu_usuario"
password = "tu_contraseña"

```

_Luego ejecutar script _

```
python3 crearProducto.py

```

El script creara un producto de nombre **Test** y con el codigo **12345**



## Autores ✒️


* **Israel ubeda** - *Trabajo Inicial* - [Israel ubeda](https://github.com/israelubeda)



---
⌨️ con ❤️ por [Israel ubeda](https://github.com/israelubeda) 😊