//
// This is only a SKELETON file for the 'Scrabble Score' exercise. It's been provided as a
// convenience to get you started writing code faster.
//

const letterScoreMap = new Map();

letterScoreMap.set("a", 1);
letterScoreMap.set("b", 3);
letterScoreMap.set("c", 3);
letterScoreMap.set("d", 2);
letterScoreMap.set("e", 1);
letterScoreMap.set("f", 4);
letterScoreMap.set("g", 2);
letterScoreMap.set("h", 4);
letterScoreMap.set("i", 1);
letterScoreMap.set("j", 8);
letterScoreMap.set("k", 5);
letterScoreMap.set("l", 1);
letterScoreMap.set("m", 3);
letterScoreMap.set("n", 1);
letterScoreMap.set("o", 1);
letterScoreMap.set("p", 3);
letterScoreMap.set("q", 10);
letterScoreMap.set("r", 1);
letterScoreMap.set("s", 1);
letterScoreMap.set("t", 1);
letterScoreMap.set("u", 1);
letterScoreMap.set("v", 4);
letterScoreMap.set("w", 4);
letterScoreMap.set("x", 8);
letterScoreMap.set("y", 4);
letterScoreMap.set("z", 10);

export const score = (word) => {
  let finalScore = 0;

  for (let char of word.toLowerCase()) {
    finalScore += letterScoreMap.get(char);
  }

  return finalScore;
};
