# dp + state compression
class Solution(object):
    def smallestSufficientTeam(self, req_skills, people):
        n, m = len(req_skills), len(people)
        key = {v: i for i, v in enumerate(req_skills)}
        dp = {0: []}
        for i, p in enumerate(people):
            his_skill = 0
            for skill in p:
                if skill in key:
                    his_skill |= 1 << key[skill]
            for skill_set, need in dp.items():
                with_him = skill_set | his_skill
                if with_him == skill_set: continue
                if with_him not in dp or len(dp[with_him]) > len(need) + 1:
                    dp[with_him] = need + [i]
        return dp[(1 << n) - 1]


# Runtime: 92 ms, faster than 88.12% of Python3 online submissions for Smallest Sufficient Team.
# Memory Usage: 14 MB, less than 100.00% of Python3 online submissions for Smallest Sufficient Team.
# link: https://leetcode.com/problems/smallest-sufficient-team/discuss/334630/Python-Optimized-backtracking-with-explanation-and-code-comments-88-ms
class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        for i, skill in enumerate(people):
            people[i] = set(skill)
        for i, i_skills in enumerate(people):
            for j, j_skills in enumerate(people):
                if i != j and i_skills.issubset(j_skills):
                    people[i] = set()
        skills_to_people = collections.defaultdict(set)
        for i, skills in enumerate(people):
            for skill in skills:
                skills_to_people[skill].add(i)
            people[i] = set(skills)
        self.unmet_skills = set(req_skills)
        self.smallest_length = float("inf")
        self.current_team = []
        self.best_team = []
        def meet_skill(skill=0):
            if not self.unmet_skills:
                if self.smallest_length > len(self.current_team):
                    self.smallest_length = len(self.current_team)
                    self.best_team = self.current_team[::]
                return 
            if req_skills[skill] not in self.unmet_skills:
                return meet_skill(skill + 1)
            for i in skills_to_people[req_skills[skill]]:
                skills_add_by_person = people[i].intersection(self.unmet_skills)
                self.unmet_skills = self.unmet_skills - skills_add_by_person
                self.current_team.append(i)
                meet_skill(skill + 1)
                self.current_team.pop()
                self.unmet_skills = self.unmet_skills.union(skills_add_by_person)

        meet_skill()
        return self.best_team
