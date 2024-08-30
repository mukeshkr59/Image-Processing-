import cv2
import numpy as np

def solution(image_path):
    ############################
    ############################

    ############################
    ############################
    ## comment the line below before submitting else your code wont be executed##
    # pass
    def rot(image,text_angle):
        height, width = image.shape[:2]
        center = (width // 2, height // 2)
        rotation_matrix = cv2.getRotationMatrix2D(center, text_angle, 1.0)
        new_width = int(abs(rotation_matrix[0, 0] * width) + abs(rotation_matrix[0, 1] * height))
        new_height = int(abs(rotation_matrix[1, 0] * width) + abs(rotation_matrix[1, 1] * height))
        rotation_matrix[0, 2] += (new_width - width) / 2
        rotation_matrix[1, 2] += (new_height - height) / 2
        rotated_image = cv2.warpAffine(image, rotation_matrix, (new_width, new_height), borderMode=cv2.BORDER_CONSTANT, borderValue=(255, 255, 255))
        return rotated_image  
    
    def find_text_angle(image_path):
        image = cv2.imread(image_path)
        edges = cv2.Canny(image, 50, 150, apertureSize=3)
        lines = cv2.HoughLines(edges, 1, np.pi / 180, 80)
        if lines is not None:
            angle = lines[0][0][1]
            angle_degrees = np.degrees(angle)
            return angle_degrees-90
        return 0
    image = cv2.imread(image_path)
    text_angle = find_text_angle(image_path)
    rotated_image=rot(image,text_angle)
    image_height= rotated_image.shape[0]
    image_width=  rotated_image.shape[1]
    top_half = rotated_image[:image_height // 2, :]
    bottom_half = rotated_image[image_height // 2:, :]
    if (abs(text_angle)>5):
      if np.sum(top_half > 0) < np.sum(bottom_half > 0):
          print("Enter")
          rotated_image = rot(rotated_image,180)
    image=rotated_image
    return image
