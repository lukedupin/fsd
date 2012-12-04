from website.models import Tracker,Location
from django.contrib.gis.utils import GeoIP
import re

class IpLogger(object):
  def process_request(self, request):
    if re.search("admin", request.path ):
      return None
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')

      #Get my location info
    lat_lng = GeoIP().lon_lat(ip)
    if not lat_lng:
      lat_lng = [0, 0]

      #Get a location or create one
    loc = Location.objects.filter(ip_address=ip)
    if not loc:
      loc = Location(ip_address=ip,lat=lat_lng[1], lng=lat_lng[0])
    else:
      loc = loc[0]
    loc.save()
    loc.tracker_set.add(Tracker(path=request.path))
    return None
