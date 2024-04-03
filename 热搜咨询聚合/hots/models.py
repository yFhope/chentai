from django.db import models


class HotsModel(models.Model):
    title = models.CharField(verbose_name='热点标题', max_length=255,blank=True, null=True)
    url = models.CharField(verbose_name='详情页URL', max_length=255,blank=True, null=True)
    source = models.CharField(verbose_name='数据来源',max_length=255,blank=True, null=True)

    def __str__(self):
        return self.title


# class Resou(models.Model):
#     title = models.CharField(max_length=255, blank=True, null=True)
#     url = models.CharField(max_length=255, blank=True, null=True)
#     source = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'resou'

