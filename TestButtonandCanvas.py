from tkinter import *
from os import walk
import cv2, numpy as np


class Widegts:

    class Resize_Class:
        def resize(self, img1, img2=None):
            width = int(input("WHIDTH  :  "))
            height = int(input("HEIGHT :  "))
            img1 = cv2.resize(img1, (width, height))
            if img2 is not None:
                img2 = cv2.resize(img2, (width, height))
                return img1, img2
            return img1

    class ImageFile_Class:
        def Image_File(self, path):
            f = []
            imagefile = []
            for (dirpath, dirnames, filenames) in walk(path):
                f.append(filenames)
            print('FILENAMES:------------------------')
            j = 0
            for file in f:
                for fname in file:
                    if '.png' in fname or '.jpg' in fname:
                        print(f"{j}.  {fname}")
                        j += 1
                        imagefile.append(fname)
                    else:
                        pass
            print('----------------------------------')
            return imagefile

    class CheckImage_Class:
        def Check_Images(self, imageFile):
            ans = True
            imgname = ''
            while ans:
                print("\n.........Choose an image...........")
                imgname = input('image :  ')
                counter = 0
                for i in imageFile:
                    counter += 1
                    if imgname == i:
                        ans = False
                    if counter == len(imageFile) and ans == True:
                        print("*****name is Incorrect, Please Try Again*****")
            return imgname

    class Read_Class(ImageFile_Class,CheckImage_Class):
        def read(self):
            #    path=input("Input your Path")
            path = 'E:\Python Exc Image Proccesing'
            imagefile = self.Image_File(path)
            imgname = self.Check_Images(imagefile)
            img = cv2.imread(imgname)
            return img

    class HSV_Class:
        def HSV(self):
            def empty():
                pass

            cv2.namedWindow('TaskBar')
            cv2.resizeWindow('TaskBar', 500, 250)
            cv2.createTrackbar('Hue Min', 'TaskBar', 0, 179, empty)
            cv2.createTrackbar('Hue Max', 'TaskBar', 179, 179, empty)
            cv2.createTrackbar('Saturation Min', 'TaskBar', 0, 255, empty)
            cv2.createTrackbar('Saturation Max', 'TaskBar', 255, 255, empty)
            cv2.createTrackbar('Value Min', 'TaskBar', 0, 255, empty)
            cv2.createTrackbar('Value Max', 'TaskBar', 255, 255, empty)
            cap = cv2.VideoCapture(0)
            print("===================================================")
            print("\t\tPress Q  to Exit")
            print("===================================================")
            while True:
                hmin, hmax = cv2.getTrackbarPos('Hue Min', 'TaskBar'), cv2.getTrackbarPos('Hue Max', 'TaskBar')
                smin, smax = cv2.getTrackbarPos('Saturation Min', 'TaskBar'), cv2.getTrackbarPos('Saturation Max',
                                                                                                 'TaskBar')
                vmin, vmax = cv2.getTrackbarPos('Value Min', 'TaskBar'), cv2.getTrackbarPos('Value Max', 'TaskBar')
                _, frame = cap.read()
                hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
                lower = np.array([hmin, smin, vmin])
                upper = np.array([hmax, smax, vmax])
                mask = cv2.inRange(hsv, lower, upper)
                res = cv2.bitwise_and(frame, frame, mask=mask)
                cv2.imshow('mask', mask)
                cv2.imshow('res', res)
                br = cv2.waitKey(5)
                if br == 113:
                    cv2.destroyAllWindows()
                    break

    class Prespective_Class(Read_Class,Resize_Class):
        def Perspective(self):
            img = self.read()
            print(f"image shape : {img.shape}")
            ans = input("Do you need resize the Original Image (y/n) ?   ")
            if ans == 'y' or ans == "Y":
                img = self.resize(img)
            pos = input('\nInput Positions (8-digit split by " , "):\n   ')
            a, b, c, d, e, f, g, h = pos.split(',')
            point_1 = np.float32([[a, b], [c, d], [e, f], [g, h]])
            width = int(input('Enter Width for Perespective  !!    '))
            height = int(input('Enter Height for Perespective !!    '))
            point_2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
            matrix = cv2.getPerspectiveTransform(point_1, point_2)
            res = cv2.warpPerspective(img, matrix, (width, height))
            cv2.imshow('Res', res)
            cv2.imshow('IMG', img)

    class Blur_Class(Read_Class):
        def Blur(self):
            img = self.read()
            bmin = int(input('Limit Of BLUR Min :   '))
            bmax = int(input('Limit Of BLUR Max :   '))
            blur = cv2.blur(img, (bmin, bmax))
            medianBlur = cv2.medianBlur(img, 7)
            cv2.imshow('IMG', img)
            cv2.imshow('BLUR', blur)
            cv2.imshow('MedianBlur', medianBlur)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

    class SplitMerge_Class(Read_Class,Resize_Class):
        def SplitMerge(self):
            img__1 = self.read()
            img__2 = self.read()
            img__1, img__2 = self.resize(img__1, img__2)
            blau, grun, rot = cv2.split(img__1)
            cv2.imshow('img__1', img__1)
            cv2.imshow('Blau', blau)
            cv2.imshow('Grun', grun)
            cv2.imshow('Rot', rot)
            imgPLUS = img__1 + img__2
            imgADD = cv2.add(img__1, img__2)
            cv2.imshow('ImgPLUS', imgPLUS)
            cv2.imshow('ImgADD', imgADD)

    class Threshold_Class(Read_Class,Resize_Class):
        def Threshold(self):
            img = self.read()
            cv2.imshow('img', img)
            ans = input('Do you need Resize(y/n)?  ')
            if ans == 'y' or ans == 'Y': img = self.resize(img)
            _, thresholdBinary_1 = cv2.threshold(img, 10, 255, cv2.THRESH_BINARY)
            _, thresholdBinary_2 = cv2.threshold(img, 130, 255, cv2.THRESH_BINARY)
            _, thresholdBINARY_INV = cv2.threshold(img, 10, 255, cv2.THRESH_BINARY_INV)
            _, thresholdTozero = cv2.threshold(img, 10, 255, cv2.THRESH_TOZERO)
            _, thresholdTozero_INV = cv2.threshold(img, 10, 255, cv2.THRESH_TOZERO_INV)
            _, thresholdTrunc = cv2.threshold(img, 10, 255, cv2.THRESH_TRUNC)
            _, thresholdMask = cv2.threshold(img, 10, 255, cv2.THRESH_MASK)
            _, thresholdOTSU = cv2.threshold(img, 10, 255, cv2.THRESH_OTSU)
            _, thresholdTRIANGLE = cv2.threshold(img, 10, 255, cv2.THRESH_TRIANGLE)
            cv2.imshow('Binary,th=10', thresholdBinary_1)
            cv2.imshow('Binary,th=130', thresholdBinary_2)
            cv2.imshow('Tozero', thresholdBINARY_INV)
            cv2.imshow('Tozero', thresholdTozero)
            cv2.imshow('Tozero_INV', thresholdTozero_INV)
            cv2.imshow('Tozero', thresholdTrunc)
            cv2.imshow('Tozero', thresholdOTSU)
            cv2.imshow('Tozero', thresholdMask)
            cv2.imshow('Tozero', thresholdTRIANGLE)

    class Draw_Class:
        def draw(self):
            blackshape = np.zeros((512, 512, 3))
            blackshape = cv2.line(blackshape, (0, 0), (512, 512), (2, 20, 12), 2)
            blackshape = cv2.rectangle(blackshape, (24, 24), (488, 488), (255, 0, 0), 4)
            blackshape = cv2.circle(blackshape, (256, 256), 244, (0, 250, 10), 2)
            blackshape = cv2.circle(blackshape, (256, 256), 224, (0, 250, 250), -1)
            pts = np.array([[6, 2], [256, 12], [506, 2], [500, 256], [506, 510], [256, 500], [2, 510], [12, 256], [6, 2]],
                           np.int32)
            blackshape = cv2.polylines(blackshape, [pts], 1, (0, 0, 250), 2)
            blackshape = cv2.ellipse(blackshape, (256, 256), (120, 70), 0, 0, 360, (25, 255, 0), -1)
            # blackshape = cv2.ellipse(blackshape,(256,256),(100,50),0,0,360,(0,255,0),2)
            # pol = cv2.ellipse2Poly(blackshape, (256, 256), (70, 20),2, 0, 360)
            # blackshape=cv2.fillConvexPoly(blackshape, pol, (10,0,10))
            cv2.imshow('DRAW', blackshape)
            cv2.waitKey(0)

    class Substruction_Class:
        def Substraction(self):
            cap = cv2.VideoCapture(0)
            fg = cv2.createBackgroundSubtractorMOG2()

            while True:
                _, frame = cap.read()
                mask = fg.apply(frame)

                cv2.imshow('Frame', frame)
                cv2.imshow('Mask', mask)
                k = cv2.waitKey(27) & 0xFF
                if k == 27: break

            cv2.destroyAllWindows()
            cap.release()

    class Authentication_Class:
        def Authentication(self):
            faceXML = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
            eyeXML = cv2.CascadeClassifier('haarcascade_eye.xml')
            cap = cv2.VideoCapture(0)

            while True:
                _, frame = cap.read()
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                faces = faceXML.detectMultiScale(gray)
                for (x, y, w, h) in faces:
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
                    roi_gray = gray[y:y + h, x:x + w]
                    roi_color = frame[y:y + h, x:x + w]
                    eyes = eyeXML.detectMultiScale(roi_gray)
                    for (eyx, eyy, eyw, eyh) in eyes:
                        cv2.rectangle(roi_color, (eyx, eyy), (eyx + eyw, eyy + eyh), (255, 0, 0), 2)

                cv2.imshow('Face', frame)
                k = cv2.waitKey(27) & 0xFF
                if k == 27:
                    break

            cv2.destroyAllWindows()
            cap.release()




