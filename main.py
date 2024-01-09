import matplotlib.pyplot as plt
import numpy as np 
from PIL import Image

# Load the yummy_macarons image
image_path = 'yummy_macarons.jpg'
macarons_image = Image.open(image_path)

# Get image information
image_size = macarons_image.size
image_mode = macarons_image.mode

# Convert the image to grayscale
gray_macarons_image = macarons_image.convert('L')

# Create a figure with custom styling
fig, axes = plt.subplots(1, 3, figsize=(18, 6))
fig.suptitle('Exploring Yummy Macarons Image', fontsize=16)

# Display the original image with additional information
axes[0].imshow(macarons_image)
axes[0].set_title(f'Original Image\nSize: {image_size}\nMode: {image_mode}')
axes[0].axis('off')  # Turn off axis labels

# Display the grayscale image
axes[1].imshow(gray_macarons_image, cmap='gray')
axes[1].set_title('Grayscale Image')
axes[1].axis('off')

# Display the histogram of the grayscale image directly without creating hist_data
axes[2].hist(np.array(gray_macarons_image).ravel(), bins=256, color='gray', alpha=0.7)
axes[2].set_title('Grayscale Image Histogram')
axes[2].set_xlabel('Pixel Intensity')
axes[2].set_ylabel('Frequency')

# Add a grid for better visibility in the histogram bar plot
axes[2].grid(axis='y', linestyle='--', alpha=0.7)

# Adjust layout for better spacing
plt.tight_layout()

# Show the plot
plt.show()
