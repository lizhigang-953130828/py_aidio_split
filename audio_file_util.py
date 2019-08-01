import math

from pydub import AudioSegment  ###需要安装pydub、ffmpeg
import os


# 转换音频工具
def audio_conversion(filePath, file_name, file_suffix):
    if file_suffix == '.mp3':
        conversion_path = "aideo_file/conversion_audio/" + file_name + ".wav"
        ss = "C:/Users/lzg95/Desktop/ffmpeg-20190727-47b6ca0-win64-static/bin/ffmpeg.exe -i " + filePath + " -ar 16000 -ac 1 " + conversion_path
        os.system(ss)
        return conversion_path
    else:
        return filePath


# 合并音频工具
def audio_merge(resolution_path, file_name, meger_time):
    meger_path = "aideo_file/merge_audio/" + file_name
    os.makedirs(meger_path)
    file_num = len(
        [lists for lists in os.listdir(resolution_path) if os.path.isfile(os.path.join(resolution_path, lists))])
    # 拆分后的文件数必须大于1
    return_path_list = []
    if file_num > 1:
        output_audio_file = 0  # file
        output_audio_time = 0  # time
        for idx in range(0, file_num):
            resolution_audio_file = AudioSegment.from_wav(resolution_path + "/" + str(idx) + ".mp3")
            output_audio_time += math.ceil(len(resolution_audio_file))
            if output_audio_time < meger_time:
                output_audio_file += resolution_audio_file
            else:
                # 当前文件时间达到指定时间后，文件合并输出
                meger_file = meger_path + "/" + str(idx) + ".mp3"
                output_audio_file.export(meger_file)
                return_path_list.append(meger_file)
                output_audio_file = resolution_audio_file
                output_audio_time = math.ceil(len(resolution_audio_file))
            # 末尾文件不能合并上的，直接输出
            if idx == (file_num - 1):
                meger_file = meger_path + "/" + str((idx + 1)) + ".mp3"
                output_audio_file.export(meger_file)
                return_path_list.append(meger_file)
    else:
        return_path_list.append("aideo_file/resolution_audio/" + file_name + "/0.mp3")
    return return_path_list
