alunos = []

def exibir_menu():
    print("-----------SISTEMA DE CADASTRO DE ALUNOS-----------")
    print("1. Adicionar aluno")
    print("2. Listar todos os alunos")
    print("3. Buscar aluno pelo nome")
    print("4. Remover aluno")
    print("5. Mostrar média geral das notas")
    print("6. Sair")
    print("---------------------------------------------------")
    
def exibir_aluno(aluno):
    return (
        f"Nome: {aluno['nome']}\n"
        f"Idade: {aluno['idade']} anos\n"
        f"Nota: {aluno['nota']:.1f}"
    )
    
def ler_nome():
    while True:
        nome = input("Digite o nome do aluno: ").strip()
        if nome:
            return nome
        print("O nome não pode ficar vazio.")

def ler_idade():
    while True:
        texto = input("Digite a idade do aluno: ").strip()

        try:
            idade = int(texto)
        except ValueError:
            print("A idade deve ser um número inteiro.")
            continue

        if idade > 0:
            return idade
        print("A idade deve ser maior que 0.")
    
def ler_nota():
     while True:
            texto = input("Digite a nota do aluno: ").strip().replace(",", ".")
            try:
                nota = float(texto)
            except ValueError:
                print("A nota deve ser um número.")
                continue
            if 0 <= nota <= 10:
             return nota
            print("A nota deve estar entre 0 e 10.")
                
def adicionar_aluno():
    aluno = {
            "nome": ler_nome(),
            "idade": ler_idade(),
            "nota": ler_nota(),
        }
    alunos.append(aluno)
    print("Aluno cadastrado com sucesso!")

def achar_aluno(nome):
    for aluno in alunos:
        if aluno["nome"].lower() == nome.lower():
            return aluno
    return None

def sem_alunos():
    if len(alunos) == 0:
        print("Nenhum aluno cadastrado.")
        return True
    return False

def listar_alunos():
    if sem_alunos():
        return
    print("------------------Lista de Alunos------------------")
    for aluno in alunos:
            print(exibir_aluno(aluno))
            print("---------------------------------------------------")

def buscar_aluno():
    if sem_alunos():
        return
    nome_buscar = input("Digite o nome do aluno que deseja buscar: ").strip()
    aluno = achar_aluno(nome_buscar)
    if aluno is None:
        print("Aluno não encontrado.")
        return
    print("\nAluno encontrado!")
    print(exibir_aluno(aluno))

def remover_aluno():
    if sem_alunos():
        return

    nome_remover = input("Digite o nome do aluno que deseja remover: ").strip()
    aluno = achar_aluno(nome_remover)

    if aluno is None:
        print("Aluno não encontrado.")
        return

    alunos.remove(aluno)
    print("Aluno removido com sucesso!")

def mostrar_media():
    if sem_alunos():
        return
    media = sum(aluno["nota"] for aluno in alunos) / len(alunos)
    print(f"A média geral é {media:.2f}")

def main():
 while True:
    exibir_menu()
    opcao = input("Digite uma opção: ").strip()
    print("---------------------------------------------------")

    if opcao == "1":
        adicionar_aluno()

    elif opcao == "2":
        listar_alunos()

    elif opcao == "3":
        buscar_aluno()

    elif opcao == "4":
        remover_aluno()

    elif opcao == "5":
        mostrar_media()

    elif opcao == "6":
        print("Saindo......")
        break

    else:
        print("Opção inválida. Digite uma opção de 1 a 6.")
        
if __name__ == "__main__":
    main()