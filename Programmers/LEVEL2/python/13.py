def solution(skill, skill_trees):
    not_answer = 0
    for skill_t in skill_trees:
        idx = 0
        for s in skill_t:
            if s not in skill: continue
            if skill[idx] != s:
                not_answer += 1
                break
            idx += 1
        
    return len(skill_trees) - not_answer

print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]	))