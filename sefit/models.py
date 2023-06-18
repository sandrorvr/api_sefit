from django.db import models

class Roteiro(models.Model):
    id_roteiro = models.IntegerField(primary_key=True)
    posto_base = models.CharField(max_length=25, null=False)
    area_semanal = models.CharField(max_length=20, null=False)
    area_fds = models.CharField(max_length=20, null=False)

    def __str__(self):
        return str(self.id_roteiro)

class Servidor(models.Model):
    ch_sexo = [('f', 'Femenino'), ('m', 'Masculino')]
    mat = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=30, null=False)
    sexo = models.CharField(max_length=1, choices=ch_sexo)
    email = models.EmailField(null=False)

    def __str__(self):
        return self.nome

class Afastamento(models.Model):
    ch_motivo = [('fl', 'Folga'), ('fr', 'Ferias'), 
                ('lp', 'Licença Premio'), ('lm', 'Licença medica'), 
                ('em', 'Cedido')]
    fk_servidor = models.ForeignKey(Servidor, on_delete=models.CASCADE, null=False)
    data_criacao = models.DateField(auto_now_add=True, null=False)
    data_inicio = models.DateField(null=False)
    data_fim = models.DateField(null=False)
    motivo = models.CharField(max_length=10, choices=ch_motivo, null=False)
    obs = models.TextField(max_length=120, null=True, blank=True)

    def __str__(self):
        return self.fk_servidor.nome

class Permuta(models.Model):
    ch_tipo = [('n','Noturna'),('f','FDS'),('s','Semanal')]
    fk_substituto = models.ForeignKey(Servidor, related_name='substituto',on_delete=models.CASCADE, null=False)
    fk_escalado = models.ForeignKey(Servidor, related_name='escalado',on_delete=models.CASCADE, null=False)
    data = models.DateField(null=False)
    tipo = models.CharField(max_length=1, choices=ch_tipo, null=False)

    def getNameFirst(self, name):
        split_name = name.split(' ')
        return f"{split_name[0]} {split_name[1][:3]}..."

    def __str__(self):
        fk_escalado = self.getNameFirst(self.fk_escalado.nome)
        fk_substituto = self.getNameFirst(self.fk_substituto.nome)
        return f'{fk_escalado} -> {fk_substituto} - {self.data}'

class Tp_noturno(models.Model):
    ch_grupo = [('a', 'Noturno-A'),
                ('b', 'Noturno-B'),
                ('c', 'Noturno-C')]
    grupo = models.CharField(max_length=2, choices=ch_grupo, null=False)
    fk_permuta = models.ForeignKey(Permuta,on_delete=models.CASCADE, null=False)
    

class Tp_fds(models.Model):
    ch_grupo = [('i', 'I'),('ii', 'II'),
                ('iii', 'III'),('iv', 'IV'),
                ('v', 'V')]
    grupo = models.CharField(max_length=3, choices=ch_grupo, null=False)
    roteiro = models.ForeignKey(Roteiro,on_delete=models.CASCADE, null=False)
    fk_permuta = models.ForeignKey(Permuta,on_delete=models.CASCADE, null=False)


class Tp_semanal(models.Model):
    ch_turno = [('m', 'Matutino'),('v', 'Vespertino')]
    turno = models.CharField(max_length=1, choices=ch_turno, null=False)
    roteiro = models.ForeignKey(Roteiro,on_delete=models.CASCADE, null=False)
    fk_permuta = models.ForeignKey(Permuta,on_delete=models.CASCADE, null=False)

