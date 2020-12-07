from django.contrib.gis.db import models
# from django.contrib.gis.db.models.manager import GeoManager

class County(models.Model):
    objectid = models.IntegerField()
    area = models.FloatField()
    perimeter = models.FloatField()
    county3_field = models.FloatField()
    county3_id = models.FloatField()
    county = models.CharField(max_length=20)
    shape_leng = models.FloatField()
    shape_area = models.FloatField()
    geom = models.MultiPolygonField(srid=4236)

    def __unicode__(self):
        return self.county
    class Meta:
        ordering=('objectid',)
        verbose_name_plural='Counties'

class Headquarter(models.Model):
    name = models.CharField(max_length=100)
    location = models.PointField(srid=4326)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    # objects = GeoManager()
    def __unicode__(self):
        return self.name
    class Meta:
        ordering=('name',)
        verbose_name_plural='Headquarters'

class RegionalOffice(models.Model):
    name = models.CharField(max_length=100)
    location = models.PointField(srid=4326)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    headquarter = models.ForeignKey(Headquarter, on_delete=models.CASCADE)
    description = models.CharField(max_length=50)
    # objects = GeoManager()
    def __unicode__(self):
        return self.name
    class Meta:
        ordering=('name',)
        verbose_name_plural='RegionalOffices'

class FieldOffice(models.Model):
    name = models.CharField(max_length=100)
    location = models.PointField(srid=4326)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    number_of_staff = models.IntegerField()
    ISSUE_CHOICES = [
        ('WATER', 'Water'),
        ('EROSION', 'Erosion'),
        ('EDUCATION', 'Education'),
        ('HEALTH', 'Health'),
        ]
    issue = models.CharField(
        max_length=100,
        choices=ISSUE_CHOICES,
        default='WATER',
    )
    
    region = models.ForeignKey(RegionalOffice, on_delete=models.CASCADE)
    # objects = GeoManager()
    def __unicode__(self):
        return self.name
    class Meta:
        ordering=('name',)
        verbose_name_plural='FieldOffices'