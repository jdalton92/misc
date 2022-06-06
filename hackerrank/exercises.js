// Minimum Absolute Difference in an Array
function minimumAbsoluteDifference(arr) {
  let sortedArr = arr.sort((a, b) => a - b);
  let minDifference = Math.abs(sortedArr[0] - sortedArr[1]);

  for (let i = 1; i < sortedArr.length; i++) {
    let minDifferenceTemp = Math.abs(sortedArr[i] - sortedArr[i + 1]);
    minDifference =
      minDifferenceTemp < minDifference ? minDifferenceTemp : minDifference;
  }

  return minDifference;
}

// Luck Balance
function luckBalance(k, contests) {
  let sortedImportant = contests
    .filter((c) => c[1] === 1)
    .sort((a, b) => a[0] - b[0]);

  const luckCount = contests.reduce((sum, acc) => sum + acc[0], 0);

  const importantWinCount = sortedImportant
    .splice(0, sortedImportant.length - k)
    .reduce((sum, acc) => sum + acc[0], 0);

  return luckCount - 2 * importantWinCount;
}

// Swap Nodes [Algo]
function swapNodes(indexes, queries) {}

//2D Array - DS
function hourglassSum(arr) {
  let hourglassTotals = [];
  for (let row = 0; row < 4; row++) {
    for (let col = 0; col < 4; col++) {
      let total = 0;
      total += arr[row][col];
      total += arr[row][col + 1];
      total += arr[row][col + 2];
      total += arr[row + 1][col + 1];
      total += arr[row + 2][col];
      total += arr[row + 2][col + 1];
      total += arr[row + 2][col + 2];
      hourglassTotals.push(total);
    }
  }
  return Math.max(...hourglassTotals);
}

// Minimum bribes
function minimumBribes(q) {
  let bribeCount = 0;
  let message;
  for (let i = 0; i < q.length; i++) {
    const id = q[i];
    const rank = i + 1;
    if (id - rank > 2) {
      message = "Too chaotic";
    }
    for (let j = Math.max(0, id - 2); j < i; j++) {
      if (q[j] > id) {
        bribeCount++;
      }
    }
  }
  console.log(message ? message : bribeCount);
}

//Minimum Swaps 2
function minimumSwaps(arr) {
  let swapCount = 0;
  let isVisited = [];
  for (let i = 0; i < arr.length; i++) {
    let j = i;
    let cycle = 0;
    while (!isVisited[j]) {
      isVisited[j] = true;
      j = arr[j] - 1;
      cycle++;
    }
    if (cycle != 0) {
      swapCount += cycle - 1;
    }
  }
  return swapCount;
}

// Sock Merchant
function sockMerchant(n, ar) {
  const sortedSocks = ar.sort();
  let pairsCount = 0;

  for (let i = 0; i < n; i++) {
    if (sortedSocks[i] === sortedSocks[i + 1]) {
      pairsCount++;
      i++;
    }
  }

  return pairsCount;
}

// Jumping on the Clouds
function jumpingOnClouds(c) {
  let jumpCount = 0;

  for (let i = 0; i < c.length - 1; i++) {
    if (c[i + 1] === 1) {
      jumpCount++;
      i++;
    } else if (c[i + 1] === 0 && c[i + 2] === 0) {
      jumpCount++;
      i++;
    } else {
      jumpCount++;
    }
  }

  return jumpCount;
}

// HashTables: Ransom Note
function checkMagazine(magazine, note) {
  let mHash = {};
  let answer = "Yes";

  // Hash to hashtable
  for (let i = 0; i < magazine.length; i++) {
    mHash[magazine[i]] = mHash[magazine[i]] ? mHash[magazine[i]] + 1 : 1;
  }

  // Check if note is in hashtable
  for (let j = 0; j < note.length; j++) {
    if (mHash[note[j]] > 0 && mHash[note[j]] !== undefined) {
      mHash[note[j]] -= 1;
    } else {
      answer = "No";
    }
  }
  console.log(answer);
}

// Two Strings
function twoStrings(s1, s2) {
  return s1.split("").filter((char) => s2.contains(char)).length > 0
    ? "YES"
    : "NO";
}

// Hash Tables: Ice Cream Parlor
function whatFlavors(cost, money) {
  let costHash = {};

  for (let i = 0; i < cost.length; i++) {
    let iceCreamCost = cost[i];
    let remainingMoney = money - iceCreamCost;

    if (costHash[remainingMoney]) {
      console.log(`${[costHash[remainingMoney]]} ${i + 1}`);
      return;
    }

    if (!costHash[iceCreamCost]) {
      costHash[iceCreamCost] = i + 1;
    }
  }
}

