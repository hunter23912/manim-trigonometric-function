from wordcloud import WordCloud
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

with open("words-for-wordcloud.txt", "r", encoding="utf-8") as file:
    text = file.read()

mask_image = np.array(Image.open("trangle_for_wordcloud.png"))

wordcloud = WordCloud(
    width=1920 * 2,
    height=1080,
    font_path="SIMYOU.TTF",
    prefer_horizontal=0.5,
    colormap="Set3",
    mask=mask_image,
    scale=2,
    min_font_size=5,
    max_font_size=200,
).generate(text)

plt.figure(figsize=(10, 6))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()
