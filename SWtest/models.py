from __future__ import unicode_literals
import PIL
from django.db import models

# Create your models here.

def path(instance, name):
    return 'SWtest/images/%s' % name


class Answ(models.Model):
    answer = models.TextField(verbose_name='Answer', max_length=300, blank=True)
    true = ((True, 'Right',),
            (False, u'False',))
    true_or_false = models.BooleanField(verbose_name='Right Answer?', max_length=5, choices=true, default=False)

    def __unicode__(self):
        return '%s' % self.answer




class Quest(models.Model):
    subj = models.TextField(verbose_name='Question', max_length=300)
    img_pic = models.ImageField(verbose_name='Image for question', help_text='Not required',  blank=True, upload_to=path)
    answer1 = models.ForeignKey(Answ, verbose_name='Answer', related_name='question1', blank=True, null=True)
    answer2 = models.ForeignKey(Answ, verbose_name='Answer', related_name='question2', blank=True, null=True)
    answer3 = models.ForeignKey(Answ, verbose_name='Answer', related_name='question3', blank=True, null=True)
    answer4 = models.ForeignKey(Answ, verbose_name='Answer', related_name='question4', blank=True, null=True)

    def __unicode__(self):
        return '%s' % self.id


