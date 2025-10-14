/*
 in general there were issues with double 'ON DELETE CASCADE' (a known problem), in the tables
 we had problem, we kept this as a comment.
 */

CREATE TABLE MyContacts (
    contactName VARCHAR(20) PRIMARY KEY,
    address VARCHAR(20),
    phoneNumber VARCHAR(12) NOT NULL, CHECK (phoneNumber LIKE '9725%')
)

CREATE TABLE ContactsOFContacts (
    myContact VARCHAR(20),
    contactInHisList VARCHAR(20),
    PRIMARY KEY (myContact,contactInHisList),
    FOREIGN KEY (myContact) REFERENCES MyContacts (contactName) ON DELETE CASCADE,
    FOREIGN KEY (contactInHisList) REFERENCES MyContacts (contactName) /*ON DELETE CASCADE
                                                                         */
)


CREATE TABLE ZoomMeetings (
    startTime TIMESTAMP,
    subject VARCHAR(20) NOT NULL ,
    PRIMARY KEY (startTime)

)


CREATE TABLE Participants(
    startTime TIMESTAMP,
    participant VARCHAR(20),
    PRIMARY KEY(startTime, participant),
    FOREIGN KEY (startTime) REFERENCES ZoomMeetings(startTime) /*ON DELETE CASCADE*/,
    FOREIGN KEY (participant) REFERENCES MyContacts (contactName) ON DELETE CASCADE

)
/*

 */
CREATE TABLE LateToMeeting (
    startTime TIMESTAMP,
    participant VARCHAR(20),
    personCausingDelay VARCHAR(20) NOT NULL ,
    minutes INT NOT NULL ,
    PRIMARY KEY (startTime,participant),
    FOREIGN KEY (startTime, participant) REFERENCES Participants (startTime, participant) /*ON DELETE CASCADE
                                                                                            */,
    FOREIGN KEY (personCausingDelay) REFERENCES MyContacts (contactName) ON DELETE CASCADE,
    CHECK (participant <> LateToMeeting.personCausingDelay)
)

CREATE TABLE Folder (
    folderId INT PRIMARY KEY,
    folderName VARCHAR(20) DEFAULT ('new folder'),
    dateOfCreate DATE NOT NULL,
    parentFolderId INT DEFAULT null,
    FOREIGN KEY (parentFolderId) REFERENCES Folder (folderId) /* ON DELETE CASCADE */ ,
    CHECK (folderId <> parentFolderId)
)

CREATE TABLE Files (
    nameOfFile VARCHAR(20),
    folderId INT,
    type VARCHAR(3) CHECK (LEN(type) = 3),
    size INT NOT NULL,
    PRIMARY KEY (nameOfFile,folderId,type),
    FOREIGN KEY (folderId) REFERENCES Folder (folderId) ON DELETE CASCADE
)

CREATE TABLE DBAssignmentFiles(
    nameOfFile VARCHAR(20),
    folderId INT,
    type VARCHAR(3) CHECK (LEN(type) = 3),
    size INT NOT NULL,
    isFormat INT CHECK (isFormat = 0 or isFormat = 1)
    PRIMARY KEY (nameOfFile,folderId,type),
    FOREIGN KEY (nameOfFile,folderId,type) REFERENCES Files (nameOfFile,folderId,type) ON DELETE CASCADE
)


CREATE TABLE ImportantFiles(
    nameOfFile VARCHAR(20),
    folderId INT,
    type VARCHAR(3) CHECK (LEN(type) = 3),
    size INT NOT NULL ,
    hoursOfWorking INT,
    PRIMARY KEY (nameOfFile,folderId,type),
    FOREIGN KEY (nameOfFile,folderId,type) REFERENCES Files (nameOfFile,folderId,type) ON DELETE CASCADE
)


CREATE TABLE editInMeeting(
    nameOfFile VARCHAR(20),
    folderId INT,
    type VARCHAR(3) CHECK (LEN(type) = 3),
    startTime TIMESTAMP,
    PRIMARY KEY (nameOfFile,folderId,type, startTime),
    FOREIGN KEY (nameOfFile,folderId,type) REFERENCES ImportantFiles (nameOfFile,folderId,type) ON DELETE CASCADE,
    FOREIGN KEY (startTime) REFERENCES ZoomMeetings(startTime) /* ON DELETE CASCADE */
)

CREATE TABLE AccessPermission(
    contactName VARCHAR(20),
    type VARCHAR(3) CHECK (LEN(type) = 3),
    dateOfPermission DATE,
    reason VARCHAR (20) NOT NULL,
    PRIMARY KEY (contactName,type,dateOfPermission),
    FOREIGN KEY (contactName) REFERENCES MyContacts (contactName) ON DELETE CASCADE
)

CREATE TABLE Exceptions(
    exceptionNum INT PRIMARY KEY,
    dangerLevel FLOAT CHECK (dangerLevel >=0 and dangerLevel <= 10)
)


CREATE TABLE ExceptionsDetected(
    contactName VARCHAR(20),
    type VARCHAR(3) CHECK (LEN(type) = 3),
    dateOfPermission DATE,
    exceptionNum INT,
    PRIMARY KEY (contactName,type,dateOfPermission,exceptionNum),
    FOREIGN KEY (contactName,type,dateOfPermission) REFERENCES AccessPermission (contactName,type,dateOfPermission) ON DELETE CASCADE ,
    FOREIGN KEY (exceptionNum) REFERENCES Exceptions (exceptionNum) ON DELETE CASCADE
)
