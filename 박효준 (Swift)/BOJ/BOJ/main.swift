// 24년 겨울 알고리즘 스터디
// BOJ & 프로그래머스
//
// Created by 박효준 on 1/10/24.

// 1. 인풋으로 값이 들어오면 양방향으로 연결

import Foundation

var input : [Int] = readLine()!.split(separator: " ").map{Int($0)!}
var n : Int = input[0]
var k : Int = input[1]

var arr : [[(Int, Bool)]] = Array(repeating: [(Int, Bool)](), count: k+1)

for _ in 0..<k {
    input = readLine()!.split(separator: " ").map{Int($0)!}
    let x = input[0]
    let y = input[1]
    arr[x].append((y, true))
    arr[y].append((x, false))
}

var s : Int = Int(readLine()!)!
for _ in 0..<s {
    input = readLine()!.split(separator: " ").map{Int($0)!}
    let key : Int = input[0]
    var check : Bool = false
    var dir : Bool = true
    for j in 0..<arr[key].count {
        if arr[key][j].0 == input[1] {
            check = true
            dir = arr[key][j].1
        }
    }
    
    if check {
        if dir {
            print(-1)
        }else {
            print(1)
        }
    }else{
        print(0)
    }
}


//for i in 0..<k {
//    print(arr[i])
//}

