from django import template
import re

register = template.Library()

@register.filter(name='correct')
def correct(text):
    incorrect_words = ["редиска"]
    for word in incorrect_words:
        ch_words = re.findall(word, text, re.IGNORECASE)
        for ch_word in ch_words:
            text = text.replace(ch_word, f'{ch_word[:1]}' + (len(ch_word[2:]) + 1) * '*')
    return text

