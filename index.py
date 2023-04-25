#INTRODUÇÃO DO PROGRAMA - Armazenando respostas com inputs 

print("Seja bem vindo a nossa plataforma! Deseja fazer o seu cadastro?")
respostaCadastro = input()
if respostaCadastro != "nao":
    print("Para fazer o seu cadastro, insira os seus dados para prosseguir.\nDigite seu novo usuario")
    nomeUsuario = input()
    print("Agora, digite a sua nova senha numerica.")
    senhaUsuario = int(input())
else:
    print("Ok! Programa encerrado!")

print("Cadastro feito! Voce deseja fazer o seu login?")
respostaLogin = input()

if respostaLogin == "sim":
    print("Por favor, insira o seu nome de usuario.")
    nomeUsuario = input()
    print("Agora, digite a sua senha numerica.")
    senhaUsuario = int(input())

    print(f"Seja bem vindo ao seu perfil, {nomeUsuario}.")
else:
    print(f"Ok! Programa encerrado. Ate mais, {nomeUsuario}!")


#CONSTRUINDO UMA FUNÇÃO DE MENU COM LOOPS:

