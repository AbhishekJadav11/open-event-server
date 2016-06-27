from flask_admin import expose

from open_event.helpers.data_getter import DataGetter
from super_admin_base import SuperAdminBaseView


class SuperAdminTrashView(SuperAdminBaseView):
    @expose('/')
    def index_view(self):
        return self.render('/gentelella/admin/super_admin/trash/trash.html')
