from django.shortcuts import render

from django.shortcuts import render, HttpResponse
from django.shortcuts import render, redirect
from .models import *
from .forms import *

def fan(request):
    fanlar = Subject.objects.all()
    if request.method == 'POST':
        f =FanForm(request.POST)
        if f.is_valid():
            f.save()
        return redirect('/fan/')
    data = {
        'forma':FanForm(),
        'fan': fanlar
    }
    return render(request, 'Subject.html', data)


def teacher(request):
    if request.method == 'POST':
        t = TeacherForm(request.POST)
        if t.is_valid():
            data = t.cleaned_data
            Teacher.objects.create(
                first_name = data.get('first_name'),
                last_name = data.get('last_name'),
                degree = data.get('degree'),
            )
        return redirect("/oqituvchilar/")
    teach = Teacher.objects.all()
    o_t = {
        'forma':TeacherForm(),
        'oqituvchi': teach
    }
    return render(request, 'Teacher.html', o_t)

def teacher_del(request, pk):
    Teacher.objects.filter(id=pk).delete()
    return redirect("/oqituvchilar/")

def teacher_edit(request, pk):
    if request.method == 'POST':
        Teacher.objects.filter(id=pk).update(
            first_name = request.POST.get('f_n'),
            last_name = request.POST.get('l_n'),
            degree = request.POST.get('d')
        )
        return redirect('/oqituvchilar/')
    data = {
        'teacher': Teacher.objects.get(id=pk)
    }
    return render(request, 'teacher_edit.html', data)


def speciality(request):
    if request.method == 'POST':
        s = YonalishForm(request.POST)
        if s.is_valid():
            s.save()
        # Speciality.objects.create(
        #     name = request.POST.get('n'),
        #     code = request.POST.get('c')
        # )
        return redirect("/yonalishlar/")
    yonalish = Speciality.objects.all()
    sy = {
        'forma': YonalishForm(),
        'yonalish': yonalish
    }
    return render(request, 'Speciality.html', sy)


def speciality_del(request, pk):
    Speciality.objects.filter(id=pk).delete()
    return redirect("/yonalishlar")

def speciality_edit(request, pk):
    if request.method == 'POST':
        Speciality.objects.filter(id=pk).update(
            name = request.POST.get('n'),
            code = request.POST.get('c'),
            start_date = request.POST['sd'],
            is_active = request.POST['ia']
        )
        return redirect('/yonalishlar/')
    s = Speciality.objects.get(id=pk)
    data = {
        'yonalishlar': s
    }
    return render(request, 'speciality_edit.html', data)

