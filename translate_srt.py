from deep_translator import GoogleTranslator

input_path = "input/original.srt"
output_path = "output/translated.srt"
translator = GoogleTranslator(source='en', target='ar')

with open(input_path, 'r', encoding='utf-8') as infile:
    lines = infile.readlines()

translated_lines = []
for line in lines:
    if "-->" in line or line.strip().isdigit() or line.strip() == "":
        translated_lines.append(line)
    else:
        translated_text = translator.translate(line.strip())
        translated_lines.append(translated_text + "\n")

with open(output_path, 'w', encoding='utf-8') as outfile:
    outfile.writelines(translated_lines)

print("✅ Translation complete. You can now review 'translated.srt' in Notepad.")
