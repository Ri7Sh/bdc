# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import *
# Create your views here.
# from attendance.forms import UserPForm

from django.http import HttpResponse
import xlwt


def attend(request):
	# user_form = UserPForm()
	if request.method == 'POST':
		#user_form=UserPForm(data=request.POST)
		#if user_form.is_valid():
			data=request.POST
			user = UserProfile()
			user.username=data['username']
			user.Department=data['Department']
			user.Year=data['Year']
			Time = timezone.now()
			user.Time = Time.strftime("%d/%m/%Y %H:%M:%S")
			user.save()
			state= 'saved'
			print("1")
			return render(request,'attend.html',{'state':state})
		
	return render(request,'attend.html')







def export_users_xls(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="users.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Users')

    # Sheet header, first row
    row_num = 0

    # font_style = xlwt.XFStyle()
    # font_style.font.bold = True
    columns = ['username', 'Department', 'Year', 'Time' ]

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num])

    # Sheet body, remaining rows
    # font_style = xlwt.XFStyle()

    rows = UserProfile.objects.all().values_list('username', 'Department', 'Year', 'Time')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
        	ws.write(row_num, col_num, row[col_num])

    wb.save(response)
    return response