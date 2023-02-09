# Generated by Django 4.1 on 2022-09-01 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dnit_bi', '0009_alter_ticket_freshdesk_prioridade_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faixa',
            name='sentido',
            field=models.CharField(choices=[('D', 'DECRESCENTE'), ('C', 'CRESCENTE')], max_length=11),
        ),
        migrations.AlterField(
            model_name='ticket_freshdesk',
            name='prioridade',
            field=models.CharField(choices=[('Baixa', 'Baixa'), ('Media', 'Media'), ('Alta', 'Alta'), ('Urgente', 'Urgente')], max_length=30),
        ),
        migrations.AlterField(
            model_name='ticket_freshdesk',
            name='tipo',
            field=models.CharField(choices=[('Implantação/Reparo de sinalização vertical', 'Implantação/Reparo de sinalização vertical'), ('Sem passagem / Não infracionando', 'Sem passagem / Não infracionando'), ('Solicitação de Análise', 'Solicitação de Análise'), ('Ajuste de Display', 'Ajuste de Display'), ('Equipamento sem energia', 'Equipamento sem energia'), ('Falha de infração', 'Falha de infração'), ('OCR', 'OCR'), ('Internet', 'Internet'), ('Implantação/Reparo de sinalização horizontal', 'Implantação/Reparo de sinalização horizontal'), ('Iluminador', 'Iluminador'), ('Conectorização', 'Conectorização'), ('Enquadramento', 'Enquadramento'), ('Implantação / ajuste de sinalização', 'Implantação / ajuste de sinalização'), ('Outro', 'Outro'), ('infraestrutura', 'infraestrutura'), ('Manutenção corretiva', 'Manutenção corretiva'), ('Poda / Roçada', 'Poda / Roçada'), ('Falha de disco', 'Falha de disco'), ('Manutenção Preventiva', 'Manutenção Preventiva'), ('Configuração de envio SIOR', 'Configuração de envio SIOR'), ('Instalação / Reparo de cabo lógico', 'Instalação / Reparo de cabo lógico'), ('Aferição', 'Aferição'), ('Equipamento Offline', 'Equipamento Offline'), ('PISTA DANIFICADA SEM CONDIÇÕES PRA REFAZER LAÇOS', 'PISTA DANIFICADA SEM CONDIÇÕES PRA REFAZER LAÇOS'), ('Instalação / Reparo de energia eletrica', 'Instalação / Reparo de energia eletrica'), ('Falha de Camera', 'Falha de Camera'), ('Ajuste Fino', 'Ajuste Fino'), ('Ajuste de Imagem', 'Ajuste de Imagem')], max_length=100, null=True),
        ),
    ]