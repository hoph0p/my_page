from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

# Create your views here.
week_dict = {
    'monday': 'Понедельник',
    'tuesday': 'Вторник',
    'wednesday': 'Среда',
    'thursday': 'Четверг',
    'friday': 'Пятница',
    'saturday': 'Суббота',
    'sunday': 'Воскресение',
}


def get_info_by_week_day(request, week_name: str):
    description = week_dict.get(week_name)
    if description:
        return HttpResponse(description)
    else:
        return HttpResponseNotFound(f'Нет такого дня - {week_name}')


def get_response_by_num(request, week_name: int):
    days = list(week_dict)
    if week_name > len(days):
        return HttpResponseNotFound(f'Неверный номер дня - {week_name}')
    name_day = days[week_name - 1]
    redirect_url = reverse("todo", args=(name_day,))
    return HttpResponseRedirect(redirect_url)


def get_response(request):
    return render(request, 'week_days/greeting.html')
