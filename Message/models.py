from django.db import models
from Player.models import Player


class Message(models.Model):
    playerFrom = models.ForeignKey(Player, on_delete='', related_name='PlayerFrom')
    playerTo = models.ForeignKey(Player, on_delete='', related_name='PlayerTo')
    messageText = models.TextField(verbose_name=u'MessageText', max_length=1000, blank=True)

    def __unicode__(self):
        return self.messageText
