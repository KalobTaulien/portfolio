from django.core.cache import cache
from django.core.cache.utils import make_template_fragment_key
from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.admin.edit_handlers import (
    FieldPanel, MultiFieldPanel, PageChooserPanel, StreamFieldPanel
)
from wagtail.snippets.edit_handlers import SnippetChooserPanel

from wagtail.images import get_image_model_string
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.core import blocks as wagtail_blocks
from streams import blocks


class BasicPage(Page):
    template = "basic/basic_page.html"
    subpage_types = ['basic.BasicPage']
    parent_page_types = ['basic.BasicPage', 'wagtailcore.Page']

    banner_title = models.CharField(max_length=150, null=True, blank=True)
    banner_subtitle = models.CharField(max_length=300, blank=True, null=True)
    banner_image = models.ForeignKey(
        get_image_model_string(),
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )
    footer_cta = models.ForeignKey(
        'cta.CallToAction',
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='Optional footer call to action for this page'
    )

    social_sharing_image = models.ForeignKey(
        'wagtailimages.Image',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='+',
    )

    body = StreamField([
        ("cta", blocks.CallToActionBlock()),
        ("large_text", blocks.LargeTextBlock()),
        ("large_listing_block", blocks.LargeListingBlock()),
        ("small_listing_block", blocks.SmallListingBlock()),
        ("richtext", wagtail_blocks.RichTextBlock(
            template="streams/simple_richtext_block.html",
            features=["h3", "bold", "italic", "ol", "ul", "link", "image"],
            group="Text Sections"
        )),
        ("buttons", blocks.ButtonBlock()),
        ("image_gallery", blocks.ImageGallery()),
        ("hr", blocks.HorizontalRuleBlock()),
        ("horizontal_gallery", blocks.HorizontalGallery()),
        ("child_pages", blocks.HorizontalGallery()),
    ], null=True, blank=True)


    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('banner_title'),
            FieldPanel('banner_subtitle'),
            ImageChooserPanel('banner_image')
        ], heading='Banner Settings'),
        StreamFieldPanel("body"),
        MultiFieldPanel([
            SnippetChooserPanel("footer_cta")
        ], 'Optional footer cta'),
    ]

    promote_panels = Page.promote_panels + [
        ImageChooserPanel("social_sharing_image"),
    ]

    def get_template(self, request, *args, **kwargs):
        if request.is_preview:
            self.template = "basic/basic_page_preview.html"
        return self.template

    def save(self, *args, **kwargs):
        key = make_template_fragment_key(
            "page_cache",
            [self.id],
        )
        cache.delete(key)

        return super().save(*args, **kwargs)
