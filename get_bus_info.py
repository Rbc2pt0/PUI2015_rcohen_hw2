__author__ = 'rachelcohen'
import json
import urllib2
import sys
import csv

# sys arg 1 api key = 5581b1e3-06db-4291-bfdc-5c4afea1631e
# sys argv 2 is the bus line
# sys arg 3 csv file name


if __name__ == '__main__':
    url = "http://api.prod.obanyc.com/api/siri/vehicle-monitoring.json?key=%s&VehicleMonitoringDetailLevel=calls&LineRef=%s" % (sys.argv[1], sys.argv[2])
    request = urllib2.urlopen(url)
    data = json.loads(request.read())
    buses = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']

    with open(sys.argv[3], 'wb') as csvFile:
        writer = csv.writer(csvFile)
        headers = ['Latitude', 'Longitude', 'Stop Name', 'Stop Status']
        writer.writerow(headers)
        
        for b in buses:
            lat = b['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
            lon = b['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
            if b['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['StopPointName'] == "":
                stop = 'N/A'
            else:
                stop = b['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['StopPointName']
            if b['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['Extensions']['Distances']['PresentableDistance'] == "":
                status = 'N/A'
            else:
                status = b['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['Extensions']['Distances']['PresentableDistance']

            writer.writerow([lat, lon, stop, status])