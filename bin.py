from google_trans_new import google_translator

#谷歌翻译
def fanyi(data):
    translator = google_translator()
    translate_text = translator.translate(data, lang_tgt='zh')
    return translate_text
