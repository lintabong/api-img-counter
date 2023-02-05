import cv2

cascade_src = 'cars.xml'
car_cascade = cv2.CascadeClassifier(cascade_src)

while True:
    img = cv2.imread("cars1.jpg")
    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    cars = car_cascade.detectMultiScale(gray, 1.1, 1)

    for (x,y,w,h) in cars:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)      

    print("total count=", len(cars))
    
    cv2.imshow('video', img)
    
    if cv2.waitKey(33) == 27:
        break

img.release()
cv2.destroyAllWindows()