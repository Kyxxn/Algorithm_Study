// 24년 겨울 알고리즘 스터디
// BOJ & 프로그래머스
//
// Created by 박효준 on 1/10/24.
// 투 포인터 & 정렬

import Foundation

var n = Int(readLine()!)!
var input : [Int] = readLine()!.split(separator: " ").map{Int(String($0))!}
input.sort()
var count : Int = 0

func solve(_ s: inout Int, _ e: inout Int, _ g: Int) {
    var maxIdx = n
    while s < e {
        let tmp = input[s] + input[e]
        if tmp < g {
            s += 1
        } else if tmp == g {
            if input[s] == input[e] {
                count += e - s
            } else {
                if maxIdx > e {
                    maxIdx = e
                    while maxIdx > 0 && input[maxIdx - 1] == input[e] {
                        maxIdx -= 1
                    }
                }
                count += e - maxIdx + 1
            }
            s += 1
        } else {
            e -= 1
        }
    }
}

for i in 0..<n-1 {
    var start = i + 1
    var end = n - 1
    let goal = -input[i]
    solve(&start, &end, goal)
}

print(count)


//for i in 0..<N {
//    var standard = input[i]
//    for j in stride(from: N-1, to: 0, by: -1) {
//        var middle = standard + input[j]
//        if middle > 0{
//            // 뺀 결과가 양수일 때, i+1부터 다시 더해야함
//            for k in i+1..<N {
//                if middle + input[k] == 0 {
//                    count += 1
//                }
//            }
//        }else {
//            // 뺀 결과가 음수일 때, j-1부터 다시 더해야함
//            for k in stride(from: j-1, to: 0, by: -1) {
//                if middle + input[k] == 0 {
//                    count += 1
//                }
//            }
//        }
//    }
//}



//if start + end + input[i] == 0 {
//    count += 1
//}else if start + end + input[i] > 0 {
//    // 결과가 양수일 때 (end를 앞으로)
//    for j in stride(from:end-1, to: i, by: -1){
//        if start + input[j] + input[i] == 0 {
//            count += 1
//        }
//    }
//}else {
//    // 결과가 음수일 때 (start를 뒤로)
//    for j in i+1..<N-1 {
//        if input[j] + end + input[i] == 0 {
//            count += 1
//        }
//    }
//}
