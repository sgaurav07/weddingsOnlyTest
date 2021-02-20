from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from rest_framework.response import Response
from .utilities import authenticate
from .models import *
import json
from rest_framework import filters
from rest_framework import generics
from django.template.defaultfilters import slugify

# @csrf_exempt
# @api_view(["GET"])
# def helloView(request):
#     content = {'message': 'Hello, World!'}
#     return Response(content, status=HTTP_200_OK)

@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def generateToken(request):
    username = request.data.get("username")
    password = request.data.get("password")
    if username is None or password is None:
        return Response({'error': 'Please provide both username and password'},
                        status=HTTP_400_BAD_REQUEST)
    user = authenticate(username=username, password=password)
    if not user:
        return Response({'error': 'Invalid Credentials'},status=HTTP_404_NOT_FOUND)
    else:
        try:
            userObj =  User.objects.get(username=username)
            try:
                tokenObj = Token.objects.get(user=userObj)
            except:
                tokenObj = Token.objects.create(user=userObj)
            message = "Use this generated Token with Authorisation : Token " + str(tokenObj.key )
        except:
            userObj = User(username=username)
            userObj.is_superuser=False
            userObj.is_staff=False
            userObj.save()
            tokenObj = Token.objects.create(user=userObj)
            message = "Use this generated Token with Authorisation : Token " + str(tokenObj.key )
    return Response({'token': tokenObj.key, 'message': message},status=HTTP_200_OK)

@csrf_exempt
@api_view(["POST"])
def createBlog(request):
    title = request.data.get('title')
    image = request.data['image']
    description = request.data.get('description')
    try:
        blogobj = Blog.objects.create(title=title, description=description, image=image)
        message = "Blog Created Successfully"
        status = HTTP_200_OK
    except:
        message = "Some Error Occured in Blog Creation Contact admin"
        status = HTTP_400_BAD_REQUEST
    return Response({'message': message},status=status)

@csrf_exempt
@api_view(["PUT"])
def updateBlog(request):
    blogid, title, image, description = None, None, None, None
    if "id" in request.data:
        blogid = request.data.get('blogid')
    if "title" in request.data:
        title = request.data.get('title')
    if "image" in request.data:
        image = request.data['image']
    if "description" in request.data:
        description = request.data.get('description')
    try:
        blogobj = Blog.objects.get(id=blogid)
        if title:
            blogobj.title = title
            blogobj.slug = slugify(title)
        if description:
            blogobj.description = description
        if image:
            blogobj.image = image
        blogobj.save()
        message = "Blog Updated Successfully"
        status = HTTP_200_OK
    except:
        message = "Blog not available with the given Blog-Id"
        status = HTTP_400_BAD_REQUEST
    return Response({'message': message},status=status)

@csrf_exempt
@api_view(["PUT"])
def softDeleteBlog(request):
    blogid = request.data.get('blogid')
    isDelete = request.data.get('delete')
    try:
        blogobj = Blog.objects.get(id=blogid)
        if isDelete == True or isDelete == "true" or isDelete == "True" or isDelete == "TRUE":
            blogobj.isDelete = 1
        blogobj.save()
        message = "Blog Deleted Successfully"
        status = HTTP_200_OK
    except:
        message = "Blog not available with the given Blog-Id"
        status = HTTP_400_BAD_REQUEST
    return Response({'message': message},status=status)


@csrf_exempt
@api_view(["GET"])
def searchBlog(request):
    try:
        blogTitle = request.data.get('title')
        search_fields = ['title']
        filter_backends = (filters.SearchFilter,)
        queryset = Blog.objects.all()
        queryResults = queryset.filter(title__contains = blogTitle)
        # serializerData = BlogSerializer
        # retval = json(serializerData.data)
        returnData = list()
        for q in queryResults:
            returnList = []
            title = q.title
            description = q.description
            if q.isDelete == 0:
                returnList.append(title)
                returnList.append(description)
                returnData.append(returnList)
            else:
                returnData.append("Searched blog is not in the Database. Maybe it was deleted by You!")
            status = HTTP_200_OK
    except:
        returnData ="Some error occurred while finding blog"
        status = HTTP_400_BAD_REQUEST
    return Response(returnData,status=status)

@csrf_exempt
@api_view(["PUT"])
def publishBlog(request):
    blogid = request.data.get('blogid')
    published = request.data.get('publish')
    try:
        blogobj = Blog.objects.get(id=blogid)
        if published == str(1) or published == True:
            blogobj.published = 1
        blogobj.save()
        message = "Blog Published Successfully"
        status = HTTP_200_OK
    except:
        message = "Blog not available with the given Blog-Id"
        status = HTTP_400_BAD_REQUEST
    return Response({'message': message},status=status)


@csrf_exempt
@api_view(["GET"])
def viewBlog(request):
    try:
        blogobj = Blog.objects.all()
        returnData = list()
        for q in blogobj:
            returnDict = dict()
            blogid = q.id
            title = q.title
            description = q.description
            published = q.published
            isDelete = q.isDelete
            createdDate = q.createdDate
            lastUpdated = q.lastUpdated
            returnDict["blogid"]=blogid
            returnDict["title"]=title
            returnDict["description"]=description
            returnDict["createdDate"]=createdDate
            returnDict["published"]=published
            returnDict["isDelete"]=isDelete
            returnDict["lastUpdated"]=lastUpdated
            returnData.append(returnDict)
        message = "All Blog Fetched Successfully"
        status = HTTP_200_OK
    except:
        returnData ="Some error occurred while fetching blog"
        status = HTTP_400_BAD_REQUEST
    return Response(returnData,status=status)