// Bubble sort
function countSwaps(a) {
  let countSwaps = 0;
  for (let i = 0; i < a.length; i++) {
    for (let j = 0; j < a.length - 1; j++) {
      if (a[j] > a[j + 1]) {
        let temp = a[j];
        a[j] = a[j + 1];
        a[j + 1] = temp;
        countSwaps += 1;
      }
    }
  }
  console.log("Array is sorted in", countSwaps, "swaps.");
  console.log("First Element:", a[0]);
  console.log("Last Element:", a[a.length - 1]);
}

// Toy Cout
function maximumToys(prices, k) {
  const sortedPrices = prices.sort((a, b) => a - b);
  let cumulativePrices = [sortedPrices[0]];
  let toyCount = 0;

  if (sortedPrices[0] > k) {
    return toyCount;
  } else {
    toyCount++;
  }

  for (let i = 1; i < sortedPrices.length; i++) {
    cumulativePrices.push(cumulativePrices[i - 1] + sortedPrices[i]);

    if (cumulativePrices[i] <= k) {
      toyCount++;
    }
  }

  return toyCount;
}

// Sherlock and Anagrams
function sherlockAndAnagrams(s) {
  let substrings = [];
  let anagramsCount = 0;

  // Get all the substrings from s
  for (let i = 0; i < s.length; i++) {
    for (let j = i + 1; j < s.length + 1; j++) {
      substrings.push(s.slice(i, j).split("").sort().join(""));
    }
  }

  // Find all matches
  for (let k = 0; k < substrings.length; k++) {
    for (let l = k + 1; l < substrings.length; l++) {
      if (substrings[k] === substrings[l]) {
        anagramsCount++;
      }
    }
  }

  return anagramsCount;
}

// countingValleys
function countingValleys(n, s) {
  const stepsAltitude = s.split("").map((step) => (step === "U" ? 1 : -1));
  const cumulativeAltitude = [stepsAltitude[0]];
  let countValleys = 0;

  for (let i = 1; i < n; i++) {
    cumulativeAltitude[i] = cumulativeAltitude[i - 1] + stepsAltitude[i];
    if (cumulativeAltitude[i] === 0 && cumulativeAltitude[i - 1] < 0) {
      countValleys++;
    }
  }

  return countValleys;
}

// Repeated String
function repeatedString(s, n) {
  const countString = s.split("").filter((c) => c === "a").length;
  let repeats = Math.floor(n / s.length);
  const remainderIndex = n % s.length;
  const countRemainder = s
    .slice(0, remainderIndex)
    .split("")
    .filter((c) => c === "a").length;

  const totalCount = countString * repeats + countRemainder;

  return totalCount;
}

// Making Anagrams
function makeAnagram(a, b) {
  let characterHashtable = {};

  const aArray = a.split("");
  const bArray = b.split("");

  for (let character of aArray) {
    characterHashtable[character] = (characterHashtable[character] || 0) + 1;
  }

  for (let character of bArray) {
    characterHashtable[character] = (characterHashtable[character] || 0) - 1;
  }

  const countDeletions = Object.values(characterHashtable).reduce(
    (sum, value) => sum + Math.abs(value),
    0
  );

  return countDeletions;
}

// Marc's Cakewalk
function marcsCakewalk(calorie) {
  const sortedCalorie = calorie.sort((a, b) => b - a);
  let minMiles = 0;

  for (let i = 0; i < calorie.length; i++) {
    minMiles += Math.pow(2, i) * sortedCalorie[i];
  }

  return minMiles;
}

// Maximum perimeter triangle
function maximumPerimeterTriangle(sticks) {
  let max = 0;
  let sides = "";
  let maxSide = 0;

  for (let i = 0; i < sticks.length - 2; i++) {
    for (let j = i + 1; j < sticks.length - 1; j++) {
      for (let k = j + 1; k < sticks.length; k++) {
        const a = sticks[i];
        const b = sticks[j];
        const c = sticks[k];

        if (a < b + c && b < c + a && c < a + b) {
          if (a + b + c > max) {
            max = a + b + c;
            sides = [a, b, c];
            maxSide = Math.max(a, b, c);
          } else if (a + b + c === max && Math.max(a, b, c) > maxSide) {
            sides = [a, b, c];
            maxSide = Math.max(a, b, c);
          }
        }
      }
    }
  }
  if (max > 0) {
    return sides.sort();
  } else {
    return [-1];
  }
}

// Beautiful Binary String
function beautifulBinaryString(b) {
  return (b.match(/010/g) || []).length;
}

