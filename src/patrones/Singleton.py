def singleton(cls):
    instancias = dict()

    def wrap(*args, **kwargs):
        if cls not in instancias:
            instancias[cls] = cls(*args, **kwargs)
        return instancias[cls]

    return wrap