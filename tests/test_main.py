from src import main
import requests
from unittest.mock import MagicMock, patch, call
import pytest


class MockQuestionResponse:
    def json(self):
        return {
            "data": {
                "problemsetQuestionList": {
                    "questions": [
                        {"status": "ac", "titleSlug": "problem-1"},
                        {"status": "notcomplete", "titleSlug": "problem-2"},
                        {"status": "notcomplete", "titleSlug": "problem-3"},
                        {"status": "ac", "titleSlug": "problem-4"},
                    ]
                }
            }
        }


class MockProblem2Passes:
    def json(self):
        return {
            "data": {
                "question": {
                    "questionId": 2,
                    "title": "Problem 2",
                    "likes": 3,
                    "dislikes": 2,
                    "codeSnippets": [{"lang": "Python3"}],
                    "titleSlug": "problem-2"
                }
            }
        }


class MockProblem3FailsLikeRatio:
    def json(self):
        return {
            "data": {
                "question": {
                    "questionId": 3,
                    "title": "Problem 3",
                    "likes": 3,
                    "dislikes": 4,
                    "codeSnippets": [{"lang": "Python3"}],
                    "titleSlug": "problem-2"
                }
            }
        }


class MockProblem4FailsLanguage:
    def json(self):
        return {
            "data": {
                "question": {
                    "questionId": 4,
                    "title": "Problem 4",
                    "likes": 3,
                    "dislikes": 1,
                    "codeSnippets": [{"lang": "SQL"}],
                    "titleSlug": "problem-2"
                }
            }
        }


COOKIES = {
    "LEETCODE_SESSION": "insert actual session here",
}

HEADERS = {
    "x-csrftoken": "insert actual token here",
}

JSON_DATA = {
    "operationName": "questionData",
    "query": "query questionData($titleSlug: String!) {\n  question(titleSlug: $titleSlug) {\n    questionId\n    questionFrontendId\n    boundTopicId\n    title\n    titleSlug\n    content\n    translatedTitle\n    translatedContent\n    isPaidOnly\n    canSeeQuestion\n    difficulty\n    likes\n    dislikes\n    isLiked\n    similarQuestions\n    exampleTestcases\n    categoryTitle\n    contributors {\n      username\n      profileUrl\n      avatarUrl\n      __typename\n    }\n    topicTags {\n      name\n      slug\n      translatedName\n      __typename\n    }\n    companyTagStats\n    codeSnippets {\n      lang\n      langSlug\n      code\n      __typename\n    }\n    stats\n    hints\n    solution {\n      id\n      canSeeDetail\n      paidOnly\n      hasVideoSolution\n      paidOnlyVideo\n      __typename\n    }\n    status\n    sampleTestCase\n    metaData\n    judgerAvailable\n    judgeType\n    mysqlSchemas\n    enableRunCode\n    enableTestMode\n    enableDebugger\n    envInfo\n    libraryUrl\n    adminUrl\n    challengeQuestion {\n      id\n      date\n      incompleteChallengeCount\n      streakCount\n      type\n      __typename\n    }\n    __typename\n  }\n}\n",
}


@pytest.fixture(autouse=True)
def init_requests_post():
    requests.post = MagicMock()

    requests.post.side_effect = [
        MockQuestionResponse(),
        MockProblem2Passes(),
        MockProblem3FailsLikeRatio(),
        MockProblem4FailsLanguage(),
    ]


@patch("builtins.print")
def test_problems_filtered(mock_print):
    main.print_problems()
    mock_print.assert_any_call("Total problems: 2")


def test_question_calls():
    json_data_problem_2 = {**JSON_DATA, "variables": {"titleSlug": "problem-2"}}
    json_data_problem_3 = {**JSON_DATA, "variables": {"titleSlug": "problem-3"}}

    main.print_problems()

    requests.post.assert_any_call(
        "https://leetcode.com/graphql/",
        cookies=COOKIES,
        headers=HEADERS,
        json=json_data_problem_2,
        timeout=10,
    )

    requests.post.assert_any_call(
        "https://leetcode.com/graphql/",
        cookies=COOKIES,
        headers=HEADERS,
        json=json_data_problem_3,
        timeout=10,
    )


@patch("builtins.print")
def test_problems_output(mock_print):
    main.print_problems()

    mock_print.assert_has_calls([call("Total problems: 2"), call("https://leetcode.com/problems/problem-2")])
