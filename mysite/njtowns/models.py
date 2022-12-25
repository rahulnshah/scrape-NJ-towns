# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class ScrapedColleges(models.Model):
    college = models.CharField(primary_key=True, max_length=100)
    town = models.ForeignKey('ScrapedTowns', models.DO_NOTHING, db_column='town', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'scraped_colleges'


class ScrapedTowns(models.Model):
    town = models.CharField(primary_key=True, max_length=100)
    population = models.IntegerField(blank=True, null=True)
    area_in_sq_mi = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    water_area = models.CharField(max_length=100, blank=True, null=True)
    land_area = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    elevation_in_ft = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'scraped_towns'
