from django.shortcuts import render
from PIL import Image
import os
from django.core.files.storage import default_storage
from django.conf import settings
import uuid

def index(request):
    return render (request, 'converter/index.html')

def convert_images(request):
    message = ''
    converted_files = []
    if request.method == 'POST' and request.FILES.getlist('images'):
        images = request.FILES.getlist('images')
        output_format = request.POST.get('format', 'PNG').lower()
        width = request.POST.get('width')
        height = request.POST.get('height')
        quality = request.POST.get('quality')

        try:
            width = int(width) if width else None
            height = int(height) if height else None
            quality = int(quality) if quality else 85
        except ValueError:
            message = "Width, Height, and Quality must be valid numbers!"
            return render(request, 'converter/index.html', {'message': message})
        
        output_dir = os.path.join(settings.MEDIA_ROOT, 'converted')
        os.makedirs(output_dir, exist_ok=True)

        success = 0
        
        for image_file in images:
            try :
                img = Image.open(image_file)
                if width and height:
                    img = img.resize((width, height))
                
                if output_format in ["jpg", "jpeg"]:
                    img = img.convert("RGB")

                filename = f"{uuid.uuid4()}.{output_format}"
                path = os.path.join(output_dir, filename)

                if output_format in ["jpg", "jpeg"]:
                    img.save(path, output_format.upper(), quality=quality)
                else:
                    img.save(path, output_format.upper())
                
                converted_files.append(f"{settings.MEDIA_URL}converted/{filename}")
                success += 1
            except Exception as e:
                print(f"Error: {e}")

        message = f"Conversion complete: {success} / {len(images)} files converted."

    return render(request, 'converter/index.html', {
        'message': message, 
        'converted_files': converted_files
    })