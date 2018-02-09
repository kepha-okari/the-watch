from django.db import models
import datetime as dt
from django.contrib.auth.models import User

class Neighborhood(models.Model):
    '''
    A class that defines the blueprint of a Neighborhood model
    '''
    neighborhood_name = models.CharField(max_length =30,null=True)
    neighborhood_location = models.CharField(max_length =30, null =True)
    population = models.PositiveIntegerField(default=0)
    user = models.ForeignKey(User)

    def __str__(self):
        return self.neighborhood_name

    def create_neighborhood(self):
        '''
        Methods that saves a new neighborhood
        '''
        self.save()

    def delete_neighborhood(self):
        '''
        Methods that deletes an exiting neighborhood
        '''
        self.delete()

    def update_neighborhood(self):
        '''
        Methods that updates an exiting neighborhood
        '''
        pass

    def update_occupants(self):
        email = models.EmailField(max_length=70,blank=True)
        '''
        Methods that updates the population size
        '''

        pass

    @classmethod
    def find_neighbourhood(neigborhood_id):
        '''
        Method to search for a particular neighbourhood
        '''
        query = cls.objects.filter(pass__icontains=search_term)
        return query

class Business(models.Model):
    '''
    A class that defines the business blueprint
    '''
    business_name = models.CharField(max_length =30,null=True)
    email =  models.EmailField(max_length=70,blank=True)
    hood_id = models.ForeignKey(User,on_delete=models.CASCADE)

class Profile(models.Model):
    '''
    A class that defines the profile blueprint of the User
    '''
    profile_photo = models.ImageField(upload_to = 'profiles/', null=True)
    name = models.CharField(max_length =30,null=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)


    pass
class Post(models.Model):
    '''
    A class that defines posts of the users
    '''
    image = models.ImageField(upload_to = 'photos/', null = True,blank=True,)
    image_name = models.CharField(max_length=30)
    message =models.TextField(max_length = 100, null =True,blank=True)
    date_uploaded = models.DateTimeField(auto_now_add=True, null=True)
    profile = models.ForeignKey(Profile,null =True,blank=True, on_delete=models.CASCADE)
    user = models.ForeignKey(User)

    class Meta:
        ordering = ['-date_uploaded']

    def save_post(self):
        '''Method to save an post in the database'''
        self.save()

    def delete_post(self):
        ''' Method to delete an post from the database'''
        self.delete()

    @classmethod
    def get_posts(cls):
        '''
        Method that gets all posts from the database
        Returns:
            images : list of post objects from the database
        '''
        messages = Post.objects.all()
        return messages
