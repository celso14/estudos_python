class Viagem:

    def viajar(self, viagem: str):
        try:
            if(viagem.upper() == "NITEROI"):
                print(self.__atividade_niteroi())
            elif(viagem.upper() == 'BELO HORIZONTE'):
                print(self.__atividade_bh())
            elif(viagem.upper() == 'FORTALEZA'):
                print(self.__atividade_fortaleza())
            else:
                print('Nome de cidade inválido, tente: \n -> Niteroi \n -> Belo Horizonte \n -> Fortaleza')
        except:
            print('Nome de cidade inválido, tente: \n -> Niteroi \n -> Belo Horizonte \n -> Fortaleza')
    
    def __atividade_niteroi(self):
        return 'Ir para a praia'
    
    def __atividade_bh(self):
        return 'Visitar Inhotim'

    def __atividade_fortaleza(self):
        return 'Ir para o Beach Park'