# Generated by Django 4.1 on 2022-09-02 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dnit_bi', '0014_alter_ticket_freshdesk_prioridade_and_more'),
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
            field=models.CharField(choices=[('Baixa', 'Baixa'), ('Alta', 'Alta'), ('Media', 'Media'), ('Urgente', 'Urgente')], max_length=30),
        ),
        migrations.AlterField(
            model_name='ticket_freshdesk',
            name='tipo',
            field=models.CharField(choices=[('OCR', 'OCR'), ('Poda / Roçada', 'Poda / Roçada'), ('Manutenção corretiva', 'Manutenção corretiva'), ('Internet', 'Internet'), ('infraestrutura', 'infraestrutura'), ('Ajuste de Imagem', 'Ajuste de Imagem'), ('Implantação/Reparo de sinalização vertical', 'Implantação/Reparo de sinalização vertical'), ('Implantação/Reparo de sinalização horizontal', 'Implantação/Reparo de sinalização horizontal'), ('Falha de Camera', 'Falha de Camera'), ('Falha de disco', 'Falha de disco'), ('Configuração de envio SIOR', 'Configuração de envio SIOR'), ('Falha de infração', 'Falha de infração'), ('Iluminador', 'Iluminador'), ('Ajuste Fino', 'Ajuste Fino'), ('Instalação / Reparo de energia eletrica', 'Instalação / Reparo de energia eletrica'), ('Aferição', 'Aferição'), ('Ajuste de Display', 'Ajuste de Display'), ('Manutenção Preventiva', 'Manutenção Preventiva'), ('Service Task', 'Service Task'), ('Equipamento sem energia', 'Equipamento sem energia'), ('Outro', 'Outro'), ('PISTA DANIFICADA SEM CONDIÇÕES PRA REFAZER LAÇOS', 'PISTA DANIFICADA SEM CONDIÇÕES PRA REFAZER LAÇOS'), ('Solicitação de Análise', 'Solicitação de Análise'), ('Sem passagem / Não infracionando', 'Sem passagem / Não infracionando'), ('Enquadramento', 'Enquadramento'), ('Conectorização', 'Conectorização'), ('Equipamento Offline', 'Equipamento Offline'), ('Implantação / ajuste de sinalização', 'Implantação / ajuste de sinalização'), ('Instalação / Reparo de cabo lógico', 'Instalação / Reparo de cabo lógico')], max_length=100, null=True),
        ),
    ]
