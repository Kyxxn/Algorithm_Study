// 24년 겨울 알고리즘 스터디
// BOJ & 프로그래머스
//
// Created by 박효준 on 1/10/24.

import Foundation

let nm = readLine()!.split(separator: " ").map{Int($0)!}
let n = nm[0], m = nm[1]
var miro: [[Int]] = Array(repeating: [], count: n)
let mx = [0,0,-1,1], my = [1,-1,0,0]

for i in 0..<n {
    let input = readLine()!.map{Int(String($0))!}
    miro[i] = input
}

var visited: [[Bool]] = Array(repeating: Array(repeating: false, count: m), count: n)
var distance: [[Int]] = Array(repeating: Array(repeating: 0, count: m), count: n)
func bfs() {
    var queue: [(Int, Int)] = []
    queue.append((0,0))
    visited[0][0] = true
    distance[0][0] = 1
    
    while !queue.isEmpty {
        let cur = queue.removeFirst()
        
        for i in 0..<4 {
            let nx = mx[i] + cur.0, ny = my[i] + cur.1
            
            if nx >= 0 && nx < n && ny >= 0 && ny < m {
                if !visited[nx][ny] && (miro[nx][ny] == 1){
                    distance[nx][ny] = distance[cur.0][cur.1] + 1
                    queue.append((nx, ny))
                    visited[nx][ny] = true
                }
            }
        }
    }
}

bfs()
print(distance[n-1][m-1])
