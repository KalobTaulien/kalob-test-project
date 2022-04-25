from django.db import models
from wagtail.documents.models import AbstractDocument, Document
from wagtail.images.models import AbstractImage, AbstractRendition, Image


class CustomDocument(AbstractDocument):
    admin_form_fields = Document.admin_form_fields


class CustomImage(AbstractImage):
    admin_form_fields = Image.admin_form_fields


class CustomRendition(AbstractRendition):
    image = models.ForeignKey(
        CustomImage, on_delete=models.CASCADE, related_name="renditions"
    )

    class Meta:
        unique_together = (("image", "filter_spec", "focal_point_key"),)
