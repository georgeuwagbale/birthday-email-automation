from PIL import Image, ImageFont, ImageDraw


class Writer:
    def __init__(self, image_path: str) -> None:
        self._image_path = image_path
        self._image = Image.open(image_path)
        self._font = ImageFont.truetype('../fonts/calibri-bold.ttf', 140)
        self._image_editable = ImageDraw.Draw(self._image)

    def write_on_image(self, texts: list, name_to_save_file_as: str = 'output.jpg'):
        no_of_celebrants = len(texts)
        
        spacing = 0
        if no_of_celebrants <= 5:
            for text in texts:
                self._image_editable.text((1240, 2095 + spacing), text, font=self._font, anchor="ms", fill=(255, 200, 0))
                spacing += 150

        elif 5 < no_of_celebrants <= 6:
            for text in texts:
                self._image_editable.text((1240 , 2095 + spacing), text, font=self._font, anchor="ms", fill=(255, 200, 0))
                spacing += 150

        elif 6 < no_of_celebrants <= 14:
            self._font = ImageFont.truetype('../fonts/calibri-bold.ttf', 90)

            if no_of_celebrants % 2 == 0:
                # self.font.size = 60
                for text in texts[ : no_of_celebrants//2]:
                    self._image_editable.text((650, 2095 + spacing), text, font=self._font, anchor="ms", fill=(255, 200, 2))
                    spacing += 130

                spacing = 0
                for text in texts[no_of_celebrants//2: ]:
                    self._image_editable.text((1700, 2085 + spacing), text, font=self._font, anchor="ms", fill=(255, 200, 0))
                    spacing += 130

            else:
                
                for text in texts[ : (no_of_celebrants//2)+1]:
                    self._image_editable.text((650 , 2095 + spacing), text, font=self._font, anchor="ms", fill=(255, 200, 0))
                    spacing += 130

                spacing = 0
                for text in texts[(no_of_celebrants//2)+1: ]:
                    self._image_editable.text((1700, 2095 + spacing), text, font=self._font, anchor="ms", fill=(255, 200, 0))
                    spacing += 130

        elif 14 < no_of_celebrants <= 20:
            self._font = ImageFont.truetype('../fonts/calibri-bold.ttf', 65)

            if no_of_celebrants % 2 == 0:
                # self.font.size = 60
                for text in texts[ : no_of_celebrants//2]:
                    self._image_editable.text((650, 2095 + spacing), text, font=self._font, anchor="ms", fill=(255, 200, 0))
                    spacing += 90

                spacing = 0
                for text in texts[no_of_celebrants//2: ]:
                    self._image_editable.text((1700, 2095 + spacing), text, font=self._font, anchor="ms", fill=(255, 200, 0))
                    spacing += 90

            else:
                # self.font.size = 60
                for text in texts[ : (no_of_celebrants//2)+1]:
                    self._image_editable.text((650, 2095 + spacing), text, font=self._font, anchor="ms", fill=(255, 200, 0))
                    spacing += 90

                spacing = 0
                for text in texts[(no_of_celebrants//2)+1: ]:
                    self._image_editable.text((1700, 2095 + spacing), text, font=self._font, anchor="ms", fill=(255, 200, 0))
                    spacing += 90

        return self._image.save("../img/results/" + name_to_save_file_as)


