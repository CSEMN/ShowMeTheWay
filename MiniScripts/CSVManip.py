import csv
from MiniScripts import GeoCalculator
CSV_FILE_NAME='assets/eg.csv'
CSV_FILE_HEADER=['city', 'lat', 'lng','province','country']#,cities...
#old_header = ['city', 'lat', 'lng', 'country',
#  'iso2', 'admin_name', 'capital', 'population', 'population_proper']
def getCSVData():
    csvfile= open(CSV_FILE_NAME,'r', newline='',encoding="utf8")
    data=list()
    reader = csv.DictReader(csvfile)
    for row in reader:
        data.append(row)
    csvfile.close()
    return data
    
def getCitiesNamesList():
    lst=list()
    data=getCSVData()
    for line in data:
        lst.append(line['city'])
    return lst


def dictCSVdata():
    data=getCSVData()
    dictData=dict()
    for line in data:
        dictData[line['city']]=line
    return dictData

def getAdjDict():
    cities= getCitiesNamesList()
    dataList=getCSVData()
    adjDict=dict() # city:{adjCity1:distance,adjCity2:distance}
    for cityData in dataList:
        #scanLimit= 20.0 km 
        cityAdj=dict()
        for multiplier in range(1,20):
            if len(cityAdj)>=3:
                break
            scanLimit=20.0*multiplier
            for otherCity in cities:
                if otherCity== cityData['city']:
                    continue
                distance=float(cityData[otherCity])
                if distance<scanLimit:
                    cityAdj[otherCity]= distance
        cityAdj=dict(sorted(cityAdj.items(), key=lambda item: item[1]))#sort adj by nearest
        adjDict[cityData['city']]=cityAdj
    return adjDict
     


def setCitiesDistance():
    data=getCSVData()
    dictData=dictCSVdata()
    #adjDict=getAdjDict()
    for line in data:
        CSV_FILE_HEADER.append(line['city'])
        CSV_FILE_HEADER.append(line['city']+"_r")
        lat1=float(line['lat'])
        lng1=float(line['lng'])
        for city in dictData.keys():
            lat2=float(dictData[city]['lat'])
            lng2=float(dictData[city]['lng'])
            dist =  GeoCalculator.calc_distance(lat1,lng1,lat2,lng2)
            line[city]=dist
            #use google api to calculate real distance
            # if(city in adjDict[line['city']]):
            #     print("calculating... ("+city+","+line["city"]+")")
            #     dist =  GeoCalculator.calc_driving_distance(lat1,lng1,lat2,lng2)
            #     line[city+"_r"]=dist
            #     print("done")
    csvfile= open(CSV_FILE_NAME,'w', newline='',encoding="utf8")
    writer = csv.DictWriter(csvfile, fieldnames=CSV_FILE_HEADER)
    writer.writeheader()
    writer.writerows(data)
    csvfile.close()

#setCitiesDistance()


def resetCSV():
    data=getCSVData()
    csvfile= open(CSV_FILE_NAME,'w', newline='',encoding="utf8")
    writer = csv.DictWriter(csvfile, fieldnames=CSV_FILE_HEADER)
    writer.writeheader()
    newData=list()
    for line in data:
        newData.append(
            {
                CSV_FILE_HEADER[0]:line['city'],
                CSV_FILE_HEADER[1]:line['lat'],
                CSV_FILE_HEADER[2]:line['lng'],
                CSV_FILE_HEADER[3]:line['admin_name'],
                CSV_FILE_HEADER[4]:line['country'],
        })

    writer.writerows(newData)
    csvfile.close()
