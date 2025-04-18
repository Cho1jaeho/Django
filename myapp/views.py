from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import GuestbookEntry
from .forms import GuestbookForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden  # 꼭 import 해줘!

def home(request):
    context = {
        'username': 'Jaeho',
        'message': '템플릿 상속까지 마스터 중!',
        'items': ['Python', 'Django', 'HTML', 'CSS'],
    }
    return render(request, 'myapp/home.html', context)

def about(request):
    context = {
        'name': '최재호',
        'major': '컴퓨터공학',
        'interests': '웹 개발, 인공지능, Django',
        'email': 'chlwogh6309@naver.com',
    }
    return render(request, 'myapp/about.html', context)

@login_required
def guestbook(request):
    if request.method == 'POST':
        form = GuestbookForm(request.POST)
        if form.is_valid():
            entry = form.save(commit=False)      # ✅ 저장 미루기
            entry.author = request.user          # ✅ 작성자 정보 추가
            entry.save()                         # ✅ DB에 최종 저장
            return redirect('guestbook')
    else:
        form = GuestbookForm()

    entries = GuestbookEntry.objects.order_by('-created_at')
    return render(request, 'myapp/guestbook.html', {'form': form, 'entries': entries})

def delete_entry(request, pk):
    entry = get_object_or_404(GuestbookEntry, pk=pk)

    # 🔐 작성자 확인
    if entry.author != request.user:
        return HttpResponseForbidden("이 글은 삭제할 수 없습니다.")
    
    entry.delete()
    return redirect('guestbook')

def edit_entry(request, pk):
    entry = get_object_or_404(GuestbookEntry, pk=pk)

    # 🔐 작성자 확인
    if entry.author != request.user:
        return HttpResponseForbidden("이 글은 수정할 수 없습니다.")

    if request.method == 'POST':
        form = GuestbookForm(request.POST, instance=entry)
        if form.is_valid():
            form.save()
            return redirect('guestbook')
    else:
        form = GuestbookForm(instance=entry)

    return render(request, 'myapp/edit_entry.html', {'form': form, 'entry': entry})