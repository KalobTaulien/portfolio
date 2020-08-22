from django import forms
from django.core.exceptions import ValidationError
from django.forms.utils import ErrorList

from wagtail.core import blocks
from wagtail.embeds.blocks import EmbedBlock
from wagtail.images.blocks import ImageChooserBlock
from wagtail.snippets.blocks import SnippetChooserBlock


class RadioSelectBlock(blocks.ChoiceBlock):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.field.widget = forms.RadioSelect(
            choices=self.field.widget.choices
        )


class LinkValue(blocks.StructValue):
    """Additional logic for links."""

    def url(self) -> str:
        internal_link = self.get('internal_link')
        external_link = self.get('external_link')
        if internal_link:
            return internal_link.url
        elif external_link:
            return external_link
        return ""


class Link(blocks.StructBlock):
    """A link struct block."""

    link_text = blocks.CharBlock(
        max_length=50,
        null=True,
        blank=True,
        required=False,
    )
    internal_link = blocks.PageChooserBlock(
        required=False,
        help_text='Select an internal page to link to. Internal links are used before external links (if both are provided).',
    )
    external_link = blocks.URLBlock(
        required=False,
        help_text='Type an external website to link to. Internal links are used before external links (if both are provided).',
    )

    def clean(self, value):
        internal_link = value.get("internal_link")
        external_link = value.get("external_link")
        errors = {}
        if internal_link and external_link:
            errors["internal_link"] = ErrorList(["Both of these fields cannot be filled. Please select or enter only one option."])
            errors["external_link"] = ErrorList(["Both of these fields cannot be filled. Please select or enter only one option."])

        if errors:
            raise ValidationError("Validation error in your Link", params=errors)

        return super().clean(value)

    class Meta:
        template = "streams/link.html"
        icon = "link"
        label = "Link"
        value_class = LinkValue


class LinkNoText(blocks.StructBlock):
    """A link struct block."""

    internal_link = blocks.PageChooserBlock(
        required=False,
        help_text='Select an internal page to link to. Internal links are used before external links (if both are provided).',
    )
    external_link = blocks.URLBlock(
        required=False,
        help_text='Type an external website to link to. Internal links are used before external links (if both are provided).',
    )

    class Meta:
        icon = "link"
        label = "Link"
        value_class = LinkValue


class CallToActionBlock(blocks.StructBlock):

    text_alignment = RadioSelectBlock(
        choices=(
            ('left', 'Left'),
            ('right', 'Right'),
        ),
        default='left',
    )
    content = blocks.RichTextBlock(features=["h2", "h3", "link", "bold", "italic", "image", "brand-color"])
    image = ImageChooserBlock()
    link = Link()

    class Meta:
        template = "streams/call_to_action_block.html"
        icon = "pilcrow"
        label = "Call to Action"


class LargeTextBlock(blocks.StructBlock):

    text = blocks.TextBlock()
    text_alignment = RadioSelectBlock(
        choices=(
            ('left', 'Left'),
            ('right', 'Right'),
            ('center', 'Center'),
        ),
        default='left',
    )

    class Meta:
        template = "streams/large_text_block.html"
        icon = "pilcrow"
        label = "Large Text"
        group = "Text Sections"


class LargeListingBlock(blocks.StructBlock):

    image = ImageChooserBlock()
    text_alignment = RadioSelectBlock(
        choices=(
            ('left', 'Left'),
            ('right', 'Right'),
        ),
        default='left',
    )
    title = blocks.CharBlock(max_length=50)
    internal_link = blocks.PageChooserBlock(
        required=False,
        help_text='Select an internal page to link to. Internal links are used before external links (if both are provided).',
    )
    external_link = blocks.URLBlock(
        required=False,
        help_text='Type an external website to link to. Internal links are used before external links (if both are provided).',
    )

    def clean(self, value):
        internal_link = value.get("internal_link")
        external_link = value.get("external_link")
        errors = {}
        if internal_link and external_link:
            errors["internal_link"] = ErrorList(["Both of these fields cannot be filled. Please select or enter only one option."])
            errors["external_link"] = ErrorList(["Both of these fields cannot be filled. Please select or enter only one option."])

        if errors:
            raise ValidationError("Validation error in your Link", params=errors)

        return super().clean(value)

    def get_context(self, value, parent_context=None):
        context = super().get_context(value, parent_context=None)
        internal_link = value.get('internal_link')
        external_link = value.get('external_link')
        if internal_link:
            url = internal_link.url
        elif external_link:
            url = external_link
        else:
            url = ''
        context['url'] = url
        return context

    class Meta:
        template = "streams/large_listing_block.html"
        icon = "placeholder"
        label = "Large Listing Block"
        group = "Listing Blocks"


