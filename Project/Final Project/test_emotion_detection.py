import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetector(unittest.TestCase):
    def test_emotion_detector(self):
        # Test case for Joy
        result_1 = emotion_detector("I am glad this happened")
        self.assertEqual(result_1['label'], 'joy')

        # Test case for Anger
        result_2 = emotion_detector("I am really mad about this")
        self.assertEqual(result_2['label'], 'anger')

        # Test case for Disgust
        result_3 = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(result_3['label'], 'disgust')

        # Test case for Sadness
        result_4 = emotion_detector("I am so sad about this")
        self.assertEqual(result_4['label'], 'sadness')

        # Test case for Fear
        result_5 = emotion_detector("I am really afraid that this will happen")
        self.assertEqual(result_5['label'], 'fear')

if __name__ == '__main__':
    unittest.main()
