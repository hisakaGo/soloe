from django.db import models


class List(models.Model):
    """リスト"""
    title = models.CharField('みだし', max_length=140, blank=True,)
    
    description = models.TextField('つけたし', blank=True,)
    
    def __str__(self):
        return self.title

class Content(models.Model):
    """収集する内容"""
    sort = models.IntegerField('ならび', default=0,)
    
    link = models.CharField('ありか', max_length=255, blank=True,)
    
    description = models.TextField('つけたし', blank=True,)
    
    image = models.ImageField('さしえ', \
                              height_field=90, \
                              width_field=160, \
                              blank=True,)
    
    parent = models.ForeignKey(List, \
                               verbose_name='そろい', \
                               on_delete=models.CASCADE, \
                               blank=True,
                               default=0)
    
    def __str__(self):
        return self.title

class Comment(models.Model):
    """コメント"""
    NONE = ''
    COOL = 'C'
    HOT = 'H'
    USEFUL = 'U'
    SPREAD = 'S'
    
    COMMENT_TYPE = ((NONE, ' '),
                    (COOL, 'かっけー'),
                    (HOT, 'あっちー'),
                    (USEFUL, 'やくだつ'),
                    (SPREAD, 'おひろめ'))
    
    comment = models.CharField('おもひ', max_length=255, blank=True)
    
    type = models.CharField('かんじ', \
                            max_length=1, \
                            choices=COMMENT_TYPE, \
                            default=NONE, \
                            blank=True)
    
    parent = models.ForeignKey(Content, \
                               verbose_name='かんじ', \
                               on_delete=models.CASCADE)
    
    def __str__(self):
        return self.comment
