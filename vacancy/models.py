from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.admin.edit_handlers import StreamFieldPanel, FieldRowPanel, FieldPanel, MultiFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel

from streams import blocks

class VacancyPage(Page):
    template = "vacancy_page.html"

    parent_page_type = [
        "home.HomePage"
    ]

    preview_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text="This image appears at the top of the page and in social media previews."
    )
    location = models.CharField(max_length=100, null=True, blank=False)
    closing_date = models.DateField(null=True, blank=True)
    # location = models.CharField(max_length=100, null=True, blank=False)
    # salary = models.CharField(max_length=100, null=True, blank=False)
    content = StreamField(
        [
            ("text", blocks.TextBlock()),
            ("key_stats", blocks.KeyStatsBlock()),
            ("case_studies", blocks.CaseStudiesBlock()),
            ("call_to_action", blocks.CallToActionBlock())
        ],
        null=True,
        blank=True
    )

    content_panels = Page.content_panels + [
        MultiFieldPanel([FieldRowPanel([
            FieldPanel("location"),
            FieldPanel("closing_date")
        ])], "Key vacancy info"),
        StreamFieldPanel("content")
    ]

    promote_panels = Page.promote_panels + [
        ImageChooserPanel("preview_image")
    ]