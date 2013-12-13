import datetime

from django.http import HttpResponse, Http404
from django.db import connection
from django.template import Template, Context
from django.template.loader import get_template
from django.shortcuts import render_to_response

def hello(request):
    return HttpResponse("gao wen zhe da mei nv!")

#def current_datetime(request):
#    now = datetime.datetime.now()
#    t = get_template("currentDate.txt")
#    c = Context({'currentDate':now})
#    timeHtml = t.render(c)
#    return HttpResponse(timeHtml)

def current_datetime(request):
    currentDate = datetime.datetime.now()
    return render_to_response("headDate.html", {'currentDate':currentDate})

def future_datetime(request,offset):
    try:
        hour_offset = int(offset)
    except ValueError:
        raise Http404()
    next_time = datetime.datetime.now() + datetime.timedelta(hours = hour_offset)
    return render_to_response("headFuDate.html",locals())

def testPostgre(request):
    cursor = connection.cursor()
    sql_sel = "select * from COMPANY;"
    cursor.execute(sql_sel)    
    a = ""
    for row in cursor:  
        print row
        a = row
#        result = result + row
#    print result
    return HttpResponse(a)