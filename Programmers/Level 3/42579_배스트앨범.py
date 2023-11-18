from collections import defaultdict

def solution(genres, plays):
    
    answer = []

    info = defaultdict(list)
    info_cnt = defaultdict(int)
    for i in range(len(genres)):
        genre, play = genres[i], plays[i]
        info[genre].append((play, i))
        info_cnt[genre] += play
        
    info_cnt_lst = list(info_cnt.items())    
    info_cnt_lst.sort(key = lambda x:x[1], reverse = True)
    
    for genre, _ in info_cnt_lst:
        genre_lst = list(info[genre])
        
        genre_lst.sort(key = lambda x:(-x[0], x[1]))
        
        limit = 0
        for _, idx in genre_lst:
            answer.append(idx)
            limit += 1
            
            if limit == 2: break
        
    return answer