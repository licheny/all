from PIL import Image
from io import BytesIO

f=open("1demo_2016051112_03_05_400_0_0_XX_5.mix","rb")
r=f.read()
i = Image.open(BytesIO(r))