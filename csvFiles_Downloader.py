"""
2.	Design a system (Python/Java) and write the  code  which can download hundreds of csv files and
    parse and put them in Database(You can choose mySQL or MongoDB etc).You have been given only one Machine with
    Linux ( with Multi-core CPU – 8 vCPU)  installed. File should be downloaded from remote server at some IP using SFTP.
    And remote server allows maximum only one SFTP connection at a time from any remote machine(One IP only One SFTP  connection allowed).
"""

import pysftp
import os
import csv
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["csvdatabase"]

ip = "127.0.0.1"
username = "user"
password = "passw0rd"
localFilePath = "\\CSVFiles\\"

# getting files from remote server
with pysftp.Connection(host=ip, username=username, password=password) as sftp:
    print("Connection succesfully stablished ... ")

    # CSV files directory
    sftp.cwd('/Home/files/')

    # list of files in files directory
    directory_structure = sftp.listdir_attr()

    for attr in directory_structure:
        #print(attr.filename, attr)

        if attr.filename[-4:] == ".csv":
            remoteFile= attr.filename
            sftp.get(remoteFile, localFilePath)

# reading data from csv files and storing in datadabe
list_files = os.listdir(localFilePath)
for file in list_files:
    mycol=mydb[file[:-4]]
    with open(file) as fh:
        mycol = mydb[file[:-4]]
        rd = csv.DictReader(fh, delimiter=',')
        for row in rd:
            x = mycol.insert_one(row)
print("Data inserted into MongoDB data base")


