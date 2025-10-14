create VIEW view1
as
select Appusers.aname as appName, ROUND(CAST(AVG(1.0 * rating) AS FLOAT), 2)as AvgGrade
                    from Appusers
                    GROUP BY Appusers.aname;


create VIEW view2
as
    select view1.appName as appName, Applications.aCategory as aCategory, AvgGrade as AvgGrade
    FROM view1, Applications
    where view1.appName = Applications.aName;


create view view3
as
    select Appusers.aName
    from Appusers
    where Appusers.aName in
(
select a.appName
from view2 as a
where a.AvgGrade = (select max(b.AvgGrade)
                    from view2 as b
                    where a.aCategory = b.aCategory)
    )
    group by Appusers.aName
    having count(Appusers.aName) > 21;


create view view4
as
    select Contacts.cname as ContactsName,Contacts.phone as Contactphone ,count(*) as numgoodapps
                    from Contacts, view3, Appusers
                    where Contacts.cname = Appusers.cname  and Appusers.aname = view3.aName and Contacts.city = 'Haifa'
                    group by Contacts.cname, Contacts.phone
                    UNION
                    SELECT DISTINCT Contacts.cname as ContactsName, Contacts.phone as Contactphone, 0 as numgoodapps
                    FROM Contacts,Appusers
                    WHERE Contacts.cname = Appusers.cname and Contacts.city = 'Haifa' and not exists(
                    SELECT *
                    FROM view3,AppUsers as a2
                    WHERE view3.aName = a2.aname and a2.cname = Appusers.cname);


CREATE view view5
as
select AppUsers.cName as exceedingContact
from Applications,
     AppUsers
where Applications.aname = AppUsers.aname
GROUP BY AppUsers.cName
having sum(Applications.asize) > 1200;


create view view6
as
    select DISTINCT Contacts.city
                        from Contacts
                        where not exists(
                        select c2.cname
                        from Contacts as c2
                        where c2.city = Contacts.city and c2.cname not in(
                        select *
                        from view5)
                        );


create view view7
as
    select view6.city, Appusers.aName, count(*) as count
    from view6, AppUsers, Contacts
    where view6.city = Contacts.city and Contacts.cname = Appusers.cname
    group by view6.city, Appusers.aName;



