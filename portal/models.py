from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
# Create your models here.




class Person(models.Model):
    FACULTY=(
        ('NS', 'Not Set'),
        ('BCT', 'Bachelor in Computer Engineering'),
        ('BCE', 'Bachelor in Civil Engineering')
    )
    ACADEMIC_STATUS=(
        (1, 'Not Set'),
        (2, 'Studying'),
        (3, 'Completed'),
        (4, 'Teaching'),
    )
    objects = models.Manager()
    full_name = models.CharField(max_length=100)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    relationships = models.ManyToManyField('self', through='Relationship', symmetrical=False, related_name='related_to')
    user_type = models.CharField(max_length=3, choices=FACULTY, default='NS')
    academic_status = models.IntegerField(choices=ACADEMIC_STATUS, default=1)
    description = models.TextField(max_length=500, null=True)
    status = models.BooleanField(default=False)

    def get_followers_number(self):
        return len(Relationship.objects.filter(to_person=self))
    
    def get_following_number(self):
        return len(Relationship.objects.filter(from_person=self))

    def get_following(self):
        following = Relationship.objects.filter(from_person=self)
        return following
    
    def get_followers(self):
        followers = Relationship.objects.filter(to_person=self)
        return followers
    
    def add_relationship(self, person, status):
        relationship, created = Relationship.objects.get_or_create(from_person=self, to_person=person)
        return relationship

    def remove_relationship(self, person, status):
        Relationship.objects.filter(
            from_person=self,
            to_person=person,
            status=status).delete()
        return

    def get_favourites(self):
        favourites =  Favourite.objects.filter(from_person=self)
        return favourites


    def __str__(self):
        return self.full_name


class Article(models.Model):
    DOC_TYPE = (
        (1, 'Paper'),
        (2, 'Project')
    )
    objects = models.Manager()
    name = models.CharField(max_length=500)
    last_edited = models.DateField(auto_now= True)
    uploaded_by = models.ForeignKey(Person, on_delete=models.CASCADE,related_name="owner")
    document = models.FileField(upload_to='files/', null=True)
    doc_type = models.IntegerField(choices=DOC_TYPE, default=1)
    collaborators = models.ManyToManyField(Person, related_name="collaborators")
    def get_favouritee(self):
        favourites = Favourite.objects.filter(to_article=self)
        return favourites
    def check_favourite(self, person):
        try:
            status = Favourite.objects.get(from_person=person, to_article=self)
            return True
        except:
            return False
    def get_comments(self):
        comments = Comment.objects.filter(to_article=self)
        return comments

    def __str__(self):
        return self.name

class Relationship(models.Model):
    objects = models.Manager()
    from_person = models.ForeignKey(Person, related_name='from_people', on_delete=models.CASCADE)
    to_person = models.ForeignKey(Person, related_name='to_people', on_delete=models.CASCADE)
    followed_on = models.DateField(auto_now=True)

    
    def __str__(self):
        return self.from_person.user.username

class Favourite(models.Model):
    objects = models.Manager()
    from_person = models.ForeignKey(Person, on_delete=models.CASCADE)
    to_article = models.ForeignKey(Article, on_delete=models.CASCADE)
    def __str__(self):
        return self.from_person.user.username + "-" + self.to_article.name


class Comment(models.Model):
    objects = models.Manager()
    from_person = models.ForeignKey(Person, on_delete=models.CASCADE)
    to_article = models.ForeignKey(Article, on_delete=models.CASCADE)
    comment = models.CharField(max_length=500)

    def __str__(self):
        return self.comment
