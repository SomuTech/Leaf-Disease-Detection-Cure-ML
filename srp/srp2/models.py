
from django.db import models

LeafName =(
    ("apple.h5", "apple"),
    ("blueberry.h5", "blueberry"),
    ("cherry.h5", "cherry"),
    ("corn.h5", "corn"),
    ("grape.h5", "grape"),
    ("orange.h5", "orange"),
    ("peach.h5", "peach"),
    ("pepper.h5", "pepper"),
    ("potato.h5", "potato"),
    ("raspberry.h5", "raspberry"),
    ("soybean.h5", "soybean"),
    ("squash.h5", "squash"),
    ("strawberry.h5", "strawberry"),
)

# Create your models here.
class PredictImg(models.Model):
    
    LeafName= models.CharField(max_length=20, choices = LeafName)
    userImg = models.ImageField(upload_to='upload/')
    
    
    