from django.shortcuts import render,HttpResponse
from .form import fill_form,file_upload_form
# from .train import *
from .models import file_upload
from .random_test import *
def train_again(request):

    if request.method == "POST":
        data = file_upload_form(request.POST,request.FILES)
        if data.is_valid():
            data.save()
            file = file_upload.objects.all().order_by('-id')
            name = file[0].file
            retrain(name)
            return HttpResponse("Model retrained")
    else:
        data = file_upload_form()

    return render(request,"file_upload.html",{'form':data})


def pred(request):
    # modeltrain('train.csv')
    if request.method == 'POST':
        data = fill_form(request.POST)
        if data.is_valid():
            gender = data.cleaned_data.get('gender')
            married = data.cleaned_data.get('married')
            dependents = data.cleaned_data.get('dependents')
            education = data.cleaned_data.get('education')
            self_emp = data.cleaned_data.get('self_emp')
            ApplicantIncome = data.cleaned_data.get('ApplicantIncome')
            CoapplicantIncome = data.cleaned_data.get('CoapplicantIncome')
            LoanAmount = data.cleaned_data.get('LoanAmount')
            Loan_Amount_Term = data.cleaned_data.get('Loan_Amount_Term')
            Credit_History = data.cleaned_data.get('Credit_History')
            prop_area = data.cleaned_data.get('prop_area')
            val = []
            temp = list([int(gender),int(married),int(dependents),int(education),int(self_emp),ApplicantIncome,CoapplicantIncome,LoanAmount,Loan_Amount_Term,int(Credit_History),int(prop_area)])
            val.extend(temp)
            ans = predict(val)
            return HttpResponse(ans)
    else:
        data = fill_form()

    return render(request,"form.html",{'form':data})