# pylint: disable=C0114

import time
import requests
from typing_extensions import TypedDict

LEETCODE_SESSION = "insert actual session here"
CSRF_TOKEN = "insert actual token here"
LANGUAGE = 'Python3'
# Increase this if LeetCode is returning rate limit errors
SLEEP_TIME = 0.5

# pylint: disable=C0116
def print_problems() -> None:
    cookies = {
        "LEETCODE_SESSION": LEETCODE_SESSION,
    }

    headers = {
        "x-csrftoken": CSRF_TOKEN,
    }

    json_data = {
        # pylint: disable=C0301
        "query": "\n    query problemsetQuestionList($categorySlug: String, $limit: Int, $skip: Int, $filters: QuestionListFilterInput) {\n  problemsetQuestionList: questionList(\n    categorySlug: $categorySlug\n    limit: $limit\n    skip: $skip\n    filters: $filters\n  ) {\n    total: totalNum\n    questions: data {\n      acRate\n      difficulty\n      freqBar\n      frontendQuestionId: questionFrontendId\n      isFavor\n      paidOnly: isPaidOnly\n      status\n      title\n      titleSlug\n      topicTags {\n        name\n        id\n        slug\n      }\n      hasSolution\n      hasVideoSolution\n    }\n  }\n}\n    ",
        "variables": {
            "categorySlug": "all-code-essentials",
            "skip": 0,
            "limit": 4000,
            "filters": {
                "difficulty": "MEDIUM",
                "orderBy": "FRONTEND_ID",
                "sortOrder": "ASCENDING",
            },
        },
        "operationName": "problemsetQuestionList",
    }

    response = requests.post(
        "https://leetcode.com/graphql/",
        cookies=cookies,
        headers=headers,
        json=json_data,
        timeout=10,
    )

    # pylint: disable=C0103
    QuestionFromAll = TypedDict("QuestionFromAll", {"status": str, "titleSlug": str})
    questions: list[QuestionFromAll] = response.json()["data"][
        "problemsetQuestionList"
    ]["questions"]

    questions = list(filter(lambda question: question["status"] != "ac", questions))
    print(f"Total problems: {len(questions)}")

    for question in questions:
        slug = question["titleSlug"]

        json_data = {
            "operationName": "questionData",
            "variables": {
                "titleSlug": slug,
            },
            # pylint: disable=C0301
            "query": "query questionData($titleSlug: String!) {\n  question(titleSlug: $titleSlug) {\n    questionId\n    questionFrontendId\n    boundTopicId\n    title\n    titleSlug\n    content\n    translatedTitle\n    translatedContent\n    isPaidOnly\n    canSeeQuestion\n    difficulty\n    likes\n    dislikes\n    isLiked\n    similarQuestions\n    exampleTestcases\n    categoryTitle\n    contributors {\n      username\n      profileUrl\n      avatarUrl\n      __typename\n    }\n    topicTags {\n      name\n      slug\n      translatedName\n      __typename\n    }\n    companyTagStats\n    codeSnippets {\n      lang\n      langSlug\n      code\n      __typename\n    }\n    stats\n    hints\n    solution {\n      id\n      canSeeDetail\n      paidOnly\n      hasVideoSolution\n      paidOnlyVideo\n      __typename\n    }\n    status\n    sampleTestCase\n    metaData\n    judgerAvailable\n    judgeType\n    mysqlSchemas\n    enableRunCode\n    enableTestMode\n    enableDebugger\n    envInfo\n    libraryUrl\n    adminUrl\n    challengeQuestion {\n      id\n      date\n      incompleteChallengeCount\n      streakCount\n      type\n      __typename\n    }\n    __typename\n  }\n}\n",
        }

        response = requests.post(
            "https://leetcode.com/graphql/",
            cookies=cookies,
            headers=headers,
            json=json_data,
            timeout=10,
        )

        CodeSnippet = TypedDict("CodeSnippet", {"lang": str})
        # pylint: disable=C0103
        QuestionFromDetail = TypedDict(
            "QuestionFromDetail",
            {
                "questionId": int,
                "title": str,
                "likes": int,
                "dislikes": int,
                "codeSnippets": list[CodeSnippet],
            },
        )
        questionFromDetail: QuestionFromDetail = response.json()["data"]["question"]

        snippets = list(
            map(lambda question: question["lang"], questionFromDetail["codeSnippets"])
        )

        if (
            questionFromDetail["likes"] > questionFromDetail["dislikes"]
            and questionFromDetail["codeSnippets"]
            and LANGUAGE in snippets
        ):
            print(questionFromDetail["title"])

        time.sleep(SLEEP_TIME)


if __name__ == "__main__":
    print_problems()
