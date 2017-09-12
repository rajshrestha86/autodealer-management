from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from main.models import *
from workshop.models import job_records
from parts.models import *
from showrooms.models import *
from datetime import date, timedelta
from django.db.models.functions.datetime import ExtractWeekDay
from django.db.models import Count
from django.db.models.functions import  TruncMonth

# Create your views here.


def dashboard(request):
    session=check_session_exist(request)
    if session==True:
        work_obj=job_records.objects.filter(date=date.today())
        workshop_today_count=work_obj.count()

        parts_obj=part_processing.objects.filter(out_date=date.today())
        parts_today=parts_obj.count()

        sales_obj=Sales.objects.filter(dateOfSale=date.today())
        sales_today=sales_obj.count()

        name=request.session['user']


        d = date.today() - timedelta(days=7)
        weekly_sales_obj=  Sales.objects.filter(dateOfSale__gte=d)
        weekly_sales=weekly_sales_obj.annotate(weekday=ExtractWeekDay('dateOfSale')).values('weekday').annotate(count=Count('id')).values('weekday','count')
        print('################################################################')
        print(weekly_sales)
        Sun=0
        Mon=0
        Tue=0
        Wed=0
        Thu=0
        Fri=0
        Sat=0
        for data in weekly_sales:
            if data['weekday']==1:
                Sun+=data['count']
            elif data['weekday']==2:
                Mon+=data['count']
            elif data['weekday']==3:
                Tue+=data['count']
            elif data['weekday']==4:
                Wed+=data['count']
            elif data['weekday']==5:
                Thu+=data['count']
            elif data['weekday']==6:
                Fri+=data['count']
            elif data['weekday']==7:
                Sat+=data['count']

        week=['Sun','Mon','Tue','Wed','Thu', 'Fri','Sat']
        week_sales=[Sun,Mon,Tue,Wed,Thu,Fri,Sat]
        print(week)
        print(week_sales)

        # Monthly Sales
        d = date.today()
        monthly_sales_obj=Sales.objects.filter(dateOfSale__year=d.year)
        monthly_sales =monthly_sales_obj.annotate(month=TruncMonth('dateOfSale')).values('month').annotate(
            count=Count('id')).values('month', 'count')
        print(monthly_sales)
        month_label = ["January", "February", "March", "April", "May", "June", "July", "August", "September",
                             "October", "November", "December"]
        month_data=[]
        jan = 0
        feb = 0
        mar = 0
        apr = 0
        may = 0
        june = 0
        july = 0
        august = 0
        september = 0
        oct = 0
        nov = 0
        dec = 0
        for data in monthly_sales:
            if data['month'].month==1:
                jan+=data['count']
            elif data['month'].month==2:
                feb+=data['count']
            elif data['month'].month==3:
                mar+=data['count']
            elif data['month'].month==4:
                apr+=data['count']
            elif data['month'].month==5:
                may+=data['count']
            elif data['month'].month==6:
                june+=data['count']
            elif data['month'].month==7:
                july+=data['count']
            elif data['month'].month==8:
                august+=data['count']
            elif data['month'].month==9:
                september+=data['count']
            elif data['month'].month==10:
                oct+=data['count']
            elif data['month'].month==11:
                nov+=data['count']
            elif data['month'].month==12:
                dec+=data['count']

            month_data = [jan, feb, mar, apr, may, june, july, august, september, oct, nov, dec]

        #parts_out for current month
        parts_obj_month = part_processing.objects.filter(out_date__month=date.today().month)
        parts_today_month = parts_obj_month.count()
        print("HOLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLo")
        print(parts_today_month)
        #workshop month
        work_obj = job_records.objects.filter(date__month=date.today().month)
        workshop_today_month = work_obj.count()

        # Monthly Parts
        d = date.today()
        monthly_parts_obj = part_processing.objects.filter(out_date__year=d.year)
        monthly_parts = monthly_parts_obj.annotate(month=TruncMonth('out_date')).values('month').annotate(
            count=Count('id')).values('month', 'count')
        print(monthly_parts)

        jan=0
        feb=0
        mar=0
        apr=0
        may=0
        june=0
        july=0
        august=0
        september=0
        oct=0
        nov=0
        dec=0
        for data in monthly_parts:
            if data['month'].month==1:
                jan+=data['count']
            elif data['month'].month==2:
                feb+=data['count']
            elif data['month'].month==3:
                mar+=data['count']
            elif data['month'].month==4:
                apr+=data['count']
            elif data['month'].month==5:
                may+=data['count']
            elif data['month'].month==6:
                june+=data['count']
            elif data['month'].month==7:
                july+=data['count']
            elif data['month'].month==8:
                august+=data['count']
            elif data['month'].month==9:
                september+=data['count']
            elif data['month'].month==10:
                oct+=data['count']
            elif data['month'].month==11:
                nov+=data['count']
            elif data['month'].month==12:
                dec+=data['count']

        month_data_parts=[jan, feb, mar, apr, may, june, july, august, september, oct, nov, dec]


        print("Partsssssssssssssyyyyyyyyyyyyyyyyyyyy")
        print(month_data_parts)

        context = {'name': name, 'workshop_count': workshop_today_count, 'parts_count': parts_today,
                   'sales_count': sales_today, 'week_label':week, 'week_sales':week_sales,'month_label':month_label, 'month_data':month_data,'parts_month':parts_today_month,'works_month':workshop_today_month,'parts_year_data':month_data_parts}



        return render(request, 'administration/main.html', context)
    else:
        return HttpResponseRedirect(session)


