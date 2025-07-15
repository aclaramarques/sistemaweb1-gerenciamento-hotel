from django.db import models

class Hospede(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20)
    ativo = models.BooleanField(default=False)
<<<<<<< HEAD
    cpf = models.CharField(primary_key=True, max_length=14, default='00000000000')

=======
>>>>>>> c2eec365ccb79d73d522fd0b93fd0b8756628d55

    def __str__(self):
        return self.nome