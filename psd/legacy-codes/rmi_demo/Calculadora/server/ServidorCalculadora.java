import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;

public class ServidorCalculadora {
	public static void main(String[] args) {
		try {
			Calculadora calculadora = new Calculadora();
			Registry r = LocateRegistry.createRegistry(Registry.REGISTRY_PORT);
			String objname = "servidor_calculadora";
			System.out.println("registrando " +objname+ "...");
			r.rebind(objname, calculadora);
			System.out.println("registrado!");
		}
		catch (Exception e) {
			System.err.println("erro na main()! " + e);
			e.printStackTrace();
			System.exit(2);
		}
		System.out.println("esperando requisicao...");
	} 
}
