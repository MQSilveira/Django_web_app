from django import forms
from django.core.mail.message import EmailMessage


class ContatoForm(forms.Form):
    nome = forms.CharField(label='Nome', max_length=100)
    email = forms.CharField(label='Email', max_length=100)
    assunto = forms.CharField(label='Assunto', max_length=120)
    mensagem = forms.CharField(label='Mensagem', widget=forms.Textarea())
    
    def send_mail(self):
        nome = self.cleaned_data['nome']
        email = self.cleaned_data['email']
        assunto = self.cleaned_data['assunto']
        mensagem = self.cleaned_data['mensagem']
        
        conteudo = f'Conteúdo do e-mail\npagina contato: \n{nome} \n{email} \n{assunto} \n{mensagem}'
        
        mail = EmailMessage(
            subject = "Contato via pagina web",
            to = ["email_que_ira_receber@podeservarios.com"],
            body = conteudo,
            from_email = 'contato@dominio.com',
            headers = {'Reply-To': email},
        )
        
        mail.send()



