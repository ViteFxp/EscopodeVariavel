# 🌍 Demonstração de Escopo de Variáveis (Global e Local) em Python

Este script Python (`escopo_demonstracao.py`) fornece uma demonstração visual clara da diferença entre variáveis globais e variáveis locais, incluindo o comportamento de "mascaramento" de nomes e o uso correto da palavra-chave `global`.

## 🔬 O que o código demonstra:

1.  **Variável Global:** Definida fora de qualquer função e acessível para leitura em todo o código.
2.  **Variável Local:** Definida dentro de uma função e só existe enquanto essa função está em execução.
3.  **Isolamento de Escopo:** O código mostra que uma tentativa de acessar uma variável local fora da sua função resulta em um `NameError`.
4.  **Mascaramento (Shadowing):** Demonstra que atribuir um valor a uma variável dentro de uma função (que já existe globalmente) cria uma nova variável **local** com o mesmo nome, sem afetar a global.
5.  **Modificação Global:** Ilustra o uso da palavra-chave `global` para realmente modificar a variável global de dentro de uma função.

## 🚀 Como Executar

Para ver a demonstração:

1.  Certifique-se de ter o Python instalado.
2.  Salve o código acima como `escopo_demonstracao.py`.
3.  Execute no seu terminal:

    ```bash
    python escopo_demonstracao.py
    ```

## 💡 Saída (Visualização)

A saída do programa é a chave da demonstração, mostrando claramente onde cada variável é visível e onde os erros de escopo ocorrem: