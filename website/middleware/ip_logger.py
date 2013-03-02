from website.models import Tracker,Location
from django.contrib.gis.utils import GeoIP
import re

class IpLogger(object):
  def process_request(self, request):
    return None
    if re.search("admin", request.path ):
      return None
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')

      #Get my location info
    geo = GeoIP().city(ip)
    if not geo:
      geo = {'latitude': 0, 'longitude': 0, 'city': 'None', 'region': 'none'}

      #Get a location or create one
    loc = Location.objects.filter(ip_address=ip)
    if not loc:
      loc = Location(ip_address=ip, lat=str(geo['latitude']), lng=str(geo['longitude']), city=geo['city'], region=geo['region'])
    else:
      loc = loc[0]
    loc.save()

      #Get my tracker
    track = loc.tracker_set.filter(path=request.path)
    if not track:
      loc.tracker_set.add( Tracker( path=request.path, count=1 ))
    else:
      track[0].count += 1
      track[0].save()
      
    return None
