from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

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
        return HttpResponse(f'{description}')
    else:
        return HttpResponseNotFound(f'Нет такого дня - {week_name}')


def get_response_by_num(request, week_name: int):
    if week_name > 0 and week_name < 8:
        return HttpResponse(f'Сегодня {week_name} день недели')
    else:
        return HttpResponseNotFound(f'Неверный номер дня - {week_name}')
