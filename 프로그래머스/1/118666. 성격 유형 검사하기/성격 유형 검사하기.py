def solution(survey, choices):
    mbti = {"RT":0,"CF":0,"JM":0,"AN":0}
    mbti_key = mbti.keys()
    for i,surv in enumerate(survey):
        score = choices[i]-4
        disagree_ch = surv[0]
        agree_ch = surv[1]
        for key in mbti.keys():
            if key[0] == agree_ch:
                mbti[key] += score
            elif key[0] == disagree_ch:
                mbti[key] -= score
    answer = ''
    for key in mbti_key:
        if mbti[key] >= 0:
            answer += key[0]
        else:
            answer += key[1]
            

    return answer