# Generated by Django 2.2.4 on 2019-08-23 22:47

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('vacancy', '0003_auto_20190823_2143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vacancypage',
            name='content',
            field=wagtail.core.fields.StreamField([('text_block', wagtail.core.blocks.StructBlock([('headline', wagtail.core.blocks.CharBlock(max_length=200)), ('benefits', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('crosshead', wagtail.core.blocks.CharBlock()), ('content', wagtail.core.blocks.TextBlock(max_length=200))])))]))], blank=True, null=True),
        ),
    ]