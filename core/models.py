from django.db import models
from stdimage.models import StdImageField
import uuid


class Base(models.Model):
    criados = models.DateField('Criação', auto_now_add=True)
    modificado = models.DateField('Atualização', auto_now=True)

    class Meta:
        abstract = True
        

class Cargo(Base):
    cargo = models.CharField('Cargo', max_length=100)

    class Meta:
        verbose_name = 'Cargo'
        verbose_name_plural = 'Cargos'
        
    def __str__(self):
        return self.cargo


def get_file_path(_instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    
    return filename


class Funcionario(Base):
    nome = models.CharField('Nome', max_length=100)
    cargo = models.ForeignKey('core.Cargo', verbose_name='Cargo', on_delete=models.CASCADE)
    bio = models.TextField('Bio', max_length=200)
    imagem = StdImageField('Imagem',
                           upload_to=get_file_path,
                           variations={'thumb':{
                               'width': 480,
                               'height': 480,
                               'crop': True}})
    
    
    class Meta:
        verbose_name = 'Funcionario'
        verbose_name_plural = 'Funcionarios'
        
    def __str__(self):
        return self.nome
    
    
class TipoCardapio(Base):
    tipo = models.CharField('Tipo', max_length=100)

    class Meta:
        verbose_name = 'Tipo Cardapio'
        verbose_name_plural = 'Tipos Cardapio'

        
    def __str__(self):
        return self.tipo
    
    
class Menu(Base):
    nome = models.CharField('Nome', max_length=100)
    tipo = models.ForeignKey('core.TipoCardapio', verbose_name='Tipo', on_delete=models.CASCADE)
    ingredientes = models.TextField('Ingredientes', max_length=200)
    valor = models.DecimalField('Valor', decimal_places=2, max_digits=10)
    imagem = StdImageField('Imagem',
                           upload_to=get_file_path,
                           variations={'thumb':{
                               'width': 480,
                               'height': 480,
                               'crop': True}})
    
    
    class Meta:
        verbose_name = 'Cardapio'
        verbose_name_plural = 'Cardapio'
        
        
    def __str__(self):
        return self.nome
