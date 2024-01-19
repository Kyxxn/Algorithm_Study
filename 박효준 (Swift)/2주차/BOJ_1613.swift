//  24년 겨울 알고리즘 스터디
//  BOJ & 프로그래머스
//  백준 1747번
//
//  Created by 박효준 on 1/10/24.

import Foundation

func isPrime(_ N : Int) -> Bool{
    // 소수는 1과 자기 자신만 약수인 경우
    // 아래 두 if 문이 없으면 95% 런타임 에러남 -> 왜 ?
    if N <= 1 { return false }
    if N <= 3 { return true }
    
    var isCheck : Bool = true
    for i in 2...Int(sqrt(Double(N))){
        if N % i == 0{
            isCheck = false
            break
        }
    }
    
    return isCheck
}

func isPalindrome(_ N : Int) -> Bool{
    let s = String(N)
    return s == String(s.reversed())
}

if var N = Int(readLine()!) {
    while (true){
        if (isPrime(N) && isPalindrome(N)) {
            print(N)
            break
        }
        N += 1
    }
}