// The Love Letter Mistery
function theLoveLetterMystery(s) {
  let count = 0;
  let middleChar = Math.floor(s.length / 2);
  let oppositeChar;

  for (let i = 0; i < middleChar; i++) {
    oppositeChar = s.length - 1 - i;
    count += Math.abs(s.charCodeAt(i) - s.charCodeAt(oppositeChar));
  }

  return count;
}

// Gemstones
function gemstones(arr) {
  let combined = arr.join("");
  let unique = [...new Set(combined)];
  return unique.filter((ch) => arr.every((str) => str.includes(ch))).length;
}

// Game of Thrones - I
function gameOfThrones(s) {
  let uniqueChar = new Set();
  for (let i = 0; i < s.length; i++) {
    uniqueChar.add(s.charAt(i));
  }

  let oddCount = 0;

  for (let char of uniqueChar) {
    let count = 0;

    for (let i = 0; i < s.length; i++) {
      if (char === s[i]) {
        count++;
      }
    }

    if (count % 2 === 1) {
      oddCount++;
    }

    if (s.length % 2 === 0 && oddCount > 0) {
      return "NO";
    } else if (oddCount > 1) {
      return "NO";
    }
  }

  return "YES";
}

// Funny String
function funnyString(s) {
  const sArr = s.split("");
  const reverseSArr = [...sArr].reverse();
  let sArrDiff = [];
  let reverseSArrDiff = [];

  for (let i = 0; i < s.length - 1; i++) {
    sArrDiff.push(Math.abs(sArr[i].charCodeAt() - sArr[i + 1].charCodeAt()));
    reverseSArrDiff.push(
      Math.abs(reverseSArr[i].charCodeAt() - reverseSArr[i + 1].charCodeAt())
    );
  }

  if (JSON.stringify(sArrDiff) === JSON.stringify(reverseSArrDiff)) {
    return "Funny";
  }
  return "Not Funny";
}

// Pangrams
function pangrams(s) {
  const sortedSet = new Set(
    s
      .toLowerCase()
      .split("")
      .filter((ch) => ch !== " ")
      .sort()
  );

  if (sortedSet.size === 26) {
    return "pangram";
  }
  return "not pangram";
}

// Mars exploration
function marsExploration(s) {
  const sArr = s.split("");
  let count = 0;
  for (let i = 0; i < s.length; i = i + 3) {
    if (sArr[i] !== "S") {
      count++;
    }
    if (sArr[i + 1] !== "O") {
      count++;
    }
    if (sArr[i + 2] !== "S") {
      count++;
    }
  }
  return count;
}

// HackerRank in a String
function hackerrankInString(s) {
  const target = "hackerrank";
  let index = 0;
  let match = 0;
  for (let i = 0; i < s.length; i++) {
    if (s[i] === target[index]) {
      index++;
      match++;
    }
  }
  return match === target.length ? "YES" : "NO";
}

// Weighted Uniform String (Solution Option 1)
function weightedUniformStrings(s, queries) {
  const sArr = s
    .toLowerCase()
    .split("")
    .sort()
    .map((ch) => ch.charCodeAt(0) - 96);
  let sHash = {};
  let sSubstringWeights = [];
  let results = [];

  for (let char of sArr) {
    sHash[char] = (sHash[char] || 0) + 1;
  }

  for (let key of Object.keys(sHash)) {
    for (let i = 1; i < sHash[key] + 1; i++) {
      sSubstringWeights.push(key * i);
    }
  }

  return queries.map((q) => (sSubstringWeights.includes(q) ? "Yes" : "No"));
}

// Weighted Uniform String (Solution Option 2)
function weightedUniformStrings(s, queries) {
  const uniformStrings = s.match(/([a-z])(\1)*/g);
  const values = uniformStrings.map((s) =>
    s.split("").map((c, i) => (c.charCodeAt(0) - 96) * (i + 1))
  );
  const flatValues = [].concat(...values);

  return queries.map((q) => (flatValues.includes(q) ? "Yes" : "No"));
}

// Caesar Cipher
function caesarCipher(s, k) {
  let cipher = "";
  for (let i = 0; i < s.length; i++) {
    if (s[i].match(/[A-Za-z]/i) && s[i] === s[i].toUpperCase()) {
      cipher += String.fromCharCode(((s.charCodeAt(i) + k - 65) % 26) + 65);
    } else if (s[i].match(/[A-Za-z]/i) && s[i] === s[i].toLowerCase()) {
      cipher += String.fromCharCode(((s.charCodeAt(i) + k - 97) % 26) + 97);
    } else {
      cipher += s[i];
    }
  }
  return cipher;
}

