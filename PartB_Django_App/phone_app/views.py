from django.shortcuts import render
from .models import Applications
from django.db import connection
# Create your views here.


def index(request):
    return render(request, 'index.html')

def AddApplication(request):
    errorMessage = None

    if request.method == "POST" and request.POST:
        aName = request.POST.get('aName')
        aCategory = request.POST.get('aCategory')
        aSize = request.POST.get('aSize')

        if Applications.objects.filter(aname=aName).exists():
            errorMessage = "There is already an application with that name"
        elif int(aSize) < 100 or int(aSize) > 200:
            errorMessage = "The size must be between 100 and 200"
        else:
            new_app = Applications(
                aname=aName,
                acategory=aCategory,
                asize=aSize,
                isinstalled= 0
            )
            new_app.save()
    catagoriesToPresent = Applications.objects.values_list('acategory', flat=True).distinct()

    return render(request, 'AddApplication.html', {'errorMessage': errorMessage, 'catagoriesToPresent': catagoriesToPresent})


def dictfetchall(cursor):
    columns = [col[0] for col in cursor.description]
    return [dict(zip(columns, row)) for row in cursor.fetchall()]


def queryResults(request):
    with connection.cursor() as cursor:
        cursor.execute(""" 
            select Appusers.aname as AppName, ROUND(CAST(AVG(1.0 * rating) AS FLOAT), 2) as AvgGrade
                        from Appusers 
                        where Appusers.aname in
                        (Select DISTINCT ap.aname
                        FROM Applications as ap
                        WHERE ap.isinstalled = 1 and ap.aname in(
                            select ap2.aname
                            from Appusers as ap2, Contacts
                            where Contacts.cname = ap2.cname and Contacts.city = 'Haifa'
                            ) 
                        )
                        GROUP BY Appusers.aname
                        having count(Appusers.aname) > 10
                        order by AVGGrade desc;
        """)
        query1_results = dictfetchall(cursor)

        cursor.execute(""" 
                    select view4.ContactsName as ContactsName, view4.Contactphone as Contactphone, view4.numgoodapps as numGoodApps
                    from view4
                    order by view4.numgoodapps desc
                    
                    
                """)
        query2_results = dictfetchall(cursor)

        cursor.execute(""" 
                      
                    select a.city as city, a.aname as app, a.count as count
                    from view7 as a
                    where a.count = (
                    select max(b.count)
                    from view7 as b
                    where a.city = b.city
                    ) and a.count >2
                    order by a.city, a.aname

                        """)
        query3_results = dictfetchall(cursor)

    return render(request, "queryResults.html", {
        "query1_results": query1_results,
        "query2_results": query2_results,
        "query3_results": query3_results,
        })


def InstallApplication(request):
    with connection.cursor() as cursor:
        cursor.execute("""
        select SUM(asize) AS total_size
        from Applications
        where isInstalled = 1;
        """)
        sql_result = dictfetchall(cursor)
        available_space = 1800 - (sql_result[0]['total_size'] if sql_result and sql_result[0]['total_size'] else 0)

    with connection.cursor() as cursor:
        cursor.execute("""
        select Applications.aname
        from Applications
        where isInstalled = 0;
        """
        )
        appsNotInstalled = dictfetchall(cursor)

    with connection.cursor() as cursor:
        cursor.execute("""
        select Applications.asize as asize
        from Applications
        where Applications.aname = aname
        """)
        sql_result = dictfetchall(cursor)
        appsize = sql_result[0]['asize']

        errorMessage = None

        if request.method == "POST" and request.POST:
            aname = request.POST.get('aname')
            if appsize > available_space:
                errorMessage = "Not enough space for this application"

            else:
                Applications.objects.filter(aname=aname).update(isinstalled=1)
                available_space -= appsize


    return render(request, "InstallApplication.html", {
        "available_space": available_space,
        "appsNotInstalled": appsNotInstalled,
        "errorMessage": errorMessage,
    })

def RemoveApplication(request):

    with connection.cursor() as cursor:
        with connection.cursor() as cursor:
            cursor.execute("""
               select SUM(asize) AS total_size
               from Applications
               where isInstalled = 1;
               """)
            sql_result = dictfetchall(cursor)
            available_space = 1800 - (sql_result[0]['total_size'] if sql_result and sql_result[0]['total_size'] else 0)

        with connection.cursor() as cursor:
                cursor.execute("""
                select Applications.aname
                from Applications
                where isInstalled = 1;
                """
                       )
                appsInstalled = dictfetchall(cursor)

        with connection.cursor() as cursor:
            cursor.execute("""
            select Applications.asize as asize
            from Applications
            where Applications.aname = aname
            """)
            sql_result = dictfetchall(cursor)
            appsize = sql_result[0]['asize']

        if request.method == "POST" and request.POST:
            aname = request.POST.get('aname')
            Applications.objects.filter(aname=aname).update(isinstalled=0)
            available_space += appsize



        return render(request, "RemoveApplication.html", {
            "available_space": available_space,
            "appsInstalled": appsInstalled,
        })

