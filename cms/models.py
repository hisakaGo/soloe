from django.db import models
from django.contrib.auth.models import User


class List(models.Model):
    """リスト"""
    title = models.CharField('みだし', max_length=140,)

    creatorId = models.ForeignKey(User, related_name='+', on_delete=models.DO_NOTHING,)
    creatorName = models.CharField('つくりて', max_length=255, blank=True,)
    createdOn = models.DateTimeField('つくりどき', auto_now_add=True,)
    updaterId = models.ForeignKey(User, on_delete=models.DO_NOTHING,)
    updaterName = models.CharField('なおして', max_length=255, blank=True,)
    updaterOn = models.DateTimeField('なおしどき', auto_now=True,)
    
    def __str__(self):
        return self.title

class Image(models.Model):
    """画像"""
    image = models.ImageField('さしえ',
                              height_field=90,
                              width_field=160,)
    
    isTemp = models.BooleanField('一時フラグ', default=False,)

    creatorId = models.ForeignKey(User, related_name='+', on_delete=models.DO_NOTHING,)
    creatorName = models.CharField('つくりて', max_length=255, blank=True,)
    createdOn = models.DateTimeField('とき', auto_now_add=True,)

class Content(models.Model):
    """収集する内容"""
    sort = models.IntegerField('ならび', default=0,)
    
    link = models.CharField('ありか', max_length=255, blank=True,)
    
    description = models.CharField('つけたし', max_length=255, blank=True,)
    
    image = models.ForeignKey(Image,
                              verbose_name='さしえ',
                              on_delete=models.SET_NULL,
                              null=True,)
    
    parent = models.ForeignKey(List,
                               verbose_name='そろい',
                               on_delete=models.CASCADE,
                               default=0,)

    creatorId = models.ForeignKey(User, related_name='+', on_delete=models.DO_NOTHING,)
    creatorName = models.CharField('つくりて', max_length=255, blank=True,)
    createdOn = models.DateTimeField('つくりどき', auto_now_add=True,)
    updaterId = models.ForeignKey(User, on_delete=models.DO_NOTHING,)
    updaterName = models.CharField('なおして', max_length=255, blank=True,)
    updaterOn = models.DateTimeField('なおしどき', auto_now=True,)
    
    def __str__(self):
        return self.link

class Comment(models.Model):
    """コメント"""
    coolFlg = models.BooleanField('かっけー', default=False,)
    
    hotFlg = models.BooleanField('げきあつ', default=False,)
    
    usefulFlg = models.BooleanField('おやくだち', default=False,)
    
    spreadFlg = models.BooleanField('おひろめ', default=False,)

    tags = models.CharField('しるし', max_length=255, blank=True,)
    
    comment = models.CharField('おもひ', max_length=255, blank=True)
    
    parent = models.ForeignKey(Content,
                               verbose_name='かんじ',
                               on_delete=models.CASCADE)


    creatorId = models.ForeignKey(User, related_name='+', on_delete=models.DO_NOTHING,)
    creatorName = models.CharField('つくりて', max_length=255, blank=True,)
    createdOn = models.DateTimeField('つくりどき', auto_now_add=True,)
    updaterId = models.ForeignKey(User, on_delete=models.DO_NOTHING,)
    updaterName = models.CharField('なおして', max_length=255, blank=True,)
    updaterOn = models.DateTimeField('なおしどき', auto_now=True,)
    
    def __str__(self):
        return self.comment
