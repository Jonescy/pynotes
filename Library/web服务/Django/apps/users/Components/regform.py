"""
@Author: Jonescyna@gmail.com
@Created: 2021/4/9
"""
import re
from django import forms
from apps.users import models


class RegForm(forms.Form):
    username = forms.CharField(
        label='用户名',
        min_length=3,
        max_length=15,
        error_messages={
            'required': '用户名不能为空',
            'min_length': '用户名最小3位',
            'max_length': '用户名最大15位',

        },
        widget=forms.widgets.TextInput(attrs={'class': 'form-control'})
    )
    password = forms.CharField(
        label='密码',
        min_length=3,
        max_length=12,
        error_messages={
            'required': '密码不能为空',
            'min_length': '密码最小3位',
            'max_length': '密码最大12位',
        },
        widget=forms.widgets.PasswordInput(attrs={'class': 'form-control'},
                                           render_value=True  # 输入框校验不通过时，保留当前输入值
                                           )

    )
    confirm_password = forms.CharField(
        label='确认密码',
        min_length=3,
        max_length=12,
        error_messages={
            'required': '确认密码不能为空',
            'min_length': '确认密码最小3位',
            'max_length': '确认密码最大12位',
        },
        widget=forms.widgets.PasswordInput(attrs={'class': 'form-control'},
                                           render_value=True,  # 输入框校验不通过时，保留当前输入值
                                           )
    )
    email = forms.EmailField(
        label='邮箱',
        error_messages={
            'required': '邮箱不能为空',
            'invalid': '邮箱格式不正确',
        },
        widget=forms.widgets.EmailInput(attrs={'class': 'form-control'})

    )

    # 钩子函数
    # 局部钩子：校验用户名已存在
    def clean_username(self):
        username = self.cleaned_data.get('username')
        is_exist = models.Users.objects.filter(username=username)
        if is_exist:
            # 提示信息
            self.add_error('username', '用户名已存在')
        return username

    def clean_password(self):
        password = self.cleaned_data.get('password')
        patten = re.compile(r"^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,12}$")
        is_valid = patten.match(password)
        if is_valid is None:
            self.add_error(password, '密码必须以大或小写字母开头，必须包含一个大小字母，一个小写字母，一个数字')
        return password

    # 全局钩子：校验2次密码是否一致
    def clean(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if not password == confirm_password:
            self.add_error('confirm_password', '两次密码不一致')
        return self.cleaned_data
