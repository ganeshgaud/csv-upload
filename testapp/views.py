from django.shortcuts import render
from .models import Student
from .forms import StudentForm
import csv,io
from django.contrib import messages

def file_upload(request):
    template='csvupload.html'
    context={
    'msg':'Please upload valid file only'
    }
    if request.method=='GET':
        return render(request,template,context)

    csv_file=request.FILES['file']

    if not csv_file.name.endswith('.csv'):
        messages.error(request,"Please upload Valid CSV FILE ONLY")

    data_set=csv_file.read().decode('UTF-8')
    print(data_set)
    io_string=io.StringIO(data_set)
    print(io_string)
    next(io_string)
    for column in csv.reader(io_string, delimiter=',', quotechar='|'):
        _, created=Student.objects.update_or_create(
            username=column[0],
            college_name=column[1],
            std_cell_no=column[2],
            emai_id=column[3],
        )
    context1={}
    return render(request,template,context1)
