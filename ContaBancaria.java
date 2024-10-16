  class ContaBancaria {
      private int numeroDaConta;
      private double saldo;

      public ContaBancaria(int numeroDaConta) {
          this.numeroDaConta = numeroDaConta;
          this.saldo = 0;
      }

      public void depositar(double valor) {
          if (valor <= 0) {
              throw new IllegalArgumentException("Valor de depósito deve ser positivo.");
          }
          saldo += valor;
      }

      public void sacar(double valor) {
          if (valor > saldo) {
              throw new IllegalArgumentException("Saldo insuficiente.");
          }
          saldo -= valor;
      }

      public void verSaldo() {
          System.out.println("Saldo atual: " + saldo);
      }

      public static void main(String[] args) {
          ContaBancaria conta = new ContaBancaria(12345);
          conta.depositar(500);
          conta.verSaldo();
          conta.sacar(200);
          conta.verSaldo();
      }
  }