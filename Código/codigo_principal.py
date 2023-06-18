import inf_de_dados

while True:
    print(' [0]Quadro Geral\n [1]Administrativo\n [2]Gerente \n [3]Estgiário')

    informacao_de_funcionario = int(input('Informe o cargo para ver o detalhamento: '))

    if informacao_de_funcionario!=0 and informacao_de_funcionario != 1 and informacao_de_funcionario != 2 and informacao_de_funcionario != 3:
        print("\033[31mDigite um valor válido\033[m")    
    else:
        break

inf_de_dados.inf_de_cargo(informacao_de_funcionario)
print('')

if informacao_de_funcionario == 0:
    funcionario_notificado = input('Informe o(s) nome(s) do(s) funcionário(s) para enviar a notificação por e-mail:').upper()
    
    inf_de_dados.envio_de_email(funcionario_notificado)
    
    