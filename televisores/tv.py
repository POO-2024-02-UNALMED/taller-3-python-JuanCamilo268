class TV:
    _numTV = 0
    def __init__(self, _marca, _estado, _canal = 1, _volumen = 1, _precio = 500, _control = 0):
        self._marca = _marca
        self._estado = _estado
        self._canal = _canal
        self._volumen = _volumen
        self._precio = _precio
        self._control = _control
    def setMarca(marca):
        self._marca = marca
   
    def getMarca():
        return self._marca
    
    def setCanal(canal):
        self._canal = canal
   
    def getCanal():
        return self._canal
    
    def setPrecio(precio):
        self._precio = precio
   
    def getPrecio():
        return self._precio
    
    def setVolumen(volumen):
        self._volumen = volumen
   
    def getVolumen():
        return self._volumen
    
    def setControl(control):
        self._control = control
   
    def getNombre():
        return self._control
    
    def setNumTv(num):
        TV._numTV = num