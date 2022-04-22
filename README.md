# 👨🏻‍💻 Algorithm Study

---

`LeetCode`와 `Programmers`및 기타 사이트의 Algorithm 문제로 알고리즘 study를 운영합니다

Algorithm 문제는 정답이 하나로 정해져 있지 않기때문에 많은 사람들의 다양한 풀이방법을 접하는 것만으로도 도움이 될것으로 기대하고 있습니다

언어에 상관없이 참여하고 싶은분은 자유롭게 참여가 가능합니다
아래의 내용을 꼭 읽어주세요

## 참여 방법

1. 해당 repository fork 후 원 repository를 `upstream remote`로 설정<br>
   `git remote add upstream https://github.com/Study-for-better-than-yesterday/Algorithm.git`
2. `Leetcode`, `Programmers` 포함 기타 다른 문제풀이 사이트에서 본인이 풀어보고자 하는 문제를 선정
3. `문제출처 사이트 문제이름` 으로 branch 생성 (under_bar)<br>
   **ex)** `LeetCode_1_problem`, `Programmers_problem`
4. 1. 아래 첨부된 폴더구조에 맞게 폴더 및 `readme.md` 작성 <br>(해당 사이트의 문제설명과 똑같이 작성하고, link도 걸어주세요 - 기존에 작성된 `readme.md` 파일 참고..!)
   2. 폴더가 존재한다면 본인의 문제풀이만 `githubId(or nickname).본인이 풀은 언어의 확장자` 로 생성하여 작성.<br>(최대한 변수명과 logic이 명확하게 작성해주세요. _이렇게 배워 갈 수 있는 협업 환경!!_) <br>
      **ex)** `bestDev.js`, `bestDeb.py`, `bestDev.java` etc..
   3. 필수는 아니지만 algorithm 사이트의 결과값을 주석으로 포함하면 더 좋아요! <br>
      **ex)** ` Runtime 60ms Memory 40.7MB`
5. git push origin 해당 branch!!!

**매번 `git pull upstream master` 를 하는 것을 잊지마세요**

### PR 및 commit 규칙

### Commit

1. 새로운 문제를 올린 경우(`readme.md`) `문제출처 사이트 - 문제이름` 으로 commit <br> **ex)** Leetcode - 1. Two Sum
2. 본인의 풀이를 올린 경우 `문제이름 by 본인 github id 및 nickname` 으로 commit <br> **ex)** Two Sum by bestDev

### PR

1. `[문제사이트] 문제번호(번호 존재시).문제이름(난이도-optional)` 형태로 PR 요청
   **ex)** [Leetcode] 1. Two Sum(Easy)
2. asignee는 자기 자신
3. label은 사용한 언어와 문제의 난이도

## Review

같은 언어를 쓰는 사람들끼리 코드리뷰를 하면서 서로의 코드를 보며 성장해봅시다.<br>
PR의 Reviewer가 아니더라도 적극적으로 해보아요<br>
Reviewer는 아무리 늦어도 이틀안에 comment를 남기고 PR을 요청한 본인이 확인 후 merge 합시다!<br>
매번 master branch는 pull request해서 최신화를 유지해요!

- 리뷰시 구체적이고 명시적인 피드백 제공
- 오타의 유무
- 잘한 부분은 잘했다고 적극적인 피드백
- 변수명, 비즈니스 로직 등 코드를 봤을 때 이해가 안가거나 모호한 부분 질문 - 질문받은 사람은 이를 설명하면서 다시 복기할 수 있고 질문한 사람은 답변을 보고 로직에 관한 지식을 얻는 게 목적
- 개선사항 제안

## 폴더구조 예시

```
.
├── Leetcode
│   ├── Easy
│   │   ├── 1. Two Sum
│   │   │   ├── readme.md
│   │   │   └── example.js
│   │   ├── 7. Reverse Integer
│   │   │   └── readme.md
│   │   │   └── example.js
│   │   └── 9. Palindrome Number
│   │       └── readme.md
│   │       └── example.js
│   │       └── example.py
│   └── Medium
│       ├── 102. Binary Tree Level Order Traversal
│       │   ├── readme.md
│       │   └── example.js
│       ├── 103. Binary Tree Zigzag Level Order Traversal
│       │   ├── readme.md
│       │   └── example.js
│       ├── 2. Add Two Numbers
│       │   ├── readme.md
│       │   └── example.js
│       ├── 3. Longest Substring Without Repeating Characters
│       │   ├── readme.md
│       │   └── example.js
│       └── 98. Validate Binary Search Tree
│           ├── readme.md
│           └── example.js
├── Programmers
│   ├── Level1
│   │   ├── 모의고사
│   │   │   ├── readme.md
│   │   │   └── example.js
│   │   └── 가장 큰 수
│   │   │   ├── readme.md
│   │   │   └── example.js
│   │   ├── K번째수
│   │   │   ├── readme.md
│   │   │   ├── example.js
│   │   │   └── example.py
│   │   ├── 완주하지 못한 선수
│   │   │   ├── readme.md
│   │   │   └── example.js
│   │   └── 체육복
│   │       ├── readme.md
│   │       └── example.js
│   └── Level2
│       ├── 기능개발
│       │   ├── readme.md
│       │   └── example.js
│       ├── 시저 암호
│       │   ├── readme.md
│       │   └── example.js
│       ├── 다리를 지나는 트럭
│       │   ├── readme.md
│       │   └── example.js
│       └── 약수의 합
│       │   ├── readme.md
│       │   ├── example.js
│       │   └── example.py
│       └── 프린터
│           ├── readme.md
│           └── example.js
└── README.md

```
