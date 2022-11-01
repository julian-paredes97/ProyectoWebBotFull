#from app import db
#from ModeloProducto import Producto
from utils.db import db


class Orden(db.Model):  #carrito
    
    __tablename__="Ordenes"

    idOrden=db.Column(db.Integer, primary_key=True)
    idProducto=db.Column(db.Integer)
    cantidadC=db.Column(db.Integer)
    precioxCantidad=db.Column(db.Integer) 
    
    def __repr__(self):
        return f"Orden: {self.idOrden,self.idProducto,self.cantidadC,self.precioxCantidad}"
    
    def __init__(self,idOrden,idProducto,cantidadC,precioxCantidad):
        self.idOrden=idOrden
        self.idProducto=idProducto
        self.cantidadC=cantidadC
        self.precioxCantidad=precioxCantidad
   
def format_orden(orden):
    return{
        "idOrden":orden.idOrden,
        "idProducto":orden.idProducto,
        "cantidadC":orden.cantidadC,
        "precioxCantidad":orden.precioxCantidad
    }