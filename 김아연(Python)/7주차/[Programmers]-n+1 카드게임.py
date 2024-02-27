"""
<다른사람 풀이 참고>
1. 카드 뭉치에서 항상 2장을 뽑아 사용가능한 배열에 저장
2. 처음 가지고 있는 배열에서 뽑은 2장에 카드에 적힌 수의 합이 n+1이 되면 그 카드 두장을 낸다.
3. 카드 두장을 낼 수 없는 상황이 생기면
   3-1. 코인이 1이상인 경우 
        - 내가 가지고 있는 카드에서 1장을 선택하고, 나머지 한장은 사용가능한 카드에서 1장을 선택
        - n+1이 되면 코인 1 감소, 라운드 1 증가
   3-2. 코인이 2이상인 경우
        - 사용가능한 카드에서 2장을 선택
        - n+1이 되면 코인 2 감소, 라운드 1 증가
"""

def check(arr1, arr2, n):
    arr = set(arr2)
    for card in arr1:
        if n-card in arr:
            arr1.pop(arr1.index(card))
            arr2.pop(arr2.index(n-card))
            return True
    return False

def solution(coin, cards):
    round = 1
    n = len(cards)
    deck = cards[len(cards)//3:]
    firstcard = cards[:n//3]
    getcard = []
    
    while coin >= 0 and deck:
        getcard.append(deck.pop(0))
        getcard.append(deck.pop(0))
        
        if check(firstcard, firstcard, n+1):
            pass
        elif coin >= 1 and check(firstcard, getcard, n+1):
            coin -= 1
        elif coin >= 2 and check(getcard, getcard, n+1):
            coin -= 2
        else:
            break
            
        round += 1
        
    return round