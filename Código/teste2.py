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
