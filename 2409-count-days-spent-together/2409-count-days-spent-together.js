/**
 * @param {string} arriveAlice
 * @param {string} leaveAlice
 * @param {string} arriveBob
 * @param {string} leaveBob
 * @return {number}
 */
var countDaysTogether = function(arriveAlice, leaveAlice, arriveBob, leaveBob) {
    const c = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334];
    const s = arriveAlice > arriveBob ? arriveAlice : arriveBob;
    const e = leaveAlice < leaveBob ? leaveAlice : leaveBob;
    if (s > e) return 0;
    return c[+e.slice(0, 2) - 1] + +e.slice(3) - c[+s.slice(0, 2) - 1] - +s.slice(3) + 1;
};
