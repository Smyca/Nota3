class Carrito :
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carrito = self.session.get("carrito")
        if not carrito:
            self.session["carrito"] = {}
            self.carrito = self.session["carrito"]
        else:
            self.carrito = carrito

    def agregar (self, productos):
        id = str(productos.id)
        if id not in self.carrito.keys():
            self.carrito[id] = {
                "producto_id" : productos.id,
                "nombre" : productos.nombre,
                "acumulado" : productos.precio,
                "descripcion" : productos.descripcion,
                "imagen" : productos.imagen,
                "cantidad" : 1
            }
        else: 
            for key, value in self.carrito.items():
                if key == str(productos.id):
                    value["cantidad"] = value["cantidad"] + 1
                    self.carrito[id]["acumulado"] += productos.precio
            
        self.guardar_carrito()
    
    def guardar_carrito(self):
        self.session["carrito"] = self.carrito
        self.session.modified = True
        
    def eliminar (self, productos):
        id = str(productos.id)
        if id in self.carrito:
            del self.carrito[id]
            self.guardar_carrito()
        
    def restar (self, productos):
        for key, value in list(self.carrito.items()):
            if key == str(productos.id):
                    value["cantidad"] = value["cantidad"] - 1
                    if value["cantidad"] < 1:
                        self.eliminar(productos)
                    else:
                        self.guardar_carrito()
    
    def limpiar (self):
        self.session["carrito"] = {}
        self.session.modified = True