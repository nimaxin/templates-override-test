from starlette_admin.contrib.sqla import ModelView

from .models import Product


class ProductAdmin(ModelView):
    pass


product_admin = ProductAdmin(Product)
