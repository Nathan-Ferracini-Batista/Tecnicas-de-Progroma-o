  import java.util.Scanner;

  class Pessoa {
      private double altura;
      private double peso;

      public void setAltura(double altura) {
          this.altura = altura;
      }

      public void setPeso(double peso) {
          if (peso <= 0 || peso > 200) {
              throw new IllegalArgumentException("Peso inválido, digite novamente.");
          }
          this.peso = peso;
      }

      public double getAltura() {
          return altura;
      }

      public double getPeso() {
          return peso;
      }

      public boolean calculeIMC() {
          double imc = peso / (altura * altura);
          return imc >= 18.5 && imc <= 24.9;
      }
  }

  public class Main {
      public static void main(String[] args) {
          Scanner scanner = new Scanner(System.in);
          Pessoa pessoa = new Pessoa();
          boolean running = true;

          while (running) {
              System.out.println("Menu:");
              System.out.println("1. Cadastrar pessoa");
              System.out.println("2. Sair");
              System.out.print("Escolha uma opção: ");
              int opcao = scanner.nextInt();

              switch (opcao) {
                  case 1:
                      try {
                          System.out.print("Digite a altura (em metros): ");
                          double altura = scanner.nextDouble();
                          pessoa.setAltura(altura);

                          System.out.print("Digite o peso (em kg): ");
                          double peso = scanner.nextDouble();
                          pessoa.setPeso(peso);

                          if (pessoa.calculeIMC()) {
                              System.out.println("PESO_NORMAL");
                          } else {
                              System.out.println("SOBREPESO");
                          }
                      } catch (IllegalArgumentException e) {
                          System.out.println(e.getMessage());
                      }
                      break;

                  case 2:
                      running = false;
                      break;

                  default:
                      System.out.println("Opção inválida, tente novamente.");
              }
          }
          scanner.close();
      