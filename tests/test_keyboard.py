from src.keyboard import Keyboard
def test_keyboard():
    kb = Keyboard('Keron', 3200, 1)
    assert kb.language == "EN"
    kb.change_lang()
    assert kb.language == "RU"