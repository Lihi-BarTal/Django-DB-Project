VIEWS_DICT = {
    "Q3":
        [
		"""
CREATE VIEW PopularPersons
AS
SELECT Contacts.name
FROM Contacts
WHERE(
SELECT count(DISTINCT Contacts2.city)
FROM SavedContactsOfContact, Contacts As Contacts2
WHERE SavedContactsOfContact.nameOFContact = Contacts.name AND Contacts2.name = SavedContactsOfContact.hisContact
)>1
AND
(SELECT COUNT (*)
FROM SavedContactsOfContact
WHERE SavedContactsOfContact.nameOFContact = Contacts.name AND SavedContactsOfContact.nameOFContact NOT IN (
    SELECT SavedContactsOfContact2.hisContact
    FROM SavedContactsOfContact AS SavedContactsOfContact2
    WHERE SavedContactsOfContact2.nameOfContact = SavedContactsOfContact.hisContact
    )) = 0
AND
(SELECT COUNT (*)
FROM SavedContactsOfContact,PopularityLevel
WHERE SavedContactsOfContact.nameOFContact = Contacts.name AND PopularityLevel.namePOP = SavedContactsOfContact.nameOFContact
AND PopularityLevel.countPOP<(
    SELECT PopularityLevel2.countPOP
    FROM PopularityLevel AS PopularityLevel2
    WHERE SavedContactsOfContact.hisContact = PopularityLevel2.namePOP
    ))=0;
		""",
        """
        CREATE VIEW SavedContactsOfContact
AS
SELECT Contacts.name AS nameOFContact,CommonContacts.savedContact AS hisContact
FROM Contacts,CommonContacts
WHERE Contacts.name=CommonContacts.contactSaver;
        """,
            """
            
CREATE VIEW PopularityLevel
AS
SELECT Contacts.name AS namePOP,COUNT (*) AS countPOP
FROM Contacts,CommonContacts
WHERE Contacts.name = CommonContacts.savedContact
GROUP BY Contacts.name;
            """
        ]
    ,
    "Q4":
        [
		"""
CREATE VIEW CitiesAndContact
AS
SELECT Contacts.city as city, count (*) as totalnum
From Contacts
GROUP BY Contacts.city;
		""",
        """
        
CREATE VIEW organizedPerson
as
    select Contacts2.name
    from Contacts as Contacts2
    where Contacts2.name not in
(
SELECT Contacts.name
FROM CommonContacts, Contacts, Attendance
where Contacts.name = CommonContacts.contactSaver and CommonContacts.nickname != CommonContacts.savedContact
and Attendance.contactName = Contacts.name and Attendance.delay > 50
);
        """,
            """
            CREATE VIEW cohesiveCity
as
SELECT DISTINCT CitiesAndContact.city
FROM CitiesAndContact
where CitiesAndContact.totalnum = 1 or CitiesAndContact.totalnum -1 = (
    select min(view1.count)
    FROM view1
    where view1.city = CitiesAndContact.city
    );

            """,
            """
            CREATE VIEW view1
as
select Contacts.name, contact2.city as city, count(*) as count
from Contacts, CommonContacts, Contacts as contact2
where Contacts.name = CommonContacts.contactSaver and contact2.name = CommonContacts.savedContact
and contact2.city = Contacts.city
GROUP BY Contacts.name, contact2.city;



            """
        ]
}



















