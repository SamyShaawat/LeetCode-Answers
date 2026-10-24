class Solution {
    public int countDaysTogether(String arriveAlice, String leaveAlice, String arriveBob, String leaveBob) {
        int[] c = {0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334};
        String s = arriveAlice.compareTo(arriveBob) > 0 ? arriveAlice : arriveBob;
        String e = leaveAlice.compareTo(leaveBob) < 0 ? leaveAlice : leaveBob;
        if (s.compareTo(e) > 0) return 0;
        return c[(e.charAt(0) - '0') * 10 + e.charAt(1) - '0' - 1] + (e.charAt(3) - '0') * 10 + e.charAt(4) - '0'
             - c[(s.charAt(0) - '0') * 10 + s.charAt(1) - '0' - 1] - (s.charAt(3) - '0') * 10 - s.charAt(4) + '0' + 1;
    }
}
