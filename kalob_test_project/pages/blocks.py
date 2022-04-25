from wagtail.core import blocks
from wagtail.images import blocks as image_blocks


class TitleBlock(blocks.StructBlock):
    title_block = blocks.TextBlock(label="Title Block", required=True, default="")

    class Meta:
        icon = "fa/object-group-solid"
        label = "Title Block"


class ParagraphBlock(blocks.StructBlock):
    paragraph = blocks.RichTextBlock(
        label="Paragraph",
        required=True,
        features=[
            "bold",
            "italic",
            "strikethrough",
            "h3",
            "h4",
            "h5",
            "ol",
            "ul",
            "link",
        ],
        default="",
    )

    class Meta:
        icon = "fa/object-group-solid"
        label = "Paragraph"


class LargeImageBlock(blocks.StructBlock):
    large_image = image_blocks.ImageChooserBlock(label="Large Image", required=True)

    class Meta:
        icon = "fa/object-group-solid"
        label = "Large Image"


class DoubleImageBlock(blocks.StructBlock):
    image_1 = image_blocks.ImageChooserBlock(label="Image 1", required=False)
    image_2 = image_blocks.ImageChooserBlock(label="Image 2", required=False)

    class Meta:
        icon = "fa/object-group-solid"
        label = "Double Image Block"
