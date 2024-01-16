function solution(name, yearning, photo) {
  var answer = [];
  let yearnObject = {};

  for (let i = 0; i < name.length; i++) {
    yearnObject[name[i]] = yearning[i];
  }

  for (const arr of photo) {
    let sum = 0;
    for (const score of arr) {
      sum += yearnObject[score] ? yearnObject[score] : 0;
    }
    answer.push(sum);
  }

  return answer;
}
