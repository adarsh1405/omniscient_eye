import cv2
import numpy as np
import os
import sys

from imageai.Detection.Custom import CustomObjectDetection, CustomVideoObjectDetection
import os

execution_path = os.getcwd()

#intializing the web camera device



def detect_from_video(source):

    detector = CustomVideoObjectDetection()
    detector.setModelTypeAsYOLOv3()
    detector.setModelPath(detection_model_path=os.path.join(execution_path, "detection_model-ex-33--loss-4.97.h5"))
    detector.setJsonPath(configuration_json=os.path.join(execution_path, "detection_config.json"))
    detector.loadModel()
    detected_video_path = detector.detectObjectsFromVideo(input_file_path=os.path.join(execution_path,source), frames_per_second=10, output_file_path=os.path.join(execution_path, "video1-detected"), minimum_percentage_probability=40, log_progress=True )
    print("Completed!!!")
    sys.exit()
    
if len(sys.argv)==2:
    detect_from_video(sys.argv[1])


detector = CustomObjectDetection()
detector.setModelTypeAsYOLOv3()
detector.setModelPath(detection_model_path=os.path.join(execution_path, "detection_model-ex-33--loss-4.97.h5"))
detector.setJsonPath(configuration_json=os.path.join(execution_path, "detection_config.json"))
detector.loadModel()


cap = cv2.VideoCapture(0)

def alert(number,call=False):
    cookies = {"X-App-Version": "1.0", "X-Phone-Platform": "web", "X-Default-City": "1", "X-Pincode": "400001", "XdI": "0d429faa36c459599d17506cad32cb25", "_gcl_au": "1.1.782225019.1575836626", "_omappvp": "iTEq3HaHcwk52kq9H5VOubYq7rrvfnz8pYZNWJPOeYJR14H6BOzCCODJpYMKlETqLuoAr2jH8LfGUUv7SQsToibzWk1PqWBC", "_omappvs": "1575836625625", "WZRK_S_R9Z-WWR-854Z": "%7B%22p%22%3A1%2C%22s%22%3A1575836625%2C%22t%22%3A1575836627%7D", "WZRK_G": "52d860bf981a489ca4dbd9d97078697b"}
    head = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0", "Accept": "*/*", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate", "x-real-ip": "", "x-ua": "", "x-ff": "", "Content-Type": "application/json", "Origin": "https://pharmeasy.in", "DNT": "1", "Connection": "close", "Referer": "https://pharmeasy.in/"}
    if call:
        r=requests.post("https://pharmeasy.in/api/auth/login", headers=burp0_headers, cookies=burp0_cookies, json={"contactNumber": number, "hasCalled": True, "profileEmail": ""}).text
    else:
        r=requests.post("https://pharmeasy.in/api/auth/requestOTP", headers=head, cookies=cookies, json={"contactNumber": number}).text
    print("Request Sent")
    return '"status":1' in r

ret = True
while (ret):
    ret,image_np = cap.read()
    
    proc_image,detections = detector.detectObjectsFromImage(input_image=image_np,input_type="array", output_type="array", minimum_percentage_probability=40)

    
    for detection in detections:
        print(detection["name"], " : ", detection["percentage_probability"], " : ", detection["box_points"])
    if detections:
        alert("6370548715")
        os.system("ffplay alert.mp3 -nodisp")
    #cv2.imshow('image',cv2.resize(proc_image,(1280,960)))
    time.sleep(0.1)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        cap.release()
        break




