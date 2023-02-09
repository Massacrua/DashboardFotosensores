# Generated by Django 4.1 on 2022-10-14 14:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dnit_bi', '0019_remove_estudo_tecnico_equipamento_equipamento_et_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estudo_tecnico',
            name='situacao',
            field=models.CharField(choices=[('Aguardando Ajuste Elaboração', 'Aguardando Ajuste Elaboração'), ('Em Análise', 'Em Análise'), ('Anulado', 'Anulado'), ('Aprovado', 'Aprovado'), ('Em Elaboração', 'Em Elaboração'), ('Aguardando Elaboração', 'Aguardando Elaboração'), ('Aguardando Revisão Análise', 'Aguardando Revisão Análise'), ('Aguardando Análise', 'Aguardando Análise')], max_length=40),
        ),
        migrations.AlterField(
            model_name='municipio',
            name='lote',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dnit_bi.lote'),
        ),
        migrations.AlterField(
            model_name='municipio',
            name='setor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dnit_bi.setor'),
        ),
        migrations.AlterField(
            model_name='ticket_freshdesk',
            name='prioridade',
            field=models.CharField(choices=[('Alta', 'Alta'), ('Baixa', 'Baixa'), ('Urgente', 'Urgente'), ('Media', 'Media')], max_length=30),
        ),
        migrations.AlterField(
            model_name='ticket_freshdesk',
            name='tipo',
            field=models.CharField(choices=[('Instalação / Reparo de energia eletrica', 'Instalação / Reparo de energia eletrica'), ('Ajuste Fino', 'Ajuste Fino'), ('Implantação/Reparo de sinalização vertical', 'Implantação/Reparo de sinalização vertical'), ('Manutenção Preventiva', 'Manutenção Preventiva'), ('Conectorização', 'Conectorização'), ('Solicitação de Análise', 'Solicitação de Análise'), ('Configuração de envio SIOR', 'Configuração de envio SIOR'), ('infraestrutura', 'infraestrutura'), ('OCR', 'OCR'), ('Internet', 'Internet'), ('Poda / Roçada', 'Poda / Roçada'), ('Sem passagem / Não infracionando', 'Sem passagem / Não infracionando'), ('Ajuste de Imagem', 'Ajuste de Imagem'), ('Aferição', 'Aferição'), ('Implantação / ajuste de sinalização', 'Implantação / ajuste de sinalização'), ('Falha de Camera', 'Falha de Camera'), ('Iluminador', 'Iluminador'), ('Falha de infração', 'Falha de infração'), ('Ajuste de Display', 'Ajuste de Display'), ('Outro', 'Outro'), ('Equipamento sem energia', 'Equipamento sem energia'), ('Service Task', 'Service Task'), ('PISTA DANIFICADA SEM CONDIÇÕES PRA REFAZER LAÇOS', 'PISTA DANIFICADA SEM CONDIÇÕES PRA REFAZER LAÇOS'), ('Implantação/Reparo de sinalização horizontal', 'Implantação/Reparo de sinalização horizontal'), ('Enquadramento', 'Enquadramento'), ('Manutenção corretiva', 'Manutenção corretiva'), ('Equipamento Offline', 'Equipamento Offline'), ('Falha de disco', 'Falha de disco'), ('Instalação / Reparo de cabo lógico', 'Instalação / Reparo de cabo lógico')], max_length=100, null=True),
        ),
    ]