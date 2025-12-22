from django.shortcuts import render, HttpResponse

# request - запрос
# respobse - ответ

#def test(request):
#return HttpResponse(f"{request.__dict__}")

# def test(request):
#     return render(request, 'index.html', {})

# def test2(request):
#     return HttpResponse("Салам я кастомная страница")

# def tests(request):
#     return render(request, 'second.html', {})

# def tests2(request):
#     return HttpResponse("ТЫ ЕБЛАН НАХУЙ ТЕБЕ ТУТ")
# _____________________________________________________________

# Контекст в шаблонах, ссылку

def main_view(request):
    return render(request, 'main_page.html',{})

def contacts_view(request):
    return render(request, 'contacts-page.html',{})
