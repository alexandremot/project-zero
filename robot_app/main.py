from classes.executor import Executor
from enums.screens_references import ScreensReferences as option

class App:
    def __init__(self):
        self.executor = Executor()

    def acessa_tela_login(self):
        self.executor.acessa_tela(option.TELA_INICIAL)

    def seleciona_agencia_e_conta(self):
        self.executor.acessa_tela(option.TELA_ESCOLHA_CPF_AGENCIA)

    def clica_em_agencia(self):
        self.executor.acessa_tela(option.ENTRE_COM_AGENCA_E_CONTA)
        self.executor.envia_texto("1234")  # Substitua "1234" pelo texto desejado

    def run(self):
        self.acessa_tela_login()
        self.seleciona_agencia_e_conta()
        self.clica_em_agencia()
        

def main():
    app = App()
    app.run()

if __name__ == "__main__":
    main()
