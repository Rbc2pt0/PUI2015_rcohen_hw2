__author__ = 'rachelcohen'
import json
import urllib2
import sys

#api key = 5581b1e3-06db-4291-bfdc-5c4afea1631e


if __name__ == '__main__':
    url = "http://api.prod.obanyc.com/api/siri/vehicle-monitoring.json?key=%s&VehicleMonitoringDetailLevel=calls&LineRef=%s" % (sys.argv[1], sys.argv[2])
    request = urllib2.urlopen(url)
    data = json.loads(request.read())
    buses = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']

    print 'Bus Line : ', sys.argv[2]
    print 'Number of Active Buses : ', str(len(data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']))

    for b in buses:
        lat = b['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
        lon = b['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
        bus = b['MonitoredVehicleJourney']['VehicleRef'][-4:]
        print 'Bus ', str(bus), ' is at latitude', str(lat), ' and longitude', str(lon)