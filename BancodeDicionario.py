# Dicionário global para armazenar os usuários
banco_usuarios = []

# Função para cadastrar um usuário de maneira flexível
def cadastrar_usuario(campos_obrigatorios):
    usuario = {}
    
    # Preencha os campos obrigatórios
    for campo in campos_obrigatorios:
        valor = input(f'Digite o valor para o campo "{campo}": ')
        usuario[campo] = valor
    
    # Permitir ao usuário adicionar campos extras
    while True:
        campo_extra = input('Digite um campo extra (ou "sair" para finalizar): ')
        if campo_extra.lower() == 'sair':
            break
        valor_extra = input(f'Digite o valor para o campo extra "{campo_extra}": ')
        usuario[campo_extra] = valor_extra
    
    banco_usuarios.append(usuario)
    print('Usuário cadastrado com sucesso!')

# Função para imprimir usuários com várias opções de filtragem
def imprimir_usuarios(*args, **kwargs):
    if not args and not kwargs:
        # Imprimir todos os usuários com todas as informações
        for usuario in banco_usuarios:
            print(usuario)
    else:
        # Filtrar e imprimir com base nos argumentos passados
        for usuario in banco_usuarios:
            imprimir = True
            if args:
                if usuario['nome'] not in args:
                    imprimir = False
            if kwargs:
                for campo, valor in kwargs.items():
                    if campo not in usuario or usuario[campo] != valor:
                        imprimir = False
            if imprimir:
                print(usuario)

# Função principal do programa
def main():
    campos_obrigatorios = []
    
    # Solicitar ao usuário os campos obrigatórios
    while True:
        campo = input('Digite um campo obrigatório (ou "sair" para finalizar): ')
        if campo.lower() == 'sair':
            break
        campos_obrigatorios.append(campo)
    
    while True:
        print('\nMenu:')
        print('1 - Cadastrar usuário')
        print('2 - Imprimir usuários')
        print('0 - Encerrar')
        
        escolha = input('Digite a opção desejada: ')
        
        if escolha == '1':
            cadastrar_usuario(campos_obrigatorios)
        elif escolha == '2':
            imprimir_opcao = input('1 - Imprimir todos\n2 - Filtrar por nomes\n3 - Filtrar por campos\n4 - Filtrar por nomes e campos\nDigite a opção desejada: ')
            if imprimir_opcao == '1':
                imprimir_usuarios()
            elif imprimir_opcao == '2':
                nomes = input('Digite os nomes para filtrar (separados por vírgula): ').split(',')
                imprimir_usuarios(*nomes)
            elif imprimir_opcao == '3':
                campos = input('Digite os campos para filtrar (separados por vírgula): ').split(',')
                imprimir_usuarios(**{campo: None for campo in campos})
            elif imprimir_opcao == '4':
                nomes = input('Digite os nomes para filtrar (separados por vírgula): ').split(',')
                campos = input('Digite os campos para filtrar (separados por vírgula): ').split(',')
                imprimir_usuarios(*nomes, **{campo: None for campo in campos})
        elif escolha == '0':
            break
        else:
            print('Opção inválida. Tente novamente.')

if __name__ == "__main__":
    main()