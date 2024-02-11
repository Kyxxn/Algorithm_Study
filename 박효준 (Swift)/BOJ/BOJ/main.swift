import Foundation

protocol ChildEssential {
    func forParent()
    func beOld()
}
class Person {
    var name: String
    var age: Int {
        willSet{
            print("나이가 \(age)에서 \(newValue)로 바뀔 예정임")
        }
        
        didSet {
            print("ㅊㅊ \(age)됐음 원래는 \(oldValue)였음")
        }
    }
    
    
    init(name: String, age: Int) {
        self.name = name
        self.age = age
    }
}

class Student: Person, ChildEssential {
    func forParent() {
        print("효")
    }
    
    func beOld() {
        self.age += 1
        print("ㅊㅋㅊㅋ")
    }
}

var student: Student = Student(name: "효준", age: 10)
student.beOld()
