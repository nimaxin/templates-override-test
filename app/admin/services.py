from starlette_admin.contrib.sqla import Admin

from app.db.services import engine
from app.product.admin import product_admin

admin = Admin(engine=engine, base_url="/panel", route_name="panel")


def register_admin(app):
    admin.add_view(product_admin)

    admin.mount_to(app)
