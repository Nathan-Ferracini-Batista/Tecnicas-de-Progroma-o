from datetime import datetime

class ContaComum:
    def __init__(self, numero_conta, senha):
        self.numero_conta = numero_conta
        self.data_abertura = datetime.now()
        self.data_encerramento = None
        self.situacao = 1  # 1=ativa, 2=encerrada
        self.senha = senha
        self.saldo = 0.0

    def deposito(self, valor):
        if self.situacao == 1:
            self.saldo += valor
            print(f"Depósito de {valor} realizado com sucesso. Saldo atual: {self.saldo}")
        else:
            print("Conta encerrada. Não é possível realizar depósito.")

    def saque(self, valor, senha):
        if self.situacao == 1:
            if self.conferir_senha(senha):
                if self.saldo >= valor:
                    self.saldo -= valor
                    print(f"Saque de {valor} realizado com sucesso. Saldo atual: {self.saldo}")
                else:
                    print("Saldo insuficiente.")
            else:
                print("Senha incorreta.")
        else:
            print("Conta encerrada. Não é possível realizar saque.")

    def conferir_senha(self, senha):
        return self.senha == senha

    def abrir_conta(self):
        self.situacao = 1
        self.data_abertura = datetime.now()
        self.data_encerramento = None
        print("Conta aberta com sucesso.")

    def encerrar_conta(self):
        self.situacao = 2
        self.data_encerramento = datetime.now()
        print("Conta encerrada com sucesso.")

    def data_de_abertura(self):
        return self.data_abertura

    def data_de_encerramento(self):
        return self.data_encerramento

conta = ContaComum(numero_conta=123456, senha="minhasenha")
conta.deposito(1000)
conta.saque(500, "minhasenha")
conta.saque(600, "senhaerrada")
conta.encerrar_conta()
conta.deposito(200)
conta.saque(100, "minhasenha")
