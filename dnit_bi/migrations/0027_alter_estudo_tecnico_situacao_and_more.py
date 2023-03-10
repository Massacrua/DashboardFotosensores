# Generated by Django 4.1 on 2022-11-10 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dnit_bi', '0026_equipamentoanotacoes_usuario_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estudo_tecnico',
            name='situacao',
            field=models.CharField(choices=[('Aguardando Elaboração', 'Aguardando Elaboração'), ('Em Elaboração', 'Em Elaboração'), ('Em Análise', 'Em Análise'), ('Aguardando Análise', 'Aguardando Análise'), ('Aprovado', 'Aprovado'), ('Anulado', 'Anulado'), ('Aguardando Revisão Análise', 'Aguardando Revisão Análise'), ('Aguardando Ajuste Elaboração', 'Aguardando Ajuste Elaboração')], max_length=40),
        ),
        migrations.AlterField(
            model_name='ticket_freshdesk',
            name='prioridade',
            field=models.CharField(choices=[('Baixa', 'Baixa'), ('Alta', 'Alta'), ('Urgente', 'Urgente'), ('Media', 'Media')], max_length=30),
        ),
        migrations.AlterField(
            model_name='ticket_freshdesk',
            name='tipo',
            field=models.CharField(choices=[('Ajuste Fino', 'Ajuste Fino'), ('Internet', 'Internet'), ('Ajuste de Display', 'Ajuste de Display'), ('Service Task', 'Service Task'), ('Implantação/Reparo de sinalização vertical', 'Implantação/Reparo de sinalização vertical'), ('Aferição', 'Aferição'), ('Ajuste de Imagem', 'Ajuste de Imagem'), ('Implantação / ajuste de sinalização', 'Implantação / ajuste de sinalização'), ('Instalação / Reparo de cabo lógico', 'Instalação / Reparo de cabo lógico'), ('infraestrutura', 'infraestrutura'), ('Enquadramento', 'Enquadramento'), ('Conectorização', 'Conectorização'), ('Falha de Camera', 'Falha de Camera'), ('Sem passagem / Não infracionando', 'Sem passagem / Não infracionando'), ('Equipamento Offline', 'Equipamento Offline'), ('OCR', 'OCR'), ('Falha de disco', 'Falha de disco'), ('Equipamento sem energia', 'Equipamento sem energia'), ('Implantação/Reparo de sinalização horizontal', 'Implantação/Reparo de sinalização horizontal'), ('Solicitação de Análise', 'Solicitação de Análise'), ('Manutenção corretiva', 'Manutenção corretiva'), ('Poda / Roçada', 'Poda / Roçada'), ('Outro', 'Outro'), ('Manutenção Preventiva', 'Manutenção Preventiva'), ('Configuração de envio SIOR', 'Configuração de envio SIOR'), ('PISTA DANIFICADA SEM CONDIÇÕES PRA REFAZER LAÇOS', 'PISTA DANIFICADA SEM CONDIÇÕES PRA REFAZER LAÇOS'), ('Instalação / Reparo de energia eletrica', 'Instalação / Reparo de energia eletrica'), ('Iluminador', 'Iluminador'), ('Falha de infração', 'Falha de infração')], max_length=100, null=True),
        ),
    ]
