from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect


# Create your views here.

def get_rectangle_area(request, width: int, height: int):
    return HttpResponse(f'Площадь прямоугольника размером {width}x{height} равна {width * height}')


def get_square_area(request, width: int):
    return HttpResponse(f'Площадь квадрата размером {width}x{width} равна {width ** 2}')


def get_circle_area(request, radius: int):
    return HttpResponse(f'Площадь круга радиусом {radius} равна {3.14 * (radius ** 2)}')


def rectangle_redirect(request, width: int, height: int):
    return HttpResponseRedirect(f'/calculate_geometry/rectangle/{width}/{height}')


def square_redirect(request, width: int):
    return HttpResponseRedirect(f'/calculate_geometry/square/{width}')


def circle_redirect(request, radius: int):
    return HttpResponseRedirect(f'/calculate_geometry/circle/{radius}')
