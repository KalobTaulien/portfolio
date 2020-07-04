from wagtail.admin.rich_text.converters.html_to_contentstate import BlockElementHandler
import wagtail.admin.rich_text.editors.draftail.features as draftail_features
from wagtail.core import hooks


@hooks.register('register_rich_text_features')
def register_help_text_feature(features):

    feature_name = 'brand-color'
    type_ = 'brand-color'

    control = {
        'type': type_,
        'label': 'Brand',
        'description': 'Brand Color',
        # Optionally, we can tell Draftail what element to use when displaying those blocks in the editor.
        'element': 'span',
    }

    features.register_editor_plugin(
        'draftail', feature_name, draftail_features.BlockFeature(control, css={'all': ['custom-theme.css']})
    )

    features.register_converter_rule('contentstate', feature_name, {
        'from_database_format': {'span[class=brand-color]': BlockElementHandler(type_)},
        'to_database_format': {'block_map': {type_: {'element': 'span', 'props': {'class': 'brand-color'}}}},
    })
