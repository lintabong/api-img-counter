import cv2

cascade_src = 'cooking_oil.xml'
car_cascade = cv2.CascadeClassifier(cascade_src)

i = 0
while True:
    img = cv2.imread("img/test0.jpeg")
    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    cars = car_cascade.detectMultiScale(gray, 1.1, 1)

    for (x,y,w,h) in cars:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)      

    print("total count=", len(cars))
    
    cv2.imshow('video', img)
    
    if cv2.waitKey(33) == 27:
        break

    i += 1
    if i >= 2:
        break

img.release()
cv2.destroyAllWindows()