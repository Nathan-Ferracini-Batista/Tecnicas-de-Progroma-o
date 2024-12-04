from datetime import datetime, timedelta

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


class ContaEspecial(ContaComum):
    def __init__(self, numero_conta, senha, limite):
        super().__init__(numero_conta, senha)
        self.limite = limite

    def saque(self, valor, senha):
        if self.situacao == 1:
            if self.conferir_senha(senha):
                if self.saldo + self.limite >= valor:
                    self.saldo -= valor
                    print(f"Saque de {valor} realizado com sucesso. Saldo atual: {self.saldo}")
                else:
                    print("Saldo insuficiente, mesmo considerando o limite.")
            else:
                print("Senha incorreta.")
        else:
            print("Conta encerrada. Não é possível realizar saque.")


class ContaPoupanca(ContaComum):
    def __init__(self, numero_conta, senha, data_aniversario):
        super().__init__(numero_conta, senha)
        self.data_aniversario = data_aniversario

    def creditar_juros(self):
        if datetime.now().date() == self.data_aniversario:
            self.saldo *= 1.01
            print(f"Juros creditados. Saldo atual: {self.saldo}")


conta_comum = ContaComum(numero_conta=123456, senha="minhasenha")
conta_comum.deposito(1000)
conta_comum.saque(500, "minhasenha")
conta_comum.saque(600, "senhaerrada")
conta_comum.encerrar_conta()
conta_comum.deposito(200)
conta_comum.saque(100, "minhasenha")


conta_especial = ContaEspecial(numero_conta=654321, senha="outrasenha", limite=500)
conta_especial.deposito(1000)
conta_especial.saque(1200, "outrasenha")
conta_especial.saque(1600, "outrasenha")
conta_especial.encerrar_conta()


data_aniversario = (datetime.now() + timedelta(days=1)).date() 
conta_poupanca = ContaPoupanca(numero_conta=789012, senha="senhaespecial", data_aniversario=data_aniversario)
conta_poupanca.deposito(1000)
conta_poupanca.creditar_juros()  
print("Esperando até o aniversário para creditar os juros...")
conta_poupanca.data_aniversario = datetime.now().date() 
conta_poupanca.creditar_juros()
