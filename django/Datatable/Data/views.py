from django.shortcuts import render
from .models import Member
from rest_framework.decorators import api_view
from django.http.response import JsonResponse
from .serializers import MemberSerializer


# Create your views here.


def home(request):
    return render(request,'index.html')

def index(request):

    # all_member = Member.objects.all()
    count = Member.objects.count()
    # member_list=[]
    # for i in all_member:    
    #     serializer = MemberSerializer(i).data
    #     member_list.append(serializer)

    search           =       str(request.GET['search[value]'])
    offset           =       int(request.GET['start'])
    sort_value       =       str(request.GET['order[0][dir]'])
    limit            =       int(request.GET['length']) 
    column           =       int(request.GET['order[0][column]']) # get column no
    columns          =       ['id','firstname']
    sortable_col     =       str(columns[column])
    my_list          =       [column for i in columns]

    no = 0
    no = no+offset

    # for sorting
    if search   ==  "":
        print(columns)
        if sort_value   ==      "asc":
            searchh = Member.objects.all().order_by(sortable_col)[offset:limit+offset]
        else:
            searchh = Member.objects.all().reverse()[offset:limit+offset]
        
        search_data = [searchh.get_data() for searchh in searchh]
        
        #  for Extra Column Add
        for data in search_data:
            no = no+1
            data["sr_no"] = no
            button = '<td class="text-end"><div class="dropdown dropdown-action">'
            if my_list:
                data['action'] = button+'<a href="#" class="action-icon dropdown-toggle" data-bs-toggle="dropdown" aria-expanded="false"><i class="material-icons">more_vert</i></a><div class="dropdown-menu dropdown-menu-right"><a class="dropdown-item" href="#" data-bs-toggle="modal" id="role_edit" onclick="edit_kitchen('+str(data['firstname'])+')" ><i class="fa fa-pencil m-r-5" ></i> Edit</a><a class="dropdown-item" href="#" data-bs-toggle="modal" onclick="remove_kitchen('+str(data['firstname'])+')"><i class="fa fa-trash-o m-r-5"></i> Delete</a></div></div></td>'
            else:
                data['action'] = "No Access"

        all_records     = {
                            "recordsTotal"      :   count,      #Total no of records in the database
                            "recordsFiltered"   :   count,      #Mandatory data for the datatable
                            "data"              :   search_data,    
                        }
        return JsonResponse(all_records,safe=False,content_type = "application/json")


    else:
        # For Searching
        searchh = Member.objects.filter(firstname__icontains=search)
        search_data = [searchh.get_data() for searchh in searchh]
        print(search)

        all_records      = {
                            "recordsTotal"      :   count,      #Total no of records in the database
                            "recordsFiltered"   :   count,      #Mandatory data for the datatable
                            "data"              :   search_data,    
                        }
    return JsonResponse(all_records,safe=False,content_type = "application/json")