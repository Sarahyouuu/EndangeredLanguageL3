import PyPDF2
import re

def remove_star(lines):
    # Define a function that filters out lines containing the ★ character, URLs, and Chinese text
    def filter_function(line):
        return "★" not in line and not re.search(r'(\bhttps://e-dictionary.ilrdf.org.tw\b)|([\u4e00-\u9fff]*阿美語[\u4e00-\u9fff]*)', line)
    
    # Filter out lines containing the ★ character, URLs, and Chinese text using the filter() function
    filtered_lines = filter(filter_function, lines)
    
    # Return the filtered lines
    return list(filtered_lines)


def remove_number(lines):
    pattern = r'^(\s*)\d+\.(\s*\d+\.)*\s*'

    filtered_lines = [re.sub(pattern, '', line) for line in lines]

    return filtered_lines

def remove_number_2(lines):
    pattern = r'^\d+\.\s*'

    filtered_lines = [re.sub(pattern, '', line) for line in lines]

    return filtered_lines


def remove_chinese_definition(lines):
    pattern = r'[\u4e00-\u9fff]+\.\s*'

    filtered_lines = [re.sub(pattern, '', line) for line in lines]

    return filtered_lines

def remove_chinese_definition_space(lines):
    pattern = r'[\u4e00-\u9fff]+[^.\n]*\s*\.\s*'

    filtered_lines = [re.sub(pattern, '', line) for line in lines]

    return filtered_lines



def read_pdf_text(filename, stripped_output_file, filtered_output_file):
    with open(filename, 'rb') as f:
        pdf_reader = PyPDF2.PdfFileReader(f) 
        
        with open(stripped_output_file, 'w', encoding='utf-8') as stripped_output, open(filtered_output_file, 'w', encoding='utf-8') as filtered_output:
            for page_num in range(pdf_reader.getNumPages()):
                page = pdf_reader.getPage(page_num)
                page_text = page.extractText()
                
                lines = page_text.splitlines()
                
                stripped_lines = remove_star(lines)
                for line in stripped_lines:
                    stripped_output.write(line + '\n')
                
                filtered_lines = remove_star(lines)
                filtered_lines = remove_number(filtered_lines)
                filtered_lines = remove_number_2(filtered_lines)
                filtered_lines = remove_chinese_definition(filtered_lines)
                filtered_lines = remove_chinese_definition_space(filtered_lines)
                for line in filtered_lines:
                    filtered_output.write(line + '\n')




def txt_filter(input_file, output_file):
    # Open the input file and read the text
    with open(input_file, 'r', encoding='utf-8') as f:
        text = f.read()

    pattern = r"\s[A-Za-z']+\b[\s\S]*?[\u4e00-\u9fff]+\s*。"

    filtered_text = re.sub(f'(?s)(?!{pattern}).', '', text)

    # Open the output file and write the filtered text
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(filtered_text)



read_pdf_text('amis.pdf', 'amis_stripped.txt', 'amis_filtered.txt')



txt_filter('amis_stripped.txt', 'amis_stripped2.txt')

