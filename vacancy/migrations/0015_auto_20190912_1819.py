# Generated by Django 2.2.4 on 2019-09-12 18:19

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('vacancy', '0014_auto_20190912_1718'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vacancypage',
            name='content',
            field=wagtail.core.fields.StreamField([('text', wagtail.core.blocks.StructBlock([('headline', wagtail.core.blocks.CharBlock(max_length=200)), ('sticky_headline', wagtail.core.blocks.BooleanBlock(required=False)), ('left_content', wagtail.core.blocks.TextBlock(required=False)), ('content', wagtail.core.blocks.RichTextBlock(features=['h3', 'bold', 'italic', 'link', 'ol', 'ul', 'embed'])), ('large_text', wagtail.core.blocks.BooleanBlock(required=False))])), ('key_stats', wagtail.core.blocks.StructBlock([('stats', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('label', wagtail.core.blocks.CharBlock()), ('value', wagtail.core.blocks.CharBlock())])))])), ('case_studies', wagtail.core.blocks.StructBlock([('headline', wagtail.core.blocks.CharBlock(max_length=200)), ('case_studies', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('headline', wagtail.core.blocks.CharBlock()), ('slugline', wagtail.core.blocks.CharBlock()), ('kicker', wagtail.core.blocks.CharBlock()), ('destination', wagtail.core.blocks.URLBlock())])))])), ('call_to_action', wagtail.core.blocks.StructBlock([('headline', wagtail.core.blocks.CharBlock(max_length=200)), ('content', wagtail.core.blocks.RichTextBlock(features=['bold', 'italic', 'link'])), ('large_text', wagtail.core.blocks.BooleanBlock(required=False)), ('button_destination', wagtail.core.blocks.URLBlock()), ('button_label', wagtail.core.blocks.CharBlock(max_length=30))]))], blank=True, null=True),
        ),
    ]
