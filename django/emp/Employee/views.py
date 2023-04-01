from django.shortcuts import redirect, render
from .models import Employee


# Create your views here.
def create(request):
    if request.method == 'POST':
        name = request.POST['emp_name']
        email = request.POST['emp_email']
        address = request.POST['emp_address']
        phone = request.POST['emp_phone']
        var = Employee(emp_name=name,emp_email=email,emp_address=address,emp_phone=phone)
        var.save()        
    return render(request,"create.html")


def list1(request):
    employees = Employee.objects.filter(is_delete=0).all()
    # OR
    # employees = Employee.objects.exclude(is_delete=1).all()
    
    context = {
        'employees': employees,
    }
    return render(request, 'list.html',context)


def edit(request, emp_id):
    employees = Employee.objects.get(emp_id = emp_id)
    print(employees)
    contact = {
        'employees':employees
    }
    return render(request,"edit.html", contact)


def updaterecord(request, emp_id):
    name = request.POST['emp_name']
    email = request.POST['emp_email']
    address = request.POST['emp_address']
    phone = request.POST['emp_phone']
    empl = Employee.objects.get(emp_id = emp_id)
    empl.emp_name = name
    empl.emp_email = email
    empl.emp_address = address
    empl.emp_phone = phone
    empl.save()
    empl = Employee.objects.filter(emp_id=emp_id).update(is_delete=0)
    return redirect('list')


# def delete(request, emp_id):
#     Employee.objects.filter(emp_id=emp_id).delete()
#     return render(request,"create.html")


def delete(request, emp_id):
    Employee.objects.filter(emp_id=emp_id).update(is_delete=1)
    return redirect('list')