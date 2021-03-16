public class MonitorFactory {

	//use getMonitor method to get object of type monitor
	   public Monitor getMonitor(String monitorType){
	      if(monitorType == null){
	         return null;
	      }		
	      if(monitorType.equalsIgnoreCase("CRT")){
	         return new CRTMonitor();
	         
	      } else if(monitorType.equalsIgnoreCase("LCD")){
	         return new LCDMonitor();
	         
	      } else if(monitorType.equalsIgnoreCase("LED")){
	         return new LEDMonitor();
	      }
	      
	      return null;
	   }
	
}
