from abc import update_abstractmethods
from django.forms import JSONField
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from .models import Roster, StudentData
from .models import Item
from .models import CertForm
from .forms import CreateNewList, SearchNewList

from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics, status
from .serializers import DataFormSerializer, ItemSerializer #CreateItemSerializer
from .serializers import CertFormSerializer

from django.views.generic import TemplateView

# Create your views here.

def index(response):
    return HttpResponse("<h1>Welcome Home!</h1>")


def index2(response, id):
    ls = Roster.objects.get(id=id)
    return HttpResponse("<h1>%s</h1>" %ls.name)


def index3(response, name):
    ls = Roster.objects.get(name=name)
    return HttpResponse("<h1>%s</h1>" %ls.name)

def index3(response, name):
    ls = Roster.objects.get(name=name)
    item = ls.item_set.get(id=1)
    return HttpResponse("<h1>%s</h1><br></br><p>%s</p>" %(ls.name, str(item.text)))


@api_view(['GET'])
def apiOverview(request):
    StudentInfo_urls = {
        'List':'/item-list/',
        'Detail View':'/item-detail/<str:pk>',
        'Create':'/item-create/',
        'Update':'/item-update/<str:pk>',
        'Delete':'/item-delete/<str:pk>',

        'Cert List':'/cert-list/',
        'Cert Create':'/cert-create/',
        'Cert Update':'/cert-update/<str:pk>',

        'Data List' :'/data-list/',
        'Data Create':'/data-create/',
        'Data Delete':'/data-delete/<str:pk>',
        
    }

    return Response(StudentInfo_urls)


@api_view(['GET'])
def itemList(request):
    items = Item.objects.all()
    serializer = ItemSerializer(items, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def itemDetail(request, pk):
    items = Item.objects.get(id=pk)
    serializer = ItemSerializer(items, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def itemCreate(request):
    serializer = ItemSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['POST'])
def itemUpdate(request, pk):
    item = Item.objects.get(id=pk)
    serializer = ItemSerializer(instance=item, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['DELETE'])
def itemDelete(request, pk):
    item = Item.objects.get(id=pk)
    item.delete()

    return Response("Item is deleted!")


class CertFormView(APIView):
    seralizer_class = CertFormSerializer

    def get_queryset(self):
        certForm = Item.objects.all()
        return certForm

    def post(self,request, *args, **kwargs):
        certform_data = request.data
        #new_certification = Item.objects.filter(wid=certform_data["wid"], lastName=certform_data["lastName"])
        #new_certification.save()
        #serializer = CertFormSerializer(new_certification)
        return JsonResponse("sample signature", safe=False)


@api_view(['GET'])
def certList(request):
    items = Item.objects.all()
    serializer = CertFormSerializer(items, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def certCreate(request):
    serializer = CertFormSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['POST'])
def certUpdate(request, pk):
    item = Item.objects.get(id=pk)
    serializer = CertFormSerializer(instance=item, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


def dataCreate(request):
    form = CreateNewList(request.POST)

    if form.is_valid():
        #obj = StudentData(form.cleaned_data["firstname","lastname","wid","courses"])
        #obj.save()

        obj = form.save()

        return HttpResponseRedirect("/data-create/")
    else:
        form = CreateNewList()
    return render(request, "StudentInfo/create.html", {"form":form})


@api_view(['GET'])
def dataList(request):
    things = StudentData.objects.all()
    serializer = DataFormSerializer(things, many=True)
    return Response(serializer.data)
    
@api_view(['DELETE'])
def dataDelete(request, pk):
    item = StudentData.objects.get(id=pk)
    item.delete()
    return HttpResponseRedirect("/data-delete/")


def dataSearch(request):
    form = CreateNewList(request.GET)
    if request.method == 'GET':
            datainfo = StudentData.objects.filter(id=6)
            serializer = DataFormSerializer(datainfo, many=True)
            return JsonResponse(serializer.data, safe=False)
    else:
        form = CreateNewList()
    return render(request, "StudentInfo/dataset.html", {"form":form})

'''
def dataSearch(request):
    form = CreateNewList(request.GET)

    if form in StudentData:
        datastudent = StudentData.objects.all()
        
        args = {"form":form, 'datastu': datastudent}
        return render(request, "StudentInfo/result.html", args)
    else:
        form = CreateNewList()

    return render(request, "StudentInfo/dataset.html", {"form":form})
'''

#print(StudentData.objects.all().query)



'''
template_name = "StudentInfo/dataset.html/"
    
def dataSearch(self, request):
    form = CreateNewList()
    datastudent = StudentData.objects.all()

    args = {"form":form, 'posts': datastudent}
    return render(request, self.template_name, args)
'''

'''
def dataSearch(request):
    header = "Data Set"
    form = SearchNewList(request.POST or None)
    queryset = StudentData.objects.all()
    context = {
        "form": form,
        "header": header,
        "queryset": queryset,
    }
    if request.method == 'POST':
        queryset = StudentData.objects.filter(firstname__icontains=form['firstname'].value(),
                                              lastname__icontains=form['item_name'].value(),
                                              wid__icontains=form['wid'].value(),
                                              courses__icontains=form['courses'].value()
                                              )
        context = {
        "form": form,
        "header": header,
        "queryset": queryset,
    }
    return render(request, "StudentInfo/dataset.html",{"form":form})
'''

    
'''
class DataFormView(APIView):
    seralizer_class = DataFormSerializer

    def get_queryset(self):
        certForm = Item.objects.all()
        return certForm

    def post(self,request, *args, **kwargs):
        form_data = request.data
        datacheck = StudentData.objects.filter(wid=form_data["wid"], lastname=form_data["lastname"])
        #datacheck.save()
        #serializer = CertFormSerializer(datacheck)
        return JsonResponse("Encryted-Signature", safe=False)
'''

"""
data = Students.objects.all()
stu = {
    "student_number": data
}
return render_to_response("login/profile.html", stu)



class ItemView(generics, ListAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class CreateItemView(APIView):
    serializer_class = CreateItemSerializer

    def post(self, request, format=None):
        if not self.request.session.exists(self.request.session.session_key):
            self.request.session.create()

        serializer2 = self.serializer_class(data=request.data)
        if serializer2.is_valid():
            text = serializer2.data.get('text')
            host = self.request.session.session_key
            queryset = Item.objects.filter(host=host)
            if queryset.exists():
                item = queryset[0]
                item.text = text
                item.save(update_fields=['text'])
            else:
                item = Item(host=host, text=text)
                item.save()
            
            return Response(ItemSerializer(item).data, status=status.HTTP_200_OK)
"""