class SmallListingCard(blocks.StructBlock):
    """This class is not used on its own here. It's used in a list block."""
    image = ImageChooserBlock()
    subtext = blocks.CharBlock(max_length=20, required=False, help_text='Optional. Small text at the top of the card.')
    title = blocks.CharBlock(max_length=50)
    internal_link = blocks.PageChooserBlock(
        required=False,
        help_text='Select an internal page to link to. Internal links are used before external links (if both are provided).',
    )
    external_link = blocks.URLBlock(
        required=False,
        help_text='Type an external website to link to. Internal links are used before external links (if both are provided).',
    )

    def clean(self, value):
        internal_link = value.get("internal_link")
        external_link = value.get("external_link")
        errors = {}
        if internal_link and external_link:
            errors["internal_link"] = ErrorList(["Both of these fields cannot be filled. Please select or enter only one option."])
            errors["external_link"] = ErrorList(["Both of these fields cannot be filled. Please select or enter only one option."])

        if errors:
            raise ValidationError("Validation error in your Link", params=errors)

        return super().clean(value)

    def get_context(self, value, parent_context=None):
        context = super().get_context(value, parent_context=None)
        internal_link = value.get('internal_link')
        external_link = value.get('external_link')
        if internal_link:
            url = internal_link.url
        elif external_link:
            url = external_link
        else:
            url = ''
        context['url'] = url
        return context


class SmallListingBlock(blocks.StructBlock):

    cards = blocks.ListBlock(
        SmallListingCard()
    )

    class Meta:
        template = "streams/small_listing_block.html"
        icon = "placeholder"
        label = "Small Listing Blocks"
        group = "Listing Blocks"


class ButtonBlock(blocks.StructBlock):

    buttons = blocks.ListBlock(
        Link()
    )

    class Meta:
        template = "streams/button_block.html"
        icon = "placeholder"
        label = "Button Block"


class TwoThirdsGalleryBlock(blocks.StructBlock):
    large_image_alignment = RadioSelectBlock(
        choices=(
            ('left', 'Left'),
            ('right', 'Right'),
        ),
        default='left',
    )
    two_thirds_image = ImageChooserBlock()
    two_thirds_external_link = blocks.URLBlock(required=False)
    one_third_image = ImageChooserBlock()
    one_third_external_link = blocks.URLBlock(required=False)

    class Meta:
        template = "streams/two_thirds_gallery_block.html"
        icon = "picture"
        label = "1/3 + 2/3"
        group = "Gallery Blocks"

class TwoThirdsTextGalleryBlock(blocks.StructBlock):
    text_alignment = RadioSelectBlock(
        choices=(
            ('left', 'Left'),
            ('right', 'Right'),
        ),
        default='left',
    )
    image = ImageChooserBlock()
    content = blocks.RichTextBlock(features=["h3", "link", "bold", "italic"])
    link = Link()

    class Meta:
        template = "streams/two_thirds_text_gallery_block.html"
        icon = "picture"
        label = "2/3 + Text"
        group = "Gallery Blocks"


class ImageRow(blocks.StructBlock):
    """Image row."""

    row = blocks.ListBlock(
        blocks.StructBlock([
            ("image", ImageChooserBlock()),
            ("link", LinkNoText(required=False)),
        ], icon="image")
    )

    class Meta:
        label = "Image Row"
        template = "streams/image_row_block.html"
        icon = "image"


class TwoImagesAndTextBlock(blocks.StructBlock):

    text_alignment = RadioSelectBlock(
        choices=(
            ('left', 'Left'),
            ('right', 'Right'),
        ),
        default='left',
    )
    one_third_image = ImageChooserBlock()
    one_third_image_2 = ImageChooserBlock()
    content = blocks.RichTextBlock(features=["h3", "link", "bold", "italic"])
    link = Link()

    class Meta:
        label = "2x Images + Text"
        template = "streams/two_images_and_text_block.html"
        icon = "image"
        group = "Gallery Blocks"


class TwoColumnImageGalleryBlock(blocks.StructBlock):

    large_image_alignment = RadioSelectBlock(
        choices=(
            ('left', 'Left'),
            ('right', 'Right'),
        ),
        default='left',
    )
    small_image = ImageChooserBlock()
    small_image_2 = ImageChooserBlock()
    large_image = ImageChooserBlock()

    class Meta:
        label = "1/2 Columns"
        template = "streams/two_column_image_gallery_block.html"
        icon = "image"
        group = "Gallery Blocks"


class HorizontalRuleBlock(blocks.StaticBlock):

    class Meta:
        label = "Horizontal Rule"
        template = "streams/horizontal_rule_block.html"
        icon = "horizontalrule"


class ImageGallery(blocks.StructBlock):

    row = blocks.StreamBlock([
            ("two_thirds", TwoThirdsGalleryBlock()),
            ("two_images_text", TwoImagesAndTextBlock()),
            ("two_thirds_text", TwoThirdsTextGalleryBlock()),
            ("two_column", TwoColumnImageGalleryBlock()),
            ("image_row", ImageRow())
        ], icon="image")


    class Meta:
        label = "Image Gallery"
        template = "streams/image_gallery_block.html"
        icon = "image"



class HorizontalGallery(blocks.StructBlock):
    """Image row."""

    images = blocks.ListBlock(
        blocks.StructBlock([
            ("img", ImageChooserBlock()),
        ], icon="image")
    )

    class Meta:
        label = "Horizontal Gallery"
        template = "streams/horizontal_gallery.html"
        icon = "image"


class FooterCTABlock(blocks.StructBlock):

    cta = SnippetChooserBlock(target_model='cta.CallToAction')

    class Meta:
        template = "includes/footer_cta.html"
        label = "Footer Call to Action"


class ChildPages(blocks.StaticBlock):

    class Meta:
        template = "includes/child_pages.html"
        label = "Child Pages"
