# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models


class ProductAttributeValue(models.Model):
    _inherit = "product.attribute.value"

    website_product_detail_image = fields.Binary(
        string="Website detail image",
        attachment=True,
        help="Image of the attribute value for shop online product detail.",
    )
