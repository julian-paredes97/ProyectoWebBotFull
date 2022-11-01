#from app import db
from modelos.ModeloOrden import Orden
from utils.db import db

#from modelos.ModeloProducto import Producto , format_producto
from flask import request, Blueprint

mainO = Blueprint('orden_blueprint', __name__)


@mainO.route('/orden')
def index():
    return "WEEEEEEEE puto"

#crear una orden
@mainO.route('/ordenes',methods=['POST'])
def crear_orden():
    idOrden = request.json['idOrden']
    idProducto = request.json['idProducto']
    cantidadC= request.json['cantidadC']
    precioxCantidad= request.json['precioxCantidad']
    orden = Orden(idOrden=idOrden,idProducto=idProducto,cantidadC=cantidadC,precioxCantidad=precioxCantidad)
    db.session.add(orden)
    db.session.commit()
    
    return "orden agregada"