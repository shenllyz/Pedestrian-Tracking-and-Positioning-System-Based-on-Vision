import cv2

global frame
global point1, point2

def on_mouse(event, x, y, flags, param):
    global frame, point1, point2
    img2 = frame.copy()
    if event == cv2.EVENT_LBUTTONDOWN:
        point1 = (x, y)
        cv2.circle(img2, point1, 10, (0, 255, 0), 5)
        cv2.imshow('image', img2)
    elif event == cv2.EVENT_MOUSEMOVE and (flags & cv2.EVENT_FLAG_LBUTTON):
        cv2.rectangle(img2, point1, (x, y), (255, 0, 0), 5)
        cv2.imshow('image', img2)
    elif event == cv2.EVENT_LBUTTONUP:
        point2 = (x, y)
        cv2.rectangle(img2, point1, point2, (0, 0, 255), 5)
        cv2.imshow('image', img2)
        min_x = min(point1[0], point2[0])
        min_y = min(point1[1], point2[1])
        width = abs(point1[0] - point2[0])
        height = abs(point1[1] - point2[1])
        cut_img = frame[min_y:min_y + height, min_x:min_x + width]
        cv2.imwrite('query/0001_c1s1_0_%s.jpg' % min_x, cut_img)

if __name__ == '__main__':
    file = "C:\\Users\\Hp\\Videos\\test.MP4"
    videoCapture = cv2.VideoCapture(file)
    success, frame = videoCapture.read()

    # Desired width or height
    desired_width = 640

    # Calculate the ratio of the new width to the old width
    ratio = desired_width / frame.shape[1]

    # Create new dimensions
    dim = (desired_width, int(frame.shape[0] * ratio))

    while success:
        frame = cv2.resize(frame, dim, interpolation = cv2.INTER_AREA)
        cv2.namedWindow('image')
        cv2.setMouseCallback('image', on_mouse)
        cv2.imshow('image', frame)
        if cv2.waitKey(0) & 0xFF == ord('q'):
            break
        success, frame = videoCapture.read()