// Separate the Numbers
function separateNumbers(s) {
  if (s.length === 1) {
    console.log("NO");
    return;
  }

  let subString = "";
  let incrementedString = "";
  let incrementedNum = 0;
  let isValid = false;

  for (let i = 16; i <= s.length / 2; i++) {
    // Create an string incrementing numbers by 1
    // and then check if the string equals the input
    subString = s.substring(0, i);
    incrementedNum = BigInt(parseInt(subString, 10)) + BigInt(1);
    incrementedString = subString;

    while (incrementedString.length < s.length) {
      incrementedString = `${incrementedString}${incrementedNum.toString()}`;
      incrementedNum++;
    }

    if (incrementedString === s) {
      isValid = true;
      break;
    }
  }

  console.log(isValid ? `YES ${subString}` : "NO");
}

// Palindrome Index
function palindromeIndex(s) {
  let i = 0;
  let j = s.length - 1;

  while (i < j && s[i] === s[j]) {
    ++i;
    --j;
  }

  if (i >= j) return -1;

  let checkRight = true;
  let checkLeft = true;
  let skipLeftIndex = i;
  let skipRightIndex = j;

  while (i < j && (checkRight || checkLeft)) {
    checkLeft = checkLeft && s[i + 1] === s[j];
    checkRight = checkRight && s[i] === s[j - 1];
    ++i;
    --j;
  }

  return checkLeft ? skipLeftIndex : checkRight ? skipRightIndex : -1;
}

// Sherlock and the Valid String
function isValid(s) {
  let sHash = {};
  for (let char of s.split("")) {
    sHash[char] = (sHash[char] || 0) + 1;
  }

  const values = Object.values(sHash);
  return values
    .map((num) => num - Math.min(...Object.values(sHash)))
    .reduce((num, sum) => num + sum, 0) > 1
    ? "NO"
    : "YES";
}

// String Construction
function stringConstruction(s) {
  let sHash = {};
  for (let char of s.split("")) {
    sHash[char] = (sHash[char] || 0) + 1;
  }
  return Object.keys(sHash).length;
}

// Common child
function commonChild(s1, s2) {
  let matrix = [];
  for (let i = 0; i < s1.length; i++) {
    matrix.push(new Array(s2.length).fill(0));
    if (s1[i] === s2[0] || s1[0] === s2[0]) {
      matrix[i][0] = 1;
    }
  }
  for (let i = 0; i < s2.length; i++) {
    if (s2[i] === s1[0] || s1[0] === s2[0]) {
      matrix[0][i] = 1;
    }
  }

  for (let i = 1; i < s1.length; i++) {
    for (let j = 1; j < s2.length; j++) {
      if (s1[i] === s2[j]) {
        matrix[i][j] = matrix[i - 1][j - 1] + 1;
      } else {
        matrix[i][j] = Math.max(
          matrix[i - 1][j - 1],
          matrix[i][j - 1],
          matrix[i - 1][j]
        );
      }
    }
  }
  return matrix[s1.length - 1][s2.length - 1];
}

// Bear and Steady Gene
function steadyGene(gene) {
  const geneArr = gene.split("");
  const n = gene.length;
  const targetCount = gene.length / 4;
  let geneHash = {};
  let substringLength = n;
  let index = 0;

  for (let gene of geneArr) {
    geneHash[gene] = (geneHash[gene] || 0) + 1;
  }

  for (let i = 0; i < n; i++) {
    while (
      geneHash["A"] > targetCount ||
      geneHash["C"] > targetCount ||
      geneHash["T"] > targetCount ||
      geneHash["G"] > targetCount
    ) {
      if (index === n) {
        return substringLength;
      }
      geneHash[gene[index]]--;
      index++;
    }
    substringLength = Math.min(substringLength, index - i);
    geneHash[gene[i]]++;
  }

  return substringLength;
}

// Big Sorting
function bigSorting(unsorted) {
  return unsorted.sort((a, b) => a - b);
}

// intro Tutorial
function introTutorial(V, arr) {
  return arr.indexOf(V);
}

// insertion sort 1
function insertionSort1(n, arr) {
  let num = arr[arr.length - 1];
  let flag = false;

  for (let j = arr.length - 2; j > -1; j--) {
    if (arr[j] > num) {
      arr[j + 1] = arr[j];
      console.log(arr.join(" "));
    } else {
      arr[j + 1] = num;
      console.log(arr.join(" "));
      flag = true;
      break;
    }
  }

  if (!flag) {
    arr[0] = num;
    console.log(arr.join(" "));
  }
}

// insertion sort 2
function insertionSort2(n, arr) {
  for (let i = 1; i < arr.length; i++) {
    let tmp = arr[i];
    let j = i - 1;
    for (j; j >= 0 && arr[j] > tmp; j--) {
      arr[j + 1] = arr[j];
    }
    arr[j + 1] = tmp;
    console.log(arr.join(" "));
  }
}
