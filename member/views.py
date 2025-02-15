from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login


# member 메인
def member_main(request):
    return render(request, 'member/member_main.html')  # 템플릿 파일 경로 지정

# 점주 회원관리
def member_store(request):
    return render(request, 'member/member_store.html')

# 회원 마이페이지
def member_page(request):
    return render(request, 'member/member_page.html')

# 회원정보수정
def member_edit(request):
    if request.method == "POST":
        user_id = request.POST['user_id']
        username = request.POST['username']
        phone_num = request.POST['phone_num']
        email = request.POST['email']

        # 아이디 중복 확인
        if User.objects.filter(username=user_id).exists():
            return render(request, "member/member_edit.html", {'error': '이미 존재하는 아이디입니다.'})

            return JsonResponse({"success": True})  # 성공 응답

    # 회원정보수정 페이지로 이동
    return render(request, 'member/member_edit.html')

# 비밀번호변경
def member_pw(request):
    return render(request, 'member/member_pw.html')

# 회원탈퇴
def member_delete(request):
    return render(request, 'member/member_delete.html')

# 회원탈퇴사유 입력
def member_delete_detail(request):
    return render(request, 'member/member_delete_detail.html')