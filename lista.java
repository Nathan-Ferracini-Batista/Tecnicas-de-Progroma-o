  import java.util.ArrayList;
  import java.util.Scanner;

  public class ListaDeNomes {
      public static void main(String[] args) {
          ArrayList<String> lista = new ArrayList<>();
          Scanner scanner = new Scanner(System.in);
          boolean continuar = true;

          while (continuar) {
              System.out.println("Escolha uma opção:");
              System.out.println("1. Inserir nome");
              System.out.println("2. Apagar nome");
              System.out.println("3. Consultar tamanho da lista");
              System.out.println("4. Pesquisar nome");
              System.out.println("5. Imprimir lista toda");
              System.out.println("6. Limpar lista");
              System.out.println("7. Encerrar programa");
              int opcao = scanner.nextInt();
              scanner.nextLine();  // Limpar o buffer

              switch (opcao) {
                  case 1:
                      System.out.print("Digite o nome a ser inserido: ");
                      String nomeInserir = scanner.nextLine();
                      lista.add(nomeInserir);
                      break;
                  case 2:
                      System.out.print("Digite o nome a ser apagado: ");
                      String nomeApagar = scanner.nextLine();
                      lista.remove(nomeApagar);
                      break;
                  case 3:
                      System.out.println("Tamanho da lista: " + lista.size());
                      break;
                  case 4:
                      System.out.print("Digite o nome a ser pesquisado: ");
                      String nomePesquisar = scanner.nextLine();
                      if (lista.contains(nomePesquisar)) {
                          System.out.println(nomePesquisar + " está na lista.");
                      } else {
                          System.out.println(nomePesquisar + " não está na lista.");
                      }
                      break;
                  case 5:
                      System.out.println("Lista de nomes:");
                      for (String nome : lista) {
                          System.out.println(nome);
                      }
                      break;
                  case 6:
                      lista.clear();
                      System.out.println("Lista limpa.");
                      break;
                  case 7:
                      continuar = false;
                      break;
                  default:
                      System.out.println("Opção inválida. Tente novamente.");
              }
          }

          scanner.close();
      }
