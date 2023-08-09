from django.http import FileResponse
from django.shortcuts import get_object_or_404
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from authentication.models import CustomUser
from document.models import Document
from document.serializers import DocumentListSerializer, DocumentSerializer
from authentication.permissions import IsAdminOrOwner
from django.contrib.auth.models import User
from django.db.models import Q



# Retrieve all documets
@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_all_document(request):
    try:
        documents = Document.objects.all()

        serializer = DocumentListSerializer(documents, many=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response(f"Error: {str(e)}", status=status.HTTP_400_BAD_REQUEST)
   

# Retrieve a document
@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated, IsAdminOrOwner])
def document_detail_view(request, document_id):

    document = Document.objects.get(id=document_id)

    serializer = DocumentListSerializer(document)

    return Response(serializer.data, status=status.HTTP_200_OK)



# Update a documemnt
@api_view(['PUT'])
@permission_classes([permissions.IsAuthenticated, IsAdminOrOwner])
def document_update_view(request, document_id):
    document = Document.objects.get(id=document_id)
    
    serializer = DocumentSerializer(document, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




# Delete a document
@api_view(['DELETE'])
@permission_classes([permissions.IsAuthenticated, IsAdminOrOwner])
def document_delete_view(request, document_id):
    document = Document.objects.get(id=document_id)
    document.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)



# Upload a document
@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def document_upload_view(request):
    data = request.data
    filtered_data = {}
    filtered_data['title'] = data.get('title')
    filtered_data['description'] = data.get('description')
    filtered_data['format'] = data.get('format')
    filtered_data['file'] = data.get('file')
    # owner_id = data.request.get('owner')
    filtered_data['owner'] = request.user.id

    serializer = DocumentSerializer(data=filtered_data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Download a document
@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def document_download_view(request, document_id):
    document = get_object_or_404(Document, id=document_id)
    print(request.user, document.owner)
    print(document)

    if request.user.id == document.owner.id or request.user in document.shared_with.all():
        file_path = document.file.path
        response = FileResponse(open(file_path, 'rb'))
        response['Content-Disposition'] = f'attachment; filename="{document.title}.{document.format}"'
        return response
    else:
        return Response({'detail': 'You do not have permission to access this document.'}, status=status.HTTP_403_FORBIDDEN)




# Search documentss
@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def document_search_view(request):
    search_query = request.query_params.get('q', '')
    
    documents = Document.objects.filter(
        Q(title__icontains=search_query) |
        Q(description__icontains=search_query) |
        Q(format__icontains=search_query) |
        Q(upload_date__icontains=search_query)
    )
    
    serializer = DocumentListSerializer(documents, many=True)
    return Response(serializer.data)


#! Share Documents
@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def shared_document_list_view(request):
    shared_documents = Document.objects.filter(shared_with=request.user)
    serializer = DocumentListSerializer(shared_documents, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated, IsAdminOrOwner])
def share_document_view(request, document_id):
    document = Document.objects.get(id=document_id)
    
    user_ids = request.data.get('user_ids', [])
    for user_id in user_ids:
        user = User.objects.get(id=user_id)
        document.shared_with.add(user)
    
    document.save()
    serializer = DocumentSerializer(document)
    return Response(serializer.data)





@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated, IsAdminOrOwner])
def admin_document_download_view(request, document_id):
    document = get_object_or_404(Document, id=document_id)
    file_path = document.file.path
    response = FileResponse(open(file_path, 'rb'))
    response['Content-Disposition'] = f'attachment; filename="{document.title}.{document.format}"'
    return response


# Search documentss
@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def document_search_view(request):
    search_query = request.query_params.get('q', '')
    
    # Search documents by title, description, format, or upload date
    documents = Document.objects.filter(
        Q(title__icontains=search_query) |
        Q(description__icontains=search_query) |
        Q(format__icontains=search_query) |
        Q(upload_date__icontains=search_query)
    )
    
    serializer = DocumentListSerializer(documents, many=True)
    return Response(serializer.data)