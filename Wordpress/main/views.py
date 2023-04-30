from django.shortcuts import render
from .models import Section, Subsection
from django.shortcuts import render, get_object_or_404

def section_list(request):
    sections = Section.objects.all()
    return render(request, 'main/section_list.html', {'sections': sections})

def subsection_list(request, section_id):
    subsections = Subsection.objects.filter(section=section_id)
    return render(request, 'main/subsection_list.html', {'subsections': subsections})

def subsection_detail(request, subsection_id):
    subsection = get_object_or_404(Subsection, id=subsection_id)
    return render(request, 'main/subsection_detail.html', {'subsection': subsection})
