import speech_recognition as sr
from pydub import AudioSegment

# Функция для конвертации аудио в текст


def audio_to_text(audio_file):
    # Инициализируем распознаватель
    recognizer = sr.Recognizer()

    # Читаем аудиофайл
    audio_format = audio_file.split('.')[-1]  # Получаем формат файла

    # Если аудиофайл не в формате WAV, конвертируем его
    if audio_format != 'wav':
        sound = AudioSegment.from_file(audio_file, format=audio_format)
        audio_file = 'converted_audio.wav'  # Временный WAV файл
        sound.export(audio_file, format="wav")

    # Открываем аудиофайл через библиотеку speech_recognition
    with sr.AudioFile(audio_file) as source:
        audio_data = recognizer.record(source)  # Читаем содержимое файла
        try:
            # Распознаем речь на английском языке с использованием Google Web Speech API
            text = recognizer.recognize_google(audio_data, language="en-US")
            print("Распознанный текст: ", text)
            return text
        except sr.UnknownValueError:
            print("Google Web Speech API не смог распознать аудио.")
        except sr.RequestError as e:
            print(
                f"Не удалось подключиться к сервису Google Web Speech API; {e}")


# Пример использования функции
# Путь к твоему аудиофайлу
audio_file_path = r"C:\Users\A191a\Downloads\audio_2024-09-04_17-38-33.ogg"
audio_to_text(audio_file_path)