class main_Menu:
    window = Tk()
    window.title('BTNCVS')
    window.configure(bg='#ddd')
    clas = Widegts()

    lbl = Label(window, text='Image Processing', bd=4, font=('tahoma', 16),
                bg='#000', fg='#fff', pady=20, justify='center', width=48)
    lbl.grid(row=0, columnspan=4, ipadx=10, pady=(3, 0))

    btn1 = Button(window, bd=4, font=('tahoma', 12), text='HSV', bg='#FF0000',
                  fg='#fff', pady=20, activebackground="#fff",
                  justify='center', width=15, activeforeground="#D40000", command=clas.HSV_Class.HSV)
    btn1.grid(row=1, column=0)

    btn2 = Button(window, bd=4, font=('tahoma', 12), text='PERESPECTIVE',
                  bg='#FF0000', fg='#fff', pady=20, activebackground="#fff",
                  justify='center', width=15, activeforeground="#D40000", command=clas.Prespective_Class.Perspective)
    btn2.grid(row=1, column=1)

    btn3 = Button(window, bd=4, font=('tahoma', 12), text='BLUR', bg='#FF0000',
                  fg='#fff', pady=20, activebackground="#fff",
                  justify='center', width=15, activeforeground="#D40000", command=clas.Blur_Class.Blur)
    btn3.grid(row=1, column=2)
    btn4 = Button(window, bd=4, font=('tahoma', 12), text='DRAW', bg='#FF0000',
                  fg='#fff', pady=20, activebackground="#fff",
                  justify='center', width=15, activeforeground="#D40000", command=clas.Draw_Class.draw)
    btn4.grid(row=2, column=0)

    btn5 = Button(window, bd=4, font=('tahoma', 12), text='SPLIT & MERGE',
                  bg='#FF0000', fg='#fff', pady=20, activebackground="#fff",
                  justify='center', width=15, activeforeground="#D40000", command=clas.SplitMerge_Class.SplitMerge)
    btn5.grid(row=2, column=1)

    btn6 = Button(window, bd=4, font=('tahoma', 12), text='THRESHOLD',
                  bg='#FF0000', fg='#fff', pady=20, activebackground="#fff",
                  justify='center', width=15, activeforeground="#D40000", command=clas.Threshold_Class.Threshold)
    btn6.grid(row=2, column=2)

    btn7 = Button(window, bd=4, font=('tahoma', 12), text='Authentication', bg='#FF0000',
                  fg='#fff', pady=20, activebackground="#fff",
                  justify='center', width=15, activeforeground="#D40000",
                  command=clas.Authentication_Class.Authentication)
    btn7.grid(row=2, column=3)
    btn8 = Button(window, bd=4, font=('tahoma', 12), text='CBS', bg='#FF0000',
                  fg='#fff', pady=20, activebackground="#fff",
                  justify='center', width=15, activeforeground="#D40000", command=clas.Substruction_Class.Substraction)
    btn8.grid(row=1, column=3)

    btnexit = Button(window, text='Exit', bd=4, font=('tahoma', 16),
                     bg='#FFFF19', fg='#000', pady=16, justify='center', width=49,
                     activebackground='#990000', command=exit)
    btnexit.grid(row=3, column=0, columnspan=5)

    window.mainloop()


root = main_Menu()

#
# class tkinterApp(Tk):
#
#     # __init__ function for class tkinterApp
#     def __init__(self, *args, **kwargs):
#         # __init__ function for class Tk
#         Tk.__init__(self, *args, **kwargs)
#
#         # creating a container
#         container = Frame(self)
#         container.pack(side="top", fill="both", expand=True)
#
#         container.grid_rowconfigure(0, weight=1)
#         container.grid_columnconfigure(0, weight=1)
#
#         # initializing frames to an empty array
#         self.frames = {}
#
#         # iterating through a tuple consisting
#         # of the different page layouts
#         for F in (StartPage, Page1, Page2):
#             frame = F(container, self)
#
#             # initializing frame of that object from
#             # startpage, page1, page2 respectively with
#             # for loop
#             self.frames[F] = frame
#
#             frame.grid(row=0, column=0, sticky="nsew")
#
#         self.show_frame(StartPage)
#
#     # to display the current frame passed as
#     # parameter
#     def show_frame(self, cont):
#         frame = self.frames[cont]
#         frame.tkraise()
#
#     # first window frame startpage





