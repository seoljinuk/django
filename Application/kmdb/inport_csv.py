# movies/import_csv.py
import csv
# from movies.models import Movie
from Application.kmdb.models import Movie

def import_movies_from_csv(file_path):
    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            Movie.objects.create(
                moviecd=row['moviecd'],
                movienm=row['movienm'],
                movienmen=row['movienmen'],
                prdtyear=int(row['prdtyear']),
                opendt=int(row['opendt']),
                typenm=row['typenm'],
                prdtstatnm=row['prdtstatnm'],
                nationalt=row['nationalt'],
                genrealt=row['genrealt'],
                repnationnm=row['repnationnm'],
                repgenrenm=row['repgenrenm']
                # CSV 파일의 열에 맞게 필드를 추가합니다.
            )
        # end for
    # end with
#end def

csvfile = 'kmdb_get_movie_list_100_new.csv'
import_movies_from_csv(csvfile)