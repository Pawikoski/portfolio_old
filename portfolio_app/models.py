from django.db import models

# Create your models here.
class Technology(models.Model):
    name = models.CharField(max_length=40)

    class Meta:
        verbose_name = "Technology"
        verbose_name_plural = "Technologies"
    
    def __str__(self):
        return self.name


class Framework(models.Model):
    name = models.CharField(max_length=40)

    class Meta:
        verbose_name = "Framework"
        verbose_name_plural = "Frameworks"
    
    def __str__(self):
        return self.name


class Tool(models.Model):
    name = models.CharField(max_length=65)

    class Meta:
        verbose_name = "Tool"
        verbose_name_plural = "Tools"
    
    def __str__(self):
        return self.name


class Ide(models.Model):
    name = models.CharField(max_length=65)

    class Meta:
        verbose_name = "IDE"
        verbose_name_plural = "IDEs"
    
    def __str__(self):
        return self.name


class OperatingSystem(models.Model):
    name = models.CharField(max_length=65)

    class Meta:
        verbose_name = "Operating system"
        verbose_name_plural = "Operating systems"
    
    def __str__(self):
        return self.name

# TODO: custom manage.py command to add base values to models above

class About(models.Model):
    technologies = models.ManyToManyField(Technology)
    frameworks = models.ManyToManyField(Framework)
    tools = models.ManyToManyField(Tool)
    ides = models.ManyToManyField(Ide)
    operating_systems = models.ManyToManyField(OperatingSystem)

    total_exp_years = models.PositiveSmallIntegerField(verbose_name="Total experience (in years)", default=0)
    current_employer = models.CharField(max_length=65, default="Unemployed")
    current_employer_website = models.URLField(verbose_name="Current employer website (ex. Linkedin profile) [optional]", null=True, blank=True)

    class Meta:
        verbose_name = "About section"
        verbose_name_plural = "About section"

    def save(self, *args, **kwargs):
        if self.__class__.objects.count():
            self.pk = self.__class__.objects.first().pk
        super().save(*args, **kwargs)


class Social(models.Model):
    name = models.CharField(verbose_name="Name", max_length=45)
    url = models.URLField(verbose_name="URL", max_length=200)
    icon = models.CharField(verbose_name="FontAwesome icon (html i tag)", max_length=80)