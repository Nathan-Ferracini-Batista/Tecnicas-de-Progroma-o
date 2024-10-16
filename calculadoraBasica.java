  class Calculadora {
      public int somar(int a, int b) {
          return a + b;
      }

      public int subtrair(int a, int b) {
          return a - b;
      }

      public int multiplicar(int a, int b) {
          return a * b;
      }

      public int dividir(int a, int b) {
          if (b == 0) {
              throw new IllegalArgumentException("Divisão por zero não permitida.");
          }
          return a / b;
      }

      public static void main(String[] args) {
          Calculadora calc = new Calculadora();
          System.out.println("Soma: " + calc.somar(10, 5));
          System.out.println("Subtração: " + calc.subtrair(10, 5));
          System.out.println("Multiplicação: " + calc.multiplicar(10, 5));
          System.out.println("Divisão: " + calc.dividir(10, 5));
      }
