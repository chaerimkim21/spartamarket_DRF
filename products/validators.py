from django.core.validators import validate_image_file_extension
from django.core.exceptions import ValidationError
from django.core.files.uploadedfile import UploadedFile
from rest_framework.exceptions import PermissionDenied
from .models import Product

def validate_product_upload(product_data):
    title = product_data.get('title'),
    content = product_data.get('content'),
    image = product_data.get('image')

    err_msg_list = []

    required_fields = ['title', 'content', 'image']
    for field in required_fields:
        if not product_data.get(field):
            err_msg_list.append(f"{field.replace('_', ' ').capitalize()} 입력이 필요합니다")

    # image가 제공되었다면 image file을 validate하기
    if image:
        # 제공된 파일이 UploadedFile 객체인지 validate
        if not isinstance(image, UploadedFile):
            err_msg_list.append("올바른 파일이 아닙니다.")
        else:
            try:
                validate_image_file_extension(image)
            except ValidationError:
                err_msg_list.append("이미지 파일의 확장자가 올바르지 않습니다. .jpg, .png 등만 허용됩니다.")

    return not bool(err_msg_list), err_msg_list

def validate_product_update(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        raise PermissionDenied("상품을 찾을 수 없습니다.")

    # 요청자가 게시글의 작성자와 일치하는지 확인 
    if product.author != request.user:
        raise PermissionDenied("상품의 작성자만 수정할 수 있습니다.")

    return product

def validate_product_delete(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        raise PermissionDenied("상품을 찾을 수 없습니다.")

    # 요청자가 게시글의 작성자와 일치하는지 확인 
    if product.author != request.user:
        raise PermissionDenied("상품의 작성자만 삭제할 수 있습니다.")

    return product
