from django.conf import settings
from django.shortcuts import render
from .forms import ImageUploadForm
from fastai.vision.all import load_learner
from pathlib import Path
from .models import UploadedImage  # Import the UploadedImage model

# Ensure this function is updated with the correct path
def load_model():
    model_path = Path(settings.BASE_DIR) / 'models' / 'model_exported.pkl'
    learn = load_learner(model_path)
    return learn

def upload_and_predict(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            # Save the uploaded image using the model
            uploaded_image = UploadedImage(image=request.FILES['image'])
            uploaded_image.save()

            # The image file is now saved in MEDIA_ROOT/images/
            # Now prepare the image for prediction
            img_path = Path(uploaded_image.image.path)  # Use the path from the ImageField
            learn = load_model()  # Load the model
            pred, pred_idx, probs = learn.predict(img_path)  # Make a prediction

            # Prepare the context for rendering the results
            context = {
                'prediction': pred,
                'probability': probs[pred_idx].item(),  # Convert to a plain Python number
                'filename': uploaded_image.image.name,
                'image_url': uploaded_image.image.url  # Use the URL from the ImageField
            }

            # No need to manually remove the image file, as it's now managed by Django

            # Render the prediction result template
            return render(request, 'solarpanel_checker/prediction_result.html', context)
    else:
        form = ImageUploadForm()

    # Render the upload form template
    return render(request, 'solarpanel_checker/upload.html', {'form': form})
