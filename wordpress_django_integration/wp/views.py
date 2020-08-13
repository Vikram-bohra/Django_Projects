from django.shortcuts import render, get_object_or_404

from .models import WpPosts,WpWpdevartImages,WpComments,Extra_image,video
from django.http import HttpResponse
from .serializer import data_serializer,image_serializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status


from wp.forms import put_form,update_form,ImageForm,videoform


def demo(request):
    data = WpPosts.objects.get(id = 2713)
    sdata = data.post_content

    return HttpResponse(sdata)


class demo2(APIView):

    def get(self,request):
        stu = WpPosts.objects.all()
        # print(stu)
        serial = data_serializer(stu,many=True)
        # print(serial)
        return Response(serial.data)

    # def put(self, request, pk, format=None):
    #     device = self.get_object(pk)
    #     serializer = data_serializer(device, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def post(self,request):
    #     Fdata = put_form(data = request.POST or None, instance=request.user)
    #     serializer = data_serializer(Fdata, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return HttpResponse("record added")
    #     else:
    #         return HttpResponse("record not added")
    #
    # def post(self, request, format=None):
    #     serializer = data_serializer(data=request.DATA)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def demo3(request):

    data = put_form(request.POST)
    print(data)
    if data.is_valid():
        data.save()
        return HttpResponse("data stored")

        # serializer = data_serializer(Fdata,many=True)
        # if serializer.is_valid():
        #     serializer.save()

    return render(request, "form1.html", {'form': data})


def delete(request,pid):
    data = get_object_or_404(WpPosts,id = pid)
    data.delete()
    return HttpResponse("record deleted")


def update(request,pid):

    try:
        data = get_object_or_404(WpPosts, id=pid)
    except:
        return HttpResponse("wrong ID")
    else:
        fdata = update_form(request.POST, instance=data)
        if fdata.is_valid():
            fdata.save()
            return HttpResponse("record updated")

        fdata = update_form(instance = data)
        return render(request,"update.html",{'form': fdata,})


def image(request):
    data = WpWpdevartImages.objects.all()
    l=[]
    for i in data:
        l.append(i)

    return HttpResponse(l)


def comments(request):
    data = WpComments.objects.get(comment_id = 2)
    ldata = [data.comment_author,data.comment_author_email,data.comment_author_url,data.comment_date,data.comment_author_ip,data.comment_date,data.comment_content,data.comment_agent]

    return HttpResponse(ldata)


def in_image(request):
    data = ImageForm(request.POST, request.FILES)
    v_data = videoform(request.POST,request.FILES)

    print(data)
    if data.is_valid():
        data.save()
        return HttpResponse("image stored")
    if v_data.is_valid():
        v_data.save()
        return HttpResponse("video stored")
    return render(request, "image_in.html", {'form': data,'form1':v_data})


def view_image(request):
    data = Extra_image.objects.all()
    vdata = video.objects.all()
    # fdata = data.name
    return render(request, "image.html", {'form': data,'form1' : vdata,})


class image_api(APIView):

    def get(self,request):
        stu = WpWpdevartImages.objects.all()
        # print(stu)
        serial = image_serializer(stu,many=True)
        # print(serial)
        return Response(serial.data)
