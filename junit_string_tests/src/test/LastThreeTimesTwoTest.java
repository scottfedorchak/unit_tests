package test;

import main.LastThreeTimesTwo;
import org.junit.*;

public class LastThreeTimesTwoTest {
    LastThreeTimesTwo threeTimes;

    @Before
    public void setUp(){
        threeTimes = new LastThreeTimesTwo();
    }

    @Test
    public void testRepeatedThreeTimes(){
        String testString = "testing";
        String result = threeTimes.lastThreeRepeated(testString);
        Assert.assertEquals("ERROR: expected the last 3 chars of " + testString + " to be repeated.", "inging", result);
    }

    @Test(expected=StringIndexOutOfBoundsException.class)
    public void testStringException() {
        //pass empty string to cause exception
        String testString = "";
        threeTimes.lastThreeRepeated(testString);
    }

    @Test(expected=NullPointerException.class)
    public void testNull() {
        //pass null string to cause exception
        String testString = null;
        threeTimes.lastThreeRepeated(testString);
    }

    @Test
    public void testThreeCharOnly(){
        String testString = "Ivy";
        String result = threeTimes.lastThreeRepeated(testString);
        Assert.assertEquals("ERROR: expected the last 3 chars of " + testString + " to be repeated.", "IvyIvy", result);
    }

    @Test
    public void testSpecialChar(){
        String testString = "%^~@*";
        String result = threeTimes.lastThreeRepeated(testString);
        Assert.assertEquals("ERROR: expected the last 3 chars of " + testString + " to be repeated.", "~@*~@*", result);
    }
}
