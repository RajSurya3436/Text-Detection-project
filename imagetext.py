import pytesseract
import cv2

# Set Tesseract path 
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\rajsu\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

# Configuration for Tesseract
myconfig = r"--psm 3 --oem 3"

# Load the image using OpenCV
img = cv2.imread("sample3.jpg")

# Check if image was loaded successfully
if img is None:
    print("Error: Could not load image 'sample3.jpg'")
    exit()

# Get the height and width of the image
height, width, _ = img.shape

# Use pytesseract to get the bounding boxes of each word
boxes = pytesseract.image_to_data(img, config=myconfig)

# Clear the output file
with open("recognized.txt", "w", encoding="utf-8") as file:
    file.write("")

# Draw rectangles around each recognized word and extract text
for i, box in enumerate(boxes.splitlines()):
    if i == 0:  # Skip header line
        continue
    
    box_data = box.split()
    if len(box_data) == 12:
        x, y, w, h = int(box_data[6]), int(box_data[7]), int(box_data[8]), int(box_data[9])
        text = box_data[11]  # The recognized text
        conf = float(box_data[10])  # Confidence score
        
        # Only process if confidence is reasonable and text is not empty
        if conf > 0 and text.strip():
            # Draw rectangle on image
            img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
            
            # Write text to file
            with open("recognized.txt", "a", encoding="utf-8") as file:
                file.write(text + " ")

# Alternative: Get all text at once 
full_text = pytesseract.image_to_string(img, config=myconfig)
print("Recognized text:")
print(full_text)

# Save the full text to file (overwrites the word-by-word version)
with open("recognized_full.txt", "w", encoding="utf-8") as file:
    file.write(full_text)

# Display the image with bounding boxes
cv2.imshow("img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("\nText saved to 'recognized_full.txt'")
