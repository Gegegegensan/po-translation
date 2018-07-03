import sys
import polib

from googletrans import Translator
translator = Translator()

reload(sys)
# sys.stdout = codecs.getwriter('utf-8')(sys.stdout)
sys.setdefaultencoding('utf-8')

def potext_translator():
	po = polib.pofile('/Users/ryo.yamamoto/ja/test-notification.po')
	for entry in po:
		text = translator.translate(entry, dest='ja')
		print('{}: {}'.format(entry.msgid, text.msgstr))

if __name__ == '__main__':
    potext_translator()

