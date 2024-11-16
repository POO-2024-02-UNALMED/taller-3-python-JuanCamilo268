class TV:
    _numTV = 0
    def __init__(self, _marca, _estado, _canal = 1, _volumen = 1, _precio = 500, _control = 0):
        self._marca = _marca
        self._estado = _estado
        self._canal = _canal
        self._volumen = _volumen
        self._precio = _precio
        self._control = _control
        TV._numTV += 1
    def setMarca(marca):
        self._marca = marca
   
    def getMarca():
        return self._marca
    
    def setCanal(canal):
        if self._estado == True:
            self._canal = canal
   
    def getCanal():
        return self._canal
    
    def setPrecio(precio):
        self._precio = precio
   
    def getPrecio():
        return self._precio
    
    def setVolumen(volumen):
        if self._estado == True:
            self._volumen = volumen
   
    def getVolumen():
        return self._volumen
    
    def setControl(control):
        self._control = control
   
    def getNombre():
        return self._control
    
    def setNumTv(num):
        TV._numTV = num
    
    def getNumTv():
        return TV._numTV

    def turnOff():
        if self._estado == True:
            self._estado = False
    
    def turnOn():
        if self._estado == False:
            self._estado = True
    
    def getEstado():
        return self._estado
    
    def canalUp():
        if self._estado ==True:
            if self._canal < 120:
                self._canal += 1
    
    def canalDown():
        if self._estado == True:
            if self._canal > 1:
                self.canal -= 1
    
    def volumenUp():
        if self.estado == True:
            if self._volumen < 7:
                self._volumen += 1
    
    def volumenDown():
        if self._volumen == True:
            if self._volumen > 0:
                self._volumen -= 1
