import cv2
import os

# 视频文件路径
video_path = '007.mp4'

# 输出文件夹路径
output_folder = '007'

# 创建输出文件夹（如果不存在）
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# 打开视频文件
video = cv2.VideoCapture(video_path)

# 获取视频的帧率
fps = video.get(cv2.CAP_PROP_FPS)

# 逐帧读取视频并保存图片
for frame_num in range(int(video.get(cv2.CAP_PROP_FRAME_COUNT))):
    ret, frame = video.read()
    if ret:
        # 构造输出图片文件名
        image_path = os.path.join(output_folder, f'wyj{frame_num}.jpg')
        # 保存图片
        cv2.imwrite(image_path, frame)
    else:
        break

    # 关闭视频文件
video.release()