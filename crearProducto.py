#Creando Productos utilizando protcolo xmlrpc
from xmlrpc import client
import ssl

url = "https://tu-instancia-odoo.com"
db = "tu_base_de_datos"
username = "tu_usuario"
password = "tu_contraseña"

gcontext = ssl._create_unverified_context()

common = client.ServerProxy("{}/xmlrpc/2/common".format(url),context=gcontext,use_datetime=True)
uid = common.authenticate(db, username, password,{})

models = client.ServerProxy('{}/xmlrpc/2/object'.format(url))

product_template = {
    'name': 'Test',
    'default_code': '12345',  # Reemplaza con el código que desees
    # Aquí puedes añadir más atributos según sea necesario
}

product_id = models.execute_kw(db, uid, password, 'product.template', 'create', [product_template])

product = models.execute_kw(db, uid, password, 'product.template', 'read', [product_id])
print(product)
