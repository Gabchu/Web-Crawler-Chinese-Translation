# converter/zh_conversion.py
import json
import sys
sys.path.append('C:/Users/terre/OneDrive/Desktop/Project_Converter')


class Converter:
    def __init__(self):
        # Load the JSON data
        with open('zh2Hant.json', 'r', encoding='utf-8') as json_file:
            self.zh2Hant = json.load(json_file)
        # Reverse the mapping for simplified to traditional
        self.Hant2zh = {v: k for k, v in self.zh2Hant.items()}

    def convert_to_simplified_chinese(self, text):
        # Convert the text character by character
        converted_text = ''
        for char in text:
            if char in self.Hant2zh:
                # If the character is in the reversed mapping, use the simplified version
                converted_text += self.Hant2zh[char]
            else:
                # If the character is not in the data, keep it unchanged
                converted_text += char
        return converted_text
