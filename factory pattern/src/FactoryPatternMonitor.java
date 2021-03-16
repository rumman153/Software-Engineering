public class FactoryPatternMonitor {
	
		   public static void main(String[] args) {
		      MonitorFactory monitorFactory = new MonitorFactory();

		      //get an object of CRT and call its draw method.
		      Monitor monitor1 = monitorFactory.getMonitor("CRT");

		      //call draw method of CRT
		      monitor1.produce();

		      //get an object of LCD and call its draw method.
		      Monitor monitor2 = monitorFactory.getMonitor("LCD");

		      //call draw method of LCD
		      monitor2.produce();

		      //get an object of LED and call its draw method.
		      Monitor monitor3 = monitorFactory.getMonitor("LED");

		      //call draw method of LED
		      monitor3.produce();
		   }
		

}
