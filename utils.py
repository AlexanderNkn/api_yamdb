import random
import string

from objects.models import Object
from reviews.models import Review, Comment, User


titles = ["LOTR", "GOT", "OITNB", "BB", "ST"]
for title in titles:
    Object.objects.get_or_create(name=title)

# users = [("mark"), ("adam"), ("paul"), ("karl"), ("adolf")]
# for user in users:
#     User.objects.create_user(username=user, password="testgfhjkm")

object = Object.objects.get(id=2)
authors = User.objects.all()
for _ in range(20):
    Review.objects.create(
        object=object,
        text=''.join(random.choices(string.ascii_uppercase, k=10)),
        author = random.choice(authors),
        score = random.choice(range(1, 11))
    )
    


    