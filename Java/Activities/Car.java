package activities;

public class Car {
	String color;
    String transmission;
    int make;
    int tyres = 4;
    int doors = 4 ;
    
    public void displayCharacterstics(){
    	System.out.println("Color of the Car: " + this.color);
    	System.out.println("Make of the Car: " + this.make);
    	System.out.println("Transmission of the Car: " + this.transmission);
    	System.out.println("Number of doors on the car: " + this.doors);
        	System.out.println("Number of tyres on the car: " + this.tyres);
        }	
    
    public void accelerate() {
    	System.out.println("Car is moving forward.");

    }
    
    public void brake() {
    	System.out.println("Car has stopped.");

    }
    
}
