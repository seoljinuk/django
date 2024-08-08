from django.db import models

# Create your models here.

class Movie(models.Model):
    moviecd = models.BigIntegerField(primary_key=True)  # NUMBER(10)와 대응
    movienm = models.CharField(max_length=255, blank=True, null=True)  # VARCHAR2(255)
    movienmen = models.CharField(max_length=255, blank=True, null=True)  # VARCHAR2(255)
    prdtyear = models.IntegerField(blank=True, null=True)  # NUMBER(6)
    opendt = models.BigIntegerField(blank=True, null=True)  # NUMBER(10)
    typenm = models.CharField(max_length=255, blank=True, null=True)  # VARCHAR2(255)
    prdtstatnm = models.CharField(max_length=255, blank=True, null=True)  # VARCHAR2(255)
    nationalt = models.CharField(max_length=255, blank=True, null=True)  # VARCHAR2(255)
    genrealt = models.CharField(max_length=255, blank=True, null=True)  # VARCHAR2(255)
    repnationnm = models.CharField(max_length=255, blank=True, null=True)  # VARCHAR2(255)
    repgenrenm = models.CharField(max_length=255, blank=True, null=True)  # VARCHAR2(255)
    year = models.IntegerField(blank=True, null=True)  # NUMBER
    year_momth = models.IntegerField(blank=True, null=True)  # NUMBER

    class Meta:
        db_table = 'movies'  # 테이블 이름을 'movies'로 지정

    def __str__(self):
        return self.movienm  # 영화 이름을 반환
# end class Movie