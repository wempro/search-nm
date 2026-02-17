
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .forms import UserLoginForm,CSVUploadForm
from django.db.models import Q
import csv, io,os
from django.core.files.base import ContentFile
# from django.core.files.storage import default_storage
from django.core.files.storage import FileSystemStorage
import pandas as pd
from .models import Products, File
from django.http import JsonResponse, HttpResponse,FileResponse
from django.contrib.auth.decorators import login_required

def LoginView(request):
    
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            print(username)
            print(password)
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                # Redirect to a success page or perform other actions
                return redirect('/')
    
    else:
        if request.user.is_authenticated:
            # return render(request, 'csv-upload.html') 
            redirect('/')
        else:
            form = UserLoginForm()

    return render(request, 'login.html')

 
def success_page(request):
    return render(request, 'login-success.html',{'sidebar': False}) 
 
def logoutView(request):
    logout(request)
    print(request.user)
    return redirect('/')
 
def deleteProduct(request):
    qAll = request.GET.get('by', '')
    byQuery = request.GET.get('qu', '')
    print(qAll)
    print(byQuery)
    if qAll == 'search':
        # words = byQuery.split()
        # q_objects = Q()
        # for word in words:
        #     q_objects |= Q(productTitle__icontains=word)

        # results = Products.objects.filter(q_objects)
        results = Products.objects.filter(productTitle__icontains=byQuery)
        # return redirect('/')
        # sQuery = str("%")+byQuery.replace(" ", "%")+str("%") 
        # objs = Products.objects.raw("SELECT id  FROM `Products` WHERE `productTitle` LIKE %s ", [sQuery])
        results.delete()
        print('-------------search-----------')
    elif qAll == 'all':
        Products.objects.all().delete()
        print('elseeeeeeeeeeee')
        # Products.objects.raw("TRUNCATE TABLE `searchdb`.`products`")
    else:
        print(byQuery)
        print("-------------iproductID----------------")
        results=Products.objects.filter(productID=byQuery)
        results.delete()
        print("data")
    # if data == '':
    return redirect('productUpload')
    # return redirect('/')
 
def search(request):
    query = request.GET.get('ad', '')
    words = query.split()
    q_objects = Q()
    for word in words:
        q_objects |= Q(productTitle__icontains=word)
    # results = Products.objects.filter(q_objects)
    results = Products.objects.filter(productTitle__icontains=query)
    
    # sData = str("%")+query.replace(" ", "%")+str("%")
    # results = Products.objects.all()
    # results = Products.objects.raw("SELECT *  FROM `Products` WHERE `productTitle` LIKE %s ", [sData])
    return render(request, 'admin-search.html', {'aQuery': query, 'results': results})
 
    
def dadaExport(request):
    query = request.GET.get('q', '')
    query1 = request.GET.get('exp', '')
    file_name = "products-data.xlsx"  
    if query1 == 'search':
        print(query)
        sQuery = str("%")+query.replace(" ", "%")+str("%") 
        objs = Products.objects.raw("SELECT *  FROM `Products` WHERE `productTitle` LIKE %s ", [sQuery])
    else:
        objs=Products.objects.all()

    #export_dir = "/media/"  # Replace with the actual directory path    
    # export_file = export_dir + file_name
    data= []
    for row in objs:
        data.append({
            "productID": row.productID,
            "productTitle":row.productTitle,
            "seriesID":row.seriesID,
            "description":row.description,
            "price":row.price,
            "productImage":row.productImage,
            "searchUrl":row.searchUrl,
            "shortDescription":row.shortDescription,
            "additional1":row.additional1,
            "additional2":row.additional2,
            "additional3":row.additional3,
            "esUrl":row.esUrl,
            "pniUrl":row.pniUrl,
            "tabData":row.tabData,
            "categoryId":row.categoryId
     })
    pd.DataFrame(data).to_excel(file_name, index=False)
   
   
    # file_obj = get_object_or_404(YourModel, id=file_id)  # Replace with your model and logic to fetch the file
    # file_path = file_obj.file.path  # Get the file's full path
    response = FileResponse(open(file_name, 'rb'))
    # response['Content-Disposition'] = f'attachment; filename="{file_obj.file.name}"'  # Sets the filename for download
    return response
    # return JsonResponse({'data':objs})
    # return render(request, 'success.html',{'data1':data})





