# Student-Management-System
The aim of this project is to create a student management system using Python 3.6 <br>
In this application one can add, view, update, delete and save students data. Also the data can be plot in the form of Bar Graph by clicking Chart option. <br> <br>
Libraries to be intalled in your system are: <br>
1. Open Command Prompt: <br>
option 1: <br> >pip install requests <br>
if option 1 fails go for option 2: <br> >python -m pip install requests <br>
likewise install rest of packages using commands: <BR>
pip install bs4 <br> pip install lxml <br> pip install pandas <br> pip install numpy <br> pip install matplotlib <br> <br>

For Backend - Installation of SQLite3 on your system <BR> <BR>
Step 1: Go to https://sqlite.org/index.html and in download section scroll to Precompiled Binaries for Windows --> "sqlite-tools-win32-x86-3320300.zip" <br>
Step 2: You need to download the zip file and extract files from that.<br>
Step 3: After extracting the file, open the file and copy all the three files : sqldiff, sqlite3, sqlite3_analyzer. <br>
Step 4: Now create a new folder name sqlite3 in C Drive and paste all that 3 files you have copied.<br>
Step 5: Now press windows key and open "Edit the system environment variables" --> Environment Variables --> System Variables --> Path --> Edit the path by clicking "Edit" --> Add new path by clicking "New" --> Path name "c:\sqlite" --> Enter Ok. <br>
Step 6: Now open the folder in which you have downloaded the project code from github --> enter cmd and open command prompt --> sqlite3 test.db --> Enter --> The following will be displayed on cmd prompt <br>
SQLite3 version 3.31.1 <br>
Enter ".help" for usage hints.<br>
sqlite3> <br>
This means you have successfully installed sqlite3 on your desktop. <br> <br>
Now create a table in database <br>
In command prompt write -> student_database.db --> enter --> .database --> enter --> sqlite> create table student(rno int primary key, name text, marks float); --> enter --> sqlite> .table student --> sqlite> .schema student --> sqlite> select * from student;  <br>
<br> Else just delete all the records from databse by using Delete option in application.
