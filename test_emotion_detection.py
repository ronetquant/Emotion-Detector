import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetector(unittest.TestCase):
    """Unit tests for the emotion_detector function."""
    def test_emotion_detector(self):
        # Test for Joy
        result_1 = emotion_detector('I am glad this happened')
        self.assertEqual(result_1['dominant_emotion'], 'joy')
        # Test for Anger
        result_2 = emotion_detector('I am really mad about this')
        self.assertEqual(result_2['dominant_emotion'], 'anger')
        # Test for Sadness
        result_3 = emotion_detector('I am so sad about this')
        self.assertEqual(result_3['dominant_emotion'], 'sadness')

if __name__ == '__main__':
    unittest.main()
