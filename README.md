# QnA_extractor

-- 본 프로젝트는 고려대학교 데이터청년캠퍼스 대회 출품 프로젝트입니다.
-- Youtube video에서 초단위로 글자를 추출해서 질문 부분만 추출해서 Timeline을 만들어주는 프로젝트입니다.

# Detecting-Pytorch
## CRAFT: Character-Region Awareness For Text detection
Official Pytorch implementation of CRAFT text detector | [Paper](https://arxiv.org/abs/1904.01941) | [Pretrained Model](https://drive.google.com/open?id=1Jk4eGD7crsqCCg9C9VjCLkMN3ze8kutZ) | [Supplementary](https://youtu.be/HI8MzpY8KMI)

**[Youngmin Baek](mailto:youngmin.baek@navercorp.com), Bado Lee, Dongyoon Han, Sangdoo Yun, Hwalsuk Lee.**
 
Clova AI Research, NAVER Corp.
### 사용법
1. download pretrained model
### Test instruction using pretrained model
 *Model name* | *Used datasets* | *Languages* | *Purpose* | *Model Link* |
 | :--- | :--- | :--- | :--- | :--- |
General | SynthText, IC13, IC17 | Eng + MLT | For general purpose | [Click](https://drive.google.com/open?id=1Jk4eGD7crsqCCg9C9VjCLkMN3ze8kutZ)
IC15 | SynthText, IC15 | Eng | For IC15 only | [Click](https://drive.google.com/open?id=1i2R7UIUqmkUtF0jv_3MXTqmQ_9wuAnLf)
LinkRefiner | CTW1500 | - | Used with the General Model | [Click](https://drive.google.com/open?id=1XSaFwBkOaFOdtk4Ane3DFyJGPRw6v5bO)

2. Run with pretrained model
``` (with python 3.7)
python test.py --trained_model=[weightfile] --test_folder=[folder path to test images]

```


# Recognition - fine-tuned trOCR

  https://huggingface.co/gg4ever/trOCR-youtube-kor-OCR

(미완...작성중)
