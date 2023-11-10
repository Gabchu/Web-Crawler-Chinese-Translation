from converter.zh_conversion import Converter
from crawler.web_crawler import Crawl_and_Convert


def convert_file(input_file, output_file):
    # Initialize the Converter class
    converter = Converter()

    try:
        with open(input_file, 'r', encoding='utf-8') as input_text:
            traditional_chinese_text = input_text.read()

        # Convert the traditional Chinese text to simplified Chinese
        simplified_chinese_text = converter.convert_to_simplified_chinese(
            traditional_chinese_text)

        with open(output_file, 'w', encoding='utf-8') as output_text:
            output_text.write(simplified_chinese_text)

        print("Conversion complete. Output saved to:", output_file)

    except Exception as e:
        print("An error occurred:", str(e))


def main():
    Crawl_and_Convert()
    input_file = 'product_data.txt'
    output_file = 'product_data_simplified.txt'

    convert_file(input_file, output_file)


if __name__ == "__main__":
    main()
