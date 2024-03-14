# IMPORT
import os
import shutil
import time
import platform
from datetime import datetime


# GET IMAGES FROM DIRECTORY

def getImages(folder):
    print("> locating images...")

    # initialize variables, get list of everything in folder
    fileList = []
    removeList = []
    try:
        os.chdir("/Users/youcef-badjadi/Pictures/DCIM")
        fileList = os.listdir()
    except:
        print("> error x3: unable to locate directory " + folder)
        exit()

    # remove folders from fileList
    for file in fileList:
        folderFlag = True

        for letter in file:

            if letter == ".":
                folderFlag = False
                break

        if folderFlag == True:
            removeList.append(file)

    for file in removeList:
        fileList.remove(file)

    # error checking: empty directory
    if fileList == []:
        print("> error x1: no files detected in this directory")
        time.sleep(2)
        exit()

    # ask for user confirmation to proceed
    if input("> found " + str(len(fileList)) + " photos. Proceed (y/n)? ") != "y":
        exit()

    return fileList


# CREATE FOLDERS FOR ORGANIZATION BY YEAR

def createFolders(fileList, MONTHS):
    print("> detected years...")

    # initialize variables
    yearList = []

    # check through file years, add to yearlist
    for file in fileList:
        year, na = getExifData(file)

        if year not in yearList:
            yearList.append(year)
            print("> " + year)

    # conduct error checking, get directories that already exist
    existingYearList = checkFiles(fileList, yearList)

    # make directories that correspond to yearList
    for year in yearList:

        # if directory already exists, skip it
        if year not in existingYearList:

            for month in MONTHS:
                os.makedirs(year + "/" + month)

    print("> folder structure complete")
    time.sleep(2)


# SORT PHOTOS

def sortPhotos(fileList, MONTHS):
    count = 0

    # go through each file and move it
    for file in fileList:

        count += 1

        # get year and month from exif data
        year, monthNum = getExifData(file)
        month = MONTHS[int(monthNum) - 1]

        # use shutil.move to move dat file! (and skip if it already exists!)
        try:
            shutil.move(file, year + "/" + month)
            print("> move " + file)
        except shutil.Error:
            print("> error x6: Unable to move " + file + " because file already exists at destination. Skipping!")

    print("> moved " + str(count) + " files")


# CHECK FOR ERRORS AND ABORT IF FOUND

def checkFiles(fileList, yearList):
    # initialize variables
    existingYearList = []
    flag = False
    error = ""

    """
    #ensure that first 6 chars of filename are numbers
    for file in fileList:
        try:
            int(file[0:6])
        except:
            flag = True
            error = "x2: invalid file name: " + file
    """

    # get list of already existing year folders
    for year in yearList:
        files = os.listdir()
        if year in files:
            existingYearList.append(year)
            print("> found directory " + str(year))

    """
    #ensure that chars 4-6 are a valid month
    erroneousfilename = ""
    try:
        for file in fileList:
            erroneousfilename = file
            if int(file[4:6]) > 12:
                flag = True
                error = "x4: "+file[4:6]+" is not a valid month: " + file

    #check if something really weird happens
    except:
        flag = True
        error = "x5: invalid file names" + erroneousfilename
    """

    # if flag was set to true, then there is an error somewhere
    if flag == True:
        print("> error " + error)
        time.sleep(2)
        exit()

    return existingYearList


# GET DATE OF CREATION FOR A GIVEN FILE

def getExifData(filename):
    # Get current operating environment
    SYSTEM = platform.system()

    # If on Windows
    if SYSTEM == "Windows":
        data = os.path.getmtime(filename)

    # If on MacOS or Linux
    else:
        data = os.stat(filename).st_mtime

    # Convert unix time to month and year
    month = datetime.utcfromtimestamp(data).strftime("%m")
    year = datetime.utcfromtimestamp(data).strftime("%Y")

    return year, month

