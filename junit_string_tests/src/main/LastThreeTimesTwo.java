package main;

/**
 * This class returns the last 3 chars of as string repeated twice.
 */
public class LastThreeTimesTwo {

    public String lastThreeRepeated(String input){
        String lastThree = input.substring((input.length() - 3));
        return lastThree + lastThree + lastThree;
    }
}
