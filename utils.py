from objects.models import Object
from reviews.models import Review, Comment, User


titles = ["LOTR", "GOT", "OITNB", "BB", "ST"]
for title in titles:
    Object.objects.get_or_create(name=title)

users = [("mark"), ("adam"), ("paul"), ("karl"), ("adolf")]
for user in users:
    User.objects.create_user(username=user, password="testgfhjkm")
