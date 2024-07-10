import matplotlib.pyplot as plt
import numpy as np

# Load the image
image = plt.imread('images/image.jpg')

# Display the image
plt.imshow(image)

# Set the title and axis labels
plt.title('My Image')
plt.xlabel('X')
plt.ylabel('Y')

# Add a colorbar
plt.colorbar()

# Display the plot
plt.show()