from django.core.validators import validate_email

def validate_signup(signup_data):
    username = signup_data.get('username')
    password = signup_data.get('password')
    nickname = signup_data.get('nickname')
    birth = signup_data.get('birth')
    first_name = signup_data.get('first_name')
    last_name = signup_data.get('last_name')
    email = signup_data.get('email')
    
    # validation
    if len(nickname) > 20:
        return False, "닉네임은 20자 이내로 입력하세요."

    try:
        validate_email(email)
    except:
        return False, "올바른 이메일 형식이 아닙니다."

    return True, None
