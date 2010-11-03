from bandcamp.models import *
from datetime import datetime
from copy import copy
import urllib
import urllib2
import json

API_URL = 'http://api.bandcamp.com/api/%(object_type)s/%(version)s/%(method)s?%(params)s'

class BandCampError(Exception):
  pass

class BandCampService(object):
  def __init__(self, api_key):
    self.api_key     = api_key
    self.api_version = 1

  def _fetch(self, object_type, method, params):
    params = copy(params)

    params.update({'key': self.api_key})

    url = API_URL % {'object_type': object_type, 'version': self.api_version, 'method': urllib.quote(method), 'params': urllib.urlencode(params)}

    try:
      res = urllib2.urlopen(url)

      data = json.loads(res.read())

      return data
    except urllib2.HTTPError, e:
      if e.code == 500:
        error = json.loads(e.read())

        raise BandCampError(error.get('error_message'))
      else:
        raise

  def get_band_by_id(self, band_id):
    return Band.new_from_json(self._fetch('band', 'info', {'band_id': band_id}))

  def get_band_by_url(self, band_url):
    return Band.new_from_json(self._fetch('band', 'info', {'band_url': band_url}))

  def get_discography_by_band_id(self, band_id):
    discography = self._fetch('band', 'discography', {'band_url': band_url})['discography']

    return [AlbumInfo.new_from_json(params) for params in discography]

  def get_discography_by_band_url(self, band_url):
    discography = self._fetch('band', 'discography', {'band_url': band_url})['discography']

    return [AlbumInfo.new_from_json(params) for params in discography]

  def get_album(self, album_id):
    return Album.new_from_json(self._fetch('album', 'info', {'album_id': album_id}))

  def get_track(self, track_id):
    return Track.new_from_json(self._fetch('track', 'info', {'track_id': track_id}))
