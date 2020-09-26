"""
ffmpeg -i "ENTRADA" -i "LEGENDA" -c:v libx264 -crf 23 -preset ultrafast
-c:a aac -b:a 320k -c:s srt -map v:0 -map a -map 1:0 -ss 00:00:00 -to 00:00:10 "SAIDA"
"""
import os
import fnmatch
import sys

if sys.platform == 'linux':
    comando_ffmpeg = 'ffmpeg'
else:
    comando_ffmpeg = r'ffmpeg\ffmpeg.exe'

codec_video = '-c:v libx264'
crf = '-crf 23'
preset = '-preset ultrafast'
codec_audio = '-c:a aac'
bitrate_audio = '-b:a 320k'
debug = '-ss 00:00:00 -to 00:00:10'

caminho_origem = '/home/ivander/Downloads'
caminho_destino = '/home/ivander/Downloads/saida'

for root, directory, files in os.walk(caminho_origem):
    for file in files:
        if not fnmatch.fnmatch(file, '*.mp4'):
            continue
        caminho_completo = os.path.join(root, file)
        filename, fileext = os.path.splitext(caminho_origem)
        caminho_legenda = filename + '.srt'

        if os.path.isfile(caminho_legenda):
            input_legenda = f'-i "{caminho_legenda}"'
            map_legenda = '-c:s srt -map v:0 -map a -map 1:0'
        else:
            input_legenda = ''
            map_legenda = ''

        filename, fileext = os.path.splitext(file)

        arquivo_saida = f'{caminho_destino}/{filename}_novo{fileext}'

        comando = f'{comando_ffmpeg} -i "{caminho_completo}" {input_legenda} {codec_video} {crf} {preset}' \
                  f' {codec_audio} {bitrate_audio} {debug} {map_legenda} "{arquivo_saida}"'

        os.system(comando)
