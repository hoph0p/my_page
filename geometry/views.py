from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse


# Create your views here.

def get_rectangle_area(request, width: int, height: int):
    result_area = width * height
    return HttpResponse(f'Площадь прямоугольника размером {width}x{height} равна {result_area}')


def get_square_area(request, width: int):
    result_area = width ** 2
    return HttpResponse(f'Площадь квадрата размером {width}x{width} равна {result_area}')


def get_circle_area(request, radius: int):
    result_area = 3.14 * (radius ** 2)
    return HttpResponse(f'Площадь круга радиусом {radius} равна {result_area}')


def rectangle_redirect(request, width: int, height: int):
    return HttpResponseRedirect(f'/calculate_geometry/rectangle/{width}/{height}')


def square_redirect(request, width: int):
    return HttpResponseRedirect(f'/calculate_geometry/square/{width}')


def circle_redirect(request, radius: int):
    return HttpResponseRedirect(f'/calculate_geometry/circle/{radius}')


