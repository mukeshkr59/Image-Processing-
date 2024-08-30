import cv2
import numpy as np
def solution(image_path):
    ######################################################################
    ######################################################################
    #####  WRITE YOUR CODE BELOW THIS LINE ###############################
    img= cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, thresholded = cv2.threshold(gray, 1, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(thresholded, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    largest_contour = max(contours, key=cv2.contourArea)
    epsilon = 0.02 * cv2.arcLength(largest_contour, True)
    approx = cv2.approxPolyDP(largest_contour, epsilon, True)
    if len(approx) == 4:
        rect_points = approx
    else:
        raise ValueError("The detected shape is not a rectangle.")
    rect_points = np.array([point[0] for point in rect_points])
    ordered_rect_points = np.array((rect_points))
    ordered_rect_points = ordered_rect_points.astype(np.float32)
    center_x = sum(ordered_rect_points[:,0]) / len(ordered_rect_points[:,0])
    center_y = sum(ordered_rect_points[:,1]) / len(ordered_rect_points[:,1])
    center = [center_x, center_y]
    points = [(ordered_rect_points[:,0][i], ordered_rect_points[:,1][i]) for i in range(4)]
    angles = [np.arctan2(point[1] - center[1], point[0] - center[0]) for point in points]
    sorted_points = [point for _, point in sorted(zip(angles, points))]
    sorted_points = np.array(sorted_points)
    width, height = 600, 600
    dst_points = np.array([[0, 0], [width - 1, 0], [width - 1, height - 1], [0, height - 1]], dtype=np.float32)
    dst_points = dst_points.astype(np.float32)
    matrix = cv2.getPerspectiveTransform(sorted_points, dst_points)
    warped_image = cv2.warpPerspective(img, matrix, (width, height))
    image=warped_image
    ######################################################################

    return image