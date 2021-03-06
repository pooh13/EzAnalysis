from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Career',
            fields=[
                ('career_id', models.CharField(max_length=4, primary_key=True, serialize=False)),
                ('career_name', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='DefaultThing',
            fields=[
                ('things_id', models.CharField(max_length=4, primary_key=True, serialize=False)),
                ('things', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Diary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('mood', models.IntegerField(null=True)),
                ('note', models.CharField(max_length=255)),
                ('pic', models.ImageField(null=True, upload_to='images')),
            ],
        ),
        migrations.CreateModel(
            name='UserInform',
            fields=[
                ('line_id', models.CharField(max_length=120, primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=20)),
                ('gender', models.CharField(blank=True, max_length=2, null=True)),
                ('birth', models.DateField(blank=True, null=True)),
                ('career_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='AI_analyze.career')),
            ],
        ),
        migrations.CreateModel(
            name='UserThings',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AI_analyze.diary')),
                ('line_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AI_analyze.userinform')),
                ('things_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AI_analyze.defaultthing')),
            ],
        ),
        migrations.CreateModel(
            name='InstantPhotoAnalysis',
            fields=[
                ('photo_id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateTimeField()),
                ('pic', models.ImageField(upload_to='images')),
                ('line_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AI_analyze.userinform')),
            ],
        ),
        migrations.AddField(
            model_name='diary',
            name='line_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AI_analyze.userinform'),
        ),
        migrations.CreateModel(
            name='AnalysisDiary',
            fields=[
                ('photo_id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateTimeField()),
                ('pic', models.ImageField(upload_to='')),
                ('line_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AI_analyze.userinform')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='diary',
            unique_together={('line_id', 'date')},
        ),
        migrations.CreateModel(
            name='DefaultNote',
            fields=[
                ('note_id', models.CharField(max_length=4, primary_key=True, serialize=False)),
                ('default_note', models.CharField(max_length=255)),
                ('things_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AI_analyze.defaultthing')),
            ],
            options={
                'unique_together': {('things_id', 'note_id')},
            },
        ),
    ]
