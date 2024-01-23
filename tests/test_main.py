from src import main
import requests
from unittest.mock import MagicMock, patch, call


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
                                'status': 'ac',
                                'titleSlug': 'problem-1'
                            },
                            {
                                'status': 'notcomplete',
                                'titleSlug': 'problem-2'
                            },
                            {
                                'status': 'notcomplete',
                                'titleSlug': 'problem-3'
                            },
                        ]
                    }
                }
            }
    
    class MockProblem2Response:
        def json(self):
            return {
                'data': {
                    'question': {
                        'questionId': 2,
                        'title': 'Problem 2',
                        "likes": 3,
                        "dislikes": 2,
                        "codeSnippets": [{ 'lang': 'Python3' }],
                    }
                }
            }

    class MockProblem3Response:
        def json(self):
            return {
                'data': {
                    'question': {
                        'questionId': 3,
                        'title': 'Problem 3',
                        "likes": 3,
                        "dislikes": 4,
                        "codeSnippets": [{ 'lang': 'Python3' }],
                    }
                }
            }

    requests.post.side_effect = [MockQuestionResponse(), MockProblem2Response(), MockProblem3Response()]

    main.print_problems()
    mock_print.assert_has_calls([call('Total problems: 2'), call('Problem 2')])

    cookies = {
        "LEETCODE_SESSION": 'somesession',
    }

    headers = {
        "x-csrftoken": 'token',
    }

    json_data = {
        "operationName": "questionData",
        "variables": {
            "titleSlug": 'problem-2',
        },
        "query": "query questionData($titleSlug: String!) {\n  question(titleSlug: $titleSlug) {\n    questionId\n    questionFrontendId\n    boundTopicId\n    title\n    titleSlug\n    content\n    translatedTitle\n    translatedContent\n    isPaidOnly\n    canSeeQuestion\n    difficulty\n    likes\n    dislikes\n    isLiked\n    similarQuestions\n    exampleTestcases\n    categoryTitle\n    contributors {\n      username\n      profileUrl\n      avatarUrl\n      __typename\n    }\n    topicTags {\n      name\n      slug\n      translatedName\n      __typename\n    }\n    companyTagStats\n    codeSnippets {\n      lang\n      langSlug\n      code\n      __typename\n    }\n    stats\n    hints\n    solution {\n      id\n      canSeeDetail\n      paidOnly\n      hasVideoSolution\n      paidOnlyVideo\n      __typename\n    }\n    status\n    sampleTestCase\n    metaData\n    judgerAvailable\n    judgeType\n    mysqlSchemas\n    enableRunCode\n    enableTestMode\n    enableDebugger\n    envInfo\n    libraryUrl\n    adminUrl\n    challengeQuestion {\n      id\n      date\n      incompleteChallengeCount\n      streakCount\n      type\n      __typename\n    }\n    __typename\n  }\n}\n",
    }

    requests.post.assert_called_with(
        "https://leetcode.com/graphql/",
        cookies=cookies,
        headers=headers,
        json=json_data,
        timeout=10,
    )

    # print(res)
    # assert False
    
