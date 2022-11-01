#from app import db
from utils.db import db

from modelos.ModeloProducto import Producto , format_producto
from flask import request, Blueprint

mainP = Blueprint('producto_blueprint', __name__)


@mainP.route('/producto')
def index():
    return "WEEEEEEEE"

#@app.route('/')
#def hello():
#    return 'hey!'

#crear un producto
@mainP.route('/productos',methods=['POST'])
def crear_producto():
    codigo = request.json['codigo']  #era id
    categoria = request.json['categoria']
    descripcion = request.json['descripcion']
    precio = request.json['precio']
    cantidad = request.json['cantidad']
    imagen = request.json['imagen']
    producto = Producto(codigo = codigo,categoria = categoria,descripcion = descripcion,
                        precio = precio,cantidad = cantidad, imagen = imagen)
    db.session.add(producto)
    db.session.commit()
    
    return "producto agregado"

#traer todos los productos
@mainP.route('/productos',methods=['GET'])
def get_productos():
    productos=Producto.query.order_by(Producto.codigo.asc()).all()  #era id producto.id.asc
    prod_lista=[]
    for prod in productos:
        prod_lista.append(format_producto(prod))
    return {'productos':prod_lista}

#traer un producto
@mainP.route('/productos/<codigo>',methods=['GET'])  #era id
def get_producto(codigo):
    producto = Producto.query.filter_by(codigo=codigo).one()
    formatted_producto = format_producto(producto)
    return {'event':formatted_producto}

#borrar un producto
@mainP.route('/productos/<codigo>',methods=['DELETE']) #era id
def delete_producto(codigo):
    producto = Producto.query.filter_by(codigo=codigo).one()
    db.session.delete(producto)
    db.session.commit()
    #return 'Event deleted!'
    return f'Producto (codigo: {codigo}) Eliminado!'

#editar producto
@mainP.route('/productos/<codigo>',methods=['PUT']) #era id
def update_producto(codigo):
    producto=Producto.query.filter_by(codigo=codigo)
    #id=request.json['description']
    categoria = request.json['categoria']
    descripcion = request.json['descripcion']
    precio = request.json['precio']
    cantidad = request.json['cantidad']
    imagen = request.json['imagen']
    producto.update(dict(categoria=categoria,descripcion=descripcion,precio=precio,cantidad=cantidad,imagen=imagen))
    db.session.commit()
    return {'event':format_producto(producto.one())}