def admin_charts(request):
    session = check_session_exist(request)
    if session == True:
        linedata = [10, 12, 30, 14, 50, 6, 7]
        datas = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 11, 12]
        name = request.session['user']
        context = {'linedata': linedata, 'datas': datas, 'name': name}

        return render(request, 'administration/charts.html', context)
    else:
        return HttpResponseRedirect(session)




def admin_users(request):
    session = check_session_exist(request)
    if session == True:
        linedata = [10, 12, 30, 14, 50, 6, 7]
        datas = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 11, 12]
        name = request.session['user']
        context = {'linedata': linedata, 'datas': datas, 'name': name}

        return render(request, 'administration/users.html', context)
    else:
        return HttpResponseRedirect(session)


class list_users(ListView):
    model = user
    template_name = './administration/users.html'

    def get_context_data(self, **kwargs):
        name = self.request.session['user']
        extra = {'name': name}
        context = super(list_users, self).get_context_data(**kwargs)
        context.update(extra)
        return context

    def get(self, request, *args, **kwargs):
        temp = check_session_exist(self.request)
        if temp == True :
            return super(list_users, self).get(request, *args, **kwargs)
        else:
            return HttpResponseRedirect(temp)


class detail_user(DetailView):
    model = user
    template_name = './administration/user_detail.html'
    context_object_name = 'user'

    def get_context_data(self, **kwargs):
        context = super(detail_user, self).get_context_data(**kwargs)
        return context


    def get(self, request, *args, **kwargs):
        temp = check_session_exist(self.request)
        if temp == True :
            return super(detail_user, self).get(request, *args, **kwargs)
        else:
            return HttpResponseRedirect(temp)


class detail_dep(UpdateView):
    model = department
    fields = ['address_city', 'address_district', 'contact', 'email']
    template_name = './administration/dep_edit.html'
    success_url = reverse_lazy('administrator:department')


class delete_user(DeleteView):
    model = user
    success_url = reverse_lazy('administrator:users')

class create_user(CreateView):
    model = user
    fields = ['user_id', 'username', 'password', 'created_date']
    template_name='./administration/user_add.html'
    success_url = reverse_lazy('administrator:users')



class update_user(UpdateView):
    model = user
    fields = ['user_id', 'username', 'password','created_date']
    template_name = './administration/user_add.html'
    success_url = reverse_lazy('administrator:users')


    # def get_object(self):
    #     obj=user.objects.get(username=self.kwargs['pk'])
    #     print (obj.username)
    #     return obj

class list_department(ListView):

    model = department
    template_name = './administration/department.html'

    def get_context_data(self, **kwargs):

        name = self.request.session['user']
        extra = { 'name': name}
        context = super(list_department, self).get_context_data(**kwargs)
        context.update(extra)
        return context

    def get(self, request, *args, **kwargs):
        temp = check_session_exist(self.request)
        if temp == True :
            return super(list_department, self).get(request, *args, **kwargs)
        else:
            return HttpResponseRedirect(temp)



def check_session_exist(request):
    try:
        department= request.session['department']
        if department != 'administration':
            raise ValueError
        return True
    except KeyError:
        return (reverse('main:login_page'))
    except ValueError:
        return (reverse('main:login_page'))


