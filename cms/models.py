from django.db import models


class List(models.Model):
    """リスト"""
    title = models.CharField('みだし', max_length=140, blank=True,)

    tags = models.CharField('しるし', max_length=255, blank=True,)
    
    def __str__(self):
        return self.title

class Image(models.Model):
    """画像"""
    image = models.ImageField('さしえ',
                              height_field=90,
                              width_field=160,)

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
    
    def __str__(self):
        return self.link

class Comment(models.Model):
    """コメント"""
    coolFlg = models.BooleanField('かっけー', default=False,)
    
    hotFlg = models.BooleanField('あっちー', default=False,)
    
    usefulFlg = models.BooleanField('おやくだち', default=False,)
    
    spreadFlg = models.BooleanField('おひろめ', default=False,)
    
    comment = models.CharField('おもひ', max_length=255, blank=True)
    
    parent = models.ForeignKey(Content,
                               verbose_name='かんじ',
                               on_delete=models.CASCADE)
    
    def __str__(self):
        return self.comment
