from django.shortcuts import render

# Create your views here.
def index(request): # 사용자가 접근할 때 호출될 뷰 함수
    data = [
        {"item": "장편", "cnt": 4913},
        {"item": "단편", "cnt": 3316},
        {"item": "옴니버스", "cnt": 591},
        {"item": "기타", "cnt": 106}
    ]

    # 'index.html'라는 문서에서 렌더링합니다.
    # 'index.html'라는 탬플릿 문서에서 'movieinfo'라는 이름으로 접근할 수 있습니다.
    return render(request, 'index.html', {'movieinfo': data})
# end def