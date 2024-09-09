from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from .models import User


def validate_signup(signup_data):
    username = signup_data.get('username')
    password = signup_data.get('password')
    nickname = signup_data.get('nickname')
    birth = signup_data.get('birth')
    first_name = signup_data.get('first_name')
    last_name = signup_data.get('last_name')
    email = signup_data.get('email')

    err_msg_list = []

    required_fields = ['username', 'password', 'nickname', 'birth', 'first_name', 'last_name', 'email']
    for field in required_fields:
        if not signup_data.get(field):
            err_msg_list.append(f"{field.replace('_', ' ').capitalize()} 입력이 필요합니다")

    # validation
    if len(nickname) > 20:
        err_msg_list.append("닉네임은 20자 이내로 입력하세요.")

    if username and User.objects.filter(username=username).exists():
        err_msg_list.append("이미 존재하는 유저네임입니다.")

    # 이메일 validation
    try:
        if email:
            validate_email(email)
    except ValidationError:
        err_msg_list.append("이메일 형식이 올바르지 않습니다.")

    return not bool(err_msg_list), err_msg_list


def validate_update_user(user_data):
    nickname = user_data.get('nickname')

    # validation
    if len(nickname) < 3:
        return False, "닉네임임은 3자 이상으로 입력하세요."
    if len(nickname) > 20:
        return False, "닉네임은 20자 이내로 입력하세요."
