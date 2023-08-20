import os
from PIL import Image
from datetime import datetime, timedelta
from transformers import VisionEncoderDecoderModel,AutoTokenizer, TrOCRProcessor
processor = TrOCRProcessor.from_pretrained("microsoft/trocr-base-handwritten")
import torch
from PIL import Image

# 입력 폴더 경로 설정
input_folder = 'result'

# 출력 폴더 경로 설정
output_folder = 'timestamp'

# 입력 폴더 내의 파일 목록 가져오기
files = [file for file in os.listdir(input_folder) if file.lower().endswith('.png')]


device = torch.device('cpu') # change 'cuda' if you need.

#model can be .jpg or .png
#hugging face download: https://huggingface.co/gg4ever/trOCR-10k

trocr_model = "gg4ever/trOCR-youtube-kor-OCR"
model = VisionEncoderDecoderModel.from_pretrained(trocr_model).to(device)
tokenizer = AutoTokenizer.from_pretrained(trocr_model)


# 텍스트 추출 및 저장
for file in files:
    file_name, ext = os.path.splitext(file)
    timestamp_seconds = int(file_name.split('_')[0][4:])  # 파일 이름에서 초 단위 추출
    timestamp = str(timedelta(seconds=timestamp_seconds))  # 초 단위를 시간 형식으로 변환
    output_file = os.path.join(output_folder, f'{file_name}.txt')
    image_path = os.path.join(input_folder, file)

    # 이미지에서 텍스트 추출
    pixel_values = (processor(Image.open(image_path), return_tensors="pt").pixel_values).to(device)
    generated_ids = model.generate(pixel_values)
    generated_text = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]

    # 추출된 텍스트와 타임스탬프를 파일에 저장
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(f"{timestamp}:")
        f.write(f"{generated_text}\n")

    print(f"Extracted text from '{file}' and saved to '{output_file}'")

print("Text extraction and saving complete.")
