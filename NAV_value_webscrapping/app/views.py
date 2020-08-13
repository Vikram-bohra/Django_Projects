from django.views.generic.base import TemplateView
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import NameForm, RegisterForm
from django.contrib.auth.decorators import login_required
from .models import NAV_Details
from django.contrib.auth.models import User
class Nav_view(TemplateView):
    def get(self, request):
        form = NameForm()
        data = NAV_Details.objects.filter(usr = request.user).order_by("-id")
        return render(request, "Nav.html", {'form': form,'data':data})

    def post(self, request):
        form = NameForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['name']

        import requests
        from bs4 import BeautifulSoup
        import csv

        nav_url = "https://www.amfiindia.com/nav-history-download"
        nav_response = requests.get(nav_url)

        nav_soup = BeautifulSoup(nav_response.text, "html.parser")

        fin = nav_soup.find_all('a', href=True, attrs={'style': 'color:#20A7A4'})

        fin_url = "https://www.amfiindia.com" + fin[0]['href']

        # r = requests.get("https://www.amfiindia.com/spages/NAVAll.txt?t=23012020105639")
        r = requests.get(fin_url)

        soup = BeautifulSoup(r.text, "html.parser")

        st = str(soup.text)
        new_st = st.split("\n")

        new_lst = []
        for i in new_st:
            new_lst.append(i.split(";"))

        # code = "119551"
        # code = "147712"
        code = text
        print("\n\n\n\n",code, "\n\n\n", len(new_lst))
        lst = []
        # temp = []
        for i in new_lst:
            if i[0] == code:
                print("ok")
                lst.append(i)
                # temp.append(i)
                # # temp[0].pop(2)
                # with open ("data.csv", "a", newline = "") as csvfile:
                #     movies = csv.writer(csvfile)
                #     movies.writerow(temp[0])
                # break
        print(lst)
        if len(lst) == 0:
            return HttpResponse("code dose not match")

        NAV_Details.objects.create(code = int(lst[0][0]), isin = lst[0][1], name = lst[0][2], nav = lst[0][-2], date = lst[0][-1],usr = request.user)
        data = NAV_Details.objects.filter(usr = request.user).order_by("-id")
        arg = {
            'form' : form,
            'data' : data,
        }
        return render(request, "Nav.html", arg)

def Register_View(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = RegisterForm()
    return render(request,"registration/register.html",{'form':form})

def home(request):
    return render(request,"sds.html")