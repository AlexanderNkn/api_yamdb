import random
import string

from contents.models import Title
from reviews.models import Review, Comment
from users.models import User 


titles = ["LOTR", "GOT", "OITNB", "BB", "ST"]
for title in titles:
    Title.objects.get_or_create(name=title)

# users = [("mark"), ("adam"), ("paul"), ("karl"), ("adolf")]
# for user in users:
#     User.objects.create_user(username=user, password="testgfhjkm")

title = Title.objects.get(id=2)
authors = User.objects.all()
for _ in range(20):
    Review.objects.create(
        title=title,
        text="".join(random.choices(string.ascii_uppercase, k=10)),
        author=random.choice(authors),
        score=random.choice(range(1, 11)),
    )


User.objects.create(username="arseniy", password="testfhjkm")
