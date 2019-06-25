import re

class StringAtomizer:
    def __init__(self):
        self.KOR_BASE = ord('가') # 44032

        # consonants and vowels
        self.INITAIL = list('ㄱㄲㄴㄷㄸㄹㅁㅂㅃㅅㅆㅇㅈㅉㅊㅋㅌㅍㅎ')
        self.VOWELS = list('ㅏㅐㅑㅒㅓㅔㅕㅖㅗㅘㅙㅚㅛㅜㅝㅞㅟㅠㅡㅢㅣ')
        self.FINAL = list('\0ㄱㄲㄳㄴㄵㄶㄷㄹㄺㄻㄼㄽㄾㄿㅀㅁㅂㅄㅅㅆㅇㅈㅊㅋㅌㅍㅎ')
        self.FINAL[0] = ''
        self.FINAL_CONSONANT_COUNT = len(self.FINAL) # 종성의 갯수
        self.INITIAL_CONSONANT_RANGE = len(self.VOWELS) * self.FINAL_CONSONANT_COUNT # 한 초성으로 표현 가능한 문자의 갯수

        self.HANGEUL_REGEX = re.compile(r'[ㄱ-ㅎ가-힣]+')
    def atomizeString(self, string):
        # 입력받은 문자열을 리스트화한다.
        resultString = list(string)

        # 한국어로 된 모든 단어의 Match Object를 얻어낸다.
        koreanWordMatches = self.HANGEUL_REGEX.finditer(string)

        # Match Objects 순회
        for m in koreanWordMatches:
            word = list(m.group()) # 결과 단어 문자열을 리스트화한다.
            buffer = [] 

            # 리스트화 된 단어를 문자단위로 순회
            for syllable in word:
                # 분리시킨 문자를 임시 결과 버퍼에 저장
                buffer.append(self.separateKoreanLetters(syllable))
            
            # 원래 단어가 존재하던 인덱스를 구해낸다.
            start, end = m.span()
            # 최종 결과 문자열에서 원래 있던 문자열을 원자화한 문자들로 바꾼다.
            resultString[start:end] = buffer

        return resultString

    def separateKoreanLetters(self, char):
        result = []
        charIndex = ord(char) - self.KOR_BASE # 문자인덱스 = 실제문자코드 - 베이스('가', 44032)

        initialConsonant = int( charIndex / self.INITIAL_CONSONANT_RANGE ) # 문자인덱스 / (중성갯수 * 종성갯수)
        vowel = int( ( charIndex % self.INITIAL_CONSONANT_RANGE ) / self.FINAL_CONSONANT_COUNT ) # (initialConsonant 를 구한 식에서의 나머지) / 종성갯수 로 중성을 구한다.
        finalConsonant = int( ( charIndex % self.INITIAL_CONSONANT_RANGE ) % self.FINAL_CONSONANT_COUNT ) # medialConsonant 를 구한 식에서의 나머지를 통해 종성을 구한다.

        return (self.INITAIL[initialConsonant], self.VOWELS[vowel], self.FINAL[finalConsonant])    
    
    
def main():
    string = '가 나다 라마1바 사#아 자ab차cd카 타w o파 r? d!하'
    print(string)
    print(StringAtomizer().atomizeString(string))
    '''
    Expected outputs:
    
    (1) 가 나다 라마1바 사#아 자ab차cd카 타w o파 r? d!하
    (2) [('ㄱ', 'ㅏ', ''), ' ', ('ㄴ', 'ㅏ', ''), ('ㄷ', 'ㅏ', ''), ' ', ('ㄹ', 'ㅏ', ''), ('ㅁ', 'ㅏ', ''), '1', ('ㅂ', 'ㅏ', ''), ' ', ('ㅅ', 'ㅏ', ''), '#', ('ㅇ', 'ㅏ', ''), ' ', ('ㅈ', 'ㅏ', ''), 'a', 'b', ('ㅊ', 'ㅏ', ''), 'c', 'd', ('ㅋ', ' ㅏ', ''), ' ', ('ㅌ', 'ㅏ', ''), 'w', ' ', 'o', ('ㅍ', 'ㅏ', ''), ' ', 'r', '?', ' ', 'd', '!', ('ㅎ', 'ㅏ', '')]
    '''


if __name__ == "__main__":
    main()
