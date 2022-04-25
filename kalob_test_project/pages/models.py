from django.db import models
from wagtail import images
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel, StreamFieldPanel
from wagtail.core.fields import StreamField
from wagtail.core.models import Page
from wagtail.images import edit_handlers as image_edit_handlers
from wagtail.search import index

from kalob_test_project.pages import blocks as pages_blocks


class HomePage(Page):
    class Meta:
        verbose_name = "Homepage"


class AboutPage(Page):
    subtitle = models.TextField(verbose_name="Subtitle", max_length=254)
    background_image = models.ForeignKey(
        to=images.get_image_model_string(),
        on_delete=models.SET_NULL,
        related_name="+",
        verbose_name="Background Image",
        blank=True,
        null=True,
    )
    body = StreamField(
        block_types=[
            ("title", pages_blocks.TitleBlock()),
            ("paragraph", pages_blocks.ParagraphBlock()),
            ("largeimage", pages_blocks.LargeImageBlock()),
            ("doubleimage", pages_blocks.DoubleImageBlock()),
        ],
        verbose_name="Body",
        blank=True,
    )

    hero_panels = [
        FieldPanel("subtitle"),
        image_edit_handlers.ImageChooserPanel("background_image"),
    ]
    content_panels = Page.content_panels + [
        MultiFieldPanel(heading="Hero", children=hero_panels),
        StreamFieldPanel("body"),
    ]

    parent_page_types = [
        "pages.HomePage",
        "pages.AboutPage",
    ]

    class Meta:
        verbose_name = "About Page"
