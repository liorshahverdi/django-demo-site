from django.db import models
from django.utils import timezone

# Create your models here.
class ImageToText(models.Model):
    """
    This model stores the lookup for an image to text from Keras Models (defined in image_processing.py)
    parameters:
    @file_name - the filename being processed
    @labels - the set of labels associated with the filename
    @state - the state or province the ad appeared in
    @city - the city or town the ad appeared in
    @location - the location parsed from the ad
    @url - the url of the ad
    @timestamp - the timestamp of when the ad was scraped
    @phone_number - the phone number associated with the ad
    @latitude - latitude parsed from the ad
    @longitude - longitude parsed from the ad
    @image_url - image_url used for image lookup
    """
    
    filename = models.CharField(max_length=200)
    labels = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    url = models.CharField(max_length=200)
    timestamp = models.DateTimeField('image_to_text_timestamp')
    phone_number = models.CharField(max_length=20)
    latitude = models.CharField(max_length=200)
    longitude = models.CharField(max_length=200)
    image_url = models.CharField(max_length=200)
    throw_away = models.CharField(max_length=200)

    def __init__(self, image_url, filename, labels, state, city, location, url, timestamp, phone_number, latitude, longitude, throw_away):
        self.image_url = image_url
        self.filename = filename
        self.labels = labels
        self.state = state
        self.city = city
        self.location = location
        self.url = url
        self.timestamp = timestamp
        self.phone_number = phone_number
        self.latitude = latitude
        self.longitude = longitude
        self.throw_away = throw_away


class AreaCodeLookup(models.Model):
    """
    This model provides a look up for phone number area codes and aids in converting them to latitude, longitude.
    Specifically this mapping provides: 
    Area code and it's corresponding township.
    From there geopy provides the lookup to latitude, longitude

    Because location may not be unique - there could be multiple towns with the same name,
    there is not 100% guarantee all lookups will be accurate.

    Source: https://www.allareacodes.com/
    parameters:
    @area_code - the area code from a phone number
    @city - a string city
    @state - a string state
    @latitude - latitude for the area code
    @longitude - longitude for the area code
    """

    area_code = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    latitude = models.CharField(max_length=200)
    longitude = models.CharField(max_length=200)

    def __init__(self, area_code, city, state, latitude, longitude):
        self.area_code = area_code
        self.city = city
        self.state = state
        self.latitude = latitude
        self.longitude = longitude


class BackpageAdInfo(models.Model):
    """
    This model gives us a set of specific information from each add scraped from backpage.
    
    parameters:
    @ad_title - used primarily to uniquely identify package ads - since titles are unique
    @phone_number - the phone number used in the ad, can be empty. This number is stored as a 
    string since it should be thought of as immutable.
    @city - the city the ad is from
    @state - the state the ad is from
    @location - the location mentioned in the advertisement
    @latitude - latitude derived from the location mentioned in the advertisement
    @longitude - longitude derived from the location mentioned in the advertisement
    @ad_body - the long form text in the ad
    @photos - a filepath link to the set of pictures downloaded from the ad
    @post_id - an id for each backpage post from backpage
    @timestamp - when the ad was scraped
    @url - the url of the scraped ad
    """

    ad_title = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    latitude = models.CharField(max_length=200)
    longitude = models.CharField(max_length=200)
    ad_body = models.CharField(max_length=200)
    photos = models.CharField(max_length=200)
    post_id = models.CharField(max_length=200)
    timestamp = models.DateTimeField('backpage_ad_info_timestamp')
    url = models.CharField(max_length=200)

    def __init__(self, url, ad_title, phone_number, ad_body, location, latitude, longitude, photos, post_id, timestamp, city, state):
        self.url = url
        self.ad_title = ad_title
        self.phone_number = phone_number
        self.location = location
        self.latitude = latitude
        self.longitude = longitude
        self.ad_body = ad_body
        self.photos = photos
        self.post_id = post_id
        self.timestamp = timestamp
        self.city = city
        self.state = state
        

class Backpage(models.Model):
    """
    This model gives us high level information about backpage, the website.
    It is used to determine some metrics found in lectures/scraping_the_web.md 

    parameters:
    @timestamp - this is the time at which the content was scraped, it is assumed scrapers will run all the time,
    therefore the scrape time should be accurate to within an hour of scraping, this is used in some of the metrics
    for analysis.
    @frequency - this is the number of ads scraped at @timestamp and is used in many of the metrics for the scraper.
    """
    timestamp = models.DateTimeField('backpage_timestamp')
    frequency = models.CharField(max_length=200)

    def __init__(self, timestamp, frequency):
        self.timestamp = timestamp
        self.frequency = frequency
