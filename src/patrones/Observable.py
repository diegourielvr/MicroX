class Observable:
    def __init__(self):
        self.observers = list()

    def suscribirse(self, observer):
        self.observers.append(observer)

    def desuscribirse(self, observer):
        self.observers.remove(observer)

    def notificar(self):
        for obs in self.observers:
            obs.actualizar()