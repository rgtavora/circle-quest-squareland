class GameComponentError(Exception):
    def __init__(self, msg):
        self.msg = msg

class Platform:
    velocidade_maxima = 10 #pixel por segundo no módulo do vetor
    def __init__(self, width, height, *positions):
        if (len(positions) == 0):
            print('erro, forneça pela menos uma posição para a plataforma')
            raise GameComponentError('forneça pela menos uma posição para a plataforma')
        self.positions = positions
        self.position = [positions[0][0], positions[0][1]]
        self.movable = len(positions) > 1
        self.pos_atual = 0
        self.direcao_mudou = True
        self.definir_vetor_direcao()


    def definir_vetor_direcao(self):
        if (self.direcao_mudou):
            pass

class Level:
    def __init__(self):
        pass