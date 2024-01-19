//  24년 겨울 알고리즘 스터디
//  BOJ & 프로그래머스
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


//var n : Int = Int(readLine()!)!
//var graph : [[(Int, Int)]] = Array(repeating: [(Int, Int)](), count: n+1)
//var visited : [Bool] = Array(repeating: false, count: n+1)
//
//for _ in 0..<n-1{ // 0~10 11번
//    let tmp : [Int] = readLine()!.split(separator: " ").map{Int($0)!}
//    let x : Int = tmp[0]
//    let y : Int = tmp[1]
//    let weight : Int = tmp[2]
//    graph[x].append((y, weight))
//    graph[y].append((x, weight))
//}
//// 인접 리스트 완성
//
//var weightSum : Int = 0 // 노드 - 노드간의 가중치
//var rootToleaf : [Int] = Array(repeating: 0, count : n+1)
//// 시작 노드 X에서 N개의 노드들까지 가중치를 담는 배열
//
//func dfs(_ vertex : Int) {
//    visited[vertex] = true
//    
//    for next in graph[vertex]{
//        let nextVertex : Int = next.0
//        let nextWeight : Int = next.1
//        
//        if (!visited[nextVertex]){
//            weightSum = weightSum + nextWeight
//            dfs(nextVertex)
//            weightSum = weightSum - nextWeight
//        }else{
//            rootToleaf[vertex] = weightSum
//        }
//    }
//}
//
//dfs(1)
//// 1번 : 루트와 가장 먼 리프노드
//var weightMax : Int = rootToleaf.max()!
//var start = rootToleaf.firstIndex(of: weightMax)!
//
//// 2번 : 1번 노드와 가장 먼 리프노드
//weightSum = 0
//for i in 0...n{
//    visited[i] = false
//    rootToleaf[i] = 0
//}
//
//dfs(start)
//weightMax = rootToleaf.max()!
//print(weightMax)
//
////for i in rootToleaf{
////    print(i, terminator: " ")
////}
//
////for i in 0..<n{
////    print(graph[i])
////}
