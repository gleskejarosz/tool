from django.contrib import admin

from gemba.models import CalculationModel, DowntimeDetail, DowntimeModel, HourModel, LineHourModel, Pareto, \
    ParetoDetail, ScrapDetail, ScrapModel, DowntimeUser, DowntimeGroup, ScrapUser, JobModel2, Editors


class ScrapDetailAdmin(admin.ModelAdmin):
    ordering = ("-id",)
    list_display = ("id", "pareto_date", "scrap", "user", "job", "qty", "pareto_id", "completed", )
    list_display_links = ("id",)
    list_per_page = 20
    fieldsets = [
        ("General", {
            "fields": ["id", "pareto_id", "pareto_date", "scrap", "job", "qty", "user", "completed"],
        }),
    ]
    readonly_fields = ["id", "user"]


class DowntimeDetailAdmin(admin.ModelAdmin):
    @admin.display(description='Pareto date')
    def admin_downtimes(self, obj):
        return obj.pareto_date.strftime('%d-%m-%Y')
    ordering = ("-id",)
    list_display = ("id", "pareto_date", "downtime", "user", "job", "minutes", "pareto_id", "completed", )
    list_display_links = ("id",)
    list_per_page = 20
    fieldsets = [
        ("General", {
            "fields": ["id", "pareto_id", "pareto_date", "downtime", "job", "minutes", "user", "completed"],
        }),
    ]
    readonly_fields = ["id", "user"]


class ParetoDetailAdmin(admin.ModelAdmin):
    ordering = ("-id",)
    list_display = ("id", "pareto_date", "job", "output", "good", "scrap", "pareto_id", "completed", )
    list_display_links = ("id",)
    list_per_page = 20
    fieldsets = [
        ("General", {
            "fields": ["id", "pareto_id", "pareto_date", "job", "output", "good", "scrap", "user", "completed"],
        }),
    ]
    readonly_fields = ["id", "user"]


class ParetoAdmin(admin.ModelAdmin):
    ordering = ("-id",)
    list_display = ("id", "pareto_date", "user", "shift", "hours", "ops", "not_scheduled_to_run",
                    "availability", "performance", "quality", "oee", "completed", )
    list_display_links = ("id",)
    list_per_page = 20
    fieldsets = [
        ("General", {
            "fields": ["id", "user", "pareto_date", "time_stamp", "shift", "hours", "not_scheduled_to_run",
                       "availability", "performance", "quality", "oee", "jobs", "job_otg", "downtimes", "scrap",
                       "ops", "completed"],
        }),
    ]
    readonly_fields = ["id", "user", "jobs", "downtimes", "scrap", "availability", "performance", "quality", "oee"]


class ScrapModelAdmin(admin.ModelAdmin):
    ordering = ("code",)
    list_display = ("code", "description", )
    list_display_links = ("code",)
    list_per_page = 20
    fieldsets = [
        ("General", {
            "fields": ["id", "code", "description"],
        }),
    ]
    readonly_fields = ["id"]


class DowntimeModelAdmin(admin.ModelAdmin):
    ordering = ("code",)
    list_display = ("code", "description", )
    list_display_links = ("code",)
    list_per_page = 20
    fieldsets = [
        ("General", {
            "fields": ["id", "code", "description"],
        }),
    ]
    readonly_fields = ["id"]


class DowntimeGroupModelAdmin(admin.ModelAdmin):
    ordering = ("user",)
    list_display = ("user", "name", "description", "calculation", )
    list_display_links = ("user",)
    list_per_page = 20
    fieldsets = [
        ("General", {
            "fields": ["user", "name", "description", "calculation"],
        }),
    ]
    readonly_fields = []


class DowntimeUserModelAdmin(admin.ModelAdmin):
    ordering = ("id",)
    list_display = ("downtime", "group", "order", "gemba", )
    list_display_links = ("downtime",)
    list_per_page = 20
    fieldsets = [
        ("General", {
            "fields": ["id", "downtime", "group", "order", "gemba"],
        }),
    ]
    readonly_fields = ["id"]


class ScrapUserModelAdmin(admin.ModelAdmin):
    ordering = ("id",)
    list_display = ("scrap", "group", "order", "gemba", )
    list_display_links = ("scrap",)
    list_per_page = 20
    fieldsets = [
        ("General", {
            "fields": ["id", "scrap", "group", "order", "gemba"],
        }),
    ]
    readonly_fields = ["id"]


class JobModelAdmin2(admin.ModelAdmin):
    ordering = ("name",)
    list_display = ("id", "name", "target", "inner_size", "group", )
    list_display_links = ("name",)
    list_per_page = 20
    fieldsets = [
        ("General", {
            "fields": ["id", "name", "target", "inner_size", "group"],
        }),
    ]
    readonly_fields = ["id"]


admin.site.register(Pareto, ParetoAdmin)
admin.site.register(ParetoDetail, ParetoDetailAdmin)
admin.site.register(DowntimeModel, DowntimeModelAdmin)
admin.site.register(DowntimeDetail, DowntimeDetailAdmin)
admin.site.register(HourModel)
admin.site.register(LineHourModel)
admin.site.register(ScrapModel, ScrapModelAdmin)
admin.site.register(ScrapDetail, ScrapDetailAdmin)
admin.site.register(DowntimeUser, DowntimeUserModelAdmin)
admin.site.register(DowntimeGroup, DowntimeGroupModelAdmin)
admin.site.register(ScrapUser, ScrapUserModelAdmin)
admin.site.register(JobModel2, JobModelAdmin2)
admin.site.register(Editors)
