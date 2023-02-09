# Generated by Django 4.1 on 2022-09-02 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dnit_bi', '0011_alter_faixa_sentido_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket_freshdesk',
            name='prioridade',
            field=models.CharField(choices=[('Baixa', 'Baixa'), ('Urgente', 'Urgente'), ('Alta', 'Alta'), ('Media', 'Media')], max_length=30),
        ),
        migrations.AlterField(
            model_name='ticket_freshdesk',
            name='tipo',
            field=models.CharField(choices=[('Implantação/Reparo de sinalização horizontal', 'Implantação/Reparo de sinalização horizontal'), ('Internet', 'Internet'), ('Falha de infração', 'Falha de infração'), ('Poda / Roçada', 'Poda / Roçada'), ('Manutenção corretiva', 'Manutenção corretiva'), ('Implantação / ajuste de sinalização', 'Implantação / ajuste de sinalização'), ('Falha de disco', 'Falha de disco'), ('OCR', 'OCR'), ('Instalação / Reparo de cabo lógico', 'Instalação / Reparo de cabo lógico'), ('Equipamento sem energia', 'Equipamento sem energia'), ('Manutenção Preventiva', 'Manutenção Preventiva'), ('Ajuste de Imagem', 'Ajuste de Imagem'), ('Ajuste de Display', 'Ajuste de Display'), ('Ajuste Fino', 'Ajuste Fino'), ('Iluminador', 'Iluminador'), ('Configuração de envio SIOR', 'Configuração de envio SIOR'), ('Enquadramento', 'Enquadramento'), ('infraestrutura', 'infraestrutura'), ('Sem passagem / Não infracionando', 'Sem passagem / Não infracionando'), ('Equipamento Offline', 'Equipamento Offline'), ('Falha de Camera', 'Falha de Camera'), ('Solicitação de Análise', 'Solicitação de Análise'), ('Outro', 'Outro'), ('Instalação / Reparo de energia eletrica', 'Instalação / Reparo de energia eletrica'), ('Conectorização', 'Conectorização'), ('Implantação/Reparo de sinalização vertical', 'Implantação/Reparo de sinalização vertical'), ('PISTA DANIFICADA SEM CONDIÇÕES PRA REFAZER LAÇOS', 'PISTA DANIFICADA SEM CONDIÇÕES PRA REFAZER LAÇOS'), ('Aferição', 'Aferição')], max_length=100, null=True),
        ),
    ]
