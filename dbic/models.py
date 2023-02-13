from django.db import models


class Cientista(models.Model):
    nome = models.CharField(max_length=60)
    sobrenome = models.CharField(max_length=60)
    biografia = models.TextField(blank=True)

    def __str__(self) -> str:
        return f"{self.nomde} {self.sobrenome}"

class Artigo(models.Model):
    autor = models.ForeignKey(Cientista, on_delete=models.CASCADE, related_name="artigo")
    titulo = models.CharField(max_length=50)
    descricao = models.CharField(max_length=200)
    corpo = models.TextField()
    local = models.CharField(max_length=120)
    data_publicacao = models.DateField()
    status = models.BooleanField(default=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.autor} {self.titulo}"

