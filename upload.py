import flask, os, sys, time, json
import BIC.speech_segmentation as bic_seg
import audio_file_util as audio_file_util
from flask import request

interface_path = os.path.dirname(__file__)
sys.path.insert(0, interface_path)  # 将当前文件的父目录加入临时系统变量

server = flask.Flask(__name__)


# post方法：上传文件的
@server.route('/upload', methods=['post'])
def upload():
    frame_size = 256
    frame_shift = 128
    sr = 16000

    fname = request.files.get('file')  # 获取上传的文件
    merger_time = int(request.form.get('merger_time'))  # 获取合并时间参数
    if fname:
        save_name = time.strftime('%Y%m%d%H%M%S') + "_" + fname.filename
        save_path = r'aideo_file/upload_audio/' + save_name
        # 保存原始音频
        fname.save(save_path)  # 保存文件到指定路径
        file_name = save_name[:save_name.index(".")]
        file_suffix = save_name[save_name.index("."):]
        # 转换音频
        conversion_path = audio_file_util.audio_conversion(save_path, file_name, file_suffix)
        # 拆分音频
        resolution_path = bic_seg.multi_segmentation(conversion_path, file_name, sr, frame_size, frame_shift,
                                                     plot_seg=False, save_seg=True,
                                                     cluster_method='bic')
        # 合并音频
        return_path = audio_file_util.audio_merge(resolution_path, file_name, merger_time)
        return json.dumps(return_path)

server.run(port=8000, debug=True)
