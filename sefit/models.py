from django.db import models

class Servidor(models.Model):
    ch_sexo = [('f', 'Femenino'), ('m', 'Masculino')]
    mat = models.IntegerField(min_value=100000 ,max_value=999999, primary_key=True)
    nome = models.CharField(max_length=30, null=False)
    sexo = models.CharField(max_length=1, choices=ch_sexo)
    email = models.EmailField(null=False)

    def __str__(self):
        return self.nome

class Afastamento(models.Model):
    fk_servidor = models.ForeignKey(Servidor, on_delete=models.CASCADE, null=False)
    data_criacao = models.DateField(auto_now_add=True, null=False)
    data_inicio = models.DateField(null=False)
    data_fim = models.DateField(null=False)
    motivo = models.CharField(max_length=10, null=False)
    obs = models.TextField(max_length=120, null=True)

    def __str__(self):
        return self.fk_servidor

class Permuta(models.Model):
    ch_tipo = [('n','Noturna'),('f','FDS'),('s','Semanal')]
    fk_substituto = models.ForeignKey(Servidor, name='substituto',on_delete=models.CASCADE, null=False)
    fk_escalado = models.ForeignKey(Servidor, name='escalado',on_delete=models.CASCADE, null=False)
    data = models.DateField(null=False)
    tipo = models.CharField(max_length=1, choices=ch_tipo, null=False)

    def __str__(self):
        return f'{self.fk_escalado.mat} -> {self.fk_substituto.mat} - {self.data}'

class tp_noturno(models.Model):
    ch_grupo = [('a', 'Noturno-A'),
                ('a', 'Noturno-B'),
                ('a', 'Noturno-C')]
    grupo = models.CharField(max_length=2, choices=ch_grupo, null=False)
    fk_permuta = models.ForeignKey(Permuta,on_delete=models.CASCADE, null=False)
    

class tp_fds(models.Model):
    ch_grupo = [('i', 'I'),('ii', 'II'),
                ('iii', 'III'),('iv', 'IV'),
                ('v', 'V')]
    grupo = models.CharField(max_length=2, choices=ch_grupo, null=False)
    roteiro = models.IntegerField(min_value=1000 ,max_value=9999, null=False)
    fk_permuta = models.ForeignKey(Permuta,on_delete=models.CASCADE, null=False)


class tp_semanal(models.Model):
    ch_turno = [('m', 'Matutino'),('v', 'Vespertino')]
    turno = models.CharField(max_length=1, choices=ch_turno, null=False)
    roteiro = models.IntegerField(min_value=1000 ,max_value=9999, null=False)
    fk_permuta = models.ForeignKey(Permuta,on_delete=models.CASCADE, null=False)

class roteiro(models.Model):
    id_roteiro = models.IntegerField(primary_key=True)
    posto_base = models.CharField(max_length=25, null=False)
    area_semanal = models.CharField(max_length=20, null=False)
    area_fds = models.CharField(max_length=20, null=False)

    def __str__(self):
        return self.id_roteiro

