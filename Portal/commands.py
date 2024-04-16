from news.models import *

u1=User.objects.create_user('User_Python')
u2=User.objects.create_user('User_Go')
u3=User.objects.create_user('User_Java')

a1=Author.objects.create(user=u1)
a2=Author.objects.create(user=u2)

c1=Category.objects.create(name='Спорт')
c2=Category.objects.create(name='Политика')
c3=Category.objects.create(name='Природа')
c4=Category.objects.create(name='Космос')

p1 = Post.objects.create(author_id=a1, _type='N', heading='Новый президент Аргентины', text_article='Что-то про президента Аргентины')
p2 = Post.objects.create(author_id=a1, _type='A', heading='Как правильно искать полярную звезду', text_article='Инструкция как правильно искать полярную звезду')
p3 = Post.objects.create(author_id=a1, _type='A', heading='Польза спорта на природе', text_article='Какой-то рассказ про огромную пользу спорта на природе')

p1.category.add(c2)
p2.category.add(c4)
p3.category.add(c1)
p3.category.add(c3)

com1 = Comment.objects.create(post_id=p1, user_id=User.objects.get(id=3), text='Some text')
com2 = Comment.objects.create(post_id=p1, user_id=User.objects.get(id=2), text='Some text')
com3 = Comment.objects.create(post_id=p2, user_id=User.objects.get(id=3), text='Some text')
com4 = Comment.objects.create(post_id=p3, user_id=User.objects.get(id=2), text='Some text')
com5 = Comment.objects.create(post_id=p2, user_id=User.objects.get(id=1), text='Some text')

p1.like()
p1.like()
p1.like()
p1.dislike()
p1.like()
p1.dislike()
p1.like()

p2.like()
p2.like()
p2.like()
p2.dislike()
p2.like()
p2.dislike()
p2.like()

p3.like()
p3.like()
p3.like()
p3.dislike()
p3.like()
p3.dislike()
p3.like()

a1.update_rating()
a2.update_rating()

result1 = Author.objects.all().order_by('rating').values('user__username', 'rating').first()
print(result1)

result2 = Post.objects.all().order_by('-rating').values('time_in', 'author_id__user__username', 'rating', 'heading').first()
print(result2)
result2 = Post.objects.all().order_by('-rating').first()
result2.preview()

result3 = Comment.objects.filter(post_id=result2)
print(result3)

