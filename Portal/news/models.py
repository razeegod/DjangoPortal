from django.db import models
from django.contrib.auth.models import User


news = 'N'
article = 'A'

articles_types = [
    (news, 'Новость'),
    (article, 'Статья')
]


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rating = models.FloatField(default=0.0)

    def update_rating(self):
        sum_rating_com_to_auth = 0
        posts = Post.objects.filter(author_id=self)
        comments = Comment.objects.filter(user_id=self.user)
        comments_to_author = Comment.objects.filter(post_id__author_id=self)
        self.rating = 0
        for post in posts:
            post.rating = post.rating * 3
            post.save()
        for comment in comments:
            print(comment.rating)
            self.rating += comment.rating
        for comment in comments_to_author:
            sum_rating_com_to_auth += comment.rating

        self.save()

        print(f'Суммарный рейтинг всех комментариев автора: {self.rating}')
        print('-'*10)
        print(f'Суммарный рейтинг комментариев к статьям автора: {sum_rating_com_to_auth}')
        print('-'*10)
        print(f'Рейтинг каждой статьи автора был умножен на 3')




class Category(models.Model):
    name = models.CharField(unique=True, max_length=255)


class Post(models.Model):
    author_id = models.ForeignKey(Author, on_delete=models.CASCADE)
    _type = models.CharField(choices=articles_types, max_length=1)
    time_in = models.DateTimeField(auto_now_add=True)
    category = models.ManyToManyField(Category, through='PostCategory')
    heading = models.CharField(max_length=255)
    text_article = models.TextField()
    rating = models.FloatField(default=0.0)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

    def preview(self):
        return f'{self.text_article[:125]}...'


class PostCategory(models.Model):
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    category_id = models.ForeignKey(Category, models.CASCADE)


class Comment(models.Model):
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    time_add = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()