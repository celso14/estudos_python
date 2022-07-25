from random import choice

class Game:
    
    def __init__(self) -> None:
        self.__p1=['PEDRA', 'PAPEL', 'TESOURA']
        self.__p2=['PEDRA', 'PAPEL', 'TESOURA']
        self.__placar_p1=0
        self.__placar_p2=0

    def jogada(self):
        for i in range(0,3):
            jogada1=choice(self.__p1)
            jogada2=choice(self.__p2)
            if(jogada1 == jogada2):
                print(f'EMPATE - P1 {jogada1} x {jogada2} P2')
                print(self.__get_placar())
            elif((jogada1 == 'PEDRA' and (jogada2) == 'TESOURA') or (jogada1 == 'PAPEL' and (jogada2) == 'PEDRA') or (jogada1 == 'TESOURA' and (jogada2) == 'PAPEL')):
                print(self.__placar(1, jogada1, jogada2))
                print(self.__get_placar())
            elif((jogada2 == 'PEDRA' and (jogada2) == 'TESOURA') or (jogada2 == 'PAPEL' and (jogada2) == 'PEDRA') or (jogada2 == 'TESOURA' and (jogada2) == 'PAPEL')):
                print(self.__placar(2, jogada1, jogada2))
                print(self.__get_placar())
            pass

    def __placar(self, p1: int, jogada1: str, jogada2: str) -> None:
        if(p1 == 1):
            self.__placar_p1 +=1
            return f'Jogador 1 Venceu - P1 {jogada1} X {jogada2} P2'
        else:
            self.__placar_p2 +=1
            return f'Jogador 2 Venceu - P2 {jogada2} X {jogada1} P1'
    
    def __get_placar(self) -> None:
        return f'Player 1 {self.__placar_p1} X {self.__placar_p2} Player 2'
        
