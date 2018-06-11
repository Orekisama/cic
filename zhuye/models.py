from django.db import models

# Create your models here.
class Cic(models.Model):
    id = models.AutoField(primary_key=True)
    datetime = models.DateTimeField(verbose_name=u"报障时间", auto_now=True)
    ip = models.GenericIPAddressField(verbose_name=u"客户出口ip", null=True)
    dns = models.GenericIPAddressField(verbose_name=u"客户出口dns")
    domain = models.CharField(verbose_name=u"报障域名", max_length=200)
    ccip = models.GenericIPAddressField(verbose_name=u"蓝汛ip")
    faultImg = models.ImageField(verbose_name=u"报错截图", null=True)                                                                    
