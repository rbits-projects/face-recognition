import cv2
import csv
import os
import time


# Function to capture user image
def capture_image(name):
    camera = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    timeout = 5  # 10 seconds timeout
    start_time = time.time()

    while time.time() - start_time < timeout:
        ret, frame = camera.read()
        cv2.imshow("Camera Feed", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):  # Press 'q' to exit
            break

    # Save the captured image
    image_path = f"{name}.jpg"
    cv2.imwrite(image_path, frame)
    print("Image captured and saved successfully!")

    camera.release()
    cv2.destroyAllWindows()


# Function to store user details in a CSV file
def store_user_details(name, age, gender, phone):
    file_exists = os.path.isfile('user_details.csv')
    with open('user_details.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(['Name', 'Age', 'Gender', 'Phone', 'Image'])
        writer.writerow([name, age, gender, phone, f"{name}.jpg"])
    print("User details stored successfully!")


# Main function
def main():
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    gender = input("Enter Gender (Male, Female, Others): ")
    phone = input("Enter phone number: ")

    # Capture user image
    capture_image(name)

    # Store user details in CSV file
    store_user_details(name, age, gender, phone)


if __name__ == "__main__":
    main()
