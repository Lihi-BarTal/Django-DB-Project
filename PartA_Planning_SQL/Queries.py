QUERY_ANSWERS = {
    "Q3":
        """
        SELECT DISTINCT Attendance.date as date
FROM Attendance,PopularPersons
WHERE Attendance.contactName = PopularPersons.name
ORDER BY Attendance.date asc;

        """
    ,
    "Q4":
        """
        SELECT Attendance.contactName as name, min(Attendance.date) as FirstMeetingDate
FROM Attendance
where Attendance.contactName in (
select DISTINCT Contacts.name
FROM Contacts, Attendance, cohesiveCity
where Attendance.date in
(
    SELECT Attendance.date
From Contacts, Attendance, organizedPerson
WHERE Attendance.contactName = organizedPerson.name
) and Contacts.city = cohesiveCity.city)
group by Attendance.contactName;
        """
}
