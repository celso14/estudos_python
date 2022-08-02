from myclass import Sistema

email = Sistema()
email.destinos('celso@email.com')
email.email_text('Software', 'Precisamos de um prazo maior para entregar o software, se não pode apresentar muitos bugs')
email.send_email()



