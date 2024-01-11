//
//  프로그래머스 귤 고르기
//  BOJ
//
//  Created by 박효준 on 1/10/24.
import Foundation


func solution(_ k:Int, _ tangerine:[Int]) -> Int {
    var dic : [Int : Int] = [:]
    var count : Int = 0
    var tmp = k
    for data in tangerine{
        if dic[data] != nil {
            if let value = dic[data]{
                dic[data] = value + 1
            }
        }else{
            dic[data] = 1
        }
    }
    // 딕셔너리 완성
    
    var sortedDict : Array<(Int, Int)> = dic.sorted{ $0.value > $1.value }
    for data in sortedDict{
        tmp -= data.1
        count += 1
        if(tmp <= 0){
            break
        }
    }
    
    
    return count
}

var a = solution(6, [1,3,2,5,4,5,2,3])
print(a)


//import Foundation
//
//func solution(_ k:Int, _ tangerine:[Int]) -> Int {
//    var dic : [Int : Int] = [:]
//    var count : Int = 0
//    var tmp = k
//    for data in tangerine{
//        if dic[data] != nil {
//            if let value = dic[data]{
//                dic[data] = value + 1
//            }
//        }else{
//            dic[data] = 1
//        }
//    }
//    // 딕셔너리 완성
//
//    while(tmp > 0){
//         if let maxValue = dic.values.max(), let keyOfMaxValue = dic.first(where: { $1 == maxValue })?.key {
//        tmp = tmp - maxValue // 가장 큰 값을 k에서 빼기
//        dic.removeValue(forKey: keyOfMaxValue) // 해당 키-값 쌍 삭제
//        count += 1
//    }
//    }
//
//    return count
//}
