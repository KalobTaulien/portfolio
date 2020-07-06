from django.db import models

from wagtail.admin.edit_handlers import FieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.contrib.settings.models import BaseSetting, register_setting


@register_setting
class SocialMediaSettings(BaseSetting):

    social_media_header = models.CharField(max_length=255, default='Follow Me')
    github = models.URLField(
        blank=True,
        help_text='Enter your GitHub URL'
    )
    twitter = models.URLField(
        blank=True,
        help_text='Enter your twitter URL'
    )
    instagram = models.URLField(
        blank=True,
        help_text='Enter a Instagram URL'
    )
    linkedin = models.URLField(
        blank=True,
        help_text='Enter a LinkedIn URL'
    )
    facebook = models.URLField(
        blank=True,
        help_text='Enter a Facebook URL'
    )

    panels = [
        FieldPanel("social_media_header"),
        FieldPanel("github"),
        FieldPanel("twitter"),
        FieldPanel("instagram"),
        FieldPanel("linkedin"),
        FieldPanel("facebook"),
    ]


@register_setting
class GoogleAnalytics(BaseSetting):
    tracking_id = models.CharField(max_length=20, blank=True, help_text='Enter in your google analytics tracking ID to enable analytics')

    panels = [
        FieldPanel("tracking_id"),
    ]


@register_setting
class SEOSettings(BaseSetting):
    """Fallback settings for individual page descriptions and social images."""

    site_description = models.CharField(max_length=250, blank=True, help_text='The description you want to show when someone google searches you')

    social_sharing_image = models.ForeignKey(
        'wagtailimages.Image',
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
        related_name='+',
    )

    panels = [
        FieldPanel("site_description"),
        ImageChooserPanel("social_sharing_image"),
    ]
