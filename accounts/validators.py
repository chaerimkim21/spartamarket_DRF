from datetime import datetime
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from rest_framework.exceptions import PermissionDenied
from django.contrib.auth import authenticate

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
    username = user_data.get('username')
    nickname = user_data.get('nickname')
    email = user_data.get('email')
    birth = user_data.get('birth')
    # gender, introduction 입력은 생략 가능
    gender = user_data.get('gender', '')
    introduction = user_data.get('introduction', '')

    # Email validation
    if email:
        try:
            validate_email(email)
        except ValidationError:
            return False, "유효하지 않은 이메일 주소입니다."

        if User.objects.filter(email=email).exists():
            return False, "이미 사용 중인 이메일입니다."

    # Username validation
    if not username:
        return False, "유저네임을 입력해 주세요."
    
    if User.objects.filter(username=username).exists():
        return False, "이미 사용 중인 유저네임입니다."
    
    # nickname validation
    if not nickname:
        return False, "닉네임을 입력해 주세요."

    # birth validation
    if not birth:
        return False, "생년월일을 입력해 주세요."
    try:
        datetime.strptime(birth, '%Y-%m-%d')
    except ValueError:
        return False, "유효하지 않은 생년월일 형식입니다. YYYY-MM-DD 형식으로 입력하세요."
    return True, None

def validate_delete_user(request_data, user):
    password = request_data.get("password")
    if not password:
        return False, "비밀번호를 입력해 주세요."
    
    if not user.check_password(password):
        return False, "비밀번호가 일치하지 않습니다."
    
    return True, None
