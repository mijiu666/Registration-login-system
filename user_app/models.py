from django.db import models

# Create your models here.
class UserInfo(models.Model):
    id = models.AutoField(primary_key=True,verbose_name='ID')
    username = models.CharField(max_length=10,verbose_name="用户名",unique=True)
    password = models.CharField(max_length=128,verbose_name="密码")
    sex = models.CharField(max_length=1,choices=(("0","女"),("1","男")),verbose_name="性别")
    email = models.EmailField(verbose_name="邮箱",unique=True)
    # unique = True 唯一
    phone = models.CharField(max_length=11,verbose_name="电话",unique=True)
    birthday = models.DateField(verbose_name="生日")
    is_deleted = models.BooleanField(verbose_name="删除用户",default=0)
    create_data = models.DateTimeField(auto_now_add=True,verbose_name="注册日期")
    updata = models.DateTimeField(auto_now=True,verbose_name="修改时间")

    def __str__(self):
        return f"{self.username}"
    class Meta:
        db_table = "user_info"
        verbose_name = "用户信息"
        verbose_name_plural = "用户信息"
