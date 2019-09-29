# 特征值前背景m的计算(直方图中低于和高于threshold的平均灰度)
# 目前看起来图像的特征值可能有很多基准，我使用平均灰度做特征值(因为本文用于分割，而最分割最重要的信息就是灰度)
def m_(hist, threshold):
    # average of background
    tmpa = 0
    tmpb = 0
    for i in range(threshold):
        tmpa = tmpa + i * hist[i][0]
        tmpb = tmpb + hist[i][0]
    if not tmpb:
        m0 = 0
    else:
        m0 = tmpa / tmpb


    # average of frontground
    tmpa = 0
    tmpb = 0
    for i in range(threshold, 256, 1):
        tmpa = tmpa + i * hist[i][0]
        tmpb = tmpb + hist[i][0]
    if not tmpb:
        m1 = 0
    else:
        m1 = tmpa / tmpb


    return m0, m1


# 得到计算隶属度的常数c，有两篇论文中设定为1（归一化后），所参考博客设为最大最小亮度之差
# 我设为定值，如果使用亮度差导致c在不同图之间是变化的（熵的基准改变了）
def c_(hist):
    min_index = 255
    max_index = 0
    for i in range(256):
        if hist[i][0]:
            min_index = i
            break


    for i in range(256):
        if hist[255 - i][0]:
            max_index = 255 - i
            break


    return min_index, max_index


# 隶属度,通过传入的一点像素值得到相应的隶属度
def u_(pix, m, c):
    return 1 / (1 + abs(pix - m) / c)


# main fiunction
def fuzzy_entropy(mat):
    hist = cv2.calcHist([mat], [0], None, [256], [0, 256])
    min_, max_ = c_(hist)
    # c = max_ - min_
    # 我这里暂时使用固定常数相对这里就是255
    c = 255
    bestthreshold = min_
    bestentropy = 9e+15
    
    # 遍历直方图
    # 原公式是遍历图像上每一点求出每一点的熵累加
    # 但是可以换一种思路，相同像素值的点的熵在同一threshold下，其决定式u_(pix, m, c)中pix，m，c均相同
    for t in range(min_ + 1, max_, 1):
        back_mean, front_mean = m_(hist, t)
        entropy = 0
        
        # 累计某一threshold下前背景模糊熵，比较最佳threshold
        m = back_mean
        for p in range(min_, t + 1, 1):
            # if hist[p][0]:
            u = u_(p, m, c)
            # 为了防止某pix与特征m恰好相等（这意味着该点完全符合特征，但是隶属度为1，在后续计算模糊熵时会出现log（1 - 1）的情况）,
        	# 因此我计算模糊熵时改为1 + 1e-9
            entropy = entropy + (- u * math.log10(u) - (1 + 1e-9 - u) * math.log10(1 + 1e-9 - u)) * hist[p]

        m = front_mean
        for p in range(t, max_ + 1, 1):
            u = u_(p, m, c)
            entropy = entropy + (- u * math.log10(u) - (1 + 1e-9 - u) * math.log10(1 + 1e-9 - u)) * hist[p]

        
        # 根据熵的定义，熵越低信息变化越少
        if entropy < bestentropy:
            bestentropy = entropy
            bestthreshold = t

    return bestthreshold