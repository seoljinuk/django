import csv
from django.conf import settings
from django.core.management.base import BaseCommand
# from kmdb.models import Movie
from Application.kmdb.models import Movie

# 실행하는 방법
# pip install django-extensions 우선 설치합니다.
# python manage.py runscript import_movies

class Command(BaseCommand):
    help = 'Load data from kmdb.csv into the movies table'

    def handle(self, *args, **kwargs):
        # CSV 파일 경로
        csv_file_path = 'kmdb_get_movie_list_100_new.csv'

        # CSV 파일 열기
        with open(csv_file_path, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                Movie.objects.create(
                    moviecd=row['MOVIECD'],
                    movienm=row['MOVIENM'],
                    movienmen=row.get('MOVIENMEN', None),  # 데이터가 없을 수 있으므로 get 사용
                    prdtyear=row['PRDTYEAR'],
                    opendt=row['OPENDT'],
                    typenm=row.get('TYPENM', None),
                    prdtstatnm=row.get('PRDTSTATNM', None),
                    nationalt=row.get('NATIONALT', None),
                    genrealt=row.get('GENREALT', None),
                    repnationnm=row.get('REPNATIONNM', None),
                    repgenrenm=row.get('REPGENRENM', None),
                    year=row.get('YEAR', None),
                    year_momth=row.get('YEAR_MOMTH', None),
                )
        self.stdout.write(self.style.SUCCESS('Data successfully imported into the movies table.'))
# end class Command