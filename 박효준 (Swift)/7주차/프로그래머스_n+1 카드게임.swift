// 24년 겨울 알고리즘 스터디
// BOJ & 프로그래머스
//
// Created by 박효준 on 1/10/24.

import Foundation

func solution(_ coin:Int, _ cards:[Int]) -> Int {
    // 시작할 때 n/3장을 모두 뽑아 가지고, 턴 시작마다 2장씩 뽑음
    // 뽑은 카드는 카드 한 장당 동전 하나를 소모 or 동전 소모 없이 버림
    // n + 1이 되도록 카드 두 장을 내고 다음 라운드로 진행, 못 내면 종료
    // 카드 뭉치에 카드가 없다면 종료
    
    // 1. 첫 턴 시작
    // 2. 먼저 카드를 뽑음
    // 3. 사야 되면 동전을 내고 구매함
    // 4. 다음 라운드 진행
    var round: Int = 1
    var nextCard = cards.count + 1
    var myCards: [Int] = []
    var stageCards: [Int] = cards
    var stageCoin: Int = coin
    
    for i in 0..<(cards.count/3) {
        myCards.append(cards[i])
    }
    
    while !myCards.isEmpty {
        // keepRound : n+1 카드 못 내면 false로 바뀜
        var first: Int = 0
        var firstPick: Bool = false
        var second: Int = 0
        var secondPick: Bool = false
        
        // card 남은게 0, 1, 2장일 때 로직 추가해야 함
        if stageCards.count > 0 {
            first = stageCards.removeFirst()
            second = stageCards.removeFirst()
            
            for myCard in myCards {
                if myCard + first == nextCard  && !firstPick && stageCoin > 0{
                    stageCoin -= 1
                    myCards.append(first)
                    firstPick = true
                }else if myCard + second == nextCard && !secondPick && stageCoin > 0{
                    stageCoin -= 1
                    myCards.append(second)
                    secondPick = true
                }
            }
        }
        
        
        
        // 카드 조합 확인
        var nextReady: Bool = false
        for i in 0..<myCards.count {
            for j in i+1..<myCards.count {
                if myCards[i] + myCards[j] == nextCard {
                    nextReady = true
                    round += 1
                    break
                }
            }
            if nextReady { break }
        }
        
        if !nextReady { break }
    }
    
    return round
}
