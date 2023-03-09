from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
# Create your views here.

def test(request):
    content = {'msg': '测试视图传递给模板数据'}
    views_str = "<a href='https://www.runoob.com/'>点击跳转</a>"
    #需要渲染模板，django提供了render将渲染数据提供给模板后，会返回一个httpresponse对象
    return  render(request,'book/index.html', {"views_str":views_str})
    # return HttpResponse('Hello World!')
