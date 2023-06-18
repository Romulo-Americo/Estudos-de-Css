

def inf_de_cargo(cargo):
 
  if cargo == 1:#Cargo administrativo
    print('O cargo selecionado foi administrativo')
    print('Salário: R$ 1.400.00 ')
    print('-'*35)
    print('VERIFICAÇÃO DE FREQUENICA ADMINISTRATIVOS')
    print('Rafael', '.'*20, 'falta: XX', '.'*5, 'desconto: R$ XX.XX,XX')
    print('Guilherme','.'*20, 'falta: XX', '.'*5, 'desconto: R$ XX.XX,XX')
    print('Caio', '.'*20, 'falta: XX', '.'*5, 'desconto: R$ XX.XX,XX')
       
  elif cargo == 2:#Cargo de gerente
     print('O cargo selecionado foi gerente')
     print('Salário: R$ 11.000.00')
     print('-'*35)
     print('VERIFICAÇÃO DE FREQUENICA ADMINISTRATIVOS')
     print('Debora', '.'*20, 'falta: XX', '.'*5, 'desconto: R$ XX.XX,XX')
     print('Gustavo', '.'*20, 'falta: XX', '.'*5, 'desconto: R$ XX.XX,XX')
     print('Manoel', '.'*20, 'falta: XX', '.'*5, 'desconto: R$ XX.XX,XX')

  elif cargo == 3:#Cargo de estagiário
     print('O cargo selecionado foi estagiário')
     print('Salário: R$ 1000.00')
     print('-'*35)
     print('VERIFICAÇÃO DE FREQUENICA ADMINISTRATIVOS')
     print('Rafael', '.'*20, 'falta: XX', '.'*5, 'desconto: R$ XX.XX,XX')
     print('Leonardo', '.'*20, 'falta: XX', '.'*5, 'desconto: R$ XX.XX,XX')
     print('Luana', '.'*20, 'falta: XX', '.'*5, 'desconto: R$ XX.XX,XX')

  elif cargo == 0:
     print('Quadro geral detalhado')
     print('Admnistrativo')
     print('Rafael', '.'*20, 'falta: XX', '.'*5, 'desconto: R$ XX.XX,XX')
     print('Guilherme','.'*20, 'falta: XX', '.'*5, 'desconto: R$ XX.XX,XX')
     print('Caio', '.'*20, 'falta: XX', '.'*5, 'desconto: R$ XX.XX,XX')
     print('')
     print('Gerência')
     print('Debora', '.'*20, 'falta: XX', '.'*5, 'desconto: R$ XX.XX,XX')
     print('Gustavo', '.'*20, 'falta: XX', '.'*5, 'desconto: R$ XX.XX,XX')
     print('Manoel', '.'*20, 'falta: XX', '.'*5, 'desconto: R$ XX.XX,XX')
     print('')
     print('Estágio')
     print('Rafael', '.'*20, 'falta: XX', '.'*5, 'desconto: R$ XX.XX,XX')
     print('Leonardo', '.'*20, 'falta: XX', '.'*5, 'desconto: R$ XX.XX,XX')
     print('Luana', '.'*20, 'falta: XX', '.'*5, 'desconto: R$ XX.XX,XX')

def envio_de_email(notificador): 
   import smtplib, ssl

   # Configurar as informações do remetente
   remetente_email = "romuloamericofurtadosilva@gmail.com"
   remetente_senha = "rfgmixgjlddqneav"

   # Configurar as informações do destinatário
   destinatario_email = "romuloamericofurtadosilva@gmail.com"

   # Configurar o servidor SMTP do Gmail e a porta de conexão segura
   smtp_server = "smtp.gmail.com"
   port = 465

   # Crie um objeto de conexão segura do SSL/TLS
   context = ssl.create_default_context()

   # Crie o objeto SMTP e faça login na conta do Gmail
   with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
      server.login(remetente_email, remetente_senha)

      # Crie a mensagem de e-mail
      assunto = "Assunto do e-mail"
      corpo = "teste"
      mensagem = f"Assunto: {assunto}\n\n{corpo}"

      # Envie o e-mail
      server.sendmail(remetente_email, destinatario_email, mensagem)

   print('Notificação enviada com sucesso')