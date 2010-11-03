from jsonmodels import Model, Field, DateTimeField, ListField

class BooleanField(Field):
  def to_python(self, value):
    bool_map = {1: True, 2: False}

    if value in bool_map:
      return bool_map[value]
    else:
      raise ValueError('Unknown boolean value: ' % value)

class Band(Model):
  id        = Field(key = 'band_id')
  subdomain = Field()
  name      = Field()
  url       = Field()

  def __unicode__(self):
    return self.name

class AlbumInfo(Model):
  id            = Field(key = 'album_id')
  title         = Field()
  large_art_url = Field()
  small_art_url = Field()
  release_date  = DateTimeField(format = DateTimeField.FORMAT_EPOCH_SECONDS)

class Track(Model):
  id            = Field(key = 'track_id')
  duration      = Field()
  band_id       = Field()
  album_id      = Field()
  title         = Field()
  streaming_url = Field()
  number        = Field()
  large_art_url = Field()
  small_art_url = Field()
  release_date  = DateTimeField(format = DateTimeField.FORMAT_EPOCH_SECONDS)
  downloadable  = BooleanField()
  credits       = Field()
  lyrics        = Field()
  url           = Field()

class Album(Model):
  id            = Field(key = 'album_id')
  title         = Field()
  band_id       = Field()
  large_art_url = Field()
  small_art_url = Field()
  release_date  = DateTimeField(format = DateTimeField.FORMAT_EPOCH_SECONDS)
  credits       = Field()
  tracks        = ListField(Track)
