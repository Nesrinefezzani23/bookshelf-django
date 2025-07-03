from django.db import migrations

def create_initial_categories(apps, schema_editor):
    Category = apps.get_model('hkeyet', 'Category')
    initial_categories = [
        'Roman',
        'Science-Fiction',
        'Policier',
        'Fantastique',
        'Biographie',
        'Histoire',
        'Jeunesse',
        'Poésie',
        'Théâtre',
        'Essai',
    ]
    for name in initial_categories:
        Category.objects.get_or_create(name=name)

class Migration(migrations.Migration):
    dependencies = [
        ('hkeyet', '0003_category_book_categories'),
    ]
    operations = [
        migrations.RunPython(create_initial_categories),
    ] 