import re
import unicodedata

def format_title(title, style='tn', sep='-'):

    # normalize and remove diacritics
    formatted_title = unicodedata.normalize('NFKD', title).encode('ASCII', 'ignore').decode('utf-8')

    # remove special characters
    formatted_title = re.sub(r'[^\w\s-]', '', formatted_title)

    words = formatted_title.split()

    if style == 'meta':
        # lowercase all and join with sep
        return sep.join(words).lower()
    else:
        # 'tn' style: preserve original casing and move leading article to the end
        if words and words[0] in ['The', 'A', 'An']:
            article = words.pop(0)
            words.append(article)
        return sep.join(words)