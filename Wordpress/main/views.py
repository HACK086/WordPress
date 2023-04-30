# Импортирование необходимых модулей и моделей из приложения
from django.shortcuts import render, get_object_or_404
from .models import Section, Subsection



def section_list(request):
    # Получение списка всех объектов разделов
    sections = Section.objects.all()
    # Отображение списка разделов в шаблоне 'main/section_list.html' с использованием функции render()
    return render(request, 'main/section_list.html', {'sections': sections})

def subsection_list(request, section_id):
    # Получение списка всех подразделов, связанных с определенным разделом
    subsections = Subsection.objects.filter(section=section_id)
    # Отображение списка подразделов в шаблоне 'main/subsection_list.html' с использованием функции render()
    return render(request, 'main/subsection_list.html', {'subsections': subsections})

def subsection_detail(request, subsection_id):
    # Получение подробной информации о конкретном подразделе
    subsection = get_object_or_404(Subsection, id=subsection_id)
    # Отображение информации о подразделе в шаблоне 'main/subsection_detail.html' с использованием функции render()
    return render(request, 'main/subsection_detail.html', {'subsection': subsection})
