import requests

LEETCODE_SESSION = 'insert here'
CSRF_TOKEN = 'insert here'

def main():
    cookies = {
        'gr_user_id': 'ff575bc7-ace7-4310-b8b9-6d0bee0de5a5',
        '87b5a3c3f1a55520_gr_last_sent_cs1': 'masonpimentel',
        'csrftoken': CSRF_TOKEN,
        '__stripe_mid': '9cf6ba15-26c1-49da-bf9d-355d87891bd0c0adea',
        'LEETCODE_SESSION': LEETCODE_SESSION,
        '_gid': 'GA1.2.1248421007.1705374387',
        'c_a_u': '"bWFzb25waW1lbnRlbA==:1rPnHG:bM3IPSC43R4r6B_lAGhhky_jqjizvuBQ24L0gJVTbHI"',
        '_gat': '1',
        '87b5a3c3f1a55520_gr_session_id': 'c56c610d-6723-412c-a6ba-edcece70d78e',
        '87b5a3c3f1a55520_gr_last_sent_sid_with_cs1': 'c56c610d-6723-412c-a6ba-edcece70d78e',
        '87b5a3c3f1a55520_gr_session_id_sent_vst': 'c56c610d-6723-412c-a6ba-edcece70d78e',
        '_dd_s': 'rum=0&expire=1705446773209',
        '87b5a3c3f1a55520_gr_cs1': 'masonpimentel',
        '_ga': 'GA1.1.1345551211.1704952385',
        '_ga_CDRWKZTDEX': 'GS1.1.1705445871.168.1.1705445879.52.0.0',
    }

    headers = {
        'authority': 'leetcode.com',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'authorization': '',
        'baggage': 'sentry-environment=production,sentry-release=ad2a7349,sentry-transaction=%2Fproblemset%2F%5B%5B...slug%5D%5D,sentry-public_key=2a051f9838e2450fbdd5a77eb62cc83c,sentry-trace_id=de02a39328d34479a7d550eb1fa76085,sentry-sample_rate=0.03',
        'content-type': 'application/json',
        'origin': 'https://leetcode.com',
        'random-uuid': 'c7c0fd5e-1566-9b03-8d47-19b794e40241',
        'referer': 'https://leetcode.com/problemset/',
        'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'sentry-trace': 'de02a39328d34479a7d550eb1fa76085-913195e6e2e2ca73-0',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'x-csrftoken': CSRF_TOKEN,
        'x-newrelic-id': 'UAQDVFVRGwIAUVhbAAMFXlQ=',
    }

    json_data = {
        'query': '\n    query problemsetQuestionList($categorySlug: String, $limit: Int, $skip: Int, $filters: QuestionListFilterInput) {\n  problemsetQuestionList: questionList(\n    categorySlug: $categorySlug\n    limit: $limit\n    skip: $skip\n    filters: $filters\n  ) {\n    total: totalNum\n    questions: data {\n      acRate\n      difficulty\n      freqBar\n      frontendQuestionId: questionFrontendId\n      isFavor\n      paidOnly: isPaidOnly\n      status\n      title\n      titleSlug\n      topicTags {\n        name\n        id\n        slug\n      }\n      hasSolution\n      hasVideoSolution\n    }\n  }\n}\n    ',
        'variables': {
            'categorySlug': 'all-code-essentials',
            'skip': 0,
            'limit': 50,
            'filters': {},
        },
        'operationName': 'problemsetQuestionList',
    }

    response = requests.post('https://leetcode.com/graphql/', cookies=cookies, headers=headers, json=json_data, timeout=10)
    for problem in response.json()['data']['problemsetQuestionList']['questions']:
        print(problem)


if __name__ == "__main__":
    main()

