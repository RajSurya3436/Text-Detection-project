import pytesseract
import cv2

# Configuration for Tesseract
myconfig = r"--psm 6 --oem 3"

# Load the image using OpenCV
img = cv2.imread("sample1.jpg")

# Get the height and width of the image
height, width, _ = img.shape

# Use pytesseract to get the bounding boxes of each word
boxes = pytesseract.image_to_data(img, config=myconfig)

# Draw rectangles around each recognized word
for i, box in enumerate(boxes.splitlines()):
    if i == 0:
        continue
    box = box.split()
    if len(box) == 12:
        x, y, w, h = int(box[6]), int(box[7]), int(box[8]), int(box[9])
        img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
with open("recognized.txt", "w") as file:
    file.write("")
cropped = img[y:y + h, x:x + w]    
with open("recognized.txt", "a") as file:
        # Apply OCR on the cropped image
        text = pytesseract.image_to_string(cropped)

        # Appending the text into file
        file.write(boxes)
        file.write("\n")

# Display the image with bounding boxes
cv2.imshow("img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()