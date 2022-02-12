def handle_uploaded_file(f):
    with open('flower_detection\static\js\fileuploaded'+f.name,'wb+')as destination:
        for chunk in f.chunk():
            destination.write(chunk)