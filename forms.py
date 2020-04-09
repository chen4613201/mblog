from wtforms import *


class Myvalidators(object):
    '''自定义验证规则'''
    def __init__(self,message):
        self.message = message
    def __call__(self, form, field):
        print(field.data,"用户输入的信息")
        if field.data == "haiyan":
            return None
        raise validators.ValidationError(self.message)

class LoginForm(Form):
    '''Form'''
    name = simple.StringField(
        label="用户名",
        widget=widgets.TextInput(),
        validators=[
            Myvalidators(message="用户名必须是haiyan"),#也可以自定义正则
            validators.DataRequired(message="用户名不能为空"),
            validators.Length(max=8,min=3,message="用户名长度必须大于%(max)d且小于%(min)d")
        ],
        render_kw={"class":"form-control"}  #设置属性
    )

    pwd = simple.PasswordField(
        label="密码",
        validators=[
            validators.DataRequired(message="密码不能为空"),
            validators.Length(max=8,min=3,message="密码长度必须大于%(max)d且小于%(min)d"),
            validators.Regexp(regex="\d+",message="密码必须是数字"),
        ],
        widget=widgets.PasswordInput(),
        render_kw={"class":"form-control"}
    )

    rememberme = simple.BooleanField(
        label="记住我的选择",
        widget=widgets.CheckboxInput(),
        default=False,
        render_kw={"class":"form-control","style":"height:unset"}
    )



