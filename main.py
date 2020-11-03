Last login: Wed Oct 28 17:16:38 on ttys001
(base) kpinfo@kpinfodeMacBook-Pro ~ % ls
Desktop        Library        Pictures       anaconda3      sensors
Documents      Movies         Public         fsdownload     test
Downloads      Music          Sunlogin Files opt
(base) kpinfo@kpinfodeMacBook-Pro ~ % cd Desktop 
(base) kpinfo@kpinfodeMacBook-Pro Desktop % ls
Old_Homebrew
[doi 10.1145_3321408.3322628]Yao, Liyao; Hu, Zexi; Liu, Caixing; Liu, Hanxing; Kuang, Yingjie -- [ACMPress the ACM Turing Celebration Conference - China - Chengdu, China(2019.05.17-2019.05.19)] P.pdf
key.rtf
work
图像审核开启服务方法.rtf
(base) kpinfo@kpinfodeMacBook-Pro Desktop % cd work 
(base) kpinfo@kpinfodeMacBook-Pro work % ls
Figure_1.png         Similarvideomatching pyzernikemoment.py
Similarimagematching Video-Matching       test.mp4
(base) kpinfo@kpinfodeMacBook-Pro work % mkdir Similar_vc2
(base) kpinfo@kpinfodeMacBook-Pro work % ls
Figure_1.png         Similarvideomatching test.mp4
Similar_vc2          Video-Matching
Similarimagematching pyzernikemoment.py
(base) kpinfo@kpinfodeMacBook-Pro work % vim pyzernikemoment.py 
(base) kpinfo@kpinfodeMacBook-Pro work % vim pyzernikemoment.py

    if len(src.shape) == 3:
        print('the input image src should be in gray')
        return

    H, W = src.shape
    if H > W:
        src = src[int((H - W) / 2): int((H + W) / 2), :]
    elif H < W:
        src = src[:, int((W - H) / 2): int((H + W) / 2)]

    N = src.shape[0]
    if N % 2:
        src = src[:-1, :-1]
        N -= 1
    x = range(N)
    y = x
    X, Y = np.meshgrid(x, y)
    R = np.sqrt((2 * X - N + 1) ** 2 + (2 * Y - N + 1) ** 2) / N
    Theta = np.arctan2(N - 1 - 2 * Y, 2 * X - N + 1)
    R = np.where(R <= 1, 1, 0) * R

    # get the radial polynomial
    Rad = radialpoly(R, n, m)

    Product = src * Rad * np.exp(-1j * m * Theta)
    # calculate the moments
    Z = Product.sum()

    # count the number of pixels inside the unit circle
    cnt = np.count_nonzero(R) + 1
    # normalize the amplitude of moments
    Z = (n + 1) * Z / cnt
    # calculate the amplitude of the moment
    A = abs(Z)
    # calculate the phase of the mement (in degrees)
    Phi = np.angle(Z) * 180 / np.pi

    return Z, A, Phi
if __name__ == '__main__':
    n = 4
    m = 2
    file_list = os.listdir('./')
    imglist = []
    for kk in file_list:
        if kk[-3:] == 'jpg':
            imglist.append(kk)
    for k in imglist:
        img = cv2.imread(k,0)
        print('>>>>> '+k,Zernikemoment(img, n, m))
