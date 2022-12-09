from django.conf import settings
from django.db import models

from tools.models import JobModel

AM = "Morning shift"
PM = "Afternoon shift"
NS = "Night shift"
SHIFT_CHOICES = (
    ("--", "No choice"),
    (AM, "Morning shift"),
    (PM, "Afternoon shift"),
    (NS, "Night shift"),
)
HOUR_CHOICES = (
    ("6", "6"),
    ("7", "7"),
    ("8", "8"),
    ("9", "9"),
    ("10", "10"),
    ("11", "11"),
    ("12", "12"),
)


class Pareto(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.SET_NULL, blank=True, null=True)
    pareto_date = models.DateField()
    shift = models.CharField(max_length=32, choices=SHIFT_CHOICES, default="--")
    hours = models.CharField(max_length=32, choices=HOUR_CHOICES, default=8)
    time_stamp = models.TimeField()
    completed = models.BooleanField(default=False)
    jobs = models.ManyToManyField("ParetoDetail")
    downtimes = models.ManyToManyField("DowntimeDetail")
    scrap = models.ManyToManyField("ScrapDetail")

    def __str__(self):
        return f"{self.pareto_date}"

    class Meta:
        verbose_name = "Pareto"


class ParetoDetail(models.Model):
    job = models.ForeignKey(JobModel, on_delete=models.CASCADE, related_name="jobs", blank=False, null=False)
    qty = models.PositiveIntegerField(default=0)
    good = models.PositiveIntegerField(default=0)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, blank=True, null=True)
    completed = models.BooleanField(default=False)
    pareto_id = models.PositiveIntegerField(default=0)
    pareto_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.job}"

    class Meta:
        verbose_name = "Pareto Detail"


class DowntimeModel(models.Model):
    code = models.CharField(max_length=10, blank=False, null=False)
    description = models.CharField(max_length=64, blank=False, null=False)

    def __str__(self):
        return f"{self.code} - {self.description}"

    class Meta:
        verbose_name = "Downtime"


class DowntimeDetail(models.Model):
    downtime = models.ForeignKey(DowntimeModel, on_delete=models.CASCADE, related_name="downtime", blank=False,
                                 null=False)
    job = models.ForeignKey(JobModel, on_delete=models.CASCADE, related_name="jobs5", blank=False, null=False)
    minutes = models.PositiveIntegerField(default=0, blank=False, null=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, blank=True, null=True)
    completed = models.BooleanField(default=False)
    pareto_id = models.PositiveIntegerField(default=0)
    pareto_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.downtime}"

    class Meta:
        verbose_name = "Downtime Detail"


class DowntimeGroup(models.Model):
    name = models.CharField(max_length=10, blank=False, null=False)
    description = models.CharField(max_length=64, blank=False, null=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, blank=True, null=True, unique=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "User Group Name"


class DowntimeUser(models.Model):
    downtime = models.ForeignKey(DowntimeModel, on_delete=models.CASCADE, related_name="downtime_user", blank=False,
                                 null=False)
    group = models.ForeignKey(DowntimeGroup, on_delete=models.CASCADE, related_name="downtime_group", blank=False,
                              null=False)
    order = models.PositiveIntegerField(blank=True, null=True)

    def __str__(self):
        return f"{self.downtime}"

    class Meta:
        verbose_name = "Downtime vs Group"


class ScrapModel(models.Model):
    code = models.CharField(max_length=10, blank=False, null=False)
    description = models.CharField(max_length=64, blank=False, null=False)

    def __str__(self):
        return f"{self.code} - {self.description}"

    class Meta:
        verbose_name = "Scrap reason"


class ScrapDetail(models.Model):
    scrap = models.ForeignKey(ScrapModel, on_delete=models.CASCADE, related_name="scrap", blank=False, null=False)
    job = models.ForeignKey(JobModel, on_delete=models.CASCADE, related_name="jobs3", blank=False, null=False)
    qty = models.PositiveIntegerField(default=0, blank=False, null=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, blank=True, null=True)
    completed = models.BooleanField(default=False)
    pareto_id = models.PositiveIntegerField(default=0)
    pareto_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.scrap}"

    class Meta:
        verbose_name = "Scrap detail"


class ScrapUser(models.Model):
    scrap = models.ForeignKey(ScrapModel, on_delete=models.CASCADE, related_name="scrap_user", blank=False,
                              null=False)
    group = models.ForeignKey(DowntimeGroup, on_delete=models.CASCADE, related_name="scrap_group", blank=False,
                              null=False)
    order = models.PositiveIntegerField(blank=True, null=True)

    def __str__(self):
        return f"{self.scrap}"

    class Meta:
        verbose_name = "Scrap vs Group"


class HourModel(models.Model):
    start = models.TimeField()

    def __str__(self):
        return f"{self.start}"

    class Meta:
        verbose_name = "Start hour"


class LineHourModel(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, blank=False, null=True)
    start = models.ForeignKey(HourModel, on_delete=models.CASCADE, related_name="starts", blank=False,
                              null=False)
    shift = models.CharField(max_length=32, choices=SHIFT_CHOICES, blank=False, null=False)

    def __str__(self):
        return f"{self.start}"

    class Meta:
        verbose_name = "Line start hour"