def csvUpload(request):
    # if request.user.is_authenticated:  
        if request.method == "POST": 

            if bool(request.FILES.get('csv_file', False)) == True:
                uploaded_file = request.FILES['csv_file']   
                # if not os.path.exists('product_csv/'):
                #     os.mkdir('product_csv/') 
                # print(uploaded_file.name)
                fs = FileSystemStorage()
                document_path = fs.save(uploaded_file.name, uploaded_file) 
                # print(document_path)
                # document_path = default_storage.save(file.name, file)
                xl = pd.read_excel("media/"+str(document_path), "Sheet1")
                productList=[]
                productLi= {}
                for i in range(0,len(xl)): 
                    productList.append(xl["productID"][i])
                    productLi[(xl["productID"][i])]=(xl["searchUrl"][i])
                    checkExit=Products.objects.filter(productID = xl["productID"][i]).first()
                    if not checkExit:
                        Products.objects.create(
                        productID = xl["productID"][i], 
                        productTitle  = xl["productTitle"][i], 
                        seriesID  = xl["seriesID"][i], 
                        description = xl["description"][i], 
                        price = xl["price"][i].strip(), 
                        productImage = xl["productImage"][i], 
                        searchUrl  = xl["searchUrl"][i].strip(), 
                        shortDescription = xl["shortDescription"][i], 
                        additional1 = xl["additional1"][i], 
                        additional2 = xl["additional2"][i], 
                        additional3 = xl["additional3"][i], 
                        esUrl = xl["esUrl"][i].strip(), 
                        pniUrl = xl["pniUrl"][i].strip(), 
                        tabData = xl["tabData"][i],
                        categoryId = xl["categoryId"][i]
                    ) 
                    else:
                        Products.objects.filter(productID = xl["productID"][i]).update(
                        productTitle  = xl["productTitle"][i], 
                        seriesID  = xl["seriesID"][i], 
                        description = xl["description"][i], 
                        price = xl["price"][i], 
                        productImage = xl["productImage"][i], 
                        searchUrl  = xl["searchUrl"][i], 
                        shortDescription = xl["shortDescription"][i], 
                        additional1 = xl["additional1"][i], 
                        additional2 = xl["additional2"][i], 
                        additional3 = xl["additional3"][i], 
                        esUrl = xl["esUrl"][i], 
                        pniUrl = xl["pniUrl"][i], 
                        tabData = xl["tabData"][i],
                        categoryId = xl["categoryId"][i]
                    )
            
                return render(request, 'success.html',{'da':productLi,'data':productList})
        else:
            print('after post')
            # form = CSVUploadForm()
            return render(request, 'csv-upload.html') 
    
    # else:
       
    #     print('home')
    #     return redirect('home_page')        
         

def impoerEmployeeFromExcel(request):
    # products_file = request.FILES["products_file"]
    # rows = TextIOWrapper(products_file, encoding="utf-8", newline="")
    xl = pd.read_excel("attendance_app/employee_list.xlsx", "Sheet1")
    for i in range(0,len(xl)):  
        print()
        # Products.objects.create(
        #     branch_id = 1, employee_id = xl["Employee Id"][i],department_id = xl["Department"][i],
        #     designation_id = xl["Designation"][i], first_name = xl["First Name"][i], 
        #     last_name = xl["Last Name"][i], father_name = xl["Father Name"][i], mother_name = xl["Mother Name"][i],
        #     mobile = xl["Mobile"][i], email = xl["Email"][i], gender = xl["Gender"][i], religion = xl["Religion"][i],
        #     date_of_birth = xl["Date of Birth"][i], nationality = xl["Nationality"][i]
        # ) 
    return redirect('/dashboard/')





