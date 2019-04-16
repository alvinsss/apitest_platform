import xadmin
# Register your models here.
from project.models import Project
from module.models import Module


class ProjectAdmin(object):
	list_display = ['name', 'describe', 'status', 'create_time', 'update_time']
	search_fields = ['name', 'describe', 'status', 'update_time']
	list_filter = ['name', 'describe', 'status', 'create_time', 'update_time']


xadmin.site.register(Project, ProjectAdmin)


class ModuleAdmin(object):
	list_display = ['project', 'describe', 'name', 'create_time']
	search_fields = ['project', 'describe', 'name']
	list_filter = ['project', 'describe', 'name', 'create_time']


xadmin.site.register(Module, ModuleAdmin)
