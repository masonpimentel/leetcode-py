from src import main
import requests
from unittest.mock import MagicMock
from unittest.mock import patch


@patch('builtins.print')
def test_answer(mock_print):
    requests.post = MagicMock()

    class MockQuestionResponse:
        def json(self):
            return {
                'data': {
                    'problemsetQuestionList': {
                        'questions': [
                            {
                                'status': 'ac'
                            },
                            {
                                'status': 'notcomplete'
                            },
                            {
                                'status': 'notcomplete'
                            },
                        ]
                    }
                }
            }

    requests.post.side_effect = [MockQuestionResponse()]

    main.print_problems()
    mock_print.assert_called_with('Total problems: 2')

    # print(res)
    # assert False
    
