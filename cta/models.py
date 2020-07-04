from django.db import models

from wagtail.admin.edit_handlers import FieldPanel, PageChooserPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.snippets.models import register_snippet

ALIGNMENT_CHOICES = (
    ('left', 'Left'),
    ('right', 'Right'),
)

@register_snippet
class CallToAction(models.Model):

    image = models.ForeignKey(
        'wagtailimages.Image',
        on_delete=models.CASCADE,
        blank=False,
        null=False,
        related_name='+',
    )
    content_alignment = models.CharField(choices=ALIGNMENT_CHOICES, max_length=5, default='right')
    title = models.CharField(max_length=100)
    text = models.TextField(max_length=300)
    button_page = models.ForeignKey(
        'wagtailcore.Page',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='+',
        help_text='Select an internal page to link to'
    )
    button_link = models.URLField(blank=True, help_text='Enter your external URL')
    button_text = models.CharField(max_length=50)

    panels = [
        ImageChooserPanel("image"),
        FieldPanel("content_alignment"),
        FieldPanel("title"),
        FieldPanel("text"),
        PageChooserPanel("button_page"),
        FieldPanel("button_link"),
        FieldPanel("button_text"),
    ]

    def __str__(self):
        return self.title

    @property
    def url(self) -> str:
        if self.button_page:
            return self.button_page.url
        elif self.button_link:
            return self.button_link
        return ''
