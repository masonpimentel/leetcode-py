def main():
    print('do request')

if __name__ == "__main__":
    main()



# fetch("https://leetcode.com/graphql/", {
#   "headers": {
#     "accept": "*/*",
#     "accept-language": "en-US,en;q=0.9",
#     "authorization": "",
#     "content-type": "application/json",
#     "random-uuid": "c7c0fd5e-1566-9b03-8d47-19b794e40241",
#     "sec-ch-ua": "\"Not_A Brand\";v=\"8\", \"Chromium\";v=\"120\", \"Google Chrome\";v=\"120\"",
#     "sec-ch-ua-mobile": "?0",
#     "sec-ch-ua-platform": "\"Windows\"",
#     "sec-fetch-dest": "empty",
#     "sec-fetch-mode": "cors",
#     "sec-fetch-site": "same-origin",
#     "uuuserid": "9c47aab6d1d9068267d5d6d7f5983c04",
#     "x-csrftoken": "dRQ7jAu0sVBhY7dYmWOgsa7wjbTqQ56cxEZfeT9xMhGRJqtChvZsurmzduL7EmzZ",
#     "x-newrelic-id": "UAQDVFVRGwIAUVhbAAMFXlQ="
#   },
#   "referrer": "https://leetcode.com/problemset/?difficulty=MEDIUM&page=1",
#   "referrerPolicy": "strict-origin-when-cross-origin",
#   "body": "{\"query\":\"\\n    query problemsetQuestionList($categorySlug: String, $limit: Int, $skip: Int, $filters: QuestionListFilterInput) {\\n  problemsetQuestionList: questionList(\\n    categorySlug: $categorySlug\\n    limit: $limit\\n    skip: $skip\\n    filters: $filters\\n  ) {\\n    total: totalNum\\n    questions: data {\\n      acRate\\n      difficulty\\n      freqBar\\n      frontendQuestionId: questionFrontendId\\n      isFavor\\n      paidOnly: isPaidOnly\\n      status\\n      title\\n      titleSlug\\n      topicTags {\\n        name\\n        id\\n        slug\\n      }\\n      hasSolution\\n      hasVideoSolution\\n    }\\n  }\\n}\\n    \",\"variables\":{\"categorySlug\":\"all-code-essentials\",\"skip\":0,\"limit\":50,\"filters\":{\"difficulty\":\"MEDIUM\"}},\"operationName\":\"problemsetQuestionList\"}",
#   "method": "POST",
#   "mode": "cors",
#   "credentials": "include"
# });