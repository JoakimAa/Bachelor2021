from __future__ import print_function
import cv2
import pytesseract
import numpy as np

# (https://learnopencv.com/feature-based-image-alignment-using-opencv-c-python/)

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

MAX_FEATURES = 500
GOOD_MATCH_PERCENT = 0.15


def align_images(img1, img2, prediction):

    if prediction == "trondertaxi":
        im1 = cv2.resize(img1, None, fx=0.8, fy=0.5, interpolation=cv2.INTER_AREA)
        im2 = cv2.resize(img2, None, fx=0.8, fy=0.5, interpolation=cv2.INTER_AREA)
    else:
        im1 = cv2.resize(img1, None, fx=1, fy=1, interpolation=cv2.INTER_AREA)
        im2 = cv2.resize(img2, None, fx=1, fy=1, interpolation=cv2.INTER_AREA)

    # Convert templates to grayscale
    im1Gray = cv2.cvtColor(im1, cv2.COLOR_BGR2GRAY)
    im2Gray = cv2.cvtColor(im2, cv2.COLOR_BGR2GRAY)
    # Detect ORB features and compute descriptors.
    orb = cv2.ORB_create(MAX_FEATURES)
    keypoints1, descriptors1 = orb.detectAndCompute(im1Gray, None)
    keypoints2, descriptors2 = orb.detectAndCompute(im2Gray, None)

    # Match features.
    matcher = cv2.DescriptorMatcher_create(cv2.DESCRIPTOR_MATCHER_BRUTEFORCE_HAMMING)
    matches = matcher.match(descriptors1, descriptors2, None)

    # Sort matches by score

    matches.sort(key=lambda x: x.distance, reverse=False)

    # Remove not so good matches

    numGoodMatches = int(len(matches) * GOOD_MATCH_PERCENT)

    matches = matches[:numGoodMatches]

    # Draw top matches

    imMatches = cv2.drawMatches(im1, keypoints1, im2, keypoints2, matches, None)

    cv2.imwrite("../AI/out/matches.jpg", imMatches)

    # Extract location of good matches

    points1 = np.zeros((len(matches), 2), dtype=np.float32)

    points2 = np.zeros((len(matches), 2), dtype=np.float32)

    for i, match in enumerate(matches):
        points1[i, :] = keypoints1[match.queryIdx].pt
        points2[i, :] = keypoints2[match.trainIdx].pt

    # Find homography
    h, mask = cv2.findHomography(points1, points2, cv2.RANSAC)

    # Use homography
    height, width, channels = im2.shape
    im1Reg = cv2.warpPerspective(im1, h, (width, height))

    return im1Reg, h, im2


def return_data(img1, prediction):
    # Read reference image
    template_ref_Filename = f"../AI/templates/{prediction}.jpg"
    print(f"../AI/templates/{prediction}.jpg")
    print("Reading reference image : ", template_ref_Filename)
    imReference = cv2.imread(template_ref_Filename, cv2.IMREAD_COLOR)

    # Read image to be aligned
    # imFilename = img1
    # print("Reading image to align : ", imFilename);
    im = cv2.cvtColor(img1, cv2.IMREAD_COLOR)

    print("Aligning templates ...")
    # Registered image will be resotred in imReg.
    # The estimated homography will be stored in h.
    imReg, h, im2 = align_images(im, imReference, prediction)

    # Write aligned image to disk.
    outFilename = "aligned.jpg"
    print("Saving aligned image : ", outFilename);
    cv2.imwrite("../AI/out/" + outFilename, imReg)

    template = "template.jpg"
    print("default image")
    cv2.imwrite("../AI/out/" + template, im2)

    # Print estimated homography
    print("Estimated homography : \n", h)

    return imReg

# cv2.imshow("template",im1)
# cv2.imshow("skewed",imReg)
# cv2.waitKey(0)
