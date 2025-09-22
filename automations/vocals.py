from spleeter.separator import Separator
separator = Separator('spleeter:2stems')  # 2 stems: vocals & accompaniment
separator.separate_to_file('test.mp3', '.')