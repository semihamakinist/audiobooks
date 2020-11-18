import pyttsx3

if __name__ == '__main__':
    # One time initialization
    engine = pyttsx3.init()

    # Voice IDs pulled from engine.getProperty('voices')
    # These will be system specific
    en_voice_m_id = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0'
    en_voice_f_id = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0'
    uk_voice_f_id = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-GB_HAZEL_11.0'

    # Use female English voice
    engine.setProperty('voice', en_voice_m_id)
    engine.say('Hello with my new voice')

    engine.runAndWait()
