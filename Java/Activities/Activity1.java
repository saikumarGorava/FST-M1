package activities;

public class Activity1 {

    public static void main(String[] args) {
        Car carobj = new Car();
        carobj.make = 2014;
        carobj.color = "Black";
        carobj.transmission = "Manual";
    
        //Using Car class method
        carobj.displayCharacterstics();
        carobj.accelerate();
        carobj.brake();
    }

}
