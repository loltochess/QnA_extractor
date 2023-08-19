import os
from PIL import Image
from datetime import datetime, timedelta

# 입력 폴더 경로 설정
input_folder = 'result'

# 출력 폴더 경로 설정
output_folder = 'timestamp'

# 입력 폴더 내의 파일 목록 가져오기
files = [file for file in os.listdir(input_folder) if file.lower().endswith('.png')]

# 텍스트 추출 및 저장
for file in files:
    file_name, ext = os.path.splitext(files)
    timestamp_seconds = int(file_name[6:])  # 파일 이름에서 초 단위 추출
    timestamp = str(timedelta(seconds=timestamp_seconds))  # 초 단위를 시간 형식으로 변환
    output_file = os.path.join(output_folder, f'{file_name}.txt')
    image_path = os.path.join(input_folder, file)

    # 이미지에서 텍스트 추출
    result = 1

    # 추출된 텍스트와 타임스탬프를 파일에 저장
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(f"Timestamp: {timestamp}\n\n")
        for detection in result:
            f.write(str(detection[:-1]) + '\n')

    print(f"Extracted text from '{jpg_file}' and saved to '{output_file}'")

print("Text extraction and saving complete.")