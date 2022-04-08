class Modo():
    def __init__(self,t_max_juego=600,max_preg=1,num_preg=10,num_jug=1) -> None:
        self.__t_max_juego = t_max_juego
        self.__max_preg = max_preg
        self.__num_preg = num_preg
        self.__num_jug = num_jug

    @property
    def t_max_juego(self):
        return self.__t_max_juego
    @property
    def max_preg(self):
        return self.__max_preg
    @property
    def num_preg(self):
        return self.__num_preg
    @property
    def num_jug(self):
        return self.__num_jug