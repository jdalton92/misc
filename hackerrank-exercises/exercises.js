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
