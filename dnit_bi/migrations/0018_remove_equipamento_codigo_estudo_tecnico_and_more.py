# Generated by Django 4.1 on 2022-10-07 13:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dnit_bi', '0017_paralisado_situacao_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='equipamento',
            name='codigo_estudo_tecnico',
        ),
        migrations.AlterField(
            model_name='equipamento',
            name='codigo',
            field=models.CharField(blank=True, max_length=11, null=True),
        ),
        migrations.AlterField(
            model_name='ticket_freshdesk',
            name='prioridade',
            field=models.CharField(choices=[('Urgente', 'Urgente'), ('Alta', 'Alta'), ('Baixa', 'Baixa'), ('Media', 'Media')], max_length=30),
        ),
        migrations.AlterField(
            model_name='ticket_freshdesk',
            name='tipo',
            field=models.CharField(choices=[('Manutenção Preventiva', 'Manutenção Preventiva'), ('Solicitação de Análise', 'Solicitação de Análise'), ('Outro', 'Outro'), ('Poda / Roçada', 'Poda / Roçada'), ('Implantação / ajuste de sinalização', 'Implantação / ajuste de sinalização'), ('Ajuste de Display', 'Ajuste de Display'), ('OCR', 'OCR'), ('Service Task', 'Service Task'), ('Enquadramento', 'Enquadramento'), ('Implantação/Reparo de sinalização vertical', 'Implantação/Reparo de sinalização vertical'), ('Ajuste de Imagem', 'Ajuste de Imagem'), ('Falha de Camera', 'Falha de Camera'), ('Conectorização', 'Conectorização'), ('Equipamento Offline', 'Equipamento Offline'), ('Instalação / Reparo de energia eletrica', 'Instalação / Reparo de energia eletrica'), ('Implantação/Reparo de sinalização horizontal', 'Implantação/Reparo de sinalização horizontal'), ('Falha de disco', 'Falha de disco'), ('Falha de infração', 'Falha de infração'), ('Internet', 'Internet'), ('Iluminador', 'Iluminador'), ('Sem passagem / Não infracionando', 'Sem passagem / Não infracionando'), ('Configuração de envio SIOR', 'Configuração de envio SIOR'), ('Instalação / Reparo de cabo lógico', 'Instalação / Reparo de cabo lógico'), ('PISTA DANIFICADA SEM CONDIÇÕES PRA REFAZER LAÇOS', 'PISTA DANIFICADA SEM CONDIÇÕES PRA REFAZER LAÇOS'), ('Equipamento sem energia', 'Equipamento sem energia'), ('Manutenção corretiva', 'Manutenção corretiva'), ('infraestrutura', 'infraestrutura'), ('Aferição', 'Aferição'), ('Ajuste Fino', 'Ajuste Fino')], max_length=100, null=True),
        ),
        migrations.CreateModel(
            name='Estudo_tecnico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=30)),
                ('situacao', models.CharField(choices=[('Anulado', 'Anulado'), ('Aprovado', 'Aprovado'), ('Aguardando Análise', 'Aguardando Análise'), ('Aguardando Elaboração', 'Aguardando Elaboração'), ('Em Análise', 'Em Análise'), ('Aguardando Ajuste Elaboração', 'Aguardando Ajuste Elaboração'), ('Aguardando Revisão Análise', 'Aguardando Revisão Análise'), ('Em Elaboração', 'Em Elaboração')], max_length=40)),
                ('ultima_atualizacao_situacao', models.DateTimeField(blank=True, null=True)),
                ('atualizado', models.DateTimeField()),
                ('Equipamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dnit_bi.equipamento')),
            ],
        ),
    ]
