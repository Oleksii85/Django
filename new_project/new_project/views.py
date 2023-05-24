from django.http import HttpResponse


def blogs(request):
    return HttpResponse("однажды там будут блоги :)")


def about(request):
    return HttpResponse("тут будет страница с описанием нашего блога")


def slugs(request, slug):
    return HttpResponse(f"страница для просмотра {slug} блога")


def comment(request, slug):
    return HttpResponse(f"добавления коментария к посту {slug}")


def create(request):
    return HttpResponse("Создание нового поста")


def update(request, slug):
    return HttpResponse(f"Обновление существующего поста {slug}")


def delete(request, slug):
    return HttpResponse(f"Удаление поста {slug}")


def profile(request, username):
    return HttpResponse(f"Личная страница пользователя {username}")


def change_pass(request):
    return HttpResponse("Страничка для смены пароля")


def register(request):
    return HttpResponse("Регистрация пользователя")


def login(request):
    return HttpResponse("Логин")


def logout(request):
    return HttpResponse("Логаут")
