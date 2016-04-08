package main;

/**
 * This class returns the last 3 chars of as string repeated twice.
 */
public class LastThreeTimesTwo {

    public String lastThreeRepeated(String input){
        String lastThree = input.substring((input.length() - 3));
        String result = lastThree + lastThree;

        System.out.println("INFO: last 3 repeated result = " + result);

        return result;
    }
}
