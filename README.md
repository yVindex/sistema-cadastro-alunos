# Sistema de Cadastro de Alunos

Sistema de cadastro de alunos em Python, executado no terminal. Nesta versão, os dados ficam guardados em memória (lista de dicionários) e são perdidos quando o programa é fechado.

## Integrantes

| Nome | Matrícula |
|------|-----------|
| Guilherme Barbosa da Silva França | 01879072 |

<!-- Se o trabalho for em grupo, adicione uma linha por integrante. Se for individual, pode apagar este comentário. -->

## Funcionalidades

1. **Adicionar aluno:** cadastra nome, idade e nota, com validação das entradas.
2. **Listar todos os alunos:** mostra nome, idade e nota de cada aluno cadastrado.
3. **Buscar aluno pelo nome:** busca ignorando maiúsculas e minúsculas.
4. **Remover aluno:** remove o aluno pelo nome.
5. **Mostrar média geral das notas:** calcula a média de todos os alunos.
6. **Sair:** encerra o programa.

## Validações

- O nome não pode ficar vazio (espaços no início e no fim são ignorados).
- A idade deve ser um número inteiro maior que 0.
- A nota deve ser um número entre 0 e 10 (aceita vírgula ou ponto, como `8,5` ou `8.5`).

## Como executar

É necessário ter o Python 3 instalado. No terminal, dentro da pasta do projeto:

```bash
python sistema_cadastro_alunos.py
```

## Estrutura do código

- `exibir_menu`, `exibir_aluno`: exibição de informações.
- `ler_nome`, `ler_idade`, `ler_nota`: leitura e validação dos dados digitados.
- `adicionar_aluno`, `listar_alunos`, `buscar_aluno`, `remover_aluno`, `mostrar_media`: funcionalidades do menu.
- `achar_aluno`, `sem_alunos`: funções auxiliares para evitar código repetido.
- `main`: menu principal, que repete até o usuário escolher sair.

## Tecnologias

- Python 3
>>>>>>> 7b39496 (readme adicionado)
