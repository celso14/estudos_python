class Sistema:

    def __init__(self) -> None:
        self.__email="empresa.42@email.com"
        self.__nome="Empresa 42"
        self.__destinatarios=[]
        self.__conteudo=''
    
    def email_text(self, titulo: str, texto: str)->None:
        self.__conteudo = f'{titulo}\n {texto} \n   {self.__nome}'
    
    def destinos(self, *lista):
        if(type(lista) is tuple):
            for i in lista:
                if(type(i) is str):
                    self.__destinatarios.append(i)
        else:
            print('E-mails de destinátarios inválidos!')
        
    def send_email(self):
        print(self.__conteudo)
        print(f'De: {self.__email}')
        print(f'Para: {self.__destinatarios}')
        print('E-Mail enviado!')
